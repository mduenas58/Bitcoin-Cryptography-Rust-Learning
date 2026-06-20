# Kubernetes Basics for DevOps

## A Comprehensive Tutorial with Hands-On Labs

---

> **About This Course**
> 
> This course is designed for DevOps engineers, developers, and system administrators who want to learn Kubernetes from the ground up. You will progress from understanding containers and orchestration, through cluster architecture, all the way to deploying real microservices applications. Every module includes concept explanations, guided demonstrations, and hands-on labs to reinforce learning.

---

## Table of Contents

- [Module 1 – Kubernetes Overview and Fundamental Concepts](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-1--kubernetes-overview-and-fundamental-concepts)
- [Module 2 – PODs, ReplicaSets, and Deployments](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-2--pods-replicasets-and-deployments)
- [Module 3 – Networking in Kubernetes](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-3--networking-in-kubernetes)
- [Module 4 – Services](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-4--services)
- [Module 5 – Microservices Architecture](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-5--microservices-architecture)
- [Module 6 – Conclusion](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-6--conclusion)

---

# Module 1 – Kubernetes Overview and Fundamental Concepts

## Module Overview

This module introduces container technology and its role in modern software delivery, then explains container orchestration and how Kubernetes addresses it. Learners explore Kubernetes architecture and key components, set up a local cluster with Minikube, and gain hands-on practice creating, inspecting, and managing Pods.

### Learning Objectives

- Understand the concept of Pods in Kubernetes and their role as the smallest deployable units
- Gain an understanding of container technology and its role in modern software development
- Explore the concept of container orchestration and its importance in managing containerized applications
- Learn about the architecture of Kubernetes and its components for container orchestration

---

## 1.1 Containers Overview

### What is a Container?

A **container** is a lightweight, portable, and isolated software environment that packages an application together with all its dependencies — libraries, configuration files, and runtime — into a single unit. Unlike virtual machines, containers share the host OS kernel but maintain process and filesystem isolation.

```
┌─────────────────────────────────────────────────────┐
│                    Physical Server                   │
│  ┌───────────────────────────────────────────────┐  │
│  │              Operating System                  │  │
│  │  ┌──────────────┐  ┌──────────────┐           │  │
│  │  │  Container 1 │  │  Container 2 │           │  │
│  │  │  ┌─────────┐ │  │  ┌─────────┐│           │  │
│  │  │  │  App A  │ │  │  │  App B  ││           │  │
│  │  │  │ Libs/   │ │  │  │ Libs/   ││           │  │
│  │  │  │  Deps   │ │  │  │  Deps   ││           │  │
│  │  │  └─────────┘ │  │  └─────────┘│           │  │
│  │  └──────────────┘  └──────────────┘           │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

### Containers vs. Virtual Machines

|Feature|Virtual Machines|Containers|
|---|---|---|
|**Startup time**|Minutes|Seconds|
|**Size**|Gigabytes|Megabytes|
|**OS**|Full OS per VM|Shared host OS kernel|
|**Isolation**|Strong (hypervisor)|Process-level|
|**Portability**|Limited|Highly portable|
|**Overhead**|High|Very low|
|**Use case**|Full OS isolation|Microservices, apps|

### Docker: The Most Common Container Runtime

Docker is the most widely used container platform. Core concepts include:

**Dockerfile** – Instructions to build a container image:

```dockerfile
# Example Dockerfile for a Node.js application
FROM node:18-alpine          # Base image

WORKDIR /app                 # Set working directory
COPY package*.json ./        # Copy dependency files
RUN npm install              # Install dependencies
COPY . .                     # Copy application code
EXPOSE 3000                  # Expose port
CMD ["node", "server.js"]    # Start command
```

**Docker Image** – A read-only template built from a Dockerfile:

```bash
# Build an image
docker build -t myapp:v1 .

# List images
docker images

# Pull from Docker Hub
docker pull nginx:latest
```

**Docker Container** – A running instance of an image:

```bash
# Run a container
docker run -d -p 8080:80 --name webserver nginx:latest

# List running containers
docker ps

# Stop a container
docker stop webserver

# Remove a container
docker rm webserver
```

### Why Containers Changed Software Delivery

Containers solve the classic **"it works on my machine"** problem by packaging the application and its environment together. Key benefits:

- **Consistency**: Same behavior from development to production
- **Speed**: Fast build, test, and deploy cycles
- **Efficiency**: Higher server utilization than VMs
- **Isolation**: Applications don't interfere with each other
- **Scalability**: Easily spin up or down multiple instances

---

## 1.2 Container Orchestration

### The Problem Containers Create at Scale

Running one or two containers is simple. Running hundreds or thousands across many servers introduces new challenges:

- How do you schedule containers across multiple servers?
- What happens when a container crashes — how is it restarted automatically?
- How do containers find and communicate with each other?
- How do you update containers without downtime?
- How do you distribute traffic across container instances?
- How do you manage configuration and secrets for containers?
- How do you scale up or down based on demand?

### What is Container Orchestration?

**Container orchestration** is the automated management of the lifecycle of containerized applications across a cluster of machines. An orchestration platform handles:

```
┌─────────────────────────────────────────────────────────────┐
│                   Orchestration Platform                     │
│                                                             │
│  Scheduling  │  Scaling  │  Healing  │  Networking          │
│  Deployment  │  Storage  │  Config   │  Load Balancing      │
└─────────────────────────────────────────────────────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         ┌────────┐  ┌────────┐  ┌────────┐
         │ Node 1 │  │ Node 2 │  │ Node 3 │
         └────────┘  └────────┘  └────────┘
```

### Popular Orchestration Platforms

|Platform|Description|
|---|---|
|**Kubernetes**|The industry-standard open-source orchestrator (CNCF)|
|**Docker Swarm**|Built into Docker, simpler but less feature-rich|
|**Apache Mesos**|Older platform for large-scale cluster management|
|**Amazon ECS**|AWS proprietary container orchestration service|
|**Nomad**|HashiCorp's lightweight orchestrator|

**Kubernetes has won the orchestration wars** — it is the dominant platform used in production by organizations of all sizes, from startups to Fortune 500 companies.

---

## 1.3 Kubernetes Architecture

### Overview

Kubernetes (K8s) is an open-source container orchestration system originally designed by Google, now maintained by the Cloud Native Computing Foundation (CNCF). A Kubernetes cluster consists of a **Control Plane** (master) and one or more **Worker Nodes**.

```
┌─────────────────────────────────────────────────────────────────┐
│                        Kubernetes Cluster                        │
│                                                                  │
│  ┌───────────────────────────────────────┐                      │
│  │           Control Plane               │                      │
│  │                                       │                      │
│  │  ┌─────────────┐  ┌────────────────┐ │                      │
│  │  │ API Server  │  │ Scheduler      │ │                      │
│  │  └─────────────┘  └────────────────┘ │                      │
│  │  ┌─────────────┐  ┌────────────────┐ │                      │
│  │  │  etcd       │  │Controller Mgr  │ │                      │
│  │  └─────────────┘  └────────────────┘ │                      │
│  └───────────────────────────────────────┘                      │
│                         │                                        │
│          ┌──────────────┼──────────────┐                        │
│          ▼              ▼              ▼                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  Worker Node │  │  Worker Node │  │  Worker Node │         │
│  │              │  │              │  │              │         │
│  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │         │
│  │  │kubelet │  │  │  │kubelet │  │  │  │kubelet │  │         │
│  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │         │
│  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │         │
│  │  │kube-   │  │  │  │kube-   │  │  │  │kube-   │  │         │
│  │  │proxy   │  │  │  │proxy   │  │  │  │proxy   │  │         │
│  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │         │
│  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │         │
│  │  │Container│  │  │  │Container│  │  │  │Container│  │         │
│  │  │Runtime  │  │  │  │Runtime  │  │  │  │Runtime  │  │         │
│  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
```

### Control Plane Components

#### kube-apiserver

The **API server** is the front door to Kubernetes. Every operation — from `kubectl` commands to internal cluster communication — goes through the API server. It:

- Validates and processes REST API requests
- Is the only component that talks directly to etcd
- Exposes the Kubernetes API (REST)

```bash
# All these commands communicate with the API server
kubectl get pods
kubectl create -f deployment.yaml
kubectl delete pod mypod
```

#### etcd

**etcd** is a distributed, highly available key-value store that serves as Kubernetes' "brain" — storing the entire cluster state:

- All cluster configuration
- All object definitions (Pods, Services, ConfigMaps, etc.)
- Cluster membership information

> **Critical**: etcd must be backed up regularly. Losing etcd without a backup means losing the entire cluster state.

#### kube-scheduler

The **scheduler** watches for newly created Pods that have no assigned Node and selects a Node for them to run on. It considers:

- Resource requirements (CPU, memory requests/limits)
- Node availability and capacity
- Affinity/anti-affinity rules
- Taints and tolerations
- Data locality

#### kube-controller-manager

The **controller manager** runs a collection of controllers, each responsible for a specific cluster function:

|Controller|Responsibility|
|---|---|
|**Node Controller**|Monitors and responds to node failures|
|**Replication Controller**|Maintains the correct number of Pod replicas|
|**Endpoints Controller**|Populates Endpoints objects (joining Services & Pods)|
|**Service Account Controller**|Creates default accounts for new namespaces|

#### cloud-controller-manager (optional)

Integrates Kubernetes with cloud provider APIs (AWS, GCP, Azure) for managing load balancers, persistent volumes, and node lifecycle in cloud environments.

### Worker Node Components

#### kubelet

The **kubelet** is the primary node agent running on every worker node. It:

- Registers the node with the API server
- Watches for Pods assigned to its node
- Pulls container images and starts/stops containers via the container runtime
- Reports node and Pod status back to the API server
- Runs liveness and readiness probes

#### kube-proxy

**kube-proxy** runs on every node and maintains network rules (iptables/ipvs rules) that allow network communication to Pods from inside and outside the cluster. It implements the Kubernetes Service concept at the network level.

#### Container Runtime

The software responsible for running containers. Kubernetes supports:

- **containerd** (most common, recommended)
- **CRI-O** (used in OpenShift)
- **Docker Engine** (via cri-dockerd shim, deprecated)

### How Kubernetes Brings Applications to Life

When you run `kubectl create deployment myapp --image=nginx`, here is exactly what happens behind the scenes:

```
1. kubectl sends HTTP POST request to API Server
         │
         ▼
