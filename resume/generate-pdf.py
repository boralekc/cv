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

CSS = """
@page { size: A4; margin: 16mm 14mm; }
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 10.5pt;
  line-height: 1.38;
  color: #111;
  max-width: 100%;
}
h1 { font-size: 18pt; margin: 0 0 2pt; }
h2 {
  font-size: 11.5pt;
  margin: 12pt 0 5pt;
  border-bottom: 1px solid #bbb;
  padding-bottom: 2pt;
}
h3 { font-size: 10.5pt; margin: 9pt 0 3pt; }
p { margin: 3pt 0; }
ul { margin: 3pt 0 6pt; padding-left: 16pt; }
li { margin-bottom: 2pt; }
table { border-collapse: collapse; width: 100%; margin: 5pt 0 8pt; font-size: 9.5pt; }
th, td { border: 1px solid #ccc; padding: 3pt 5pt; text-align: left; vertical-align: top; }
th { background: #f3f3f3; font-weight: 600; }
a { color: #0b57d0; text-decoration: none; }
hr { border: none; border-top: 1px solid #e5e5e5; margin: 8pt 0; }
em { font-size: 9pt; color: #555; }
"""


def prepare_markdown(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if "Kurzprofil (Portfolio)" in line or "Vollständige Dokumentation" in line:
            continue
        if line.strip().startswith("→ Ausführliche Matrix:"):
            continue
        lines.append(line)
    return "\n".join(lines)


def main() -> int:
    if not MD_FILE.is_file():
        print(f"Missing {MD_FILE}", file=sys.stderr)
        return 1
    if not CHROME.is_file():
        print(f"Chrome not found at {CHROME}", file=sys.stderr)
        return 1

    md_text = prepare_markdown(MD_FILE.read_text(encoding="utf-8"))
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
