---
tags: [kubernetes, k8s, containers, devops, cloud-native, reference]
source: "Kubernetes: Up and Running, 3rd Edition — Burns, Beda, Hightower, Fong-Jones"
created: 2026-03-08
type: reference
---

# ☸️ Kubernetes: Up and Running — Reference Note

> **Source:** *Kubernetes: Up and Running, 3rd Edition* — Brendan Burns, Joe Beda, Kelsey Hightower, Liz Fong-Jones
> **Scope:** Container orchestration, cluster management, workloads, networking, storage, security, and scaling

---
**Architecture** — a full control plane diagram with component roles explained in a table.

**Ch 2–3 · Containers & Cluster Setup** — Dockerfile patterns, Docker CLI, and cluster bootstrap commands for GKE, EKS, AKS, minikube, and kubeadm.

**Ch 4 · kubectl Reference** — fully broken out into subsections: contexts, namespaces, get/describe/delete, create/apply, rollouts, and debugging (`logs`, `exec`, `port-forward`, `top`, `events`).

**Ch 5–12 · Core Workloads** — ready-to-use YAML manifests for Pods (with probes and resource limits), ReplicaSets, Deployments (rolling update strategy), DaemonSets, Jobs, and CronJobs, each with the most relevant `kubectl` commands alongside them.

**Ch 13–14 · Config & Access** — ConfigMap and Secret YAML with all three injection methods (env, envFrom, volume mount), plus RBAC Role/RoleBinding patterns and `kubectl auth can-i` checks.

**Ch 15–17 · Advanced Topics** — Service Meshes decision guide, PV/PVC/StorageClass patterns, StatefulSets, CRDs, and Operators.

**Ch 19–22 · Security & Organization** — Security Contexts, Pod Security Admission levels, NetworkPolicy templates, ResourceQuota/LimitRange, Kustomize overlays, and Helm commands.

---
**Quick Reference** — object hierarchy tree, all resource shorthand names, and a step-by-step troubleshooting checklist.
---
## Core Philosophy

Kubernetes is an open source **container orchestrator** originally developed by Google (inspired by internal systems Borg and Omega). Key value propositions:

- **Velocity** — immutable images + declarative config + self-healing loops
- **Scaling** — horizontal auto-scaling of both apps and infrastructure
- **Abstraction** — decouple app from the underlying machine
- **Efficiency** — bin-packing workloads across nodes

> The Kubernetes API is the **standard interface** for cloud-native applications across all major public clouds.

---

## Architecture Overview

```
Control Plane                         Worker Nodes
┌─────────────────────┐              ┌──────────────────────┐
│  kube-apiserver     │◄────────────►│  kubelet             │
│  etcd               │              │  kube-proxy          │
│  kube-scheduler     │              │  container runtime   │
│  controller-manager │              │  (containerd/CRI-O)  │
└─────────────────────┘              └──────────────────────┘
```

| Component | Role |
|-----------|------|
| `kube-apiserver` | REST API gateway; all requests flow through it |
| `etcd` | Distributed key-value store; source of truth for cluster state |
| `kube-scheduler` | Assigns Pods to nodes based on resource availability |
| `controller-manager` | Runs reconciliation loops (Deployment, RS, etc.) |
| `kubelet` | Node agent; ensures containers in Pods are running |
| `kube-proxy` | Maintains network rules for Service routing |

---

## Ch 2 · Containers

Containers bundle a program **and all its dependencies** into a single portable artifact (OCI image format).

```dockerfile
# Dockerfile example
FROM golang:1.19-alpine
WORKDIR /app
COPY . .
RUN go build -o server .
CMD ["/app/server"]
```

```bash
# Build and push
docker build -t my-app:v1 .
docker tag my-app:v1 gcr.io/myproject/my-app:v1
docker push gcr.io/myproject/my-app:v1

# Run locally
docker run -d -p 8080:8080 my-app:v1
docker ps
docker logs <container-id>
docker exec -it <container-id> sh
```