2. API Server authenticates & authorizes the request,
   validates the object, and stores it in etcd
         │
         ▼
3. Controller Manager detects the new Deployment object,
   creates a ReplicaSet, which creates Pod objects
         │
         ▼
4. Scheduler detects unscheduled Pods, evaluates all
   nodes, and assigns each Pod to the best-fit Node
         │
         ▼
5. kubelet on the selected Node sees its assigned Pod,
   pulls the container image, and starts the container
         │
         ▼
6. kubelet reports Pod status back to API Server,
   which updates etcd with the current state
         │
         ▼
7. kube-proxy sets up networking rules so the Pod
   is reachable via its Service IP
```

---

## 1.4 Demo: Minikube Setup

### What is Minikube?

**Minikube** runs a single-node Kubernetes cluster on your local machine inside a VM or container. It is the fastest way to get a Kubernetes cluster up and running for development and learning.

### Prerequisites

- 2 CPUs or more
- 2 GB of free RAM
- 20 GB of free disk space
- Internet connection
- A container or VM manager: Docker, VirtualBox, or Hyper-V

### Installing Minikube

#### Linux

```bash
# Download Minikube binary
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

# Install it
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Verify installation
minikube version
```

#### macOS

```bash
# Using Homebrew
brew install minikube

# Or download directly
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
sudo install minikube-darwin-amd64 /usr/local/bin/minikube
```

#### Windows

```powershell
# Using winget
winget install Kubernetes.minikube

# Or using Chocolatey
choco install minikube
```

### Installing kubectl

**kubectl** is the command-line tool for interacting with Kubernetes clusters.

```bash
# Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl

# macOS (Homebrew)
brew install kubectl

# Verify
kubectl version --client
```

### Starting Minikube

```bash
# Start with default driver (Docker recommended)
minikube start

# Start with specific driver
minikube start --driver=docker
minikube start --driver=virtualbox

# Start with custom resources
minikube start --cpus=4 --memory=8192 --disk-size=30g

# Start with a specific Kubernetes version
minikube start --kubernetes-version=v1.28.0

# Start with multiple nodes (simulates a multi-node cluster)
minikube start --nodes=3
```

Expected output:

```
😄  minikube v1.32.0
✨  Automatically selected the docker driver
📌  Using Docker driver with root privileges
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
🔎  Verifying Kubernetes components...
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster
```

### Essential Minikube Commands

```bash
# Check cluster status
minikube status

# Stop the cluster
minikube stop

# Delete the cluster
minikube delete

# Open the Kubernetes Dashboard
minikube dashboard

# Get the cluster IP
minikube ip

# SSH into the Minikube node
minikube ssh

# View cluster logs
minikube logs

# Enable addons
minikube addons enable ingress
minikube addons enable metrics-server

# List enabled addons
minikube addons list

# Point Docker CLI to Minikube's Docker daemon
eval $(minikube docker-env)
```

### Verify Your Cluster

```bash
# Check cluster info
kubectl cluster-info

# View all nodes
kubectl get nodes

# View all system Pods
kubectl get pods -n kube-system

# View cluster configuration
kubectl config view
```

---

## 1.5 Kubernetes Pods

### What is a Pod?

A **Pod** is the smallest and most basic deployable unit in Kubernetes. A Pod represents a single instance of a running process in your cluster. Key characteristics:

- A Pod encapsulates one or more containers
- Containers within a Pod **share the same network namespace** (same IP, same port space)
- Containers within a Pod **share the same storage volumes**
- Pods are **ephemeral** — they are not self-healing; if a Pod fails, it is gone

```
┌─────────────────────────────────────────────────┐
│                      Pod                        │
│                                                 │
│  ┌─────────────────┐   ┌─────────────────────┐ │
│  │  Main Container │   │  Sidecar Container  │ │
│  │  (nginx:latest) │   │   (log-collector)   │ │
│  └─────────────────┘   └─────────────────────┘ │
│                                                 │
│  Shared Network: 10.244.0.5:80, :443           │
│  Shared Volume: /var/log/nginx                  │
│                                                 │
│  Pod IP: 10.244.0.5                             │
│  Node: worker-node-01                           │
└─────────────────────────────────────────────────┘
```

### Why Pods Instead of Containers Directly?

Kubernetes doesn't schedule containers directly — it schedules Pods. This design enables:

- **Multi-container patterns**: Sidecar, Ambassador, Adapter patterns
- **Shared lifecycle**: All containers in a Pod start and stop together
- **Tight coupling**: Containers that must share resources live together
- **Consistent networking**: One IP per Pod simplifies service discovery

### Multi-Container Pod Patterns

#### Sidecar Pattern

An auxiliary container enhances the main container:

```yaml
# Main app + log shipper sidecar
containers:
  - name: web-app
    image: myapp:latest
    volumeMounts:
      - name: log-volume
        mountPath: /var/log/app

  - name: log-shipper
    image: fluentd:latest
    volumeMounts:
      - name: log-volume
        mountPath: /var/log/app    # Shared volume!
```

#### Ambassador Pattern

A proxy container handles external communication on behalf of the main container.

#### Init Containers

Special containers that run to completion before the main containers start:

```yaml
initContainers:
  - name: init-db
    image: busybox
    command: ['sh', '-c', 'until nc -z db-service 5432; do sleep 2; done']
```

---

## 1.6 Demo: Working with Pods

### Imperative Pod Creation

```bash
# Create a simple Pod imperatively
kubectl run nginx-pod --image=nginx

# Create a Pod with a specific port exposed
kubectl run webapp --image=nginx --port=80

# Create a Pod with environment variables
kubectl run myapp --image=myapp:latest \
  --env="DATABASE_URL=postgres://db:5432/mydb" \
  --env="APP_ENV=production"

# Create a Pod and immediately delete it after it exits
kubectl run --rm -it busybox --image=busybox -- sh

# Run a one-off command in a temporary Pod
kubectl run curl-test --image=curlimages/curl --rm -it --restart=Never -- \
  curl http://my-service/health
```

### Inspecting Pods

```bash
# List all Pods in the default namespace
kubectl get pods

# List Pods with more details (node, IP, status)
kubectl get pods -o wide

# List Pods in all namespaces
kubectl get pods -A

# Watch Pods in real-time
kubectl get pods -w

# Get detailed information about a Pod
kubectl describe pod nginx-pod

# Get Pod definition as YAML
kubectl get pod nginx-pod -o yaml

# Get Pod definition as JSON
kubectl get pod nginx-pod -o json
```

### Accessing Pods

```bash
# Execute a command inside a Pod's container
kubectl exec nginx-pod -- ls /usr/share/nginx/html

# Open an interactive shell inside a Pod
kubectl exec -it nginx-pod -- /bin/bash

# If the Pod has multiple containers, specify which one
kubectl exec -it mypod -c sidecar-container -- /bin/sh

# Port-forward a Pod port to your local machine
kubectl port-forward pod/nginx-pod 8080:80
# Now access: http://localhost:8080
```

### Viewing Pod Logs

```bash
# View logs from a Pod
kubectl logs nginx-pod

# Follow logs in real time
kubectl logs -f nginx-pod

# View logs from a specific container in a multi-container Pod
kubectl logs nginx-pod -c sidecar-container

# View last 100 lines of logs
kubectl logs nginx-pod --tail=100

