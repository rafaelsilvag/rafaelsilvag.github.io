# Rafael Silva Guimarães — personal website

An English-language academic website, built with static HTML and CSS for GitHub Pages. No dependencies or build step.

## Preview locally

Run `python3 -m http.server 8000` from the repository, then open http://localhost:8000.

## Content

- `index.html`: About tab, profile, professional links, and research interests.
- `publications.html`: Publications tab with selected publications and the full Google Scholar profile link.
- `classes.html`: Classes tab with the archive organized by year and semester.
- `assets/style.css`: responsive styles shared by all pages.
- `assets/images/rafael-silva-guimaraes.jpg`: 460 × 460 photo downloaded from the public GitHub profile.
- `teaching/2027/1/computer-networks-ii/index.html`: Redes de Computadores II, Integrated Technical Program in Internet Informatics.
- `teaching/2027/1/network-services/index.html`: Serviços de Redes para Internet, Bachelor’s Degree in Information Systems.

Each course has its own directory and independent `index.html`. Place presentations, PDFs, exercises, and additional HTML pages directly in that course directory. Add relative links to the course page’s “Course resources” section, replacing the “Materials coming soon” notice when resources are available.

For example, in `teaching/2027/1/computer-networks-ii/`, save `lecture-01.html` and `slides-01.pdf`, then link them from that directory’s `index.html`:

```html
<a href="lecture-01.html">Lecture 01</a>
<a href="slides-01.pdf">Slides (PDF)</a>
```

The existing `teaching/` directory paths are retained so course URLs remain valid; the navigation tab is labeled **Classes**. Keep course names in Portuguese; the surrounding site content is in English.

For a new semester, create `teaching/<year>/<semester>/<course>/index.html` and add the corresponding year, semester, and course links to the Classes page (`classes.html`). Adjust relative asset/home paths if you change the folder depth.

Selected publication details come from https://scholar.google.com/citations?user=UhgwAEMAAAAJ&hl=en&oi=ao (accessed 2026-11-11). The full publication list links directly to Scholar; the selected list is static.

## GitHub Pages

Publish from the `main` branch and `/ (root)` in the repository’s **Settings → Pages**. This source is ready for https://rafaelsilvag.github.io/ once committed, pushed, and Pages is enabled.

## Network Services course

The 2027/1 Network Services course has 60 numbered lesson units totaling 72 hours, with Portuguese objectives, activities, future HTML presentation pages, an updated PDF course plan, and an editable XLSX plan. See `teaching/2027/1/network-services/README.md` for editing instructions and the assessment schedule.

The current profile photo is the 460 × 460 GitHub avatar, downloaded from https://github.com/rafaelsilvag.png?size=512 on 2026-11-11.