**Key principle:** Images are **immutable**. Never modify a running container — build a new image.

---

## Ch 3 · Deploying a Cluster

```bash
# Cloud providers (managed clusters)
gcloud container clusters create my-cluster --num-nodes=3    # GKE
eksctl create cluster --name my-cluster --nodes=3            # EKS
az aks create -g myRG -n my-cluster --node-count 3          # AKS

# Local development
minikube start
minikube start --driver=docker --cpus=4 --memory=8g
kind create cluster --name dev

# Bootstrap bare-metal/VMs
kubeadm init --pod-network-cidr=10.244.0.0/16   # control plane
kubeadm join <cp-ip>:6443 --token <token> ...    # worker

# Verify cluster
kubectl cluster-info
kubectl get nodes
kubectl get nodes -o wide
```

---

## Ch 4 · kubectl — Common Commands

### Contexts and Config

```bash
kubectl config get-contexts           # List all contexts
kubectl config use-context my-ctx     # Switch context
kubectl config current-context        # Show active context
kubectl config set-context --current --namespace=my-ns  # Set default namespace
```

### Namespaces

```bash
kubectl get namespaces
kubectl create namespace my-ns
kubectl delete namespace my-ns
kubectl get pods -n my-ns             # Scoped to namespace
kubectl get pods --all-namespaces     # Across all namespaces
kubectl get pods -A                   # Shorthand
```

### Core Get / Describe / Delete

```bash
kubectl get pods
kubectl get pods -o wide              # Node and IP info
kubectl get pods -o yaml              # Full YAML output
kubectl get pods -l app=my-app        # Filter by label
kubectl get all                       # All resource types

kubectl describe pod <pod-name>       # Full details + events
kubectl describe node <node-name>

kubectl delete pod <pod-name>
kubectl delete -f manifest.yaml
kubectl delete pods --all             # All pods in namespace
```

### Create / Apply

```bash
kubectl apply -f manifest.yaml        # Declarative (preferred)
kubectl apply -f ./k8s/               # Apply entire directory
kubectl create -f manifest.yaml       # Imperative create (once)

# Quick imperative creates
kubectl run my-pod --image=nginx
kubectl create deployment my-dep --image=nginx --replicas=3
kubectl expose deployment my-dep --port=80 --type=ClusterIP
```

### Editing and Patching

```bash
kubectl edit deployment my-dep
kubectl set image deployment/my-dep container=my-app:v2   # Update image
kubectl scale deployment my-dep --replicas=5
kubectl rollout status deployment/my-dep
kubectl rollout undo deployment/my-dep
kubectl rollout history deployment/my-dep
```

### Debugging

```bash
kubectl logs <pod-name>
kubectl logs <pod-name> -c <container>  # Multi-container pod
kubectl logs -f <pod-name>              # Follow / tail logs
kubectl logs --previous <pod-name>      # Previous container

kubectl exec -it <pod-name> -- /bin/sh
kubectl exec -it <pod-name> -c <container> -- bash

kubectl port-forward pod/<pod-name> 8080:8080
kubectl port-forward svc/<svc-name> 8080:80

kubectl top nodes                     # Resource usage
kubectl top pods
kubectl get events --sort-by=.lastTimestamp
```

---

## Ch 5 · Pods

The **smallest deployable unit** in Kubernetes. A Pod wraps one or more tightly coupled containers that share:
- Network namespace (same IP, same ports)
- Storage volumes
- Lifecycle (start/stop together)

```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: my-app
    env: production
spec:
  containers:
    - name: app
      image: my-app:v1
      ports:
        - containerPort: 8080
      resources:
        requests:
          cpu: "100m"
          memory: "128Mi"
        limits:
          cpu: "500m"
          memory: "256Mi"
      livenessProbe:
        httpGet:
          path: /healthz
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 10
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 3
        periodSeconds: 5
      env:
        - name: MY_ENV_VAR
          value: "hello"
      volumeMounts:
        - name: data
          mountPath: /data
  volumes:
    - name: data
      emptyDir: {}
  restartPolicy: Always   # Always | OnFailure | Never
```