# View logs from the last 1 hour
kubectl logs nginx-pod --since=1h

# View logs from a previously crashed container
kubectl logs nginx-pod --previous
```

### Deleting Pods

```bash
# Delete a Pod
kubectl delete pod nginx-pod

# Delete multiple Pods
kubectl delete pod pod1 pod2 pod3

# Delete all Pods with a specific label
kubectl delete pods -l app=nginx

# Delete Pod immediately (no graceful shutdown)
kubectl delete pod nginx-pod --grace-period=0 --force
```

---

## 🧪 Hands-on Lab: Familiarize with the Lab Environment

### Lab Objectives

- Start and verify a Minikube cluster
- Create and inspect Pods using imperative commands
- Access Pod logs and execute commands inside containers
- Understand Pod lifecycle and states

### Lab Duration: 45 minutes

---

### Exercise 1: Cluster Setup and Verification

```bash
# Step 1: Start Minikube
minikube start

# Step 2: Verify the cluster is running
kubectl cluster-info
# Expected: Kubernetes control plane is running at https://...

# Step 3: Check the node
kubectl get nodes
# Expected: minikube   Ready   control-plane   Xm   v1.28.x

# Step 4: Explore the system namespace
kubectl get pods -n kube-system
# You should see: coredns, etcd, kube-apiserver, kube-controller-manager,
#                 kube-proxy, kube-scheduler, storage-provisioner

# Step 5: Open the Dashboard (in a separate terminal)
minikube dashboard
```

---

### Exercise 2: Your First Pod

```bash
# Step 1: Create an nginx Pod
kubectl run first-pod --image=nginx:latest

# Step 2: Watch the Pod come to life
kubectl get pods -w
# Wait until STATUS shows: Running

# Step 3: Get detailed Pod information
kubectl describe pod first-pod
# Note: Events section shows what happened step by step

# Step 4: Check the Pod's logs
kubectl logs first-pod

# Step 5: Access the Pod's nginx welcome page
kubectl port-forward pod/first-pod 8080:80 &
curl http://localhost:8080
# Should return nginx HTML

# Step 6: Execute a command inside the Pod
kubectl exec first-pod -- nginx -v
kubectl exec -it first-pod -- /bin/bash
# Inside the container:
ls /usr/share/nginx/html
cat /etc/nginx/nginx.conf
exit

# Step 7: Clean up
kill %1   # Stop port-forward
kubectl delete pod first-pod
```

---

### Exercise 3: Explore Pod States

```bash
# Create a Pod that will fail (bad image name)
kubectl run broken-pod --image=nginx:doesnotexist

# Watch it fail
kubectl get pods -w
# Status will show: ErrImagePull → ImagePullBackOff

# Describe it to see why
kubectl describe pod broken-pod
# Look at Events: Failed to pull image...

# Clean up
kubectl delete pod broken-pod

# Create a Pod that exits immediately
kubectl run exit-pod --image=busybox --command -- sleep 5
kubectl get pods -w
# Completed → CrashLoopBackOff (because it keeps restarting with no policy)

kubectl delete pod exit-pod
```

---

# Module 2 – Kubernetes Concepts: PODs, ReplicaSets, Deployments

## Module Overview

This module covers essential Kubernetes concepts for managing containerized applications. Participants learn about Pods (via YAML), ReplicaSets, and Deployments through theoretical explanations, guided demonstrations, and hands-on labs.

### Learning Objectives

- Understand the concept of Pods, ReplicaSets, and Deployments in Kubernetes
- Learn how to define and manage Pods using YAML manifests
- Explore the role of ReplicaSets in ensuring the desired number of Pod replicas
- Gain proficiency in creating and managing Deployments, including updates and rollbacks

---

## 2.1 Pods with YAML

### The Pod YAML Manifest

Every Kubernetes object can be defined as a YAML manifest. All Kubernetes manifests share a common structure:

```yaml
apiVersion:   # Which API version to use
kind:         # What type of object
metadata:     # Information about the object
spec:         # Desired state of the object
```

### A Minimal Pod Manifest

```yaml
# pod-simple.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
    - name: nginx
      image: nginx:1.25
```

### A Complete Pod Manifest

```yaml
# pod-complete.yaml
apiVersion: v1
kind: Pod
metadata:
  name: webapp
  namespace: default                  # Namespace (default if omitted)
  labels:                             # Key-value labels for selection
    app: webapp
    version: "1.0"
    tier: frontend
  annotations:                        # Non-identifying metadata
    description: "Frontend web application"
    maintainer: "devops@company.com"

spec:
  containers:
    - name: webapp
      image: nginx:1.25
      ports:
        - containerPort: 80
          protocol: TCP

      env:                            # Environment variables
        - name: APP_ENV
          value: production
        - name: DB_HOST
          value: postgres-service
        - name: SECRET_KEY
          valueFrom:
            secretKeyRef:             # From a Secret
              name: app-secret
              key: secret-key

      resources:                      # CPU and memory limits
        requests:                     # Minimum guaranteed resources
          cpu: "100m"                 # 100 millicores = 0.1 CPU
          memory: "128Mi"             # 128 Megabytes
        limits:                       # Maximum allowed resources
          cpu: "500m"                 # 500 millicores = 0.5 CPU
          memory: "256Mi"

      livenessProbe:                  # Is the container alive?
        httpGet:
          path: /healthz
          port: 80
        initialDelaySeconds: 10
        periodSeconds: 5
        failureThreshold: 3

      readinessProbe:                 # Is the container ready for traffic?
        httpGet:
          path: /ready
          port: 80
        initialDelaySeconds: 5
        periodSeconds: 3

      volumeMounts:
        - name: config-volume
          mountPath: /etc/config
        - name: log-volume
          mountPath: /var/log/app

  volumes:
    - name: config-volume
      configMap:
        name: app-config
    - name: log-volume
      emptyDir: {}                    # Temporary directory (lives with Pod)

  restartPolicy: Always               # Always | OnFailure | Never

  nodeSelector:                       # Schedule on nodes with this label
    disk: ssd

  tolerations:                        # Allow scheduling on tainted nodes
    - key: "dedicated"
      operator: "Equal"
      value: "webapp"
      effect: "NoSchedule"
```

### Creating Objects from YAML

```bash
# Create from a YAML file
kubectl create -f pod-complete.yaml

# Create or update (declarative approach - preferred)
kubectl apply -f pod-complete.yaml

# Create from a URL
kubectl apply -f https://k8s.io/examples/pods/simple-pod.yaml

# Apply all YAML files in a directory
kubectl apply -f ./manifests/

# Dry run (validate without creating)
kubectl apply -f pod-complete.yaml --dry-run=client

# Generate YAML from imperative command
kubectl run nginx --image=nginx --dry-run=client -o yaml
```

### YAML Tips and Tricks

```bash
# Generate Pod YAML without creating it
kubectl run nginx --image=nginx --dry-run=client -o yaml > my-pod.yaml

# Edit a live resource
kubectl edit pod webapp

# Get the YAML of a running resource
kubectl get pod webapp -o yaml

# Explain any field in a resource
kubectl explain pod
kubectl explain pod.spec
kubectl explain pod.spec.containers
kubectl explain pod.spec.containers.resources

# Validate a YAML file
kubectl apply --dry-run=client -f pod.yaml
```

### Understanding Pod Phases

|Phase|Description|
|---|---|
|**Pending**|Pod accepted, but containers not yet created (scheduling/image pull)|
|**Running**|Pod bound to a node, all containers created, at least one is running|
|**Succeeded**|All containers exited with status 0 (success), won't be restarted|
|**Failed**|All containers have exited, at least one failed (non-zero exit)|
|**Unknown**|Pod state cannot be determined (node communication failure)|

---

## 🧪 Hands-on Lab: Pods with YAML

### Lab Duration: 45 minutes

---

### Exercise 1: Create Pods from YAML

Create the following Pod manifests and deploy them:

**`pod-nginx.yaml`:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-yaml
  labels:
    app: nginx
    tier: frontend
spec:
  containers:
    - name: nginx
      image: nginx:1.25
      ports:
        - containerPort: 80
      resources:
        requests:
          cpu: "50m"
          memory: "64Mi"
        limits:
          cpu: "200m"
          memory: "128Mi"
```

**`pod-multi.yaml`** (multi-container Pod):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container
  labels:
    app: multi
spec:
  containers:
    - name: main-app
      image: nginx:1.25
      ports:
        - containerPort: 80
      volumeMounts:
        - name: shared-logs
          mountPath: /var/log/nginx

    - name: log-watcher
      image: busybox
      command: ["/bin/sh", "-c", "tail -f /logs/access.log 2>/dev/null || sleep 3600"]
      volumeMounts:
        - name: shared-logs
          mountPath: /logs

  volumes:
    - name: shared-logs
      emptyDir: {}
