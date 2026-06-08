# nycedc-grocery

Static GitHub Pages site for the NYCEDC N.Y.C. Groceries RFP partner packet.

## Site

https://collectivewinca.github.io/nycedc-grocery/

## Contents

- `source/` — source markdown templates and downloadable form files
- `docs/` — generated HTML site published by GitHub Pages
- `tools/render_site.py` — renderer that converts the markdown packet into HTML

## Publishing

The site is intended to be published from the `docs/` directory via GitHub Pages.

To rebuild locally:

```bash
python3 -m venv .venv-site
source .venv-site/bin/activate
python -m pip install markdown
python tools/render_site.py
```
