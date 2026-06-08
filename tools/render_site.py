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
    Page(
        "07_partner-firm-shortlist.md",
        "partner-firm-shortlist.html",
        "Partner-firm shortlist",
        "Verified NYC M/WBE branding & design firms scored against the RFP scope.",
    ),
    Page(
        "08_appendix6-pricing-worksheet.md",
        "appendix6-pricing-worksheet.html",
        "Appendix 6 pricing worksheet",
        "Task-based cost build-up behind the Appendix 6 totals, with the 30% M/WBE reconciliation.",
    ),
    Page(
        "09_win-strategy.md",
        "win-strategy.html",
        "Win strategy",
        "How the award is scored and the themes that win it for DoChakki.",
    ),
    Page(
        "10_proposal-narrative.md",
        "proposal-narrative.html",
        "Proposal narrative",
        "The ≤30-page proposal structure and approach, with evidence slots to fill.",
    ),
    Page(
        "11_mwbe-plan.md",
        "mwbe-plan.html",
        "M/WBE plan",
        "How to fill Appendix 3 & 4 and clear the 30% goal credibly.",
    ),
    Page(
        "12_project-checklist.md",
        "project-checklist.html",
        "Project checklist",
        "Phased to-do from today to the June 30 submission, with owners and deadlines.",
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
    (
        ROOT / "source" / "partner-templates" / "08_appendix6-pricing-worksheet.csv",
        DOWNLOADS / "appendix6-pricing-worksheet.csv",
    ),
]


OFFICIAL_FORM_FILES = [
    "Doing-Business-Data-Form.pdf",
    "Intent-to-Perform-as-Subcontractor.pdf",
    "MWBE-DBE-Participation-Plan-03-13-2025.xlsx",
    "MWBE-Narrative-Form-03-13-2025.docx",
]


@dataclass(frozen=True)
class Step:
    title: str
    blurb: str
    link: str
    link_label: str
    tag: str


# The partner-recruitment journey for DoChakki. Each step links to the artifact that does it.
FLOW = [
    Step(
        "Pick your partners",
        "Open the verified shortlist and recruit Two Twelve first — the one firm that's both "
        "M/WBE-certified and covers the environmental-design gap DoChakki needs for Tasks 2B and 3.",
        "partner-firm-shortlist.html",
        "See the shortlist",
        "Shortlist",
    ),
    Step(
        "Reach out",
        "Send a warm, specific intro with the outreach email. Lead with the civic mission and name "
        "the exact slice of scope you want each firm to own.",
        "partner-outreach-email-template.html",
        "Use the outreach email",
        "Email template",
    ),
    Step(
        "Lock in their interest",
        "Get a short Letter of Intent signed so the partnership is real before you invest in official "
        "paperwork or name them in the proposal.",
        "partner-loi-template.html",
        "Open the LOI template",
        "LOI",
    ),
    Step(
        "Collect their details",
        "Run the intake checklist to capture EIN, NAICS codes, M/WBE certificate, references, and "
        "signatory — exactly the fields the official forms demand.",
        "partner-intake-checklist.html",
        "Open the intake checklist",
        "Checklist",
    ),
    Step(
        "Confirm scope & value",
        "Prep each firm's Intent-to-Perform with the specific work and dollar amount they'll deliver "
        "as a subconsultant.",
        "intent-to-perform-prep-template.html",
        "Prep Intent-to-Perform",
        "Intent-to-Perform",
    ),
    Step(
        "Build the team plan",
        "Drop every firm into the participation plan and confirm the team clears the 30% M/WBE goal "
        "before anything is finalized.",
        "partner-submission-map.html",
        "Review the submission map",
        "Participation plan",
    ),
    Step(
        "Price the proposal",
        "Fold partner quotes into the Appendix 6 task-based pricing build-up so the 30% M/WBE math and "
        "the cost form agree.",
        "appendix6-pricing-worksheet.html",
        "Open the pricing worksheet",
        "Pricing",
    ),
]


