# Rafael Silva Guimarães — personal website

An English-language academic website, built with static HTML and CSS for GitHub Pages. No dependencies or build step.

## Preview locally

Run `python3 -m http.server 8000` from the repository, then open http://localhost:8000.

## Content

- `index.html`: profile, professional links, selected publications, and teaching archive.
- `assets/style.css`: responsive styles shared by all pages.
- `assets/images/rafael-silva-guimaraes.jpg`: photo downloaded from the public Google Scholar profile.
- `teaching/2027/1/computer-networks-ii/index.html`: Redes de Computadores II, Integrated Technical Program in Internet Informatics.
- `teaching/2027/1/network-services/index.html`: Serviços de Redes para Internet, Bachelor’s Degree in Information Systems.

Add lecture notes and activities to each course page's “Course resources” section, replacing the “Materials coming soon” notice when resources are available. Keep course names in Portuguese; the surrounding site content is in English.

For a new semester, create `teaching/<year>/<semester>/<course>/index.html` and add the corresponding year, semester, and course links to the teaching section of the home page. Adjust relative asset/home paths if you change the folder depth.

Selected publication details and the profile photo come from https://scholar.google.com/citations?user=UhgwAEMAAAAJ&hl=en&oi=ao (accessed 2026-11-11). The full publication list links directly to Scholar; the selected list is static.

## GitHub Pages

Publish from the `main` branch and `/ (root)` in the repository’s **Settings → Pages**. This source is ready for https://rafaelsilvag.github.io/ once committed, pushed, and Pages is enabled.
