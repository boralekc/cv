# Kurzprofil & Lebenslauf

**Deutsch** · [English](../en/resume/README.md)

In diesem Ordner liegen **zwei verschiedene Dokumente**:

| Datei | Zweck | Für wen |
|-------|--------|---------|
| [resume.md](resume.md) | **Kurzprofil** — eine Seite, Links ins Repo | Besucher GitHub-Portfolio |
| [lebenslauf.md](lebenslauf.md) | **Lebenslauf** — klassisches CV für Bewerbungen | HR, Recruiter, Arbeitgeber |

Das [Portfolio](../README.md) (`01-about`, `02-career`, `03-projects` …) bleibt die ausführliche technische Dokumentation.

---

## Inhalt `lebenslauf.md`

- Persönliche Daten & Kontakt
- Kurzprofil (positive Positionierung: DevOps auf Enterprise-/Integrationsbasis)
- Beruflicher Werdegang (CDC → Medcore → Integration → BORISSOV)
- Ausbildung & Zertifikate
- Fachkenntnisse & Sprachen
- Link zum GitHub-Portfolio für Case Studies

Englische Version: [en/resume/cv.md](../en/resume/cv.md)

---

## PDF exportieren

**Schnell (empfohlen):**

```bash
python resume/generate-pdf.py
```

Erzeugt `resume/lebenslauf.pdf` aus `lebenslauf.md` (Chrome headless, Windows).

Alternativ:

- [Pandoc](https://pandoc.org/): `pandoc lebenslauf.md -o lebenslauf.pdf`
- Drucken → „Als PDF speichern“ aus der HTML-Vorschau (`lebenslauf.html` nach Skript-Lauf)

---

## Hinweis zu älteren Lebensläufen

Frühere PDF-Versionen betonten DevOps zu stark. **`lebenslauf.md` in diesem Repository** ist die aktuelle, zum Portfolio abgestimmte Version.
