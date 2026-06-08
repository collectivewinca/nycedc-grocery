from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
import shutil

import markdown


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
PARTNER_TEMPLATES = SOURCE / "partner-templates"
OFFICIAL_FORMS = SOURCE / "official-nycedc-forms"
SITE = ROOT / "docs"
DOWNLOADS = SITE / "downloads"
ASSETS = SITE / "assets"


SITE_TITLE = "NYCEDC N.Y.C. Groceries RFP Partner Packet"
SITE_DESCRIPTION = (
    "Submission-ready partner templates, verified requirements, and official NYCEDC forms "
    "for the N.Y.C. Groceries Branding & Design Consultant RFP."
)


@dataclass(frozen=True)
class Page:
    source_name: str
    output_name: str
    title: str
    summary: str


PAGES = [
    Page(
        "00_partner-submission-map.md",
        "partner-submission-map.html",
        "Partner submission map",
        "Verified requirements, signed-form expectations, and what to collect from each partner.",
    ),
    Page(
        "01_partner-outreach-email-template.md",
        "partner-outreach-email-template.html",
        "Partner outreach email template",
        "Starter outreach language for recruiting aligned partners quickly.",
    ),
    Page(
        "02_partner-loi-template.md",
        "partner-loi-template.html",
        "Partner LOI template",
        "A short letter of intent template for locking participation before the official forms.",
    ),
    Page(
        "03_intent-to-perform-prep-template.md",
        "intent-to-perform-prep-template.html",
        "Intent-to-Perform prep template",
        "A fast intake version of the official NYCEDC subcontractor intent form.",
    ),
    Page(
        "04_partner-intake-checklist.md",
        "partner-intake-checklist.html",
        "Partner intake checklist",
        "Structured intake fields for pricing, certifications, references, and signatures.",
    ),
    Page(
        "05_draft-questions-to-nycedc.md",
        "draft-questions-to-nycedc.html",
        "Draft questions to NYCEDC",
        "Clarification questions to send before the RFP inquiry deadline.",
    ),
]


DOWNLOAD_FILES = [
    (
        ROOT / "source" / "NYC Groceries Branding Design Consultant RFP.pdf",
        DOWNLOADS / "NYC-Groceries-Branding-Design-Consultant-RFP.pdf",
    ),
    (
        ROOT / "source" / "partner-templates" / "06_participation-plan-working-sheet.csv",
        DOWNLOADS / "participation-plan-working-sheet.csv",
    ),
]


OFFICIAL_FORM_FILES = [
    "Doing-Business-Data-Form.pdf",
    "Intent-to-Perform-as-Subcontractor.pdf",
    "MWBE-DBE-Participation-Plan-03-13-2025.xlsx",
    "MWBE-Narrative-Form-03-13-2025.docx",
]


STYLE = """
:root {
  color-scheme: light;
  --bg: #f6f7fb;
  --panel: #ffffff;
  --text: #18212f;
  --muted: #586174;
  --line: #d9e1ee;
  --accent: #2457ff;
  --accent-soft: #e9efff;
  --max: 1040px;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 16px/1.6 Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
code, pre {
  font: 0.95em/1.55 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
pre, code {
  background: #f2f5fa;
  border-radius: 8px;
}
code { padding: 0.14rem 0.34rem; }
pre { padding: 1rem; overflow-x: auto; }
header {
  background: linear-gradient(180deg, #0d1b4c 0%, #182a73 100%);
  color: white;
}
.header-wrap, .wrap {
  width: min(calc(100% - 2rem), var(--max));
  margin: 0 auto;
}
.header-wrap { padding: 2.25rem 0 1.5rem; }
.eyebrow {
  display: inline-block;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.15);
  font-size: 0.85rem;
  letter-spacing: 0.02em;
}
h1 { margin: 0.75rem 0 0.5rem; font-size: clamp(1.9rem, 3vw, 3rem); line-height: 1.15; }
.lede {
  max-width: 52rem;
  margin: 0;
  color: rgba(255,255,255,0.86);
}
nav {
  padding: 0.8rem 0 1rem;
}
.nav-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.nav-list a {
  display: inline-block;
  padding: 0.48rem 0.8rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.09);
  color: white;
}
.nav-list a.active {
  background: white;
  color: #14245f;
  font-weight: 600;
}
main.wrap { padding: 1.4rem 0 3rem; }
.card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 1.25rem 1.35rem;
  box-shadow: 0 8px 24px rgba(17, 24, 39, 0.05);
}
.stack { display: grid; gap: 1rem; }
.meta {
  margin: 0 0 1rem;
  color: var(--muted);
}
.grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
.grid .card h2, .grid .card h3 { margin-top: 0; }
ul, ol { padding-left: 1.3rem; }
li + li { margin-top: 0.3rem; }
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  background: white;
}
th, td {
  border: 1px solid var(--line);
  padding: 0.65rem 0.7rem;
  text-align: left;
  vertical-align: top;
}
th { background: #f7f9fd; }
.download-list, .page-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.85rem;
}
.download-list li, .page-list li {
  padding: 0.95rem 1rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: #fbfcff;
}
.page-list p, .download-list p { margin: 0.35rem 0 0; color: var(--muted); }
.pill {
  display: inline-block;
  margin-right: 0.4rem;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
  background: var(--accent-soft);
  color: #2244b4;
  font-size: 0.83rem;
  font-weight: 600;
}
footer {
  padding: 1rem 0 2.5rem;
  color: var(--muted);
  font-size: 0.95rem;
}
blockquote {
  margin: 1rem 0;
  padding: 0.8rem 1rem;
  border-left: 4px solid var(--accent);
  background: #f7f9ff;
}
"""


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def render_markdown(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "sane_lists", "nl2br"],
    )