**Pod phases:** Pending → Running → Succeeded / Failed / Unknown

**Multi-container patterns:**
- **Sidecar** — augments main container (e.g., log shipper, git sync)
- **Ambassador** — proxies external connections (e.g., envoy)
- **Adapter** — normalizes output (e.g., metrics exporter)

---

## Ch 6 · Labels and Annotations

### Labels

Key/value pairs used for **grouping, selecting, and organizing** objects.

```yaml
metadata:
  labels:
    app: my-app
    version: v1.2
    env: production
    tier: frontend
```

```bash
kubectl get pods -l app=my-app
kubectl get pods -l 'env in (production, staging)'
kubectl get pods -l 'version!=v1'
kubectl label pod my-pod hotfix=true          # Add label
kubectl label pod my-pod hotfix-              # Remove label
```

**Label selectors in specs:**
```yaml
selector:
  matchLabels:
    app: my-app
  matchExpressions:
    - key: env
      operator: In
      values: [production, staging]
```

### Annotations

Key/value pairs for **non-identifying metadata** — not queryable, used by tools.

```yaml
metadata:
  annotations:
    kubernetes.io/change-cause: "Deploy v1.2 with bug fix"
    prometheus.io/scrape: "true"
    prometheus.io/port: "9090"
    co.elastic.logs/enabled: "true"
```

---

## Ch 7 · Service Discovery

A **Service** provides a stable virtual IP and DNS name for a set of Pods selected by labels.

### Service Types

| Type | Accessibility | Use case |
|------|---------------|----------|
| `ClusterIP` | Cluster-internal only | Internal microservices |
| `NodePort` | Node IP + static port | Dev/testing external access |
| `LoadBalancer` | Cloud load balancer + external IP | Production external traffic |
| `ExternalName` | CNAME to external DNS | Connect to external services |

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - port: 80          # Service port
      targetPort: 8080  # Container port
      protocol: TCP
  type: ClusterIP
```

```bash
# DNS inside cluster resolves to:
# <service-name>.<namespace>.svc.cluster.local
curl http://my-service.my-ns.svc.cluster.local

kubectl get svc
kubectl get endpoints my-service    # See which pods are backing it
```

### Headless Service (for StatefulSets / direct pod access)

```yaml
spec:
  clusterIP: None     # Headless — DNS returns pod IPs directly
  selector:
    app: my-app
```

---

## Ch 8 · Ingress (HTTP Load Balancing)

**Ingress** operates at Layer 7 (HTTP/HTTPS) and handles path/host-based routing to multiple Services from a single IP.

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - myapp.example.com
      secretName: tls-secret
  rules:
    - host: myapp.example.com
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80
          - path: /
            pathType: Prefix
            backend:
              service:
                name: frontend-service
                port:
                  number: 80
```

**Popular Ingress controllers:** nginx-ingress, Traefik, HAProxy, AWS ALB, GCE

```bash
# Install nginx ingress controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

kubectl get ingress
kubectl describe ingress my-ingress
```

---

## Ch 9 · ReplicaSets

Ensures a **specified number of Pod replicas** are running at all times. Provides redundancy, scale, and self-healing.

```yaml
# replicaset.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: app
          image: my-app:v1
```

```bash
kubectl get replicasets
kubectl scale rs my-rs --replicas=5
kubectl describe rs my-rs
```

> **Note:** Prefer **Deployments** over bare ReplicaSets — Deployments manage ReplicaSets and add rollout/rollback capabilities.

---

## Ch 10 · Deployments

Wraps ReplicaSets and manages **rolling updates** and **rollbacks** declaratively.

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1          # Extra pods allowed during update
      maxUnavailable: 0    # Zero-downtime: no pod removed before new one is Ready
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: app
          image: my-app:v1
          ports:
            - containerPort: 8080
