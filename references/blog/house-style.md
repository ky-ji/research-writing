# House Style For ky-ji.github.io

Apply these site conventions when authoring or updating posts for `ky-ji.github.io/blogs/`.

## Directory Layout And Components

- Place each post in `ky-ji.github.io/blogs/<slug>/` with `index.html`, `style.css`, and `figures/`.
- Reuse the stylesheet and components of `blogs/noise-space-conditioning/` instead of inventing new ones:
  - TL;DR box and hero widget
  - `.sec-eyebrow` and `.claim`
  - `.hyp-grid`, `.metrics`, `.result-list`, `.lessons`
  - `details.proto`
  - `.clean-table` with `.grp`, `.hi`, and `.bad` rows

## Figures And Typography

- Generate SVG figures via a Python script stored next to the experiment results, reading archived JSON directly.
- Set native SVG width to 740px.
- Use `Hanken Grotesk` typography, at most 2 accent colors plus greys, and real subscripts via `<tspan baseline-shift="sub">`.

## Publishing And Backups

- Add the new post to `blogs/index.html` and to the "Blogs" list in the homepage `index.md`.
- Back up the previous version to the conversation scratch directory before any major rewrite.
- Verify the rendered page locally at 1440px desktop width and true 390px mobile width (using an iframe wrapper with headless Chrome) before finishing.