STYLE = """
:root {
  color-scheme: light;
  --paper: #fbfaf6;
  --paper-2: #f4f2e9;
  --card: #ffffff;
  --ink: #1a1b16;
  --muted: #6c7063;
  --line: #e7e3d6;
  --line-soft: #efece2;
  --accent: #1f7a4d;
  --accent-ink: #14542f;
  --accent-soft: #e7f2ea;
  --warm: #d8531d;
  --warm-soft: #fae9df;
  --max: 1080px;
  --shadow: 0 12px 30px rgba(31, 35, 25, 0.07);
  --radius: 16px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 16px/1.62 "Public Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  -webkit-font-smoothing: antialiased;
  background-image:
    radial-gradient(1200px 480px at 88% -8%, var(--accent-soft) 0%, transparent 60%),
    radial-gradient(900px 420px at -6% -10%, var(--warm-soft) 0%, transparent 55%);
  background-repeat: no-repeat;
}
h1, h2, h3, h4 {
  font-family: Fraunces, Georgia, "Times New Roman", serif;
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.18;
}
a { color: var(--accent-ink); text-decoration: none; }
a:hover { text-decoration: underline; }
code, pre { font: 0.92em/1.55 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
pre, code { background: var(--paper-2); border-radius: 8px; }
code { padding: 0.14rem 0.36rem; }
pre { padding: 1rem; overflow-x: auto; border: 1px solid var(--line); }

/* ---- top accent rail + header ---- */
.topbar { height: 5px; background: linear-gradient(90deg, var(--accent) 0%, #3a9e6c 55%, var(--warm) 100%); }
.header-wrap, .wrap { width: min(calc(100% - 2.2rem), var(--max)); margin: 0 auto; }
header { background: transparent; border-bottom: 1px solid var(--line); }
.header-wrap { padding: 2.6rem 0 1.4rem; }
.eyebrow {
  display: inline-flex; align-items: center; gap: 0.45rem;
  padding: 0.28rem 0.7rem; border-radius: 999px;
  background: var(--accent-soft); color: var(--accent-ink);
  font-size: 0.78rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase;
}
.eyebrow::before { content: ""; width: 7px; height: 7px; border-radius: 50%; background: var(--accent); }
h1 { margin: 0.85rem 0 0.55rem; font-size: clamp(2.1rem, 4.4vw, 3.4rem); }
h1 .accent { color: var(--accent); font-style: italic; }
.lede { max-width: 50rem; margin: 0; color: var(--muted); font-size: 1.06rem; }

/* ---- nav ---- */
nav { padding: 1.1rem 0 0.2rem; }
.nav-list { display: flex; flex-wrap: wrap; gap: 0.5rem; list-style: none; margin: 0; padding: 0; }
.nav-list a {
  display: inline-block; padding: 0.46rem 0.85rem; border-radius: 999px;
  background: var(--card); border: 1px solid var(--line); color: var(--muted);
  font-size: 0.92rem; transition: all 0.16s ease;
}
.nav-list a:hover { color: var(--ink); border-color: var(--accent); text-decoration: none; transform: translateY(-1px); }
.nav-list a.active { background: var(--ink); color: #fff; border-color: var(--ink); font-weight: 600; }

main.wrap { padding: 1.8rem 0 3.5rem; }
.stack { display: grid; gap: 1.25rem; }
.card {
  background: var(--card); border: 1px solid var(--line); border-radius: var(--radius);
  padding: 1.5rem 1.6rem; box-shadow: var(--shadow);
}
.card > :first-child { margin-top: 0; }
.card > :last-child { margin-bottom: 0; }
.meta { margin: 0 0 1.1rem; color: var(--muted); }
.grid { display: grid; gap: 1.25rem; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }

/* ---- deadline banner ---- */
.alert {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.6rem 1rem;
  background: var(--warm-soft); border: 1px solid #f0c9b6; border-left: 5px solid var(--warm);
  border-radius: 14px; padding: 0.95rem 1.2rem; color: #7a2f12;
}
.alert strong { color: #7a2f12; }
.alert .tag {
  background: var(--warm); color: #fff; font-size: 0.72rem; font-weight: 700;
  letter-spacing: 0.05em; text-transform: uppercase; padding: 0.22rem 0.55rem; border-radius: 999px;
}

/* ---- section heading ---- */
.section-head { margin: 0.5rem 0 0; }
.section-head h2 { margin: 0; font-size: clamp(1.5rem, 2.6vw, 2rem); }
.section-head p { margin: 0.4rem 0 0; color: var(--muted); max-width: 46rem; }

/* ---- the partner flow (vertical timeline) ---- */
.flow { position: relative; margin: 1.4rem 0 0; padding: 0; list-style: none; }
.flow::before {
  content: ""; position: absolute; left: 23px; top: 18px; bottom: 30px; width: 2px;
  background: linear-gradient(180deg, var(--accent) 0%, var(--line) 100%);
}
.step { position: relative; padding: 0 0 1.2rem 4rem; animation: rise 0.55s cubic-bezier(0.2, 0.7, 0.2, 1) both; }
.step .num {
  position: absolute; left: 0; top: 0; width: 48px; height: 48px; border-radius: 50%;
  display: grid; place-items: center; background: var(--card); border: 2px solid var(--accent);
  color: var(--accent-ink); font-family: Fraunces, serif; font-weight: 600; font-size: 1.2rem;
  box-shadow: 0 4px 12px rgba(31, 122, 77, 0.18); z-index: 1;
}
.step-card {
  background: var(--card); border: 1px solid var(--line); border-radius: 14px;
  padding: 1.05rem 1.2rem; transition: border-color 0.16s ease, transform 0.16s ease, box-shadow 0.16s ease;
}
.step-card:hover { border-color: var(--accent); transform: translateX(3px); box-shadow: var(--shadow); }
.step.start .num { background: var(--accent); color: #fff; }
.step.start .step-card { border-color: var(--accent); background: linear-gradient(180deg, var(--accent-soft) 0%, var(--card) 60%); }
.step h3 { margin: 0 0 0.3rem; font-size: 1.16rem; }
.step p { margin: 0 0 0.7rem; color: var(--muted); }
.step .tag {
  display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
  color: var(--accent-ink); background: var(--accent-soft); padding: 0.2rem 0.55rem; border-radius: 999px; margin-bottom: 0.55rem;
}
.step-link {
  display: inline-flex; align-items: center; gap: 0.35rem; font-weight: 600; font-size: 0.94rem; color: var(--accent-ink);
}
.step-link::after { content: "\\2192"; transition: transform 0.16s ease; }
.step-card:hover .step-link::after { transform: translateX(3px); }
.flow-end {
  margin: 0.2rem 0 0; padding: 1rem 1.2rem 1rem 4rem; position: relative; color: var(--muted);
}
.flow-end .num {
  position: absolute; left: 0; top: 0; width: 48px; height: 48px; border-radius: 50%;
  display: grid; place-items: center; background: var(--ink); color: #fff; font-family: Fraunces, serif; z-index: 1;
}
.flow-end strong { color: var(--ink); }

@keyframes rise { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
@media (prefers-reduced-motion: reduce) { .step { animation: none; } html { scroll-behavior: auto; } }

/* ---- lists for pages/downloads ---- */
.download-list, .page-list { list-style: none; margin: 0; padding: 0; display: grid; gap: 0.7rem; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.download-list li, .page-list li {
  padding: 1rem 1.1rem; border: 1px solid var(--line); border-radius: 14px; background: var(--card);
  transition: border-color 0.16s ease, transform 0.16s ease;
}
.download-list li:hover, .page-list li:hover { border-color: var(--accent); transform: translateY(-2px); }
.page-list p, .download-list p { margin: 0.35rem 0 0; color: var(--muted); font-size: 0.94rem; }
.pill {
  display: inline-block; margin-bottom: 0.45rem; padding: 0.16rem 0.55rem; border-radius: 999px;
  background: var(--paper-2); color: var(--muted); font-size: 0.72rem; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase;
}

/* ---- breadcrumb on subpages ---- */
.crumb { margin: 0 0 1rem; font-size: 0.92rem; }
.crumb a { color: var(--muted); }

/* ---- prose ---- */
ul, ol { padding-left: 1.25rem; }
li + li { margin-top: 0.3rem; }
table { width: 100%; border-collapse: collapse; margin: 1.1rem 0; background: var(--card); font-size: 0.95rem; }
th, td { border: 1px solid var(--line); padding: 0.6rem 0.7rem; text-align: left; vertical-align: top; }
th { background: var(--accent-soft); color: var(--accent-ink); font-family: "Public Sans"; }
tr:nth-child(even) td { background: #fcfbf7; }
blockquote { margin: 1.1rem 0; padding: 0.85rem 1.1rem; border-left: 4px solid var(--accent); background: var(--accent-soft); border-radius: 0 10px 10px 0; }
hr { border: none; border-top: 1px solid var(--line); margin: 1.6rem 0; }
footer { padding: 1.4rem 0 2.8rem; color: var(--muted); font-size: 0.92rem; border-top: 1px solid var(--line); margin-top: 1rem; }
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
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/site.css">
  </head>
  <body>
    <div class="topbar"></div>
    <header>
      <div class="header-wrap">
        <span class="eyebrow">DoChakki &middot; NYCEDC partner packet</span>
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
        (
            "Appendix 6 pricing worksheet",
            "downloads/appendix6-pricing-worksheet.csv",
            "Task-based cost build-up CSV with the 30% M/WBE reconciliation.",
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

    step_items = []
    for idx, step in enumerate(FLOW, start=1):
        start_cls = " start" if idx == 1 else ""
        delay = f"{0.04 * idx:.2f}s"
        step_items.append(
            f"""
            <li class="step{start_cls}" style="animation-delay: {delay}">
              <span class="num">{idx}</span>
              <div class="step-card">
                <span class="tag">{escape(step.tag)}</span>
                <h3>{escape(step.title)}</h3>
                <p>{escape(step.blurb)}</p>
                <a class="step-link" href="{escape(step.link)}">{escape(step.link_label)}</a>
              </div>
            </li>
            """
        )

    body = f"""
    <section class="stack">
      <div class="alert">
        <span class="tag">Next deadline</span>
        <span><strong>Clarification questions due Friday, June 12, 2026, 5:00 PM ET</strong> &mdash;
        email <a href="draft-questions-to-nycedc.html">the 8 drafted questions</a> to GroceriesBrandDesign@edc.nyc.</span>
      </div>

      <div class="section-head">
        <h2>Bring on partners &amp; collaborators for DoChakki</h2>
        <p>A clear, ordered path from "who do we partner with?" to a priced, M/WBE-compliant team.
        Each step opens the exact template that does the work.</p>
      </div>

      <ol class="flow">
        {''.join(step_items)}
        <li class="flow-end">
          <span class="num">&#10003;</span>
          <strong>Submit by Tuesday, June 30, 2026, 4:00 PM ET</strong> &mdash; one zip, searchable PDF,
          all required appendices, M/WBE participation at or above 30%.
        </li>
      </ol>

      <div class="section-head">
        <h2>Then: win the proposal</h2>
        <p>Assembling the team is the setup. These three move the bid from compliant to competitive &mdash;
        they target the 75% of the score that's experience and proposal quality.</p>
      </div>
      <div class="grid">
        <div class="card">
          <span class="pill">Strategy</span>
          <h3><a href="win-strategy.html">Win strategy &amp; themes</a></h3>
          <p>How NYCEDC scores the award (40/35/15/5/5) and the four themes that win it for DoChakki.</p>
        </div>
        <div class="card">
          <span class="pill">Narrative</span>
          <h3><a href="proposal-narrative.html">Proposal narrative</a></h3>
          <p>The &le;30-page structure and per-task approach, drafted &mdash; with the evidence slots DoChakki fills in.</p>
        </div>
        <div class="card">
          <span class="pill">M/WBE</span>
          <h3><a href="mwbe-plan.html">M/WBE plan</a></h3>
          <p>How to fill Appendix 3 &amp; 4 and clear 30% credibly, tied to the pricing worksheet.</p>
        </div>
      </div>

      <div class="grid">
        <div class="card">
          <h2>What's in this packet</h2>
          <ul>
            <li>A step-by-step partner-recruitment flow with ready-to-use templates</li>
            <li>A verified shortlist of NYC M/WBE branding &amp; design firms</li>
            <li>Official NYCEDC forms and the original RFP, ready to download</li>
            <li>An Appendix 6 pricing worksheet with the 30% M/WBE check built in</li>
          </ul>
        </div>
        <div class="card">
          <h2>Verified facts</h2>
          <ul>
            <li><strong>Questions due:</strong> June 12, 2026, 5:00 PM ET</li>
            <li><strong>Proposal due:</strong> June 30, 2026, 4:00 PM ET</li>
            <li><strong>M/WBE goal:</strong> 30% of contract value</li>
            <li><strong>Proposal cap:</strong> 30 pages, excluding appendices</li>
            <li><strong>Do not</strong> pitch brand concepts in the proposal</li>
          </ul>
        </div>
      </div>

      <div class="card">
        <h2>All pages</h2>
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
        <p class="crumb"><a href="index.html">&larr; Partner packet home</a></p>
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