```

```bash
# Rollouts
kubectl apply -f deployment.yaml
kubectl rollout status deployment/my-deployment
kubectl rollout history deployment/my-deployment
kubectl rollout undo deployment/my-deployment             # Roll back one version
kubectl rollout undo deployment/my-deployment --to-revision=2

# Scaling
kubectl scale deployment my-deployment --replicas=10
kubectl autoscale deployment my-deployment --min=2 --max=10 --cpu-percent=50

# Update image
kubectl set image deployment/my-deployment app=my-app:v2
```

**Deployment strategies:**
- `RollingUpdate` — gradually replaces old pods (default, zero-downtime)
- `Recreate` — kills all old pods first, then creates new (causes downtime)

---

## Ch 11 · DaemonSets

Ensures **exactly one Pod per node** (or per selected node subset). Used for infrastructure agents.

```yaml
# daemonset.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
    spec:
      containers:
        - name: fluentd
          image: fluent/fluentd:v1.14
          volumeMounts:
            - name: varlog
              mountPath: /var/log
      volumes:
        - name: varlog
          hostPath:
            path: /var/log
      tolerations:                  # Run on ALL nodes including control plane
        - key: node-role.kubernetes.io/control-plane
          operator: Exists
          effect: NoSchedule
```

```bash
kubectl get daemonsets
kubectl get daemonsets -n kube-system   # Built-in daemons (kube-proxy, etc.)
```

**Use cases:** Log shippers (Fluentd), monitoring agents (Prometheus Node Exporter), network plugins, intrusion detection.

---

## Ch 12 · Jobs and CronJobs

### Job

Runs Pods to **completion** (exit 0). Perfect for batch processing, DB migrations, one-off tasks.

```yaml
# job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration
spec:
  completions: 1          # Number of successful completions needed
  parallelism: 1          # Pods running in parallel
  backoffLimit: 4         # Retry attempts on failure
  template:
    spec:
      restartPolicy: OnFailure   # Required: Never or OnFailure
      containers:
        - name: migrate
          image: my-app:v1
          command: ["./run-migrations.sh"]
```

**Job patterns:**

| Pattern | completions | parallelism | Use case |
|---------|-------------|-------------|---------|
| One-shot | 1 | 1 | Single task |
| Fixed completion count | N | 1 | Sequential batch |
| Work queue | unset | N | Parallel consumers |

### CronJob

```yaml
# cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: nightly-report
spec:
  schedule: "0 2 * * *"     # Standard cron syntax
  concurrencyPolicy: Forbid  # Allow | Forbid | Replace
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: reporter
              image: my-app:v1
              command: ["./generate-report.sh"]
```

```bash
kubectl get jobs
kubectl get cronjobs
kubectl describe job db-migration
kubectl logs job/db-migration
```

---

## Ch 13 · ConfigMaps and Secrets

### ConfigMaps — Non-sensitive configuration

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "info"
  DATABASE_URL: "postgres://db:5432/myapp"
  config.yaml: |
    server:
      port: 8080
      timeout: 30s
```

```bash
# Create from literal values
kubectl create configmap app-config --from-literal=LOG_LEVEL=info --from-literal=PORT=8080

# Create from file
kubectl create configmap app-config --from-file=config.yaml

kubectl get configmap app-config -o yaml
```

**Using ConfigMaps in Pods:**

```yaml
spec:
  containers:
    - name: app
      # As environment variables (individual keys)
      env:
        - name: LOG_LEVEL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: LOG_LEVEL
      # Or inject ALL keys as env vars
      envFrom:
        - configMapRef:
            name: app-config
      # Or as a mounted file
      volumeMounts:
        - name: config-vol
          mountPath: /etc/config
  volumes:
    - name: config-vol
      configMap:
        name: app-config
```

### Secrets — Sensitive configuration

```yaml
# secret.yaml (values are base64-encoded)
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: cGFzc3dvcmQxMjM=   # base64 of "password123"
stringData:                    # Plain text (auto-encoded by K8s)
  api-key: "my-secret-key"
```

