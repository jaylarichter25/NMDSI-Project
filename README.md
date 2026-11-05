# Affiliated Faculty Directory

A static, searchable directory of the Northwestern Mutual Data Science Institute's affiliated faculty. It has no backend, framework or build step, and works offline after the first visit.

## Run it locally

Browsers won't let a page read `faculty.json` when it's opened directly from a folder, so use a small local server:

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Deploy it

The site needs these files, all served from the same folder: `index.html`, `styles.css`, `app.js`, `sw.js` and `faculty.json`. All paths are relative, so it also works from a subpath.

**GitHub Pages**

1. Push this folder to a GitHub repository. The source PDF is excluded by `.gitignore`. Everything else, including `scripts/`, is publicly reachable once the site is published.
2. In the repository, open **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**, then pick your branch and the `/ (root)` folder.
4. The site appears at `https://<your-username>.github.io/<repo>/` after a minute or two.

**Netlify**

Drag the folder onto <https://app.netlify.com/drop>, or connect the repository with no build command and `.` as the publish directory.

## Update the data

To regenerate `faculty.json` from a newer PDF (requires Python and `pdfplumber`). The PDF isn't in this repository, so you'll need your own copy:

```bash
pip install pdfplumber
python3 scripts/build_faculty.py <directory.pdf> faculty.json
```

The build stops if a person has no tags or a curated list no longer matches the PDF. Add or fix those people in `scripts/curation.py`, which holds the hand-written tags and list structure.

To edit a single entry, change `faculty.json` directly. Returning visitors get the new data on their second load. If you change the list of site files, also update `FILES` and the `CACHE` version in `sw.js`.

## Data notes

- Text comes from the source PDF, with one duplicate row removed and spelling variants of college and department names unified (see `COLLEGE_FIXES` and `DEPT_FIXES` in `scripts/build_faculty.py`).
- Other apparent errors in the PDF are deliberately left as published.
- `sortLastName` is used only for sorting. Multiple departments or colleges are separated by `; `, and a person with two appears under both when grouped.
