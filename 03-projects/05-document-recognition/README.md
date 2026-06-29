# Dokumentenerkennungs-System

## Projekt

**Dokumentendigitalisierungs-Plattform** für eine Hochdurchsatz-Klinik (40.000 Patienten/Jahr) — browsergesteuerte Scanner, OCR-Erkennungspipeline, strukturierte Datenextraktion und Integration mit dem Medizinischen Informationssystem.

| | |
|---|---|
| **Zeitraum** | ~2016 |
| **Rolle** | Deployment und Produktionssupport |
| **Klinikgröße** | 40.000 Patienten / Jahr |
| **Status** | Produktion |

## Rolle

**Deployment- & Support-Ingenieur**

Deployment des Dokumentenscan- und Erkennungssystems in Produktion und laufender operativer Support.

## Aufgaben

- Produktionsdeployment und Umgebungssetup
- Support der Scanner-Hardware-Integration
- Monitoring und Troubleshooting der OCR-Pipeline
- Wartung der MIS-Integration
- Produktionssupport für klinische Dokumenten-Workflows

## Architektur

```mermaid
flowchart LR
    SCAN[Browsergesteuerter Scanner]
    OCR[OCR-Pipeline]
    EXT[Datenextraktion]
    MIS[Medizinisches Informationssystem]
    SCAN --> OCR --> EXT --> MIS
```

## Technologien

`OCR` `Dokumentenscanning` `Web-Integration` `MIS-APIs` `Windows Server` `MS SQL Server`

## Herausforderungen

1. **Hohes Dokumentenvolumen** — Klinikgröße erfordert zuverlässige Batch-Verarbeitung
2. **Hardware + Software Integration** — Scanner aus dem Browser in klinischer Umgebung
3. **OCR-Genauigkeit vs. Geschwindigkeit** — strukturierte Extraktion für MIS-Verbrauch

## Lessons Learned

- Dokumentendigitalisierung in Krankenhäusern ist ein Betriebsproblem, nicht nur ein Softwareproblem
- OCR-Pipelines brauchen Monitoring — stille Fehler erzeugen klinische Datenlücken
- Deployment-Qualität entscheidet, ob Mitarbeiter Scan-Workflows tatsächlich nutzen

## Verwandt

- [Medizinisches Informationssystem](../02-medical-information-system/)
- [Case Study auf borissov-it.de](https://borissov-it.de/work)

## Fotos

Siehe [photos/](photos/) für Screenshots, sofern vorhanden.
