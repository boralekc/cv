#!/usr/bin/env python3
"""Generate lebenslauf.pdf from lebenslauf.md (Chrome headless)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import markdown

CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
MD_FILE = Path(__file__).with_name("lebenslauf.md")
HTML_FILE = Path(__file__).with_name("lebenslauf.html")
PDF_FILE = Path(__file__).with_name("lebenslauf.pdf")

CSS = """
@page { size: A4; margin: 12mm 11mm; }
* { box-sizing: border-box; }
body {
  font-family: "Segoe UI", Arial, Helvetica, sans-serif;
  font-size: 9.8pt;
  line-height: 1.36;
  color: #1a1a1a;
  margin: 0;
}
a { color: #1a4f8b; text-decoration: none; }
.cv-header {
  border-bottom: 2px solid #1a4f8b;
  padding-bottom: 8pt;
  margin-bottom: 10pt;
}
.cv-header h1 {
  font-size: 22pt;
  font-weight: 700;
  margin: 0;
  letter-spacing: -0.3pt;
}
.cv-header p {
  margin: 4pt 0 0;
  font-size: 11pt;
  color: #444;
}
.cv-grid {
  display: grid;
  grid-template-columns: 31% 1fr;
  gap: 16pt;
  align-items: start;
}
.cv-side {
  background: #f4f6f8;
  padding: 10pt 10pt 12pt;
  border-radius: 4pt;
}
.cv-side h2 {
  font-size: 9.5pt;
  text-transform: uppercase;
  letter-spacing: 0.6pt;
  color: #1a4f8b;
  margin: 0 0 6pt;
  padding-bottom: 3pt;
  border-bottom: 1px solid #c8d4e0;
}
.cv-side h2:not(:first-child) { margin-top: 12pt; }
.cv-side p, .cv-side li { font-size: 9.2pt; }
.cv-side ul { margin: 0; padding-left: 14pt; }
.cv-side li { margin-bottom: 3pt; }
.cv-main h2 {
  font-size: 11pt;
  color: #1a4f8b;
  margin: 0 0 6pt;
  padding-bottom: 2pt;
  border-bottom: 1px solid #d0d8e0;
}
.cv-main h2:not(:first-child) { margin-top: 11pt; }
.cv-main h3 {
  font-size: 10pt;
  margin: 9pt 0 2pt;
  color: #222;
}
.cv-main p { margin: 4pt 0; }
.cv-main ul { margin: 3pt 0 6pt; padding-left: 15pt; }
.cv-main li { margin-bottom: 2pt; }
.cv-main strong { font-weight: 600; }
.cv-footer {
  margin-top: 10pt;
  padding-top: 6pt;
  border-top: 1px solid #e0e0e0;
  text-align: center;
  font-size: 8.5pt;
  color: #666;
}
table { display: none; }
hr { display: none; }
"""


def main() -> int:
    if not MD_FILE.is_file():
        print(f"Missing {MD_FILE}", file=sys.stderr)
        return 1
    if not CHROME.is_file():
        print(f"Chrome not found at {CHROME}", file=sys.stderr)
        return 1

    md_text = MD_FILE.read_text(encoding="utf-8")
    body = markdown.markdown(
        md_text,
        extensions=["tables", "sane_lists", "nl2br"],
    )
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>Lebenslauf — Alex Borissov</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""
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
    HTML_FILE.unlink(missing_ok=True)
    print(f"Created {PDF_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
