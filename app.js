"use strict";

const NO_DEPARTMENT = "No department listed";
const SORTS = {
  last: { letter: (p) => p.last },
  first: { letter: (p) => p.first },
  university: { keys: (p) => [p.university], blank: "" },
  college: { keys: (p) => p.colleges, blank: "No college listed" },
  department: { keys: (p) => p.departments, blank: NO_DEPARTMENT },
  title: { keys: (p) => [p.title], blank: "No title listed" },
};
const BIO_PREVIEW = 170;
const TAGS_MIN_BIO = 100; // Short bios already read as a list of tags, so don't repeat them.

const $ = (id) => document.getElementById(id);
const ui = {
  search: $("search"), university: $("university"), department: $("department"), sort: $("sort"),
  count: $("count"), clear: $("clear"), results: $("results"), lede: $("lede"),
  viewButtons: [...document.querySelectorAll("[data-view]")],
};
const collator = new Intl.Collator("en", { sensitivity: "base", numeric: true });
const compare = (a, b) => collator.compare(a, b);
const state = { q: "", university: "", department: "", sort: "last", view: "cards" };
const expanded = new Set();
let people = [];

const normalize = (s) =>
  s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[‘’]/g, "'").toLowerCase();
const splitList = (s) => s.split(";").map((x) => x.trim()).filter(Boolean);
const byLastName = (a, b) => compare(a.last, b.last) || compare(a.first, b.first);

function prepare(raw, id) {
  const first = raw.name.split(",")[0].trim();
  const departments = splitList(raw.department);
  const colleges = splitList(raw.college);
  return {
    ...raw, id, first, last: raw.sortLastName, departments, colleges,
    haystack: normalize([raw.name, raw.university, raw.college, raw.department,
      raw.bio, raw.researchInterests.join(" ")].join(" \n ")),
  };
}

/* Filtering ------------------------------------------------------------- */
const terms = () => normalize(state.q).split(/\s+/).filter(Boolean);

function inDepartment(p, dept) {
  if (!dept) return true;
  return dept === NO_DEPARTMENT ? p.departments.length === 0 : p.departments.includes(dept);
}

function visiblePeople() {
  const ts = terms();
  return people.filter((p) =>
    (!state.university || p.university === state.university) &&
    inDepartment(p, state.department) &&
    ts.every((t) => p.haystack.includes(t)));
}

function fillSelect(select, allLabel, counts, value, showCounts = true) {
  const options = [new Option(allLabel, "")];
  const names = [...counts.keys()].filter((k) => k !== NO_DEPARTMENT).sort(compare);
  if (counts.has(NO_DEPARTMENT)) names.push(NO_DEPARTMENT);
  for (const name of names) options.push(new Option(showCounts ? `${name} (${counts.get(name)})` : name, name));
  select.replaceChildren(...options);
  select.value = value;
}

function refreshFilters() {
  const unis = new Map();
  const depts = new Map();
  const bump = (map, key) => map.set(key, (map.get(key) || 0) + 1);
  for (const p of people) {
    bump(unis, p.university);
    if (state.university && p.university !== state.university) continue;
    if (p.departments.length) p.departments.forEach((d) => bump(depts, d));
    else bump(depts, NO_DEPARTMENT);
  }
  // Departments narrow to the chosen university; drop a choice that no longer applies.
  if (state.department && !depts.has(state.department)) state.department = "";
  fillSelect(ui.university, "All universities", unis, state.university, false);
  fillSelect(ui.department, "All departments", depts, state.department);
}

/* Grouping -------------------------------------------------------------- */
function groupPeople(list) {
  const sort = SORTS[state.sort];
  const groups = new Map();
  const add = (key, p) => (groups.has(key) ? groups.get(key).push(p) : groups.set(key, [p]));
  if (sort.letter) {
    const sorted = [...list].sort(state.sort === "first"
      ? (a, b) => compare(a.first, b.first) || compare(a.last, b.last)
      : byLastName);
    for (const p of sorted) add(sort.letter(p)[0].toUpperCase(), p);
    return [...groups];
  }
  for (const p of list) {
    const keys = sort.keys(p).filter(Boolean);
    if (!keys.length) add(sort.blank, p);
    // Someone with two departments or colleges appears under each.
    for (const key of keys) {
      if (state.sort === "department" && state.department && state.department !== NO_DEPARTMENT
          && key !== state.department) continue;
      add(key, p);
    }
  }
  return [...groups]
    .sort(([a], [b]) => (a === sort.blank) - (b === sort.blank) || compare(a, b))
    .map(([key, members]) => [key, members.sort(byLastName)]);
}

