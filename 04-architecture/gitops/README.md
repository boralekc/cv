# GitOps

GitOps-Workflows und Deployment-Automatisierung.

## Diagramme

| Datei | Beschreibung |
|-------|--------------|
| <!-- argocd-workflow.png --> | <!-- ArgoCD Sync Flow --> |
| <!-- environment-promotion.png --> | <!-- dev → stage → prod Pipeline --> |

## Patterns

- **ArgoCD ApplicationSets** — Multi-Cluster, Multi-Env Deployments
- **Helm + Kustomize** — Templating und Overlays
- **Environment Promotion** — getestete Artefakte über Stages
- **Rollback-Strategie** — Git Revert + automatischer Sync

## Verwandte Projekte

- [Microservice-Plattform](../../03-projects/09-microservice-platform/)
- [KI-Lernplattform](../../03-projects/06-ai-learning-platform/)