```

```bash
# Deploy both Pods
kubectl apply -f pod-nginx.yaml
kubectl apply -f pod-multi.yaml

# Verify they are running
kubectl get pods -o wide

# Inspect each Pod
kubectl describe pod nginx-yaml
kubectl describe pod multi-container

# Access logs from each container in the multi-container Pod
kubectl logs multi-container -c main-app
kubectl logs multi-container -c log-watcher

# Execute in a specific container
kubectl exec -it multi-container -c log-watcher -- sh
```

---

### Exercise 2: Generate YAML and Modify

```bash
# Generate YAML for a redis Pod
kubectl run redis --image=redis:7 --dry-run=client -o yaml > redis-pod.yaml

# Edit the file to add:
# - A label: tier=cache
# - Resource limits: cpu=200m, memory=256Mi
# - Port: 6379

# Solution: redis-pod.yaml should look like:
cat > redis-pod.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: redis
  labels:
    app: redis
    tier: cache
spec:
  containers:
    - name: redis
      image: redis:7
      ports:
        - containerPort: 6379
      resources:
        requests:
          cpu: "50m"
          memory: "64Mi"
        limits:
          cpu: "200m"
          memory: "256Mi"
EOF

# Apply and verify
kubectl apply -f redis-pod.yaml
kubectl get pod redis -o wide
kubectl describe pod redis
```

---

## 2.2 Replication Controllers and ReplicaSets

### Why We Need Replication

A plain Pod is not self-healing. If a Pod crashes, it is gone. In production, you need:

- **High availability**: Multiple instances of your application
- **Automatic recovery**: Failed Pods automatically replaced
- **Load distribution**: Traffic spread across multiple Pod instances
- **Scaling**: Ability to add or remove instances

### Replication Controller (Legacy)

The **ReplicationController** (RC) was the original way to ensure a specified number of Pod replicas are running at any time. It is now replaced by ReplicaSets.

```yaml
# replication-controller.yaml (legacy - prefer ReplicaSet)
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx-rc
spec:
  replicas: 3
  selector:
    app: nginx         # Matches Pods with this label
  template:            # Pod template (what Pods to create)
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
```

### ReplicaSet

A **ReplicaSet** (RS) is the next-generation Replication Controller. The key difference is that ReplicaSet supports **set-based label selectors** (more expressive matching).

```yaml
# replicaset.yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
  labels:
    app: nginx
spec:
  replicas: 3           # Desired number of Pod replicas

  selector:             # How the RS finds its Pods
    matchLabels:
      app: nginx
    # matchExpressions example:
    # matchExpressions:
    #   - key: app
    #     operator: In
    #     values: [nginx, webserver]

  template:             # Pod template
    metadata:
      labels:
        app: nginx       # MUST match the selector above
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "200m"
              memory: "128Mi"
```

### How ReplicaSets Work

```
ReplicaSet Controller watches:
  Desired state (spec.replicas): 3
  Actual state (running pods):   ?

  If actual < desired → Create new Pods
  If actual > desired → Delete excess Pods
  If actual == desired → Do nothing

This reconciliation loop runs continuously.
```

### Managing ReplicaSets

```bash
# Create the ReplicaSet
kubectl apply -f replicaset.yaml

# View ReplicaSet status
kubectl get replicasets
# NAME       DESIRED   CURRENT   READY   AGE
# nginx-rs   3         3         3       30s

# Describe the ReplicaSet
kubectl describe replicaset nginx-rs

# Scale the ReplicaSet
kubectl scale replicaset nginx-rs --replicas=5

# Or edit the YAML and apply
kubectl edit replicaset nginx-rs    # Opens editor, change replicas

# Delete a Pod and watch RS recreate it
kubectl delete pod nginx-rs-xxxxx
kubectl get pods -w   # A new Pod appears immediately

# Delete the ReplicaSet (also deletes all its Pods)
kubectl delete replicaset nginx-rs

# Delete RS but keep the Pods
kubectl delete replicaset nginx-rs --cascade=orphan
```

### ReplicaSet Label Matching

The relationship between a ReplicaSet and its Pods is defined by labels:

```bash
# The RS "owns" Pods whose labels match the selector
# Important: If you manually create a Pod with matching labels,
# the RS will consider it one of its own and NOT create a new one!

# Check which Pods are owned by the RS
kubectl get pods -l app=nginx

# Labels can be filtered
kubectl get pods --selector="app=nginx,tier=frontend"
```

---

## 🧪 Hands-on Lab: ReplicaSets

### Lab Duration: 45 minutes

---

### Exercise 1: Create and Scale a ReplicaSet

```bash
# Create replicaset.yaml
cat > replicaset.yaml << 'EOF'
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: webapp-rs
  labels:
    app: webapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        - name: webapp
          image: nginx:1.25
          ports:
            - containerPort: 80
EOF

# Deploy it
kubectl apply -f replicaset.yaml

# Verify 2 Pods are running
kubectl get rs
kubectl get pods -l app=webapp

# Scale to 4 replicas
kubectl scale rs webapp-rs --replicas=4
kubectl get pods -l app=webapp   # Should show 4 Pods

# Test self-healing: delete a Pod
POD=$(kubectl get pods -l app=webapp -o jsonpath='{.items[0].metadata.name}')
kubectl delete pod $POD
kubectl get pods -l app=webapp -w   # Watch a new one appear

# Scale back down
kubectl scale rs webapp-rs --replicas=2

# Clean up
kubectl delete rs webapp-rs
```

---

### Exercise 2: ReplicaSet and Label Matching

```bash
# Create a ReplicaSet with 3 replicas
cat > rs-label-demo.yaml << 'EOF'
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: label-demo-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
EOF

kubectl apply -f rs-label-demo.yaml
kubectl get pods -l app=demo   # 3 Pods

# Now manually create a Pod with the SAME label
kubectl run extra-pod --image=nginx --labels="app=demo"

# The RS will now see 4 Pods but only wants 3
kubectl get pods -l app=demo
# One Pod will be TERMINATED by the RS to maintain 3 replicas

# Clean up
kubectl delete rs label-demo-rs
kubectl delete pod extra-pod --ignore-not-found
```

---

## 2.3 Deployments

### What is a Deployment?

A **Deployment** provides declarative updates for Pods and ReplicaSets. It is the recommended way to run stateless applications in Kubernetes. A Deployment manages a ReplicaSet, which manages Pods.

```
Deployment
    └── ReplicaSet (current version)
            ├── Pod
            ├── Pod
            └── Pod
```

### Why Deployments Over ReplicaSets?

|Feature|ReplicaSet|Deployment|
|---|---|---|
|Maintain replicas|✅|✅|
|Rolling updates|❌|✅|
|Rollbacks|❌|✅|
|Update history|❌|✅|
|Pause/Resume updates|❌|✅|

### Creating a Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx

spec:
  replicas: 3                       # Desired Pod count

  selector:
    matchLabels:
      app: nginx

  strategy:                         # Update strategy
    type: RollingUpdate             # RollingUpdate | Recreate
    rollingUpdate:
      maxSurge: 1                   # Max extra Pods during update
      maxUnavailable: 1             # Max Pods that can be unavailable

  template:                         # Pod template
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.24         # Start with version 1.24
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "200m"
              memory: "128Mi"

          readinessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 5
```

### Managing Deployments

```bash
# Create the Deployment
kubectl apply -f deployment.yaml

# View Deployment status
kubectl get deployments
# NAME               READY   UP-TO-DATE   AVAILABLE   AGE
# nginx-deployment   3/3     3            3           1m

# Rollout status (wait for completion)
kubectl rollout status deployment/nginx-deployment

# View Deployment details
kubectl describe deployment nginx-deployment

# See the managed ReplicaSet
kubectl get rs
# NAME                          DESIRED   CURRENT   READY   AGE
# nginx-deployment-5d589d69c7   3         3         3       1m

# Scale the Deployment
kubectl scale deployment nginx-deployment --replicas=5
```

---

## 2.4 Deployments – Update and Rollback

### Deployment Update Strategies

#### Rolling Update (Default and Recommended)

Rolling updates replace Pods gradually, ensuring zero downtime:

```
Before Update:   [v1] [v1] [v1] [v1]
During Update:   [v1] [v1] [v2] [v2]   (gradual replacement)
After Update:    [v2] [v2] [v2] [v2]
```

#### Recreate Strategy

All existing Pods are killed, then new ones are created. Causes downtime but ensures no two versions run simultaneously:

```yaml
strategy:
  type: Recreate
```

### Performing a Rolling Update

```bash
# Method 1: Update the image using kubectl set
kubectl set image deployment/nginx-deployment nginx=nginx:1.25

# Method 2: Edit the deployment live
kubectl edit deployment nginx-deployment
# Change the image tag in the editor

# Method 3: Apply an updated YAML file
# (change image: nginx:1.24 to image: nginx:1.25 in deployment.yaml)
kubectl apply -f deployment.yaml

# Watch the rolling update in real time
kubectl rollout status deployment/nginx-deployment

# Watch Pods being replaced
kubectl get pods -w
```