/* Rendering helpers ----------------------------------------------------- */
function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function highlighted(node, text) {
  node.replaceChildren();
  const ts = terms();
  if (!ts.length) { node.textContent = text; return node; }
  const pattern = ts
    .map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(/'/g, "['’]"))
    .sort((a, b) => b.length - a.length)
    .join("|");
  text.split(new RegExp(`(${pattern})`, "gi")).forEach((part, i) => {
    if (!part) return;
    node.append(i % 2 ? el("mark", "", part) : document.createTextNode(part));
  });
  return node;
}

function externalIcon() {
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("viewBox", "0 0 12 12");
  svg.setAttribute("class", "ext");
  svg.setAttribute("aria-hidden", "true");
  svg.innerHTML = '<path d="M4.5 1.5h6v6M10.5 1.5 2 10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>';
  return svg;
}

function nameNode(p, tag) {
  const node = el(tag, "name");
  if (/^https?:\/\//i.test(p.profileLink)) {
    const a = el("a");
    a.href = p.profileLink;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.append(highlighted(el("span"), p.name), externalIcon(), el("span", "sr", " (profile opens in a new tab)"));
    node.append(a);
  } else {
    highlighted(node, p.name);
  }
  return node;
}

function affiliation(p) {
  const box = el("p", "affil");
  const kind = p.university.startsWith("Marquette") ? "mu" : "uwm";
  box.append(highlighted(el("span", `uni uni--${kind}`), p.university));
  for (const unit of [...p.colleges, ...p.departments]) {
    box.append(highlighted(el("span", "unit"), unit));
  }
  return box;
}

function preview(bio) {
  if (bio.length <= BIO_PREVIEW + 30) return bio;
  const cut = bio.slice(0, BIO_PREVIEW);
  return cut.slice(0, cut.lastIndexOf(" ")).replace(/[\s,;:.]+$/, "") + "…";
}

function bioNode(p) {
  const box = el("div", "bio");
  const para = el("p");
  box.append(para);
  const short = preview(p.bio);
  const collapsible = short !== p.bio;
  // If the search hit is in the hidden part, show all of it so the match is visible.
  const normShort = normalize(short);
  const hitHidden = collapsible && terms().some((t) => normalize(p.bio).includes(t) && !normShort.includes(t));
  if (!collapsible || hitHidden) {
    highlighted(para, p.bio);
    return box;
  }
  const button = el("button", "linkish");
  button.type = "button";
  const update = () => {
    const open = expanded.has(p.id);
    highlighted(para, open ? p.bio : short);
    button.textContent = open ? "Show less" : "Show full bio";
    button.setAttribute("aria-expanded", String(open));
  };
  button.addEventListener("click", () => {
    if (expanded.has(p.id)) expanded.delete(p.id); else expanded.add(p.id);
    update();
  });
  update();
  box.append(button);
  return box;
}

function tagList(p) {
  const list = el("ul", "tags");
  for (const tag of p.researchInterests) {
    const item = el("li");
    const button = highlighted(el("button", "tag"), tag);
    button.type = "button";
    button.setAttribute("aria-label", `Search for ${tag}`);
    button.addEventListener("click", () => {
      state.q = tag;
      ui.search.value = tag;
      update();
      ui.results.focus({ preventScroll: true });
      window.scrollTo({ top: document.getElementById("main").offsetTop - 90 });
    });
    item.append(button);
    list.append(item);
  }
  return list;
}

function card(p) {
  const node = el("article", `card card--${p.university.startsWith("Marquette") ? "mu" : "uwm"}`);
  node.append(nameNode(p, "h3"));
  if (p.title) node.append(highlighted(el("p", "role"), p.title));
  node.append(affiliation(p), bioNode(p));
  if (p.bio.length >= TAGS_MIN_BIO) node.append(tagList(p));
  return node;
}

function tableRows(members) {
  return members.map((p) => {
    const tr = el("tr");
    const who = el("td");
    who.append(nameNode(p, "div"));
    if (p.title) who.append(highlighted(el("p", "role"), p.title));
    const where = el("td");
    where.append(affiliation(p));
    const what = el("td");
    what.append(bioNode(p));
    tr.append(who, where, what);
    return tr;
  });
}

