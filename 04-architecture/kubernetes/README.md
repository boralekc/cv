# Kubernetes

Architecture diagrams and reference designs for Kubernetes deployments.

## Diagrams

| File | Description |
|------|-------------|
| <!-- cluster-topology.png --> | <!-- Cluster layout: control plane, worker nodes, add-ons --> |
| <!-- multi-tenant-rbac.png --> | <!-- Namespace isolation, RBAC policies --> |
| <!-- gpu-node-pool.png --> | <!-- GPU scheduling for ML workloads --> |

## Patterns

- **Cluster layout** — control plane HA, worker node pools by workload type
- **Multi-tenancy** — namespace isolation, resource quotas, network policies
- **Operators** — custom controllers for stateful workloads
- **Ingress** — NGINX / Traefik / cloud LB integration

## Related Projects

- [Microservice Platform](../03-projects/09-microservice-platform/)
- [Histopathology](../03-projects/04-histopathology/)