### Deployment Rollback

```bash
# View rollout history
kubectl rollout history deployment/nginx-deployment
# REVISION  CHANGE-CAUSE
# 1         <none>
# 2         <none>

# Add a change cause (annotation) for better tracking
kubectl annotate deployment/nginx-deployment \
  kubernetes.io/change-cause="Update nginx to 1.25"

# Rollback to the previous revision
kubectl rollout undo deployment/nginx-deployment

# Rollback to a specific revision
kubectl rollout undo deployment/nginx-deployment --to-revision=1

# Check rollout history with details
kubectl rollout history deployment/nginx-deployment --revision=1
```

### Pause and Resume Updates

```bash
# Pause a rollout (useful for canary-style updates)
kubectl rollout pause deployment/nginx-deployment

# Make changes while paused (they accumulate)
kubectl set image deployment/nginx-deployment nginx=nginx:1.25
kubectl set resources deployment/nginx-deployment \
  -c nginx --limits=cpu=200m,memory=128Mi

# Resume the rollout (all changes apply together)
kubectl rollout resume deployment/nginx-deployment
```

### Full Update/Rollback Demo

```bash
# Step 1: Create initial deployment (v1.24)
cat > deployment-demo.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  annotations:
    kubernetes.io/change-cause: "Initial deployment - nginx 1.24"
spec:
  replicas: 3
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        - name: nginx
          image: nginx:1.24
          ports:
            - containerPort: 80
EOF

kubectl apply -f deployment-demo.yaml
kubectl rollout status deployment/webapp
kubectl rollout history deployment/webapp

# Step 2: Update to v1.25
kubectl set image deployment/webapp nginx=nginx:1.25
kubectl annotate deployment/webapp \
  kubernetes.io/change-cause="Updated nginx to 1.25" --overwrite

kubectl rollout status deployment/webapp
kubectl rollout history deployment/webapp

# Step 3: Simulate a bad update
kubectl set image deployment/webapp nginx=nginx:doesnotexist
kubectl annotate deployment/webapp \
  kubernetes.io/change-cause="Bad update - broken image" --overwrite

kubectl rollout status deployment/webapp   # Will show failure
kubectl get pods   # Some will show ImagePullBackOff

# Step 4: Rollback!
kubectl rollout undo deployment/webapp
kubectl rollout status deployment/webapp
kubectl get pods   # All running again on nginx:1.25

# Verify history
kubectl rollout history deployment/webapp
```

---

## 🧪 Hands-on Lab: Deployments

### Lab Duration: 60 minutes

---

### Exercise 1: Create and Scale a Deployment

```bash
# Create a deployment
cat > lab-deployment.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpd-deploy
  labels:
    app: httpd
spec:
  replicas: 3
  selector:
    matchLabels:
      app: httpd
  template:
    metadata:
      labels:
        app: httpd
    spec:
      containers:
        - name: httpd
          image: httpd:2.4
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "150m"
              memory: "128Mi"
EOF

kubectl apply -f lab-deployment.yaml

# Verify
kubectl get deployments
kubectl get rs
kubectl get pods

# Scale up
kubectl scale deployment httpd-deploy --replicas=6
kubectl get pods   # Should show 6 Pods

# Scale down
kubectl scale deployment httpd-deploy --replicas=2
kubectl get pods   # Should show 2 Pods
```

---

### Exercise 2: Perform a Rolling Update and Rollback

```bash
# Check current state
kubectl get deployment httpd-deploy
kubectl rollout history deployment/httpd-deploy

# Update the image
kubectl set image deployment/httpd-deploy httpd=httpd:2.4.57
kubectl annotate deployment/httpd-deploy \
  kubernetes.io/change-cause="Updated httpd to 2.4.57" --overwrite

# Watch the rolling update
kubectl rollout status deployment/httpd-deploy
kubectl get pods -w

# View history
kubectl rollout history deployment/httpd-deploy

# Introduce a bad update
kubectl set image deployment/httpd-deploy httpd=httpd:99.99.99
kubectl annotate deployment/httpd-deploy \
  kubernetes.io/change-cause="Bad image - testing rollback" --overwrite

# Observe the failure
kubectl get pods

# Rollback to the previous working version
kubectl rollout undo deployment/httpd-deploy

# Confirm recovery
kubectl rollout status deployment/httpd-deploy
kubectl rollout history deployment/httpd-deploy

# Clean up
kubectl delete deployment httpd-deploy
```

---

# Module 3 – Networking in Kubernetes

## Module Overview

This module provides an introduction to networking concepts in Kubernetes, including how Pods communicate with each other and with external resources.

### Learning Objectives

- Understand the basics of networking in Kubernetes

---

## 3.1 Basics of Networking in Kubernetes

### The Kubernetes Networking Model

Kubernetes defines a flat networking model with these fundamental rules:

1. **Every Pod gets its own IP address** — Pods communicate directly using IP addresses without NAT
2. **All Pods can communicate with all other Pods** — across nodes, without NAT
3. **All nodes can communicate with all Pods** — without NAT
4. **The IP a Pod sees itself as is the same IP others see it as** — no masquerading

```
Node 1 (10.0.0.1)              Node 2 (10.0.0.2)
┌──────────────────────┐       ┌──────────────────────┐
│  Pod A  (10.244.1.2) │──────▶│  Pod C  (10.244.2.3) │
│  Pod B  (10.244.1.3) │◀──────│  Pod D  (10.244.2.4) │
└──────────────────────┘       └──────────────────────┘
         │                              │
         └──────────────────────────────┘
              Direct communication
              No NAT required
```

### Container-to-Container Communication (Within a Pod)

Containers in the same Pod share a network namespace. They communicate via `localhost`:

```yaml
# Two containers in the same Pod
spec:
  containers:
    - name: web
      image: nginx
      # Nginx listens on port 80

    - name: log-collector
      image: fluentd
      # Can reach nginx via localhost:80
```

```bash
# Inside log-collector container:
curl http://localhost:80    # Works! Same network namespace
```

### Pod-to-Pod Communication

Pods communicate directly using their cluster IP addresses. No NAT is required:

```bash
# Get Pod IPs
kubectl get pods -o wide
# NAME      READY   STATUS    IP            NODE
# pod-a     1/1     Running   10.244.0.5    node1
# pod-b     1/1     Running   10.244.1.3    node2

# From inside pod-a, reach pod-b directly
kubectl exec -it pod-a -- curl http://10.244.1.3:80
```

**Problem**: Pod IPs are ephemeral. When a Pod is replaced, it gets a new IP. This is why Services exist.

### Pod-to-Service Communication

Services provide a stable virtual IP (ClusterIP) that routes to healthy Pod backends:

```
Client Pod ──▶ Service ClusterIP (10.96.0.100) ──▶ Pod 1 (10.244.0.5)
                                                ──▶ Pod 2 (10.244.1.3)
                                                ──▶ Pod 3 (10.244.2.7)
```

### External-to-Service Communication

Traffic from outside the cluster reaches Pods through:

- **NodePort**: Expose a port on every node
- **LoadBalancer**: Cloud load balancer routes to nodes
- **Ingress**: HTTP/HTTPS routing with path-based rules

### Container Network Interface (CNI)

Kubernetes doesn't implement networking itself — it relies on **CNI plugins**:

|CNI Plugin|Description|
|---|---|
|**Flannel**|Simple, flat network; suitable for most use cases|
|**Calico**|Supports Network Policies; widely used in production|
|**Weave Net**|Easy to set up; encrypted by default|
|**Cilium**|eBPF-based; advanced observability and security|
|**Canal**|Combines Flannel routing with Calico policies|

### DNS in Kubernetes

Kubernetes includes a built-in DNS service (CoreDNS) that automatically creates DNS records for Services and Pods:

```
Service DNS format:
  <service-name>.<namespace>.svc.cluster.local

Examples:
  my-service.default.svc.cluster.local
  redis.production.svc.cluster.local

Pod DNS format:
  <pod-ip-dashes>.<namespace>.pod.cluster.local
  10-244-0-5.default.pod.cluster.local
```

```bash
# Test DNS resolution from inside a Pod
kubectl run dns-test --image=busybox --rm -it --restart=Never -- \
  nslookup kubernetes.default.svc.cluster.local

# Check CoreDNS
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

### Network Policies

**NetworkPolicy** objects control traffic flow between Pods (acts like a firewall):

```yaml
# Allow ingress to Pods labeled "app: backend" only from "app: frontend"
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-policy
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

### Ports: containerPort, hostPort, nodePort