```bash
kubectl create secret generic db-secret \
  --from-literal=password=mypassword \
  --from-file=tls.crt=cert.pem

kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 -d
```

**Using Secrets in Pods (same as ConfigMap):**

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: password
```

> ⚠️ Secrets are only **base64-encoded**, not encrypted by default. Use external secret managers (HashiCorp Vault, AWS Secrets Manager) or enable **etcd encryption at rest** for production.

**Common Secret types:**

| Type | Use |
|------|-----|
| `Opaque` | Arbitrary key-value data |
| `kubernetes.io/tls` | TLS certificates |
| `kubernetes.io/dockerconfigjson` | Registry auth |
| `kubernetes.io/service-account-token` | SA tokens |

---

## Ch 14 · Role-Based Access Control (RBAC)

**Authentication → Authorization → Admission Control**

### Core RBAC Objects

| Object | Scope | Purpose |
|--------|-------|---------|
| `Role` | Namespace | Grants permissions within a namespace |
| `ClusterRole` | Cluster-wide | Grants permissions across all namespaces |
| `RoleBinding` | Namespace | Binds Role to users/groups/SA |
| `ClusterRoleBinding` | Cluster-wide | Binds ClusterRole cluster-wide |

```yaml
# role.yaml — namespace-scoped
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: my-ns
  name: pod-reader
rules:
  - apiGroups: [""]           # "" = core API group
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch"]
---
# rolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: my-ns
subjects:
  - kind: User
    name: jane
    apiGroup: rbac.authorization.k8s.io
  - kind: ServiceAccount
    name: my-sa
    namespace: my-ns
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

```bash
# Service Accounts (identity for pods)
kubectl create serviceaccount my-sa -n my-ns

# Check permissions
kubectl auth can-i create deployments --as=jane
kubectl auth can-i get pods -n my-ns --as=system:serviceaccount:my-ns:my-sa

# View roles
kubectl get roles,rolebindings -n my-ns
kubectl get clusterroles,clusterrolebindings
```

> ⚠️ **Important:** Anyone who can run arbitrary code inside the cluster can effectively obtain root privileges. Minimize RBAC permissions using **principle of least privilege**.

---

## Ch 15 · Service Meshes

A **service mesh** adds observability, security (mTLS), and traffic management to inter-service communication **without changing application code** (via sidecar proxy injection).

**Core capabilities:**

| Feature | Description |
|---------|-------------|
| **mTLS** | Automatic mutual TLS between services |
| **Traffic shaping** | Canary releases, A/B testing, circuit breaking |
| **Observability** | Distributed tracing, metrics, access logs |
| **Retries/timeouts** | Policy-based reliability without app changes |
| **Authorization** | Service-to-service access policies |

**Popular implementations:** Istio, Linkerd, Consul Connect, AWS App Mesh

> ⚠️ **Warning:** Service meshes add significant operational complexity. Do not adopt unless the benefits clearly outweigh the cost. Services + Ingress cover most use cases.

---

## Ch 16 · Storage

### Volume Types

| Type | Persistence | Use case |
|------|-------------|---------|
| `emptyDir` | Pod lifetime | Shared temp storage between containers |
| `hostPath` | Node-local | DaemonSets, dev — avoid in production |
| `configMap` / `secret` | External | Inject config/creds as files |
| `persistentVolumeClaim` | Independent | Stateful apps (databases, etc.) |
| Cloud volumes | Independent | AWS EBS, GCE PD, Azure Disk |

### PersistentVolume / PersistentVolumeClaim

```yaml
# storageclass.yaml (dynamic provisioning)
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
reclaimPolicy: Retain   # Retain | Delete | Recycle
---
# pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce     # RWO | ROX | RWX
  resources:
    requests:
      storage: 10Gi
  storageClassName: fast-ssd
---
# Use in Pod
spec:
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: my-pvc
  containers:
    - name: app
      volumeMounts:
        - name: data
          mountPath: /data
```

