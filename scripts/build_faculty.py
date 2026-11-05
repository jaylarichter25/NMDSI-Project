#!/usr/bin/env python3
"""Build faculty.json from the directory PDF. Usage: build_faculty.py <pdf> <out.json>"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from curation import LISTS, TAGS  # noqa: E402
from parse_pdf import parse  # noqa: E402

UWM = "University of Wisconsin-Milwaukee"
MU = "Marquette University"

SPLIT_CHAR = re.compile(r"\b([ASTD]) (ssociate|ssistant|eaching|ciences|chool|epartment|irector)\b")
NEW_UNIT = re.compile(
    r"^(College|School|Department|Joint Department|Joseph|Zilber|Klingler|Klinger|Lubar|Helen|Peck|Opus|"
    r"Diederich|Marquette|Programs|Office|Raynor|Academic|Biological|Physics|Freshwater|Biostatistics|"
    r"Information Technology Management Program|Industrial)"
)

# Spelling variants in the PDF, unified so filters don't show duplicates.
COLLEGE_FIXES = {
    "College of Letters and Sciences": "College of Letters and Science",
    "College of Letter and Sciences": "College of Letters and Science",
    "Klinger College of Arts and Sciences": "Klingler College of Arts and Sciences",
    "Klingler College of Arts and Science": "Klingler College of Arts and Sciences",
    "School of Arts and Sciences": "Klingler College of Arts and Sciences",
    "College of Arts and Sciences": "Klingler College of Arts and Sciences",
    "College of Engineering & Applied Science": "College of Engineering and Applied Science",
    "College of Engineering and Applied Sciences": "College of Engineering and Applied Science",
    "Helen Badar School of Social Welfare": "Helen Bader School of Social Welfare",
    "Lubar School of Business": "Lubar College of Business",
    "Zilber School of Public Health": "Joseph J. Zilber College of Public Health",
    "Zilber College of Public Health": "Joseph J. Zilber College of Public Health",
    "Joseph J Zilber College of Public Health": "Joseph J. Zilber College of Public Health",
    "Marquette University School of Dentistry": "School of Dentistry",
    "School of Rehabilitation and Technology": "School of Rehabilitation Sciences and Technology",
}
DEPT_FIXES = {
    "Department Biomedical Engineering": "Department of Biomedical Engineering",
    "Joint Department of Biomedical Engineer": "Joint Department of Biomedical Engineering",
    "Department of Computer Sciences": "Department of Computer Science",
    "Department Supply Chain, Operations Management & Business Statistics":
        "Department of Supply Chain, Operations Management & Business Statistics",
    "Biological Sciences": "Department of Biological Sciences",
    "Physics": "Department of Physics",
    "Industrial and Manufacturing Engineering": "Department of Industrial and Manufacturing Engineering",
    "College of Economics": "Department of Economics",
    "Biostatistics and Health Informatics,": "Biostatistics and Health Informatics",
}
# Rows whose affiliation lines don't follow the institution/college/department pattern.
AFFILIATION_OVERRIDES = {
    "Colleen Galambos": ("Helen Bader School of Social Welfare", "Office of Applied Gerontology"),
    "Matthew Friedel": ("", "School of Information Studies"),
    "Wan-Chen Lee": ("", "School of Information Studies"),
    "Inga Wang": ("School of Rehabilitation Sciences and Technology",
                  "Department of Occupational Therapy; Department of Science and Technology"),
    "Phoenix Do": ("Joseph J. Zilber College of Public Health",
                   "Department of Public Health Policy; Department of Epidemiology"),
    "Larry Zhiming Xu": ("Diederich College of Communication",
                         "Department of Strategic Communication; Department of Information Systems"),
}


def clean(s):
    s = SPLIT_CHAR.sub(r"\1\2", s)
    s = s.replace("University of Wisconsin- Milwaukee", UWM)
    return re.sub(r"\s+", " ", s).strip()


def merge_continuations(rows):
    """A row with no affiliation text is the tail of the previous row (e.g. a title across a page)."""
    out = []
    for r in rows:
        if out and not r["cols"][1] and not r["links"]:
            prev = out[-1]
            prev["cols"][0] += r["cols"][0]
            prev["cols"][2] += r["cols"][2]
        else:
            out.append(r)
    return out


def split_name_title(lines):
    lines = [clean(l) for l in lines]
    name = lines[0]
    i = 1
    while name.endswith((",", "-")) and i < len(lines):
        name += ("" if name.endswith("-") else " ") + lines[i]
        i += 1
    name = name.replace("PhD. MLIS", "PhD, MLIS")
    return name, " ".join(lines[i:])


def base_name(name):
    return name.split(",")[0].strip()


def sort_last_name(key):
    """Surname used only for sorting. Names are never reordered or corrected for display."""
    return {"Badar Al Lawati": "Al Lawati"}.get(key, key.split()[-1])


def split_affiliation(lines):
    lines = [clean(l) for l in lines]
    first = lines[0]
    rest = lines[1:]
    if first == UWM or first.startswith(UWM):
        university = UWM
    else:
        university = MU
        tail = first[len(MU):].strip()
        if tail:
            rest.insert(0, tail)
        elif first != MU:
            raise ValueError(first)
    units = []
    for l in rest:
        l = l.rstrip()
        if units and (not NEW_UNIT.match(l) or units[-1].endswith(("/", "and", "of"))):
            units[-1] += ("" if units[-1].endswith("/") else " ") + l
        else:
            units.append(l)
    return university, units


def classify_units(units):
    units = [u.rstrip(",").strip() if u.endswith("Engineering,") else u for u in units]
    colleges, depts = [], []
    for u in units:
        u = u.rstrip()
        is_college = re.match(r"^(College|School|Joseph|Zilber|Klingler|Klinger|Lubar|Helen|Peck|Opus|Diederich|"
                              r"Marquette University|Raynor|Academic Affairs|Freshwater)", u)
        if is_college and u != "College of Economics" and not (u in ("School of Information Studies", "School of Education") and colleges):
            for part in re.split(r",\s*(?=College of)", u.rstrip(",")):
                colleges.append(COLLEGE_FIXES.get(part, part))
        else:
            depts.append(DEPT_FIXES.get(u, u))
    return "; ".join(colleges), "; ".join(depts)


def join_research(lines):
    """Join wrapped lines, closing up words the PDF hyphenated or slashed across a line break."""
    text = ""
    for line in (clean(l) for l in lines):
        if text.endswith("/") or (text.endswith("-") and not re.match(r"^(and|or)\b", line)):
            text += line
        else:
            text += (" " if text else "") + line
    return text


def squash(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def make_bio(key, raw):
    """Use the curated list structure if there is one, after proving it matches the source words."""
    if key not in LISTS:
        return raw
    items = LISTS[key].split("|")
    if squash("".join(items)) != squash(raw):
        raise ValueError(f"curated list differs from PDF for {key}:\n{items}\n{raw}")
    return "; ".join(items)


def stem(word):
    return re.sub(r"(s|es|ing|ion|ions|al|ed)$", "", word)


def check_tags(key, tags, bio):
    """Every word of a tag must come from the person's own text (allowing simple inflections)."""
    tokens = re.findall(r"[a-z0-9]+", bio.lower())
    stems = {stem(t) for t in tokens}
    missing = []
    for tag in tags:
        for word in re.findall(r"[a-z0-9]+", tag.lower()):
            if word in {"and", "of", "in", "the"}:
                continue
            if word not in tokens and stem(word) not in stems:
                missing.append(f"{tag!r}/{word}")
    return missing


