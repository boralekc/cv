# Kubernetes

Architekturdiagramme und Referenzdesigns für Kubernetes-Deployments.

## Diagramme

| Datei | Beschreibung |
|-------|--------------|
| <!-- cluster-topology.png --> | <!-- Cluster-Layout: Control Plane, Worker Nodes, Add-ons --> |
| <!-- multi-tenant-rbac.png --> | <!-- Namespace-Isolation, RBAC-Policies --> |
| <!-- gpu-node-pool.png --> | <!-- GPU-Scheduling für ML-Workloads --> |

## Patterns

- **Cluster-Layout** — Control Plane HA, Worker Node Pools nach Workload-Typ
- **Multi-Tenancy** — Namespace-Isolation, Resource Quotas, Network Policies
- **Operators** — Custom Controller für Stateful Workloads
- **Ingress** — NGINX / Traefik / Cloud LB Integration

## Verwandte Projekte

- [Microservice-Plattform](../../03-projects/09-microservice-platform/)
- [KI-Lernplattform](../../03-projects/06-ai-learning-platform/)