function table(members) {
  const t = el("table", "table");
  const colgroup = el("colgroup");
  colgroup.append(el("col", "col-name"), el("col", "col-affil"), el("col"));
  const head = el("thead");
  const row = el("tr");
  for (const label of ["Name", "Institution", "Research"]) {
    const th = el("th", "", label);
    th.scope = "col";
    row.append(th);
  }
  head.append(row);
  const body = el("tbody");
  body.append(...tableRows(members));
  t.append(colgroup, head, body);
  return t;
}

/* Page state ------------------------------------------------------------ */
function render() {
  const list = visiblePeople();
  const active = state.q || state.university || state.department;
  ui.count.textContent = list.length === people.length
    ? `${people.length} faculty`
    : `Showing ${list.length} of ${people.length} faculty`;
  ui.clear.hidden = !active;
  ui.viewButtons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.view === state.view)));

  if (!list.length) {
    const empty = el("div", "empty");
    empty.append(el("strong", "", "No faculty match"), el("span", "", "Try a broader term or clear a filter."));
    ui.results.replaceChildren(empty);
    return;
  }
  const sections = groupPeople(list).map(([label, members]) => {
    const section = el("section", "group");
    const head = el("h2", "group__head");
    head.append(el("span", "", label), el("span", "group__count", String(members.length)));
    section.append(head);
    if (state.view === "table") {
      section.append(table(members));
    } else {
      const grid = el("div", "grid");
      grid.append(...members.map(card));
      section.append(grid);
    }
    return section;
  });
  ui.results.replaceChildren(...sections);
}

function syncUrl() {
  const params = new URLSearchParams();
  if (state.q) params.set("q", state.q);
  if (state.university) params.set("university", state.university);
  if (state.department) params.set("department", state.department);
  if (state.sort !== "last") params.set("sort", state.sort);
  if (state.view !== "cards") params.set("view", state.view);
  const query = params.toString();
  history.replaceState(null, "", query ? `?${query}` : location.pathname);
}

function update() {
  refreshFilters();
  render();
  syncUrl();
}

function readInitialState() {
  const params = new URLSearchParams(location.search);
  state.q = params.get("q") || "";
  state.university = params.get("university") || "";
  state.department = params.get("department") || "";
  if (SORTS[params.get("sort")]) state.sort = params.get("sort");
  let saved = null;
  try { saved = localStorage.getItem("faculty-view"); } catch { /* storage may be blocked */ }
  state.view = params.get("view") || saved;
  if (state.view !== "table") state.view = "cards";
  if (!people.some((p) => p.university === state.university)) state.university = "";
  ui.search.value = state.q;
  ui.sort.value = state.sort;
}

function bindEvents() {
  document.getElementById("controls").addEventListener("submit", (e) => e.preventDefault());
  ui.search.addEventListener("input", () => { state.q = ui.search.value.trim(); update(); });
  ui.university.addEventListener("change", () => { state.university = ui.university.value; update(); });
  ui.department.addEventListener("change", () => { state.department = ui.department.value; update(); });
  ui.sort.addEventListener("change", () => { state.sort = ui.sort.value; update(); });
  ui.viewButtons.forEach((b) => b.addEventListener("click", () => {
    state.view = b.dataset.view;
    try { localStorage.setItem("faculty-view", state.view); } catch { /* optional */ }
    update();
  }));
  ui.clear.addEventListener("click", () => {
    Object.assign(state, { q: "", university: "", department: "" });
    ui.search.value = "";
    update();
    ui.search.focus();
  });
}

async function start() {
  bindEvents();
  try {
    const response = await fetch("faculty.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    people = (await response.json()).map(prepare);
  } catch (error) {
    console.error(error);
    ui.count.textContent = "The directory could not be loaded.";
    const notice = el("div", "notice");
    notice.append(el("p", "", "Browsers block this page from reading its data when it's opened directly from a folder."));
    const hint = el("p");
    hint.append("Run ", el("code", "", "python3 -m http.server 8000"), " in the project folder, then visit ", el("code", "", "http://localhost:8000"), ".");
    notice.append(hint);
    ui.results.replaceChildren(notice);
    return;
  }
  const universities = new Set(people.map((p) => p.university)).size;
  ui.lede.textContent = `${people.length} researchers across ${universities} universities: Marquette University and the University of Wisconsin-Milwaukee.`;
  readInitialState();
  update();
}

start();

if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
  navigator.serviceWorker.register("sw.js").catch((e) => console.warn("Offline support unavailable", e));
}
