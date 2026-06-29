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
@page { size: A4; margin: 11mm 10mm; }
* { box-sizing: border-box; }
body {
  font-family: "Segoe UI", Arial, Helvetica, sans-serif;
  font-size: 9.6pt;
  line-height: 1.35;
  color: #1a1a1a;
  margin: 0;
}
a { color: #1a4f8b; text-decoration: none; }
a:hover { text-decoration: underline; }
.cv-header {
  border-bottom: 2px solid #1a4f8b;
  padding-bottom: 7pt;
  margin-bottom: 9pt;
}
.cv-header h1 {
  font-size: 21pt;
  font-weight: 700;
  margin: 0;
  line-height: 1.1;
}
.cv-header p {
  margin: 3pt 0 0;
  font-size: 10.5pt;
  color: #444;
}
.cv-grid {
  display: grid;
  grid-template-columns: 30% 1fr;
  gap: 14pt;
  align-items: start;
}
.cv-side {
  background: #f3f5f8;
  padding: 9pt 9pt 11pt;
  border-radius: 3pt;
  border: 1px solid #e2e8ef;
}
.cv-side h2 {
  font-size: 9pt;
  text-transform: uppercase;
  letter-spacing: 0.55pt;
  color: #1a4f8b;
  margin: 0 0 5pt;
  padding-bottom: 2pt;
  border-bottom: 1px solid #c5d0dc;
}
.cv-side h2:not(:first-child) { margin-top: 10pt; }
.cv-side p { margin: 0 0 4pt; font-size: 9pt; }
.cv-side ul { margin: 0; padding-left: 13pt; }
.cv-side li { margin-bottom: 2pt; font-size: 9pt; }
.cv-main h2 {
  font-size: 10.5pt;
  color: #1a4f8b;
  margin: 0 0 5pt;
  padding-bottom: 2pt;
  border-bottom: 1px solid #d0d8e0;
}
.cv-main h2:not(:first-child) { margin-top: 10pt; }
.cv-main h3 {
  font-size: 9.8pt;
  font-weight: 600;
  margin: 8pt 0 2pt;
  color: #222;
  line-height: 1.25;
}
.cv-main p { margin: 3pt 0 5pt; }
.cv-main ul { margin: 2pt 0 5pt; padding-left: 14pt; }
.cv-main li { margin-bottom: 2pt; }
.cv-main strong { font-weight: 600; }
.cv-main em { font-style: italic; color: #444; }
.cv-focus ul { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 2pt 8pt; }
.cv-focus li { margin: 0; font-size: 9.3pt; }
.cv-footer {
  margin-top: 8pt;
  padding-top: 5pt;
  border-top: 1px solid #e0e0e0;
  text-align: center;
  font-size: 8pt;
  color: #666;
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


def render_md(fragment: str) -> str:
    html = markdown.markdown(
        fragment,
        extensions=["sane_lists", "nl2br"],
    )
    # Schwerpunkte: two-column checklist
    html = html.replace(
        '<h2>Schwerpunkte</h2>',
        '<h2>Schwerpunkte</h2><div class="cv-focus">',
        1,
    )
    if '<div class="cv-focus">' in html:
        html = re.sub(
            r"(<div class=\"cv-focus\">.*?)(<h2>)",
            r"\1</div>\2",
            html,
            count=1,
            flags=re.DOTALL,
        )
    return html


def build_html(md_text: str) -> str:
    header_md, sidebar_md, main_md, footer_md = split_source(md_text)
    header_html = render_md(header_md)
    sidebar_html = render_md(sidebar_md)
    main_html = render_md(main_md)
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
