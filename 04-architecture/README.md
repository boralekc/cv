# Architecture

Reference architecture diagrams, design patterns, and infrastructure blueprints.

## Categories

| Topic | Description |
|-------|-------------|
| [Kubernetes](kubernetes/) | Cluster design, operators, workloads |
| [Docker](docker/) | Containerization patterns, image builds |
| [Network](network/) | Network topology, service mesh, security |
| [GitOps](gitops/) | Deployment workflows, ArgoCD, Flux |

## Diagrams

Add architecture diagrams as PNG or SVG files in the corresponding subfolder.

### Recommended naming

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

## Design Principles

- **Infrastructure as Code** — everything versioned in Git
- **GitOps** — declarative, auditable deployments
- **Observability by default** — metrics, logs, traces from day one
- **Security in depth** — RBAC, network policies, secrets management
- **High availability** — no single point of failure
