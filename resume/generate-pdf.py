#!/usr/bin/env python3
"""Generate lebenslauf.pdf from lebenslauf.md (Chrome headless)."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import markdown

CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
MD_FILE = Path(__file__).with_name("lebenslauf.md")
HTML_FILE = Path(__file__).with_name("lebenslauf.html")
PDF_FILE = Path(__file__).with_name("lebenslauf.pdf")

MARKER_SIDEBAR = "<!-- pdf-sidebar -->"
MARKER_MAIN = "<!-- pdf-main -->"
MARKER_FOOTER = "<!-- pdf-footer -->"

CSS = """
@page { size: A4; margin: 10mm 9mm; }
* { box-sizing: border-box; }
:root {
  --accent: #1d4ed8;
  --accent-light: #3b82f6;
  --accent-soft: #eff6ff;
  --side-bg: #f8fafc;
  --side-border: #e2e8f0;
  --text: #1e293b;
  --muted: #64748b;
  --card-bg: #f8fafc;
}
body {
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 9.4pt;
  line-height: 1.38;
  color: var(--text);
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
a { color: var(--accent); text-decoration: none; }
.cv-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 12pt;
  padding-bottom: 8pt;
  margin-bottom: 10pt;
  border-bottom: 3pt solid var(--accent);
}
.cv-header h1 {
  font-size: 22pt;
  font-weight: 700;
  margin: 0;
  line-height: 1.05;
  color: #0f172a;
  letter-spacing: -0.3pt;
}
.cv-header p {
  margin: 4pt 0 0;
  font-size: 10.5pt;
  color: var(--muted);
}
.cv-header p strong { color: var(--accent); font-weight: 600; }
.cv-grid {
  display: grid;
  grid-template-columns: 28% 1fr;
  gap: 12pt;
  align-items: start;
}
.cv-side {
  background: var(--side-bg);
  padding: 10pt 9pt 12pt;
  border-radius: 5pt;
  border: 1px solid var(--side-border);
  border-top: 3pt solid var(--accent-light);
}
.cv-side h2 {
  font-size: 8.2pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.6pt;
  color: #fff;
  background: linear-gradient(90deg, var(--accent) 0%, var(--accent-light) 100%);
  margin: 0 0 6pt;
  padding: 3pt 6pt;
  border-radius: 3pt;
}
.cv-side h2:not(:first-child) { margin-top: 9pt; }
.cv-side p { margin: 0 0 4pt; font-size: 8.8pt; line-height: 1.4; }
.cv-side ul { margin: 0; padding-left: 12pt; }
.cv-side li { margin-bottom: 2pt; font-size: 8.8pt; }
.cv-main h2 {
  font-size: 8.8pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.55pt;
  color: #fff;
  background: linear-gradient(90deg, var(--accent) 0%, var(--accent-light) 100%);
  margin: 0 0 6pt;
  padding: 3.5pt 7pt;
  border-radius: 3pt;
  border: none;
}
.cv-main h2:not(:first-child) { margin-top: 9pt; }
.cv-main h3 {
  font-size: 9.6pt;
  font-weight: 600;
  margin: 7pt 0 3pt;
  padding: 4pt 7pt;
  color: #0f172a;
  line-height: 1.28;
  background: var(--card-bg);
  border-left: 3pt solid var(--accent-light);
  border-radius: 0 4pt 4pt 0;
}
.cv-main p { margin: 3pt 0 5pt; }
.cv-main ul { margin: 2pt 0 5pt; padding-left: 14pt; }
.cv-main li { margin-bottom: 2.5pt; }
.cv-main strong { font-weight: 600; color: #0f172a; }
.cv-main em { font-style: italic; color: var(--muted); }
.cv-overview ul {
  list-style: none;
  padding-left: 0;
  margin: 2pt 0 6pt;
  display: block;
}
.cv-overview li {
  margin: 0 0 2pt;
  font-size: 8.8pt;
  line-height: 1.35;
  padding-left: 11pt;
  position: relative;
}
.cv-overview li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: var(--accent);
  font-weight: 700;
}
.cv-project-list {
  list-style: none !important;
  margin: 0 0 5pt 0 !important;
  padding-left: 0 !important;
}
.cv-project-list li {
  font-size: 8.7pt;
  margin-bottom: 1.5pt;
  padding-left: 11pt;
  position: relative;
}
.cv-project-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: var(--accent);
  font-weight: 700;
}
.cv-project-title {
  font-weight: 600;
  font-size: 9.2pt;
  color: #0f172a;
  margin: 5pt 0 1pt;
}
.cv-project-title em { font-weight: 500; }
.cv-overview {
  break-inside: avoid;
}
.cv-projects ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4pt;
}
.cv-projects li {
  margin: 0;
  font-size: 8.8pt;
  padding: 4pt 6pt;
  background: #fff;
  border: 1px solid var(--side-border);
  border-left: 2.5pt solid var(--accent-light);
  border-radius: 0 4pt 4pt 0;
  line-height: 1.3;
}
.cv-skills p {
  margin: 0 0 4pt;
  padding: 3pt 6pt;
  background: var(--card-bg);
  border-radius: 3pt;
  font-size: 8.8pt;
  line-height: 1.35;
}
.cv-skills strong {
  display: inline-block;
  min-width: 78pt;
  color: var(--accent);
  font-size: 8.2pt;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
}
.cv-footer {
  margin-top: 7pt;
  padding-top: 5pt;
  border-top: 1px solid var(--side-border);
  text-align: center;
  font-size: 7.8pt;
  color: var(--muted);
}
.cv-footer p { margin: 0; }
"""


def strip_markers(text: str) -> str:
    for marker in (MARKER_SIDEBAR, MARKER_MAIN, MARKER_FOOTER):
        text = text.replace(marker, "")
    return text.strip()


def split_source(text: str) -> tuple[str, str, str, str]:
    if MARKER_SIDEBAR not in text or MARKER_MAIN not in text:
        raise ValueError("lebenslauf.md must contain pdf-sidebar and pdf-main markers")

    header_part, rest = text.split(MARKER_SIDEBAR, 1)
    sidebar_part, rest = rest.split(MARKER_MAIN, 1)
    if MARKER_FOOTER in rest:
        main_part, footer_part = rest.split(MARKER_FOOTER, 1)
    else:
        main_part, footer_part = rest, ""

    return (
        header_part.strip(),
        sidebar_part.strip(),
        main_part.strip(),
        footer_part.strip(),
    )


def _wrap_section(html: str, heading: str, css_class: str) -> str:
    needle = f"<h2>{heading}</h2>"
    if needle not in html:
        return html
    html = html.replace(needle, f"{needle}<div class=\"{css_class}\">", 1)
    return re.sub(
        rf'(<div class="{css_class}">.*?)(<h2>)',
        r"\1</div>\2",
        html,
        count=1,
        flags=re.DOTALL,
    )


def render_md(fragment: str, *, is_main: bool = False) -> str:
    html = markdown.markdown(
        fragment,
        extensions=["sane_lists", "nl2br"],
    )
    if is_main:
        html = _wrap_section(html, "Kernbereiche", "cv-overview")
        html = _wrap_section(html, "Ausgewählte Projekte", "cv-projects")
        html = _wrap_section(html, "Fachkenntnisse", "cv-skills")
        html = _style_freelance_projects(html)
    return html


def _style_freelance_projects(html: str) -> str:
    """Turn bold-only paragraphs + following ul into compact project blocks."""
    pattern = re.compile(
        r"<p><strong>([^<]+)</strong>(\s*<em>[^<]*</em>)?\s*</p>\s*<ul>",
        re.IGNORECASE,
    )
    return pattern.sub(
        r'<p class="cv-project-title"><strong>\1</strong>\2</p><ul class="cv-project-list">',
        html,
    )


def build_html(md_text: str) -> str:
    header_md, sidebar_md, main_md, footer_md = split_source(md_text)
    header_html = render_md(header_md)
    sidebar_html = render_md(sidebar_md)
    main_html = render_md(main_md, is_main=True)
    footer_html = markdown.markdown(footer_md, extensions=["sane_lists"]) if footer_md else ""

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>Lebenslauf — Alex Borissov</title>
<style>{CSS}</style>
</head>
<body>
<header class="cv-header">{header_html}</header>
<div class="cv-grid">
<aside class="cv-side">{sidebar_html}</aside>
<main class="cv-main">{main_html}</main>
</div>
<footer class="cv-footer">{footer_html}</footer>
</body>
</html>
"""


def main() -> int:
    if not MD_FILE.is_file():
        print(f"Missing {MD_FILE}", file=sys.stderr)
        return 1
    if not CHROME.is_file():
        print(f"Chrome not found at {CHROME}", file=sys.stderr)
        return 1

    md_text = MD_FILE.read_text(encoding="utf-8")
    html = build_html(md_text)
    HTML_FILE.write_text(html, encoding="utf-8")

    subprocess.run(
        [
            str(CHROME),
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={PDF_FILE.resolve()}",
            HTML_FILE.resolve().as_uri(),
        ],
        check=True,
    )
    # Keep HTML for debugging if needed: HTML_FILE.unlink(missing_ok=True)
    print(f"Created {PDF_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