|Port Type|Description|
|---|---|
|`containerPort`|Port the container listens on (documentation only, doesn't expose it)|
|`hostPort`|Maps container port directly to host port (avoid in production)|
|`nodePort`|Port exposed on every node via a Service (30000-32767 range)|

---

# Module 4 – Services

## Module Overview

This module introduces Kubernetes Services, which provide a consistent way to access applications. Participants learn about NodePort, ClusterIP, and LoadBalancer services.

### Learning Objectives

- Understand the concept of Services in Kubernetes and their role in enabling communication between Pods

---

## 4.1 Why Services?

Without Services, Pod-to-Pod communication relies on Pod IPs, which change every time a Pod is recreated. Services solve this by providing:

- **A stable virtual IP** (ClusterIP) that doesn't change
- **Automatic load balancing** across all healthy Pods
- **DNS-based discovery** — find Services by name
- **Decoupling** — consumers don't need to know Pod IPs

```
Without Service:                 With Service:

Client ──▶ Pod (10.244.0.5)     Client ──▶ Service (10.96.0.100)
   Pod dies! New IP!              │         │
Client ──▶ ??? (IP changed)       │         ▼
                                  │    Pod (10.244.0.5)
                                  │    Pod (10.244.1.3)
                                  └──▶ Pod (10.244.2.7)
                                   Always the same Service IP!
```

### How Services Find Pods: Label Selectors

Services use **label selectors** to find their Pods:

```yaml
# Service selects Pods with label app=nginx
spec:
  selector:
    app: nginx    # Matches all Pods with app=nginx label

# These Pods will be included:
# Pod with labels: app=nginx, version=1.0  ✅
# Pod with labels: app=nginx, env=prod     ✅
# Pod with labels: app=apache              ❌
```

---

## 4.2 Services: NodePort

**NodePort** exposes the Service on a static port on each Node's IP. Traffic from `<NodeIP>:<NodePort>` is forwarded to the Service, which distributes it to Pods.

```
External User
      │
      ▼
  Node (192.168.1.100)
  NodePort: 30080
      │
      ▼
  Service (ClusterIP: 10.96.0.100)
      │
  ┌───┴───┐
  ▼       ▼
 Pod    Pod
(80)   (80)
```

**NodePort YAML:**

```yaml
# service-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport

spec:
  type: NodePort            # Service type

  selector:
    app: nginx              # Targets Pods with this label

  ports:
    - protocol: TCP
      port: 80              # Service port (ClusterIP:80)
      targetPort: 80        # Port on the Pod container
      nodePort: 30080       # Port on each Node (30000-32767)
                            # If omitted, Kubernetes assigns one randomly
```

```bash
# Create the Service
kubectl apply -f service-nodeport.yaml

# View Services
kubectl get services
# NAME             TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
# nginx-nodeport   NodePort   10.96.78.234   <none>        80:30080/TCP   10s

# Access via NodePort (Minikube)
minikube ip                          # Get Minikube IP
curl http://$(minikube ip):30080     # Access via NodePort

# Or use minikube service command
minikube service nginx-nodeport
minikube service nginx-nodeport --url   # Just print the URL
```

---

## 4.3 Services: ClusterIP

**ClusterIP** is the default Service type. It exposes the Service on an internal cluster IP. Only reachable from within the cluster.

```
                    Cluster (internal only)

Pod A ──▶ ClusterIP (10.96.0.100) ──▶ Pod X
                                  ──▶ Pod Y
Pod B ──▶                         ──▶ Pod Z

External traffic: NOT accessible
```

**ClusterIP YAML:**

```yaml
# service-clusterip.yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-service

spec:
  type: ClusterIP           # Default type (can be omitted)

  selector:
    app: backend

  ports:
    - protocol: TCP
      port: 5000            # Service port
      targetPort: 5000      # Container port
```

**Common Use Cases:**

- Database services (MySQL, PostgreSQL, Redis) — internal only
- Backend APIs called by frontend Pods
- Any service that should NOT be externally accessible

```bash
# Create ClusterIP service
kubectl apply -f service-clusterip.yaml

kubectl get service backend-service
# NAME              TYPE        CLUSTER-IP      PORT(S)    AGE
# backend-service   ClusterIP   10.96.155.200   5000/TCP   5s

# Access only from inside the cluster
kubectl run test --image=busybox --rm -it --restart=Never -- \
  wget -qO- http://backend-service:5000
```

---

## 4.4 Services: LoadBalancer

**LoadBalancer** exposes the Service externally using a cloud provider's load balancer. Automatically provisions an external IP.

```
Internet
    │
    ▼
Cloud Load Balancer (203.0.113.10)  ← External IP
    │
    ▼
Node 1 (NodePort)   Node 2 (NodePort)
    │                    │
    └────────┬───────────┘
             ▼
         Service
         │    │
         ▼    ▼
        Pod  Pod
```

**LoadBalancer YAML:**

```yaml
# service-loadbalancer.yaml
apiVersion: v1
kind: Service
metadata:
  name: webapp-loadbalancer

spec:
  type: LoadBalancer

  selector:
    app: webapp

  ports:
    - protocol: TCP
      port: 80              # External port
      targetPort: 8080      # Container port
```

```bash
# Create LoadBalancer service
kubectl apply -f service-loadbalancer.yaml

# View the service (EXTERNAL-IP will be <pending> locally)
kubectl get service webapp-loadbalancer
# NAME                  TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)
# webapp-loadbalancer   LoadBalancer   10.96.0.200   203.0.113.10   80:31234/TCP

# On Minikube, use tunnel to simulate LoadBalancer
minikube tunnel
# Now EXTERNAL-IP will be assigned (run in a separate terminal)
```

### Service Type Comparison

|Type|Accessible From|Use Case|
|---|---|---|
|**ClusterIP**|Inside cluster only|Internal microservice communication|
|**NodePort**|Outside cluster via NodeIP:Port|Dev/testing, simple exposure|
|**LoadBalancer**|Internet via cloud LB IP|Production external-facing services|
|**ExternalName**|DNS alias to external service|Connecting to external databases|

### Headless Services

A **Headless Service** (ClusterIP: None) returns Pod IPs directly from DNS instead of a single virtual IP. Used for StatefulSets and direct Pod addressing:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: headless-svc
spec:
  clusterIP: None     # Headless!
  selector:
    app: my-app
  ports:
    - port: 80
```

---

## 🧪 Hands-on Lab: Services

### Lab Duration: 60 minutes

---

### Exercise 1: ClusterIP Service

```bash
# Step 1: Create a backend Deployment
cat > backend-deploy.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
        - name: backend
          image: nginx:1.25
          ports:
            - containerPort: 80
EOF

kubectl apply -f backend-deploy.yaml

# Step 2: Create a ClusterIP Service
cat > backend-service.yaml << 'EOF'
apiVersion: v1
kind: Service
metadata:
  name: backend-svc
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
    - port: 80
      targetPort: 80
EOF

kubectl apply -f backend-service.yaml

# Step 3: Verify
kubectl get svc backend-svc
kubectl describe svc backend-svc   # Note the Endpoints

# Step 4: Test from inside the cluster
kubectl run test-client --image=busybox --rm -it --restart=Never -- \
  wget -qO- http://backend-svc

# Step 5: Verify DNS resolution
kubectl run dns-test --image=busybox --rm -it --restart=Never -- \
  nslookup backend-svc
```

---

### Exercise 2: NodePort Service

```bash
# Step 1: Create a frontend Deployment
cat > frontend-deploy.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
EOF

kubectl apply -f frontend-deploy.yaml

# Step 2: Expose via NodePort
cat > frontend-nodeport.yaml << 'EOF'
apiVersion: v1
kind: Service
metadata:
  name: frontend-svc
spec:
  type: NodePort
  selector:
    app: frontend
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30090
EOF

kubectl apply -f frontend-nodeport.yaml

# Step 3: Access the service
minikube service frontend-svc --url
# Copy the URL and open in browser

# Or curl it
curl $(minikube service frontend-svc --url)

# Step 4: Clean up
kubectl delete deployment frontend backend
kubectl delete service frontend-svc backend-svc
```

---

# Module 5 – Microservices Architecture

## Module Overview

This module provides an overview of Microservices Architecture and demonstrates deploying a sample voting application on Kubernetes using microservices principles.

### Learning Objectives

- Understand the principles and benefits of Microservices Architecture

---

## 5.1 Microservices Architecture

### What are Microservices?

**Microservices Architecture** is a software design approach where an application is built as a collection of small, independent services that:

- Each run in their own process
- Communicate via well-defined APIs (HTTP REST, gRPC, message queues)
- Are independently deployable and scalable
- Are organized around business capabilities
- Are owned by small, autonomous teams

```
Monolith:                          Microservices:
┌──────────────────┐               ┌─────────┐  ┌──────────┐
│                  │               │  User   │  │  Product │
│  User Service    │               │ Service │  │ Service  │
│  Product Service │    becomes    └─────────┘  └──────────┘
│  Order Service   │   ─────────▶
│  Payment Service │               ┌─────────┐  ┌──────────┐
│  Notification Svc│               │  Order  │  │ Payment  │
│                  │               │ Service │  │ Service  │
└──────────────────┘               └─────────┘  └──────────┘
```

### Key Principles of Microservices

|Principle|Description|
|---|---|
|**Single Responsibility**|Each service does one thing well|
|**Loose Coupling**|Services are independent; changing one doesn't break others|
|**High Cohesion**|Related functionality is grouped together|
|**Independently Deployable**|Each service can be deployed without deploying others|
|**Decentralized Data**|Each service owns its own database|
|**Designed for Failure**|Assumes failures happen; built to be resilient|
|**Observable**|Rich logging, metrics, and tracing|

### Advantages of Microservices

- **Independent scaling**: Scale only the services that need it
- **Technology flexibility**: Each service can use different languages/frameworks
- **Faster deployment**: Small, focused services deploy quickly
- **Fault isolation**: One service failing doesn't bring down everything
- **Team autonomy**: Teams own their services end-to-end

### Challenges of Microservices

- **Distributed system complexity**: Network failures, latency, partial failures
- **Data consistency**: No single transaction across services
- **Service discovery**: How do services find each other?
- **Operational overhead**: More services = more to manage, monitor, deploy
- **Testing complexity**: Integration testing is harder

### Kubernetes and Microservices

Kubernetes is the perfect platform for microservices because it provides:

- **Pod isolation**: Each microservice runs in its own Pods
- **Service discovery**: Services find each other via DNS
- **Independent scaling**: Scale each Deployment separately
- **Rolling updates**: Update each service with zero downtime
- **Health management**: Auto-restart failed containers
- **Configuration management**: ConfigMaps and Secrets

---

## 5.2 Deploying a Voting App on Kubernetes

### The Voting Application Architecture

We'll deploy the classic **Example Voting App** — a multi-service application that demonstrates microservices on Kubernetes:

```
                         ┌──────────────────────────────────────────┐
                         │              Kubernetes Cluster           │
                         │                                          │
  [Browser]──────────────▶  voting-app (Python/Flask)              │
  Vote: Cat or Dog        │      │                                  │
                         │      ▼                                  │
                         │  redis (in-memory queue)                 │
                         │      │                                  │
                         │      ▼                                  │
                         │  worker (.NET)                          │
                         │      │                                  │
                         │      ▼                                  │
                         │  db (PostgreSQL)                        │
                         │      │                                  │
  [Browser]──────────────▶  result-app (Node.js)                  │
  View results            │                                        │
                         └──────────────────────────────────────────┘
```

### Component Breakdown

|Component|Image|Description|
|---|---|---|
|**voting-app**|`dockersamples/examplevotingapp_vote`|Python Flask app — accept votes|
|**redis**|`redis:alpine`|Stores votes temporarily in a queue|
|**worker**|`dockersamples/examplevotingapp_worker`|Reads from Redis, writes to PostgreSQL|
|**db**|`postgres:15`|Persistent storage for vote results|
|**result-app**|`dockersamples/examplevotingapp_result`|Node.js app — display results|

### Step 1: Create the Namespace

```bash
# Create a dedicated namespace
kubectl create namespace voting-app

# Set it as the default for this session
kubectl config set-context --current --namespace=voting-app
```

### Step 2: Deploy Redis

```yaml
# redis-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: voting-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
        - name: redis
          image: redis:alpine
          ports:
            - containerPort: 6379
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "200m"
              memory: "128Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: redis
  namespace: voting-app
spec:
  type: ClusterIP
  selector:
    app: redis
  ports:
    - port: 6379
      targetPort: 6379
```

### Step 3: Deploy PostgreSQL

```yaml
# postgres-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db
  namespace: voting-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
        - name: postgres
          image: postgres:15
          env:
            - name: POSTGRES_USER
              value: "postgres"
            - name: POSTGRES_PASSWORD
              value: "postgres"
            - name: POSTGRES_DB
              value: "votes"
          ports:
            - containerPort: 5432
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: db
  namespace: voting-app
spec:
  type: ClusterIP
  selector:
    app: db
  ports:
    - port: 5432
      targetPort: 5432
```

### Step 4: Deploy the Worker

```yaml
# worker-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: worker
  namespace: voting-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: worker
  template:
    metadata:
      labels:
        app: worker
    spec:
      containers:
        - name: worker
          image: dockersamples/examplevotingapp_worker
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "200m"
              memory: "256Mi"
```

### Step 5: Deploy the Voting Frontend

```yaml
# voting-app-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: voting-app
  namespace: voting-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: voting-app
  template:
    metadata:
      labels:
        app: voting-app
    spec:
      containers:
        - name: voting-app
          image: dockersamples/examplevotingapp_vote
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "200m"
              memory: "128Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: voting-app-svc
  namespace: voting-app
spec:
  type: NodePort
  selector:
    app: voting-app
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30004
```

### Step 6: Deploy the Result Frontend

```yaml
# result-app-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: result-app
  namespace: voting-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: result-app
  template:
    metadata:
      labels:
        app: result-app
    spec:
      containers:
        - name: result-app
          image: dockersamples/examplevotingapp_result
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "200m"
              memory: "128Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: result-app-svc
  namespace: voting-app
spec:
  type: NodePort
  selector:
    app: result-app
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30005
```

### Step 7: Deploy Everything

```bash
# Create all resources at once
kubectl apply -f redis-deploy.yaml
kubectl apply -f postgres-deploy.yaml
kubectl apply -f worker-deploy.yaml
kubectl apply -f voting-app-deploy.yaml
kubectl apply -f result-app-deploy.yaml

# Or put all YAML files in a directory and apply all at once
# kubectl apply -f voting-app/

# Watch everything come up
kubectl get pods -n voting-app -w

# Once all Pods are Running:
kubectl get pods -n voting-app
kubectl get services -n voting-app
kubectl get deployments -n voting-app
```

### Step 8: Access the Application

```bash
# Get voting app URL
minikube service voting-app-svc -n voting-app --url

# Get result app URL
minikube service result-app-svc -n voting-app --url

# Open both in your browser
minikube service voting-app-svc -n voting-app
minikube service result-app-svc -n voting-app
```

### Step 9: Using Deployments for Production-Grade Setup

For production, add proper resource limits, health probes, and multiple replicas:

```yaml
# voting-app-production.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: voting-app
  namespace: voting-app
  annotations:
    kubernetes.io/change-cause: "Initial production deployment"
spec:
  replicas: 3                         # High availability
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0               # Zero downtime

  selector:
    matchLabels:
      app: voting-app

  template:
    metadata:
      labels:
        app: voting-app
    spec:
      containers:
        - name: voting-app
          image: dockersamples/examplevotingapp_vote
          ports:
            - containerPort: 80

          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "500m"
              memory: "256Mi"

          readinessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 10
            periodSeconds: 5
            failureThreshold: 3

          livenessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 30
            periodSeconds: 10
            failureThreshold: 5

      terminationGracePeriodSeconds: 30
```

---

## 🧪 Hands-on Lab: Deploy the Voting App

### Lab Duration: 75 minutes

---

### Lab Steps

```bash
# Step 1: Set up namespace
kubectl create namespace vote-lab
kubectl config set-context --current --namespace=vote-lab

# Step 2: Save all manifests from Step 2-6 above as files,
#         then deploy in dependency order:
kubectl apply -f redis-deploy.yaml
kubectl apply -f postgres-deploy.yaml
kubectl apply -f worker-deploy.yaml
kubectl apply -f voting-app-deploy.yaml
kubectl apply -f result-app-deploy.yaml

# Step 3: Monitor deployment progress
kubectl get pods -w

# Step 4: Verify all services exist
kubectl get svc

# Step 5: Access the apps
minikube service voting-app-svc --url
minikube service result-app-svc --url

# Step 6: Cast some votes and see results update

# Step 7: Scale the voting app to 3 replicas
kubectl scale deployment voting-app --replicas=3
kubectl get pods   # Verify 3 voting-app Pods

# Step 8: Check the worker logs
kubectl logs deployment/worker

# Step 9: Verify the data flow
kubectl exec -it deployment/redis -- redis-cli llen votes
kubectl exec -it deployment/db -- psql -U postgres votes \
  -c "SELECT vote, COUNT(*) FROM votes GROUP BY vote;"

# Step 10: Simulate a failure
POD=$(kubectl get pods -l app=voting-app -o jsonpath='{.items[0].metadata.name}')
kubectl delete pod $POD
kubectl get pods   # Deployment auto-creates a replacement

# Step 11: Clean up
kubectl delete namespace vote-lab
kubectl config set-context --current --namespace=default
```

---

# Module 6 – Conclusion

## Course Summary

Congratulations on completing **Kubernetes Basics for DevOps**! Here is a comprehensive review of everything you have learned.

---

## Key Concepts Recap

### Module 1: Kubernetes Overview

**Containers** package applications with all dependencies, solving the "works on my machine" problem. They are lightweight, fast, and portable compared to VMs.

**Container Orchestration** automates the management of containerized applications at scale — handling scheduling, scaling, healing, networking, and storage.

**Kubernetes Architecture** consists of:

- **Control Plane**: API Server, etcd, Scheduler, Controller Manager
- **Worker Nodes**: kubelet, kube-proxy, Container Runtime

**Pods** are the smallest deployable units in Kubernetes. Each Pod gets its own IP, and containers within a Pod share network and storage.

---

### Module 2: PODs, ReplicaSets, Deployments

**YAML Manifests** follow the structure: `apiVersion`, `kind`, `metadata`, `spec`. All Kubernetes objects are defined and managed this way.

**ReplicaSets** ensure a specified number of Pod replicas are always running. They provide self-healing — if a Pod dies, the ReplicaSet creates a replacement.

**Deployments** manage ReplicaSets and add the ability to:

- Perform rolling updates with zero downtime
- Roll back to previous versions
- Track revision history
- Pause and resume updates

---

### Module 3: Networking

Kubernetes follows a flat networking model where:

- Every Pod gets a unique IP
- All Pods can communicate directly (no NAT)
- DNS (CoreDNS) provides name-based service discovery
- CNI plugins implement the actual networking

---

### Module 4: Services

**Services** provide stable endpoints for accessing Pods:

- **ClusterIP**: Internal only — microservice-to-microservice
- **NodePort**: External access via NodeIP:Port — dev/testing
- **LoadBalancer**: Cloud load balancer — production external access

Services use **label selectors** to find target Pods dynamically.

---

### Module 5: Microservices Architecture

**Microservices** decompose monoliths into small, independent, loosely-coupled services. Kubernetes is the ideal platform for microservices because it handles:

- Independent deployment and scaling of each service
- Service discovery via DNS
- Health management and auto-recovery
- Rolling updates with zero downtime

---

## Essential kubectl Quick Reference

```bash
# ─────────────── CLUSTER INFO ───────────────
kubectl cluster-info                        # Cluster endpoint info
kubectl get nodes                           # List nodes
kubectl get nodes -o wide                   # Nodes with details

# ─────────────── NAMESPACES ─────────────────
kubectl get namespaces                      # List namespaces
kubectl create namespace my-ns              # Create namespace
kubectl config set-context --current --namespace=my-ns  # Switch namespace

# ─────────────── PODS ───────────────────────
kubectl run mypod --image=nginx             # Create pod imperatively
kubectl get pods                            # List pods
kubectl get pods -o wide                    # Pods with node/IP details
kubectl get pods -A                         # All namespaces
kubectl describe pod mypod                  # Detailed pod info
kubectl logs mypod                          # View logs
kubectl logs -f mypod                       # Follow logs
kubectl exec -it mypod -- /bin/sh          # Shell into pod
kubectl port-forward pod/mypod 8080:80     # Port forward
kubectl delete pod mypod                    # Delete pod

# ─────────────── DEPLOYMENTS ────────────────
kubectl create deployment myapp --image=nginx  # Create deployment
kubectl get deployments                     # List deployments
kubectl describe deployment myapp           # Deployment details
kubectl scale deployment myapp --replicas=5 # Scale
kubectl set image deployment/myapp nginx=nginx:1.25  # Update image
kubectl rollout status deployment/myapp     # Rollout status
kubectl rollout history deployment/myapp    # Rollout history
kubectl rollout undo deployment/myapp       # Rollback
kubectl delete deployment myapp             # Delete deployment

# ─────────────── SERVICES ───────────────────
kubectl get services                        # List services
kubectl describe service myservice          # Service details
kubectl expose deployment myapp --port=80 --type=NodePort  # Expose
minikube service myservice --url            # Get Minikube URL
kubectl delete service myservice            # Delete service

# ─────────────── REPLICASETS ────────────────
kubectl get replicasets                     # List replicasets
kubectl describe rs myrs                    # ReplicaSet details
kubectl scale rs myrs --replicas=3          # Scale RS

# ─────────────── YAML OPERATIONS ────────────
kubectl apply -f manifest.yaml              # Create/update from file
kubectl delete -f manifest.yaml             # Delete from file
kubectl get pod mypod -o yaml               # Get resource as YAML
kubectl explain pod.spec                    # API documentation
kubectl api-resources                       # List all resource types

# ─────────────── LABELS & SELECTORS ─────────
kubectl get pods -l app=nginx               # Filter by label
kubectl label pod mypod env=prod            # Add label
kubectl get pods --show-labels              # Show all labels

# ─────────────── DEBUGGING ──────────────────
kubectl describe pod mypod                  # Events and state
kubectl logs mypod --previous              # Logs from crashed container
kubectl get events                          # Cluster events
kubectl top pods                            # Resource usage (needs metrics-server)
kubectl top nodes                           # Node resource usage
```

---

## Kubernetes Object Cheat Sheet

|Object|API Version|Purpose|
|---|---|---|
|Pod|v1|Smallest deployable unit|
|ReplicaSet|apps/v1|Maintains Pod replicas|
|Deployment|apps/v1|Manages RSes, rolling updates|
|Service|v1|Stable network endpoint|
|ConfigMap|v1|Non-sensitive configuration|
|Secret|v1|Sensitive data (passwords, keys)|
|Namespace|v1|Virtual cluster isolation|
|PersistentVolume|v1|Storage resource|
|PersistentVolumeClaim|v1|Request for storage|
|Ingress|networking.k8s.io/v1|HTTP/HTTPS routing|
|StatefulSet|apps/v1|Stateful app management|
|DaemonSet|apps/v1|Run Pod on every node|
|Job|batch/v1|One-time task|
|CronJob|batch/v1|Scheduled task|

---

## Recommended Next Steps

Having completed this course, here are the next topics to explore on your Kubernetes journey:

**Immediate Next Steps:**

- **ConfigMaps & Secrets** — Manage application configuration and sensitive data
- **Persistent Volumes** — Provide durable storage for stateful applications
- **Namespaces** — Organize and isolate workloads within a cluster
- **Resource Quotas & LimitRanges** — Control resource consumption per namespace

**Intermediate Topics:**

- **Ingress Controllers** — HTTP routing, SSL termination, virtual hosting (NGINX Ingress, Traefik)
- **StatefulSets** — Manage stateful applications like databases (MySQL, MongoDB, Kafka)
- **DaemonSets** — Deploy one Pod per node (log collectors, monitoring agents)
- **RBAC** — Role-Based Access Control for securing cluster access
- **Horizontal Pod Autoscaling (HPA)** — Automatically scale based on CPU/memory metrics

**Advanced Topics:**

- **Helm** — The Kubernetes package manager for templating and managing complex applications
- **Operators** — Custom controllers that extend Kubernetes for specific workloads
- **Service Mesh** — Istio or Linkerd for advanced traffic management and observability
- **GitOps** — ArgoCD or Flux for declarative, Git-driven cluster management
- **Multi-cluster Management** — Manage multiple Kubernetes clusters

**Certifications to Pursue:**

- **CKAD** — Certified Kubernetes Application Developer
- **CKA** — Certified Kubernetes Administrator
- **CKS** — Certified Kubernetes Security Specialist

---

## Course Resources

### Official Documentation

- [Kubernetes Documentation](https://kubernetes.io/docs/) — The definitive reference
- [kubectl Reference](https://kubernetes.io/docs/reference/kubectl/) — All kubectl commands
- [Kubernetes API Reference](https://kubernetes.io/docs/reference/kubernetes-api/) — Full API spec
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/) — Deep dives on every concept

### Tools Referenced in This Course

- [Minikube](https://minikube.sigs.k8s.io/docs/) — Local Kubernetes cluster
- [kubectl](https://kubernetes.io/docs/tasks/tools/) — Kubernetes CLI
- [Helm](https://helm.sh/docs/) — Kubernetes package manager
- [Docker](https://docs.docker.com/) — Container runtime and build tool

### Practice Environments

- [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes) — Free browser-based Kubernetes environments
- [Play with Kubernetes](https://labs.play-with-k8s.com/) — Free temporary Kubernetes clusters
- [KodeKloud](https://kodekloud.com/) — Interactive Kubernetes labs

### Community

- [Kubernetes Slack](https://kubernetes.slack.com/) — Official community Slack
- [CNCF Community](https://www.cncf.io/community/) — Cloud Native Computing Foundation
- [r/kubernetes](https://www.reddit.com/r/kubernetes/) — Reddit community

---

_This tutorial was created to provide a comprehensive introduction to Kubernetes for DevOps practitioners. All examples are based on Kubernetes v1.28+ and have been validated against Minikube. Container images referenced are from Docker Hub and are provided for educational purposes._