**Access modes:**

| Mode | Abbreviation | Meaning |
|------|-------------|---------|
| ReadWriteOnce | RWO | One node, read-write |
| ReadOnlyMany | ROX | Many nodes, read-only |
| ReadWriteMany | RWX | Many nodes, read-write (NFS/etc.) |

### StatefulSets (stateful workloads)

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: my-db
spec:
  serviceName: my-db-headless
  replicas: 3
  selector:
    matchLabels:
      app: my-db
  template:
    metadata:
      labels:
        app: my-db
    spec:
      containers:
        - name: db
          image: postgres:14
          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql
  volumeClaimTemplates:       # Each Pod gets its own PVC
    - metadata:
        name: data
      spec:
        accessModes: [ReadWriteOnce]
        resources:
          requests:
            storage: 20Gi
```

**StatefulSet guarantees:** stable network identity (`pod-0`, `pod-1`...), stable storage, ordered deployment/scaling.

---

## Ch 17 · Extending Kubernetes

### Custom Resource Definitions (CRDs)

Extend the Kubernetes API with your own resource types.

```yaml
# crd.yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.myco.io
spec:
  group: myco.io
  names:
    kind: Database
    plural: databases
    singular: database
    shortNames: [db]
  scope: Namespaced
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                engine:
                  type: string
                replicas:
                  type: integer
```

### Operators

An **Operator** = CRD + custom controller that encodes operational knowledge.

```bash
# Install an operator (e.g., from OperatorHub)
kubectl apply -f https://...operator.yaml

# Use the custom resource
kubectl apply -f my-database.yaml
kubectl get databases
```

**Popular operators:** Cert-Manager, Prometheus Operator, Strimzi (Kafka), CloudNativePG (Postgres).

---

## Ch 19 · Security

### Security Contexts

```yaml
spec:
  # Pod-level security context
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      # Container-level security context
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
          add: ["NET_BIND_SERVICE"]   # Only if needed
```

### Pod Security Admission (PSA)

Applied at namespace level via labels:

```bash
# Enforce restricted policy on namespace
kubectl label namespace my-ns \
  pod-security.kubernetes.io/enforce=restricted \
  pod-security.kubernetes.io/audit=restricted \
  pod-security.kubernetes.io/warn=restricted
```

**PSA levels:**

| Level | Description |
|-------|-------------|
| `privileged` | Unrestricted (default for kube-system) |
| `baseline` | Prevents known privilege escalations |
| `restricted` | Hardened — follows security best practices |

### Network Policies

```yaml
# networkpolicy.yaml — default deny all ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
  namespace: my-ns
spec:
  podSelector: {}   # Applies to ALL pods in namespace
  policyTypes:
    - Ingress
    - Egress
---
# Allow specific traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api
spec:
  podSelector:
    matchLabels:
      app: api
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - port: 8080
```

---

## Ch 20 · Policy and Governance

**OPA/Gatekeeper** — Policy engine that validates resources against rules before they're admitted.

```bash
# Install Gatekeeper
kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/main/deploy/gatekeeper.yaml

# Create a constraint template (rego policy)
# Create a constraint (enforces the template)
kubectl get constrainttemplates
kubectl get constraints
```

**Built-in admission controllers:** ResourceQuota, LimitRange, PodSecurity.

```yaml
# resourcequota.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: ns-quota
  namespace: my-ns
spec:
  hard:
    pods: "20"
    requests.cpu: "4"
    requests.memory: "8Gi"
    limits.cpu: "8"
    limits.memory: "16Gi"
---
# limitrange.yaml — set default limits per container
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
spec:
  limits:
    - type: Container
      default:
        cpu: "500m"
        memory: "256Mi"
      defaultRequest:
        cpu: "100m"
        memory: "128Mi"
