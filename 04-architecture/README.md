# Architektur

**Deutsch** · [English](../en/04-architecture/README.md)

Referenz-Architekturdiagramme, Design-Patterns und Infrastruktur-Blueprints.

## Kategorien

| Thema | Beschreibung |
|-------|--------------|
| [Kubernetes](kubernetes/) | Cluster-Design, Operators, Workloads |
| [Docker](docker/) | Containerisierungs-Patterns, Image Builds |
| [Netzwerk](network/) | Netzwerk-Topologie, Service Mesh, Security |
| [GitOps](gitops/) | Deployment-Workflows, ArgoCD, Flux |

## Diagramme

Architekturdiagramme als PNG oder SVG in den jeweiligen Unterordnern ablegen.

### Empfohlene Benennung

```
kubernetes/
├── cluster-topology.png
├── multi-tenant-rbac.png
└── gpu-node-pool.png

docker/
├── multi-stage-build.png
└── registry-pipeline.png

network/
├── service-mesh.png
├── ingress-topology.png
└── zero-trust-segmentation.png

gitops/
├── argocd-workflow.png
└── environment-promotion.png
```

## Design-Prinzipien

- **Infrastructure as Code** — alles versioniert in Git
- **GitOps** — deklarative, auditierbare Deployments
- **Observability by default** — Metriken, Logs, Traces von Anfang an
- **Security in depth** — RBAC, Network Policies, Secrets Management
- **High availability** — kein Single Point of Failure
