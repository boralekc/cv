# Karriere-Zeitstrahl

Entwicklung der Verantwortung — von Enterprise-Software über MIS bis zu projektbezogener Infrastruktur.

---

## 2007 – 2008 · [CDC](https://cdc.ru/) · Optimum ERP

Erste Rolle: **Einführung des Optimum-ERP-Systems**.

- Geschäftsanforderungen, Konfiguration, Rollout
- Grundlage für Systemdenken in Enterprise-Umgebungen

→ [Optimum-Projekt](../03-projects/01-optimum/)

---

## 2008 – 2024 · Medcore · Medizinische Informationssysteme

**Wechsel zu Medcore (2008):** Einführung und Betrieb von **MIS Intramed** (InterSystems Caché) und **weiteren, kleineren Informationssystemen**.

- 16+ Jahre — durchgehender MIS-Betrieb; ab ~2016 **zusätzlich** Infrastrukturprojekte im Parallelbetrieb (siehe unten)
- Krankenhaus mit **40.000 Patienten pro Jahr**
- Integration: Labor, Histopathologie, Dokumentenerkennung
- Einführungen an **weiteren großen Kliniken in Russland**

→ [Medizinisches Informationssystem](../03-projects/02-medical-information-system/)

---

## ab ~2016 · Infrastruktur — parallel zum MIS-Betrieb

**Gleichzeitig** zum laufenden Intramed-Support und anderen Systemen: **Linux, WildFly, Deployment** u. a. — **je nach Projekt**, nicht als separater Vollzeit-Linux-Job:

| Jahr | Projekt | Schwerpunkt |
|------|---------|-------------|
| ~2016 | [Dokumentenerkennung](../03-projects/05-document-recognition/) | Deployment, OCR, MIS-Integration |
| ~2018 | [Histopathologie-LIS](../03-projects/04-histopathology/) | Test, Deployment, MIS-Sync |
| ~2020 | [Referenzdaten-Plattform](../03-projects/03-reference-data-platform/) | WildFly-Cluster, air-gapped |

Infrastruktur-Kenntnisse wuchsen **schrittweise und projektweise** — nicht über eine dedizierte DevOps-Stelle.

---

## 2024 – heute · Freelance · [BORISSOV Engineering](https://borissov-it.de/)

Hier werden Infrastruktur, Kubernetes und Automatisierung **bewusst und explizit** zum Kerngeschäft.

| Jahr | Projekt | Rolle |
|------|---------|-------|
| 2025 | [KI-Lernplattform](../03-projects/06-ai-learning-platform/) | DevOps — K8s, GitLab CI, Keycloak |
| 2025 | [BI-Plattform](../03-projects/07-bi-platform/) | Metabase, Monitoring, Backups |
| 2025 | [Investment-Plattform](../03-projects/08-investment-platform/) | Full Stack — Next.js, n8n, Docker |
| 2025 | [Microservice-Plattform](../03-projects/09-microservice-platform/) | DevOps *(laufend)* |

---

## Visuelle Übersicht

```mermaid
gantt
    title Karriereübersicht
    dateFormat YYYY-MM-DD
    axisFormat %Y

    section CDC
    Optimum ERP :done, 2007-01-01, 2008-12-31

    section Medcore
    Intramed MIS & kleinere IS :active, 2008-01-01, 2024-12-31

    section Infrastruktur
    Parallel zu MIS — projektbezogen :infra, 2016-01-01, 2024-12-31

    section Freelance
    BORISSOV Engineering :crit, 2024-01-01, 2027-01-01
```