```

---

## Ch 21 · Multicluster Deployments

**Reasons for multiple clusters:**
- Redundancy across failure domains (region outage resilience)
- Regulatory / data residency requirements
- Latency — regional proximity to users
- Isolation — separate prod/staging, separate tenants

**Approaches:**

| Strategy | Description |
|----------|-------------|
| Replicated services | Same app deployed identically to each cluster |
| Sharded services | Different clusters handle different data/users |
| Active/passive | Primary + standby for failover |

**Tools:** Fleet, Argo CD (multi-cluster), Rancher, Anthos, ACM.

---

## Ch 22 · Organizing Your Application

### Recommended Layout

```
my-app/
├── Dockerfile
├── src/
├── k8s/
│   ├── base/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── kustomization.yaml
│   └── overlays/
│       ├── staging/
│       │   └── kustomization.yaml
│       └── production/
│           └── kustomization.yaml
└── helm/
    └── my-app/
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
```

### Kustomize

```bash
# Apply with kustomize
kubectl apply -k k8s/overlays/production/

# kustomization.yaml
resources:
  - ../../base
patchesStrategicMerge:
  - replica-patch.yaml
images:
  - name: my-app
    newTag: v2.0
```

### Helm

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/nginx
helm upgrade my-release bitnami/nginx --set replicaCount=3
helm rollback my-release 1
helm uninstall my-release
helm list
helm template my-app ./helm/my-app/ -f values.prod.yaml   # Preview
```

---

## Quick Reference

### Object Hierarchy

```
Cluster
└── Namespace
    ├── Pod  ← (rarely created directly)
    ├── Deployment → manages → ReplicaSet → creates → Pods
    ├── StatefulSet → creates → Pods (with stable identity)
    ├── DaemonSet → creates → 1 Pod per node
    ├── Job / CronJob → creates → Pods (to completion)
    ├── Service → routes to → Pods
    ├── Ingress → routes HTTP to → Services
    ├── ConfigMap / Secret → mounted into → Pods
    └── PersistentVolumeClaim → bound to → PersistentVolume
```

### Most Used Resources

```bash
# Workloads
kubectl get pods,deployments,replicasets,statefulsets,daemonsets

# Config
kubectl get configmaps,secrets

# Networking
kubectl get services,endpoints,ingresses,networkpolicies

# Storage
kubectl get pv,pvc,storageclasses

# Access control
kubectl get serviceaccounts,roles,rolebindings,clusterroles,clusterrolebindings

# Extend
kubectl get crds
kubectl api-resources    # List ALL resource types
```

### Troubleshooting Checklist

```bash
# 1. Check pod status
kubectl get pods -n my-ns
kubectl describe pod <pod> -n my-ns   # Look at Events section

# 2. Check logs
kubectl logs <pod> -n my-ns
kubectl logs <pod> --previous -n my-ns  # After crash

# 3. Check service routing
kubectl get endpoints <svc>             # Are pods being selected?
kubectl exec -it <pod> -- curl svc-name  # Can pods reach each other?

# 4. Check resource limits
kubectl top pods
kubectl describe node <node>            # Check allocatable vs requested

# 5. Check events
kubectl get events -n my-ns --sort-by=.lastTimestamp

# 6. Check config
kubectl get configmap <name> -o yaml
kubectl get secret <name> -o jsonpath='{.data}'
```

### kubectl Shorthand

| Resource | Short |
|----------|-------|
| `pods` | `po` |
| `services` | `svc` |
| `deployments` | `deploy` |
| `replicasets` | `rs` |
| `daemonsets` | `ds` |
| `statefulsets` | `sts` |
| `configmaps` | `cm` |
| `namespaces` | `ns` |
| `persistentvolumeclaims` | `pvc` |
| `persistentvolumes` | `pv` |
| `serviceaccounts` | `sa` |
| `horizontalpodautoscalers` | `hpa` |
| `nodes` | `no` |

---

*Generated from: Kubernetes: Up and Running, 3rd Edition (Burns, Beda, Hightower, Fong-Jones)*
*Note template for Obsidian — last updated: 2026-03-08*
