# GitOps

GitOps workflows and deployment automation.

## Diagrams

| File | Description |
|------|-------------|
| <!-- argocd-workflow.png --> | <!-- ArgoCD sync flow --> |
| <!-- environment-promotion.png --> | <!-- dev → stage → prod pipeline --> |

## Patterns

- **ArgoCD ApplicationSets** — multi-cluster, multi-env deployments
- **Helm + Kustomize** — templating and overlays
- **Environment promotion** — tested artifacts across stages
- **Rollback strategy** — Git revert + automated sync

## Related Projects

- [Microservice Platform](../03-projects/09-microservice-platform/)
