#!/usr/bin/env python3
"""Rebuild the directory table from word coordinates in the source PDF.

pdfplumber's table finder only detects the middle column, so rows are recovered
from the horizontal rules, which span the first column, and cells are split at
the two vertical rules. A row can continue onto the next page.
"""
import json
import sys

import pdfplumber

COL1_END, COL2_END = 188.8, 418.4
TOP_MARGIN, BOTTOM_MARGIN = 135, 740


def cluster_lines(chars):
    """Group chars into visual lines, then words, using gaps relative to font size."""
    lines = []
    for c in sorted(chars, key=lambda c: (c["top"] + c["bottom"]) / 2):
        mid = (c["top"] + c["bottom"]) / 2
        if lines and abs(mid - lines[-1]["mid"]) < 4:
            lines[-1]["chars"].append(c)
        else:
            lines.append({"mid": mid, "chars": [c]})
    out = []
    for line in lines:
        text, prev = "", None
        for c in sorted(line["chars"], key=lambda c: c["x0"]):
            if c["text"] == " ":
                prev = c
                text += " " if not text.endswith(" ") else ""
                continue
            if prev is not None and c["x0"] - prev["x1"] > 3 and not text.endswith(" "):
                text += " "
            text += c["text"]
            prev = c
        out.append({"top": min(c["top"] for c in line["chars"]), "text": text.strip()})
    return [l for l in out if l["text"]]


def parse(path):
    rows, current = [], None
    with pdfplumber.open(path) as pdf:
        for pageno, page in enumerate(pdf.pages, 1):
            rules = sorted(
                r["top"] for r in page.rects
                if r["x0"] < 37 and abs(r["x1"] - COL1_END) < 1 and r["bottom"] - r["top"] < 1.5
            )
            # Segments of this page: before the first rule continues the previous row.
            edges = [TOP_MARGIN] + rules + [BOTTOM_MARGIN]
            for i in range(len(edges) - 1):
                top, bottom = edges[i], edges[i + 1]
                # A page's first segment continues the previous row, unless the name
                # column has text there: some rows start at a page top with no rule.
                has_name = any(c["x0"] < COL1_END and top <= (c["top"] + c["bottom"]) / 2 < bottom
                               and c["text"].strip() for c in page.chars)
                if i > 0 or current is None or has_name:
                    current = {"page": pageno, "cols": [[], [], []], "links": []}
                    rows.append(current)
                chars = [c for c in page.chars
                         if top <= (c["top"] + c["bottom"]) / 2 < bottom and c["top"] < BOTTOM_MARGIN]
                split = [[], [], []]
                for c in chars:
                    x = (c["x0"] + c["x1"]) / 2
                    split[0 if x < COL1_END else 1 if x < COL2_END else 2].append(c)
                for idx in range(3):
                    current["cols"][idx] += [l["text"] for l in cluster_lines(split[idx])]
                for h in page.hyperlinks:
                    if top - 1 <= (h["top"] + h["bottom"]) / 2 < bottom:
                        col = 0 if h["x0"] < COL1_END else 1 if h["x0"] < COL2_END else 2
                        current["links"].append({"col": col, "uri": h.get("uri"), "page": pageno})
    return [r for r in rows if any(r["cols"])]


if __name__ == "__main__":
    json.dump(parse(sys.argv[1]), open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