def build(pdf):
    rows = parse(pdf)
    rows = [r for r in rows if r["cols"][0][:1] != ["Full Name"]]
    rows = merge_continuations(rows)
    seen, out, notes = set(), [], []
    for r in rows:
        name, title = split_name_title(r["cols"][0])
        if name in seen:
            notes.append(f"duplicate row dropped: {name} (p{r['page']})")
            continue
        seen.add(name)
        university, units = split_affiliation(r["cols"][1])
        college, dept = classify_units(units)
        key = base_name(name)
        if key in AFFILIATION_OVERRIDES:
            college, dept = AFFILIATION_OVERRIDES[key]
        bio = make_bio(key, join_research(r["cols"][2]))
        if key not in TAGS:
            raise ValueError(f"no tags curated for {key}")
        missing = check_tags(key, TAGS[key], bio)
        if missing:
            notes.append(f"tag not in text: {key}: {missing}")
        links = [l["uri"] for l in r["links"] if l["col"] == 0 and l["uri"]]
        other = [l["uri"] for l in r["links"] if l["col"] != 0]
        if other:
            notes.append(f"non-name link: {name}: {other}")
        if len(set(links)) > 1:
            notes.append(f"multiple profile links: {name}: {links}")
        out.append({
            "name": name, "title": title, "university": university, "college": college, "department": dept,
            "researchInterests": TAGS[key], "bio": bio,
            "profileLink": links[0] if links else "",
            "sortLastName": sort_last_name(key),
        })
    return out, notes


if __name__ == "__main__":
    data, notes = build(sys.argv[1])
    Path(sys.argv[2]).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(len(data), "entries")
    print("\n".join(notes))