def nav_links(current: str) -> str:
    items = ['<li><a href="index.html"{}>Home</a></li>'.format(' class="active"' if current == "index.html" else "")]
    for page in PAGES:
        cls = ' class="active"' if current == page.output_name else ""
        items.append(f'<li><a href="{escape(page.output_name)}"{cls}>{escape(page.title)}</a></li>')
    return '<ul class="nav-list">' + "".join(items) + "</ul>"


def layout(title: str, body: str, current: str, description: str) -> str:
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{escape(title)} | {escape(SITE_TITLE)}</title>
    <meta name="description" content="{escape(description)}">
    <link rel="stylesheet" href="assets/site.css">
  </head>
  <body>
    <header>
      <div class="header-wrap">
        <span class="eyebrow">GitHub Pages packet</span>
        <h1>{escape(SITE_TITLE)}</h1>
        <p class="lede">{escape(SITE_DESCRIPTION)}</p>
        <nav aria-label="Primary">
          {nav_links(current)}
        </nav>
      </div>
    </header>
    <main class="wrap">
      {body}
    </main>
    <footer class="wrap">
      Built from the verified NYCEDC RFP packet and current vendor-resource forms.
    </footer>
  </body>
</html>
"""


def build_index() -> None:
    page_items = []
    for page in PAGES:
        page_items.append(
            f"""
            <li>
              <span class="pill">HTML page</span>
              <a href="{escape(page.output_name)}"><strong>{escape(page.title)}</strong></a>
              <p>{escape(page.summary)}</p>
            </li>
            """
        )

    download_items = [
        (
            "NYC Groceries RFP PDF",
            "downloads/NYC-Groceries-Branding-Design-Consultant-RFP.pdf",
            "Original solicitation packet.",
        ),
        (
            "Participation plan working sheet",
            "downloads/participation-plan-working-sheet.csv",
            "Working CSV for building the Appendix 4 team list.",
        ),
    ]

    for form_name in OFFICIAL_FORM_FILES:
        download_items.append(
            (
                form_name,
                f"downloads/official-nycedc-forms/{form_name}",
                "Official NYCEDC form copied from Vendor Resources.",
            )
        )

    downloads_html = "".join(
        f"""
        <li>
          <span class="pill">Download</span>
          <a href="{escape(href)}"><strong>{escape(name)}</strong></a>
          <p>{escape(summary)}</p>
        </li>
        """
        for name, href, summary in download_items
    )

    body = f"""
    <section class="stack">
      <div class="card">
        <p class="meta">This site publishes the partner packet created from the NYCEDC N.Y.C. Groceries Branding &amp; Design Consultant RFP, including official forms, outreach templates, intake tools, and draft clarification questions.</p>
        <div class="grid">
          <div class="card">
            <h2>What is here</h2>
            <ul>
              <li>Converted HTML versions of the partner packet markdown files</li>
              <li>Official NYCEDC forms copied into downloadable links</li>
              <li>The original RFP PDF and a working participation-plan CSV</li>
            </ul>
          </div>
          <div class="card">
            <h2>Critical verified points</h2>
            <ul>
              <li>Questions due June 12, 2026 at 5:00 PM ET</li>
              <li>Proposal due June 30, 2026 at 4:00 PM ET</li>
              <li>M/WBE goal is 30%</li>
              <li>The participation plan form states that an Intent to Perform form is included for each listed firm</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="card">
        <h2>Pages</h2>
        <ul class="page-list">
          {''.join(page_items)}
        </ul>
      </div>

      <div class="card">
        <h2>Downloads</h2>
        <ul class="download-list">
          {downloads_html}
        </ul>
      </div>
    </section>
    """
    write_text(SITE / "index.html", layout("Home", body, "index.html", SITE_DESCRIPTION))


def build_pages() -> None:
    for page in PAGES:
        md_path = PARTNER_TEMPLATES / page.source_name
        html = render_markdown(md_path.read_text(encoding="utf-8"))
        body = f"""
        <article class="card">
          <p class="meta">{escape(page.summary)}</p>
          {html}
        </article>
        """
        write_text(SITE / page.output_name, layout(page.title, body, page.output_name, page.summary))


def copy_downloads() -> None:
    for src, dst in DOWNLOAD_FILES:
        copy_file(src, dst)
    for form_name in OFFICIAL_FORM_FILES:
        copy_file(OFFICIAL_FORMS / form_name, DOWNLOADS / "official-nycedc-forms" / form_name)


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    write_text(ASSETS / "site.css", STYLE.strip() + "\n")
    write_text(SITE / ".nojekyll", "")
    copy_downloads()
    build_pages()
    build_index()


if __name__ == "__main__":
    main()
