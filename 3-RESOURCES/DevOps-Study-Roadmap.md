---
tags: [devops, roadmap, study-plan, learning, kubernetes, docker, ansible, terraform, git, jenkins, python, linux]
created: 2026-03-08
type: roadmap
duration: "4–5 months"
daily-hours: 6
total-courses: 8
---

# 🗺️ DevOps Mastery — 4 to 5 Month Study Roadmap

> **Commitment:** 6 hours/day · **Duration:** 18–20 weeks · **Total hours:** ~700–800 hrs
> **Structure:** 2 hrs Theory → 2 hrs Hands-on Labs → 1 hr Documentation/Notes → 1 hr Projects

---

## 📅 Master Timeline Overview

| Phase | Weeks | Duration | Courses |
|-------|-------|----------|---------|
| **Phase 1 — Foundation** | Weeks 1–4 | Month 1 | DevOps Prerequisites + Git |
| **Phase 2 — Developer Workflow** | Weeks 5–8 | Month 2 | Python + Jenkins |
| **Phase 3 — Containerization** | Weeks 9–12 | Month 3 | Docker + Kubernetes (intro) |
| **Phase 4 — Orchestration** | Weeks 13–15 | Month 3.5 | Kubernetes (advanced) |
| **Phase 5 — Automation & IaC** | Weeks 16–19 | Month 4–4.5 | Ansible + Terraform |
| **Phase 6 — Capstone** | Weeks 20 | Month 5 | Integration Projects + Review |

---

## ⏱️ Daily 6-Hour Study Block

```
06:00 – 08:00  ▶ Theory & Lectures          (2 hrs) — Watch, read, take notes
08:00 – 10:00  ▶ Hands-on Labs & Practice   (2 hrs) — Apply immediately what you learned
10:00 – 11:00  ▶ Documentation & Deep Dive  (1 hr)  — Official docs, man pages, blogs
11:00 – 12:00  ▶ Mini Projects & Review     (1 hr)  — Build something, review yesterday's material
```

> **Tip:** Adjust blocks to your peak energy hours. The order matters — always do theory before practice within the same session.

---

# 🟢 PHASE 1 — Foundation
## Weeks 1–4 · Month 1

---

## 📘 Course 1 — DevOps Prerequisites
### ⏳ Weeks 1–2 · ~72 hours

> **Goal:** Build the solid technical foundation that every other course depends on. If you skip this or rush it, every subsequent course will feel harder than it should.

---

### 🔑 Critical Topic 1: Linux Command Line Mastery

**Why it's critical:** Every DevOps tool — Docker, Kubernetes, Ansible, Terraform — is operated primarily through a Linux terminal. Without CLI fluency, you will be slow and error-prone in every course that follows.

**What to study:**

- **Filesystem navigation** — `pwd`, `ls`, `cd`, `find`, `locate`. Understanding the Linux directory tree (`/`, `/etc`, `/var`, `/usr`, `/home`, `/tmp`) and why each exists.
- **File operations** — `cp`, `mv`, `rm`, `mkdir`, `touch`, `ln`. The critical difference between hard links and soft (symbolic) links and when each is used.
- **Viewing & editing files** — `cat`, `less`, `head`, `tail`, `grep`, `awk`, `sed`. The vi/vim editor — you must know insert mode, command mode, saving, searching, and replacing.
- **Permissions** — `chmod`, `chown`, `chgrp`. Reading the `rwxrwxrwx` notation. Octal vs symbolic mode. Why `chmod 755` and `chmod 644` are the two most common values you'll use.
- **Processes** — `ps aux`, `top`, `htop`, `kill`, `bg`, `fg`, `jobs`, `&`. Understanding PIDs, signals (SIGTERM vs SIGKILL), and how background jobs work.
- **Pipes and redirection** — `|`, `>`, `>>`, `<`, `2>`, `&>`. Composing commands — `cat file | grep pattern | sort | uniq | wc -l` — this is how real work gets done.
- **Shell scripting basics** — Variables, conditionals (`if/elif/else`), loops (`for`, `while`), functions, and exit codes. Writing scripts that actually handle errors.

**Practice project:** Write a bash script that monitors disk usage, logs warnings when any filesystem exceeds 80%, and sends output to a timestamped log file.

---

### 🔑 Critical Topic 2: Networking Fundamentals

**Why it's critical:** DevOps is fundamentally about networked systems. Docker networking, Kubernetes Services, SSH connectivity for Ansible — all of these require you to understand how networks work.

**What to study:**

- **IP addressing** — IPv4 address classes, subnetting basics, CIDR notation (`192.168.1.0/24` means 256 addresses, `.0` is network, `.255` is broadcast). Private vs public IP ranges (`10.x.x.x`, `172.16.x.x`, `192.168.x.x`).
- **DNS** — How a hostname like `google.com` resolves to an IP. The role of `/etc/resolv.conf`, `/etc/hosts`. `nslookup` and `dig` for troubleshooting.
- **Ports & Protocols** — TCP vs UDP. Common ports to memorize: SSH (22), HTTP (80), HTTPS (443), MySQL (3306), PostgreSQL (5432), Redis (6379), Kubernetes API (6443). Understanding what `LISTEN`, `ESTABLISHED`, and `TIME_WAIT` states mean in `netstat`.
- **SSH** — Key-based authentication (why password auth is dangerous). `ssh-keygen`, `ssh-copy-id`, `~/.ssh/config` for managing multiple hosts. Port forwarding basics.
- **Firewalls** — `iptables` and `firewalld` concepts. How to open and close ports. Why this matters when containers expose ports.

**Practice project:** Set up two Linux VMs (VirtualBox or cloud), configure SSH key authentication between them, set up a basic firewall allowing only SSH and HTTP, and verify connectivity with `ping`, `curl`, and `netstat`.

---

### 🔑 Critical Topic 3: Package & Application Management

**Why it's critical:** DevOps engineers constantly install, configure, and troubleshoot applications — web servers, databases, runtimes. Understanding how applications work together is essential for writing Ansible playbooks and Dockerfiles.

**What to study:**

- **Package managers** — `apt` (Debian/Ubuntu) and `yum`/`dnf` (RHEL/CentOS). Installing, updating, removing, and searching packages. Understanding package repositories and `apt-get update` vs `upgrade`.
- **Services** — `systemctl start/stop/restart/enable/disable/status`. The difference between starting a service (now) and enabling it (on boot). Viewing service logs with `journalctl`.
- **Web servers** — Apache (`httpd`) and NGINX. Installing, configuring virtual hosts, setting document roots, checking config syntax (`nginx -t`), serving static files. Understanding how a request flows from browser → DNS → server → application.
- **Database basics** — MySQL/MariaDB setup, creating databases and users, granting permissions. Why your app server should never use the `root` database user.
- **Application runtimes** — Java (JVM, `.jar` files, `java -jar`), Python (`pip`, virtual environments, `requirements.txt`), Node.js (`npm`, `package.json`, `node_modules`). Why dependency management matters for reproducibility.
- **Data formats** — JSON and YAML deeply. You will write YAML every single day in this career. Understanding indentation sensitivity in YAML, lists, dictionaries, nested structures, and multi-line strings (`|` vs `>`).

**Practice project:** Deploy a 3-tier web app manually: NGINX as reverse proxy → Node.js or Python Flask API → MySQL database. Everything configured from scratch via CLI.

---

### 🔑 Critical Topic 4: VirtualBox & Lab Environments

**Why it's critical:** Being able to spin up, snapshot, and destroy VMs freely is how you practice safely without fear of breaking anything real.

**What to study:**

- Creating VMs, configuring CPU/RAM/disk
- Network modes: NAT, Bridge, Host-only — when to use each
- Snapshots — take one before every risky practice session, restore if you break things
- SSH into VMs from your host machine
- Vagrant basics — `Vagrantfile`, `vagrant up`, `vagrant ssh`, `vagrant destroy` — automated VM provisioning

---

### Week-by-Week Breakdown

| Week | Focus | Key Deliverable |
|------|-------|-----------------|
| Week 1 (Days 1–5) | Linux CLI, filesystem, permissions, vi editor | Bash monitoring script |
| Week 2 (Days 6–10) | Networking, SSH, package management, NGINX + MySQL | 3-tier web app deployed manually |

---

## 📘 Course 2 — Git for DevOps
### ⏳ Weeks 3–4 · ~60 hours

> **Goal:** Understand Git not just as a tool for saving code, but as the backbone of every DevOps workflow — from CI/CD pipelines to Infrastructure as Code collaboration.

---

### 🔑 Critical Topic 1: Git Internals — How It Actually Works

**Why it's critical:** Most people learn Git commands by rote and panic when something goes wrong. Understanding the internals means you can reason about any situation and fix it.

**What to study:**

- **The three areas** — Working Directory (your files), Staging Area (index), Repository (.git folder). Every Git command moves content between these three areas. `git add` moves to staging. `git commit` moves to repo.
- **Objects model** — Git stores everything as objects: `blob` (file content), `tree` (directory), `commit` (snapshot + metadata + pointer to parent). A commit is not a diff — it's a complete snapshot.
- **HEAD** — A pointer to the current branch, which itself is a pointer to the latest commit. `git checkout` moves HEAD. Detached HEAD state — what it is and how to get out.
- **The `.git` directory** — `objects/`, `refs/`, `HEAD`, `config`, `COMMIT_EDITMSG`. Understanding what's actually stored there demystifies everything.

---

### 🔑 Critical Topic 2: Branching Strategy

**Why it's critical:** In a team environment, branching strategy is the difference between smooth releases and merge chaos. DevOps pipelines are built around branch conventions.

**What to study:**

- **Creating and switching branches** — `git branch`, `git checkout -b`, `git switch`. Understanding that branches are just named pointers to commits — they're cheap and fast.
- **Merging** — Fast-forward merge (no divergence, just moves pointer) vs 3-way merge (diverged histories, creates a merge commit). When each happens.
- **Merge conflicts** — How to read the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). Resolving manually, staging the resolved file, and completing the merge.
- **Rebasing** — `git rebase main` rewrites your commits on top of the latest main, creating a linear history. When to use rebase (feature branches before merging) vs merge (never rewrite shared history).
- **Git Flow** — The standard branching model: `main` (production), `develop` (integration), `feature/*` (new features), `hotfix/*` (emergency fixes), `release/*` (release prep). Understanding why this structure maps to CI/CD stages.
- **Trunk-Based Development** — The alternative to Git Flow: everyone commits to `main` daily, features hidden with flags. Used by high-velocity teams.

---

### 🔑 Critical Topic 3: Remote Repositories & Collaboration

**What to study:**

- **Remote operations** — `git remote add origin`, `git fetch`, `git pull` (fetch + merge), `git push`. The difference between `fetch` and `pull` — always prefer `fetch` first so you know what's coming.
- **Pull Requests / Merge Requests** — The code review workflow: fork → branch → commit → push → open PR → review → merge. This is the standard for every open-source contribution and most team workflows.
- **Cherry-picking** — `git cherry-pick <commit-hash>` applies a specific commit from one branch to another. Critical for hotfixes: apply to `hotfix/` and cherry-pick to `develop`.
- **Tags** — `git tag v1.0.0` for release versioning. Annotated tags (`-a`) vs lightweight tags. `git push --tags`.

---

### 🔑 Critical Topic 4: Undoing Mistakes

**What to study:**

- `git restore <file>` — Discard changes in working directory
- `git restore --staged <file>` — Unstage a file
- `git reset --soft HEAD~1` — Undo last commit, keep changes staged
- `git reset --mixed HEAD~1` — Undo last commit, keep changes in working dir
- `git reset --hard HEAD~1` — ⚠️ Completely discard last commit and all changes
- `git revert <commit>` — Create a new commit that undoes a previous one (safe for shared history)
- `git reflog` — Your safety net. Shows every HEAD movement — recover "lost" commits.

**Practice project:** Simulate a team workflow with two cloned repos. Create feature branches, intentionally create a merge conflict, resolve it, open a "PR," merge, tag a release, then use `git revert` to undo a bad commit.

---

### Week-by-Week Breakdown

| Week | Focus | Key Deliverable |
|------|-------|-----------------|
| Week 3 (Days 11–15) | Git internals, staging, committing, branching, merging | Personal portfolio repo with proper branch strategy |
| Week 4 (Days 16–20) | Remotes, collaboration, rebasing, cherry-pick, reverting | Simulated team workflow with PRs, conflicts, and releases |

---

# 🔵 PHASE 2 — Developer Workflow
## Weeks 5–8 · Month 2

---

## 📘 Course 8 — Python for Beginners
### ⏳ Weeks 5–6 · ~60 hours

> **Goal:** Learn Python specifically as a DevOps automation language — scripting, working with APIs, parsing files, and interacting with systems. Done early so you can use Python in later courses.

---

### 🔑 Critical Topic 1: Python Fundamentals

**What to study:**

- **Data types** — `str`, `int`, `float`, `bool`. Type conversion. f-strings for formatting: `f"Server {hostname} is {status}"`.
- **Collections** — `list` (ordered, mutable), `tuple` (ordered, immutable), `dict` (key-value), `set` (unique values). List/dict comprehensions — the Pythonic way to transform data.
- **Control flow** — `if/elif/else`, `for` loops over iterables, `while` loops, `break`, `continue`, `pass`.
- **Functions** — `def`, parameters, return values, `*args`, `**kwargs`, default arguments. Understanding scope (local vs global).
- **Error handling** — `try/except/finally`. Never let scripts crash silently — always handle exceptions and log them.

---

### 🔑 Critical Topic 2: File & System Operations (DevOps-focused)

**What to study:**

- **File I/O** — Reading/writing text and binary files with `open()`. Context managers (`with open(...) as f`). Parsing CSV with `csv` module.
- **`os` and `pathlib`** — `os.path.exists()`, `os.makedirs()`, `os.listdir()`, `shutil.copy()`. The modern `pathlib.Path` approach.
- **`subprocess`** — Running shell commands from Python: `subprocess.run(["ls", "-la"], capture_output=True)`. Capturing stdout/stderr. Checking return codes. The DevOps workhorse.
- **JSON and YAML** — `import json`, `json.loads()`, `json.dumps()`. `import yaml`, `yaml.safe_load()`. Parsing API responses and config files.
- **`argparse`** — Building CLI tools with arguments and flags. Making your scripts reusable.

---

### 🔑 Critical Topic 3: Working with APIs & Automation

**What to study:**

- **`requests` library** — `GET`, `POST`, `PUT`, `DELETE`. Handling headers, authentication, and JSON responses. Error handling for HTTP status codes.
- **Regular expressions** — `import re`, `re.search()`, `re.findall()`, `re.sub()`. Extracting IP addresses, port numbers, or log patterns from text.
- **Logging** — `import logging` — always use this instead of `print()` in real scripts. Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.

**Practice project:** Write a Python script that reads a list of servers from a JSON file, SSHes into each one using `subprocess` + SSH CLI, collects disk usage and uptime, and writes a formatted report to a CSV file.

---

### Week-by-Week Breakdown

| Week | Focus | Key Deliverable |
|------|-------|-----------------|
| Week 5 (Days 21–25) | Data types, collections, control flow, functions, error handling | Server health checker script |
| Week 6 (Days 26–30) | File I/O, subprocess, JSON/YAML parsing, requests, argparse | Multi-server report generator with CLI flags |

---

## 📘 Course 3 — Jenkins for Beginners
### ⏳ Weeks 7–8 · ~60 hours

> **Goal:** Understand CI/CD deeply and build real pipelines. Jenkins is the glue between code commits and deployments — mastering it makes every other tool more useful.

---

### 🔑 Critical Topic 1: CI/CD Concepts

**Why it's critical:** Before touching Jenkins, you must internalize what problem it solves. CI/CD is the single most transformative practice in DevOps — everything else serves it.

**What to study:**

- **Continuous Integration (CI)** — Every developer merges to a shared branch frequently (at least daily). Each merge triggers an automated build and test suite. Goal: find bugs fast, before they compound.
- **Continuous Delivery (CD)** — Every code change that passes CI is automatically prepared for release. A human clicks "deploy" to production. Requires high test confidence.
- **Continuous Deployment** — Every change that passes CI goes directly to production with no human intervention. Requires exceptional automated testing and monitoring.
- **The pipeline stages** — Source → Build → Test → Artifact → Deploy → Monitor. Understanding what happens at each stage and what failures mean.
- **Artifacts** — The compiled/packaged output of a build (`.jar`, `.war`, Docker image, `.zip`). The same artifact that passed testing is what gets deployed — never rebuild for production.

---

### 🔑 Critical Topic 2: Jenkins Pipelines (Jenkinsfile)

**Why it's critical:** The `Jenkinsfile` is where CI/CD logic lives — written as code, stored in Git, reviewed like any other code. This is the modern way to use Jenkins.

**What to study:**

- **Declarative vs Scripted Pipeline** — Declarative (structured, recommended for beginners) uses `pipeline { }` blocks. Scripted uses Groovy directly (`node { }`). Learn declarative first.
- **Pipeline anatomy:**
  ```groovy
  pipeline {
      agent any                    // Where to run
      environment {                // Environment variables
          APP_VERSION = '1.0'
      }
      stages {
          stage('Build') {         // Each stage
              steps {              // Commands to run
                  sh 'mvn clean package'
              }
          }
          stage('Test') {
              steps {
                  sh 'mvn test'
              }
              post {               // Actions after stage
                  always { junit 'target/surefire-reports/*.xml' }
              }
          }
          stage('Deploy') {
              when {               // Conditional execution
                  branch 'main'
              }
              steps {
                  sh './deploy.sh'
              }
          }
      }
      post {                       // Actions after full pipeline
          success { slackSend "Build ${BUILD_NUMBER} succeeded!" }
          failure { emailext "Build failed!" }
      }
  }
  ```
- **Parallel stages** — Running tests in parallel to save time.
- **Input step** — Pause pipeline and wait for human approval before deploying to production.
- **Shared Libraries** — Reusable Groovy functions stored in a separate Git repo, shared across all pipelines.

---

### 🔑 Critical Topic 3: Jenkins Administration

**What to study:**

- **Installation & setup** — Installing Jenkins on Linux, initial setup, the Jenkins home directory (`JENKINS_HOME`), and understanding what's stored there.
- **Plugins** — Jenkins gets its power from plugins. Critical ones: Git, Pipeline, Docker Pipeline, Credentials, Blue Ocean (UI), SonarQube, Slack Notification, Kubernetes plugin.
- **Credentials management** — Storing secrets (passwords, API keys, SSH keys) safely in Jenkins Credentials Store. Using them in pipelines as `credentials('id')` — never hardcode secrets.
- **Agents/Nodes** — The controller runs orchestration; agents run actual build work. Setting up static agents (SSH) and dynamic agents (Docker containers, Kubernetes pods).
- **Security** — Role-based access control (RBAC), matrix-based security, restricting what different users/teams can do.
- **Backup and restore** — What to backup (`JENKINS_HOME`, jobs, plugins). Restoration procedures. Critical for any production Jenkins.

---

### 🔑 Critical Topic 4: Jenkins + Git Integration

**What to study:**

- **Webhooks** — GitHub/GitLab sends a POST request to Jenkins when code is pushed. Jenkins triggers the pipeline automatically. No polling required.
- **Multibranch Pipeline** — Jenkins automatically creates a pipeline for each branch in a repo that contains a `Jenkinsfile`. Essential for Git Flow.
- **Pull Request builds** — Building and testing every PR before it can be merged. The most important CI pattern.

**Practice project:** Build a full CI pipeline: Python Flask app → GitHub repo → Jenkins Multibranch Pipeline triggered by webhook → runs unit tests → builds Docker image → pushes to Docker Hub on merge to main.

---

### Week-by-Week Breakdown

| Week | Focus | Key Deliverable |
|------|-------|-----------------|
| Week 7 (Days 31–35) | CI/CD theory, Jenkins install, freestyle jobs, GitHub integration, webhooks | Jenkins server with GitHub webhook triggering test runs |
| Week 8 (Days 36–40) | Declarative Pipelines, Jenkinsfile, credentials, plugins, agents, Blue Ocean | Full CI/CD Jenkinsfile pipeline for a real application |

---

# 🟡 PHASE 3 — Containerization
## Weeks 9–12 · Month 3

---

## 📘 Course 4 — Docker for DevOps
### ⏳ Weeks 9–10 · ~60 hours

> **Goal:** Master containers — the single most important technology shift in modern infrastructure. Kubernetes requires deep Docker understanding.

---

### 🔑 Critical Topic 1: Container Fundamentals

**Why it's critical:** Understanding what containers actually are (vs what people think they are) prevents a huge category of confusion.

**What to study:**

- **Containers vs VMs** — VMs virtualize hardware (heavy, slow to start, full OS per VM). Containers virtualize the OS (lightweight, start in milliseconds, share the host kernel). A container is not a lightweight VM — it's an isolated process.
- **Linux primitives** — Containers are built from: **namespaces** (isolation — each container has its own view of PIDs, network, filesystem, users) and **cgroups** (resource limits — CPU, memory, I/O). Docker is a user-friendly API over these kernel features.
- **Container lifecycle** — `docker run` (create + start), `docker stop` (SIGTERM → SIGKILL after timeout), `docker rm` (delete stopped container), `docker ps -a` (all containers including stopped).
- **Immutability** — A container's filesystem is ephemeral. Any data written inside a container is lost when the container is removed. This is by design — it forces you to think about state explicitly.

---

### 🔑 Critical Topic 2: Docker Images & Dockerfile

**Why it's critical:** The Dockerfile is how you package your application reproducibly. Every subsequent environment — dev, staging, production — runs the same image.

**What to study:**

- **Image layers** — Each instruction in a Dockerfile creates a layer. Layers are cached. Order matters: put things that change rarely (dependencies) before things that change often (source code). This makes builds fast.
- **Critical Dockerfile instructions:**
  ```dockerfile
  FROM node:18-alpine           # Base image — always use specific tags, never 'latest'
  WORKDIR /app                  # Set working directory (creates it if missing)
  COPY package*.json ./         # Copy only package files first (cache optimization)
  RUN npm ci --only=production  # Install dependencies (cached layer)
  COPY . .                      # Copy source (changes often — goes last)
  EXPOSE 3000                   # Documents the port (doesn't actually publish it)
  USER node                     # Run as non-root — security best practice
  CMD ["node", "server.js"]     # Default command (can be overridden at runtime)
  ```
- **Multi-stage builds** — Use one stage to build, a second clean stage for the final image. Result: tiny production images without build tools:
  ```dockerfile
  FROM golang:1.19 AS builder
  WORKDIR /app
  COPY . .
  RUN go build -o myapp .

  FROM alpine:3.17              # Final image — no Go compiler, just the binary
  COPY --from=builder /app/myapp .
  CMD ["./myapp"]
  ```
- **`.dockerignore`** — Like `.gitignore` for Docker builds. Exclude `node_modules/`, `.git/`, `*.log` to keep images small and builds fast.
- **Image optimization** — Minimize layers, use `alpine` base images when possible, combine `RUN` commands with `&&`, clean up caches in the same layer.

---

### 🔑 Critical Topic 3: Docker Networking & Storage

**What to study:**

- **Network drivers** — `bridge` (default — containers on same host can communicate), `host` (container uses host's network directly), `none` (no networking), `overlay` (multi-host — used by Docker Swarm/Kubernetes).
- **Container-to-container communication** — Containers on the same custom network can reach each other by name (`curl http://database:5432`). The built-in bridge network does NOT provide DNS — always create custom networks.
- **Port publishing** — `docker run -p 8080:3000` maps host port 8080 to container port 3000. Without `-p`, the container port is inaccessible from outside.
- **Volumes** — Named volumes (`-v mydata:/data`) persist data independently of container lifecycle. Bind mounts (`-v /host/path:/container/path`) mount a host directory — useful for development.

---

### 🔑 Critical Topic 4: Docker Compose

**Why it's critical:** Real applications have multiple services. Docker Compose lets you define and run multi-container applications with a single file.

**What to study:**

```yaml
# docker-compose.yml
version: '3.9'
services:
  web:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - api
    environment:
      - API_URL=http://api:3000

  api:
    build: ./backend
    ports:
      - "3000:3000"
    depends_on:
      db:
        condition: service_healthy
    environment:
      - DB_HOST=db
      - DB_PASSWORD_FILE=/run/secrets/db_pass
    secrets:
      - db_pass

  db:
    image: postgres:14-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_pass
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      retries: 5
    secrets:
      - db_pass

volumes:
  pgdata:

secrets:
  db_pass:
    file: ./secrets/db_password.txt
```

Key commands: `docker compose up -d`, `docker compose down`, `docker compose logs -f`, `docker compose ps`, `docker compose build`.

**Practice project:** Containerize a full 3-tier application (frontend + backend API + database) using Dockerfile + Docker Compose. Integrate into your Jenkins pipeline to build and push images automatically.

---

### Week-by-Week Breakdown

| Week | Focus | Key Deliverable |
|------|-------|-----------------|
| Week 9 (Days 41–45) | Container theory, Docker CLI, images, Dockerfile, multi-stage builds | Optimized multi-stage Docker image for your app |
| Week 10 (Days 46–50) | Docker networking, volumes, Docker Compose, registry, Jenkins integration | Full 3-tier app running via Docker Compose + CI pipeline building images |

---

## 📘 Course 5 — Kubernetes for DevOps
### ⏳ Weeks 11–15 · ~150 hours (5 weeks — deepest course)

> **Goal:** Kubernetes is the most complex course and the most in-demand skill. It deserves the most time. Do not rush it.

---

### 🔑 Critical Topic 1: Kubernetes Architecture

**Why it's critical:** Every kubectl command, every YAML file, every debugging session makes more sense when you understand the components involved.

**What to study:**

- **Control Plane** — `kube-apiserver` (REST gateway — everything goes through it), `etcd` (distributed key-value store — the cluster's brain), `kube-scheduler` (picks which node each Pod runs on), `controller-manager` (runs loops that keep desired state = actual state).
- **Worker Nodes** — `kubelet` (ensures containers in Pods are running as specified), `kube-proxy` (maintains network rules for Service routing), container runtime (`containerd`).
- **The reconciliation loop** — Kubernetes is always trying to make actual state match desired state. You declare what you want (YAML), Kubernetes figures out how to get there and keeps it there. This is the fundamental mental model.
- **Namespaces** — Logical partitions of a cluster. Resources in different namespaces are isolated by default. Use them for team isolation, environment separation (not for prod vs dev — use separate clusters for that).

---

### 🔑 Critical Topic 2: Pods and Workload Resources

**What to study:**

- **Pods** — The atomic unit. One or more containers sharing a network namespace and storage. Understand container ports, resource requests vs limits, liveness/readiness probes.
  ```yaml
  resources:
    requests:        # Minimum guaranteed — used by scheduler for placement
      cpu: "100m"    # 100 millicores = 0.1 CPU
      memory: "128Mi"
    limits:          # Hard ceiling — container killed if exceeded for memory
      cpu: "500m"
      memory: "256Mi"
  ```
- **Deployments** — The standard way to run stateless applications. Manages rolling updates (zero-downtime), rollbacks, and desired replica count. Know `maxSurge` and `maxUnavailable`.
- **StatefulSets** — For stateful apps (databases): stable network identity (`pod-0`, `pod-1`), stable persistent storage per pod, ordered deployment and scaling.
- **DaemonSets** — Exactly one pod per node. For infrastructure agents: log collectors (Fluentd), monitoring agents (Prometheus Node Exporter), network plugins.
- **Jobs & CronJobs** — Run pods to completion. Jobs for one-off tasks, CronJobs for scheduled work.

---

### 🔑 Critical Topic 3: Services & Networking

**Why it's critical:** Getting traffic into, out of, and between your applications is where most Kubernetes confusion lives.

**What to study:**

- **Service types** — `ClusterIP` (internal only), `NodePort` (static port on every node), `LoadBalancer` (cloud LB with external IP). Know when to use each.
- **DNS** — Inside a cluster, `my-service.my-namespace.svc.cluster.local` resolves to the service's ClusterIP. Pods can reach other services by short name within the same namespace.
- **Ingress** — Layer 7 (HTTP/HTTPS) routing. One external IP → multiple services via hostname/path rules. Requires an Ingress controller (nginx-ingress is most common). TLS termination at the Ingress layer.
- **NetworkPolicy** — Default: all pods can talk to all pods. NetworkPolicies restrict this. Start with a default-deny-all policy, then explicitly allow required traffic. Critical for security.

---

### 🔑 Critical Topic 4: Configuration & Storage

**What to study:**

- **ConfigMaps** — Non-sensitive configuration injected as env vars or mounted files. Edit the ConfigMap, pods pick up changes without redeployment (when mounted as volume).
- **Secrets** — Sensitive data. Base64-encoded (not encrypted!). Use external secret stores (HashiCorp Vault, AWS Secrets Manager + External Secrets Operator) in production.
- **PersistentVolumes (PV) & PersistentVolumeClaims (PVC)** — PVs are cluster-level storage resources. PVCs are requests for storage by workloads. `StorageClass` enables dynamic provisioning — claim storage and cloud creates the disk automatically.

---

### 🔑 Critical Topic 5: RBAC & Security

**What to study:**

- **ServiceAccounts** — Identity for pods. Every pod runs as a ServiceAccount. Default SA has minimal permissions — create specific SAs for workloads that need API access.
- **Roles & ClusterRoles** — Define what actions are allowed on what resources.
- **RoleBindings** — Bind a Role to a user, group, or ServiceAccount.
- **Pod Security** — `securityContext` settings: run as non-root, read-only filesystem, drop Linux capabilities. Pod Security Admission (PSA) levels: `privileged`, `baseline`, `restricted`.

---

### 🔑 Critical Topic 6: kubectl Mastery

**The commands you must know by heart:**

```bash
# Get everything
kubectl get pods,svc,deploy,rs,cm,secrets -n my-ns

# Debug a failing pod
kubectl describe pod <name> -n <ns>     # Check Events section first
kubectl logs <pod> --previous           # Logs from crashed container
kubectl exec -it <pod> -- /bin/sh       # Shell into running container

# Rollout management
kubectl rollout status deployment/my-app
kubectl rollout history deployment/my-app
kubectl rollout undo deployment/my-app

# Resource usage
kubectl top pods
kubectl top nodes

# Everything
kubectl get events --sort-by=.lastTimestamp -n my-ns
```

**Practice project weeks 11–15:**
- Week 11: Deploy the 3-tier app from Docker course onto Kubernetes (Deployments + Services)
- Week 12: Add Ingress, ConfigMaps, Secrets, PVCs for the database
- Week 13: Implement RBAC, NetworkPolicies, security contexts
- Week 14: Add HorizontalPodAutoscaler, resource quotas, LimitRanges
- Week 15: Full CI/CD pipeline — Jenkins builds Docker image → pushes to registry → triggers kubectl rollout

---

### Week-by-Week Breakdown

| Week | Focus | Key Deliverable |
|------|-------|-----------------|
| Week 11 (Days 51–55) | Architecture, Pods, Deployments, ReplicaSets, Services | 3-tier app running on Kubernetes |
| Week 12 (Days 56–60) | Ingress, ConfigMaps, Secrets, PV/PVC, StatefulSets | Database with persistent storage, app configured via ConfigMaps |
| Week 13 (Days 61–65) | RBAC, NetworkPolicies, SecurityContexts, PSA | Hardened cluster with access controls and network isolation |
| Week 14 (Days 66–70) | HPA, resource management, DaemonSets, Jobs, CronJobs | Auto-scaling application with scheduled backup jobs |
| Week 15 (Days 71–75) | Full CI/CD integration, Helm basics, cluster troubleshooting | Jenkins → Docker → Kubernetes end-to-end pipeline |

---

# 🟠 PHASE 5 — Automation & Infrastructure as Code
## Weeks 16–19 · Month 4–4.5

---

## 📘 Course 6 — Ansible for Beginners
### ⏳ Weeks 16–17 · ~60 hours

> **Goal:** Master configuration management and automation. Ansible is how you manage hundreds of servers without touching them individually.

---

### 🔑 Critical Topic 1: Inventory & Connection

**What to study:**

- **Inventory file** — The list of hosts Ansible manages. Static (INI or YAML file) vs dynamic (script/plugin that queries cloud APIs for current hosts).
  ```ini
  [web_servers]
  web1 ansible_host=192.168.1.10 ansible_user=ubuntu
  web2 ansible_host=192.168.1.11 ansible_user=ubuntu

  [db_servers]
  db1 ansible_host=192.168.1.20 ansible_user=ubuntu

  [all:vars]
  ansible_ssh_private_key_file=~/.ssh/id_rsa

  [web_servers:vars]
  http_port=80
  ```
- **Connection methods** — SSH (default, agentless — no software installed on managed nodes), `ansible_connection=local` for localhost, `ansible_connection=docker` for containers.
- **Ad-hoc commands** — Single-task commands for quick operations:
  ```bash
  ansible web_servers -m ping                              # Test connectivity
  ansible all -m command -a "uptime"                       # Run command on all hosts
  ansible db_servers -m service -a "name=mysql state=restarted" -b  # Restart service
  ```

---

### 🔑 Critical Topic 2: Playbooks

**Why it's critical:** Playbooks are where Ansible becomes powerful — ordered, repeatable automation for complex multi-step configurations.

**What to study:**

- **Playbook structure** — Plays, tasks, modules, handlers. A play targets a group of hosts and runs a series of tasks. Multiple plays in one playbook.
- **Idempotency** — The single most important Ansible concept. Running the same playbook 10 times should produce the same result as running it once. Ansible modules are designed for this. `command` and `shell` are NOT idempotent — use specific modules when possible.
- **Modules** — The building blocks. Critical ones to know:
  - `copy` / `template` — Copy files or Jinja2 templates to hosts
  - `file` — Create directories, set permissions, create symlinks
  - `lineinfile` / `blockinfile` — Add/modify/remove lines in config files
  - `service` — Start/stop/restart/enable services
  - `package` / `apt` / `yum` — Install software
  - `user` / `group` — Manage OS users
  - `cron` — Schedule cron jobs
  - `git` — Clone/update Git repositories
  - `uri` — Make HTTP requests (call APIs)
  - `shell` / `command` — Run raw commands (last resort)
- **Handlers** — Tasks that run only when notified, and only once at the end of the play. Perfect for service restarts after config changes:
  ```yaml
  tasks:
    - name: Update nginx config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Restart nginx          # Only restarts if config actually changed

  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
  ```

---

### 🔑 Critical Topic 3: Variables & Jinja2 Templating

**What to study:**

- **Variable precedence** (lowest to highest): role defaults → group vars → host vars → play vars → task vars → extra vars (`-e`)
- **Variable types** — Scalars, lists, dictionaries. Accessing nested vars: `{{ db.host }}` or `{{ db['host'] }}`.
- **`register`** — Capture task output for use in subsequent tasks:
  ```yaml
  - name: Check if app is running
    shell: pgrep myapp
    register: app_status
    ignore_errors: true

  - name: Start app if not running
    command: /opt/myapp/start.sh
    when: app_status.rc != 0
  ```
- **Jinja2 templates** — `.j2` files that use `{{ variable }}` for substitution, `{% for %}` loops, and `{% if %}` conditionals. Template module renders them on the control node and copies the result:
  ```
  # nginx.conf.j2
  upstream backend {
  {% for host in groups['app_servers'] %}
      server {{ hostvars[host]['ansible_host'] }}:{{ app_port }};
  {% endfor %}
  }
  ```
- **`group_vars/` and `host_vars/`** — Directory-based variable files automatically loaded by Ansible. `group_vars/web_servers.yml` applies to all hosts in `[web_servers]`.

---

### 🔑 Critical Topic 4: Conditionals, Loops & Roles

**What to study:**

- **Conditionals** — `when:` clause. Can use any variable, registered result, Ansible facts (`ansible_os_family`, `ansible_distribution`):
  ```yaml
  - name: Install Apache (Debian)
    apt:
      name: apache2
      state: present
    when: ansible_os_family == "Debian"

  - name: Install Apache (RedHat)
    yum:
      name: httpd
      state: present
    when: ansible_os_family == "RedHat"
  ```
- **Loops** — `loop:` (modern) or `with_items:` (legacy):
  ```yaml
  - name: Create multiple users
    user:
      name: "{{ item.name }}"
      groups: "{{ item.groups }}"
      state: present
    loop:
      - { name: alice, groups: sudo }
      - { name: bob,   groups: docker }
  ```
- **Roles** — The way to organize and reuse Ansible code. A role is a structured directory with tasks, handlers, variables, templates, and files. Install community roles from Ansible Galaxy: `ansible-galaxy install geerlingguy.nginx`.

**Practice project:** Write an Ansible playbook that: provisions a full LEMP stack (Linux + NGINX + MySQL + PHP), creates application users, deploys an app from a Git repo, configures NGINX with a Jinja2 template, and sets up cron jobs — all idempotently.

---

### Week-by-Week Breakdown

| Week | Focus | Key Deliverable |
|------|-------|-----------------|
| Week 16 (Days 76–80) | Inventory, ad-hoc commands, playbooks, modules, handlers, idempotency | NGINX + application deployment playbook |
| Week 17 (Days 81–85) | Variables, Jinja2 templates, conditionals, loops, roles, Ansible Galaxy | Full LEMP stack role with host_vars for multi-environment support |

---

---

## 📘 Course 7 — Terraform for Beginners
### ⏳ Weeks 18–19 · ~60 hours

> **Goal:** Provision cloud infrastructure with code. Terraform is how you create servers, networks, databases, and load balancers reproducibly and consistently.

---

### 🔑 Critical Topic 1: Infrastructure as Code Philosophy

**Why it's critical:** Understanding *why* IaC matters prevents you from treating Terraform as just a CLI tool.

**What to study:**

- **The problem with manual infrastructure** — ClickOps creates snowflake servers. No history, no review, no reproducibility. If your cloud console burned down, how long to rebuild?
- **IaC benefits** — Version-controlled (Git), peer-reviewed (PR process), idempotent, self-documenting, testable, auditable.
- **Terraform vs Ansible** — Terraform provisions infrastructure (creates EC2 instances, VPCs, RDS databases). Ansible configures software on infrastructure (installs packages, writes config files). They complement each other — Terraform first, Ansible after.

---

### 🔑 Critical Topic 2: Terraform Core Workflow & HCL

**What to study:**

- **HCL (HashiCorp Configuration Language)** — Terraform's declarative syntax. Resources, data sources, variables, outputs, locals.
- **Core workflow:**
  ```bash
  terraform init       # Download providers, initialize backend
  terraform plan       # Show what will change (read this carefully!)
  terraform apply      # Apply changes (prompts confirmation)
  terraform destroy    # Tear down all managed resources
  ```
- **Resource blocks** — The fundamental building block:
  ```hcl
  resource "aws_instance" "web" {
    ami           = data.aws_ami.ubuntu.id
    instance_type = var.instance_type
    subnet_id     = aws_subnet.public.id
    tags = {
      Name        = "${var.project}-web-${var.environment}"
      Environment = var.environment
    }
  }
  ```
- **Data sources** — Read existing infrastructure (not managed by Terraform):
  ```hcl
  data "aws_ami" "ubuntu" {
    most_recent = true
    owners      = ["099720109477"]  # Canonical
    filter {
      name   = "name"
      values = ["ubuntu/images/hvm-ssd/ubuntu-22.04-amd64-*"]
    }
  }
  ```
- **Variables & outputs:**
  ```hcl
  variable "instance_type" {
    description = "EC2 instance type"
    type        = string
    default     = "t3.micro"
  }

  output "web_public_ip" {
    value       = aws_instance.web.public_ip
    description = "Public IP of the web server"
  }
  ```
- **`terraform.tfvars`** — Provide variable values without modifying code. Never commit sensitive values — use environment variables (`TF_VAR_db_password`) instead.

---

### 🔑 Critical Topic 3: State Management

**Why it's critical:** Terraform state is how Terraform knows what it has created. Corrupted or lost state = disaster.

**What to study:**

- **`terraform.tfstate`** — JSON file mapping your config to real cloud resources. Contains sensitive data — never commit to Git!
- **Remote state** — Store state in S3 + DynamoDB (AWS), GCS (GCP), or Terraform Cloud. Enables team collaboration and state locking (prevents concurrent applies that corrupt state).
  ```hcl
  terraform {
    backend "s3" {
      bucket         = "my-terraform-state"
      key            = "prod/network/terraform.tfstate"
      region         = "us-east-1"
      dynamodb_table = "terraform-locks"
      encrypt        = true
    }
  }
  ```
- **State commands** — `terraform state list`, `terraform state show <resource>`, `terraform state mv` (rename), `terraform import` (import existing resources into state).

---

### 🔑 Critical Topic 4: Modules

**Why it's critical:** Modules are how you avoid copy-pasting infrastructure code. They're reusable, versioned, and shareable.

**What to study:**

- **Module structure** — A directory with `main.tf`, `variables.tf`, `outputs.tf`. Call it with a `module` block:
  ```hcl
  module "vpc" {
    source  = "terraform-aws-modules/vpc/aws"  # From Terraform Registry
    version = "~> 5.0"

    name = "${var.project}-vpc"
    cidr = "10.0.0.0/16"
    azs  = ["us-east-1a", "us-east-1b"]
    private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
    public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]
    enable_nat_gateway = true
  }
  ```
- **Workspaces** — Manage multiple environments (dev/staging/prod) from one codebase. `terraform workspace new staging`, `terraform workspace select prod`.
- **`for_each` and `count`** — Create multiple resources dynamically:
  ```hcl
  resource "aws_instance" "workers" {
    for_each      = toset(var.worker_names)
    ami           = data.aws_ami.ubuntu.id
    instance_type = "t3.micro"
    tags = { Name = each.key }
  }
  ```

**Practice project:** Build a complete AWS infrastructure with Terraform: VPC with public/private subnets, Internet Gateway, NAT Gateway, EC2 instances in private subnet, Application Load Balancer in public subnet, RDS in private subnet, security groups, and remote state in S3. Then use Ansible to configure the EC2 instances.

---

### Week-by-Week Breakdown

| Week                 | Focus                                                                                | Key Deliverable                                                             |
| -------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Week 18 (Days 86–90) | IaC concepts, HCL syntax, providers, resources, data sources, variables, outputs     | AWS VPC + EC2 + security groups provisioned with Terraform                  |
| Week 19 (Days 91–95) | State management, remote backend, modules, workspaces, for_each, Terraform + Ansible | Full production-grade AWS infrastructure with remote state + Ansible config |

---

# 🔴 PHASE 6 — Capstone & Integration
## Week 20 · Month 5

---

### 🏆 Capstone Project — End-to-End DevOps Pipeline

**Duration:** 1 week (~42 hours)
**Goal:** Connect every tool into a single, automated, production-grade workflow.

**The Full Pipeline:**

```
Developer pushes code to GitHub
        ↓
GitHub Webhook triggers Jenkins
        ↓
Jenkins Pipeline:
  [Stage 1] Checkout code
  [Stage 2] Run Python unit tests
  [Stage 3] Build Docker image (multi-stage)
  [Stage 4] Run container security scan (Trivy)
  [Stage 5] Push image to Docker Hub / ECR
  [Stage 6] Update Kubernetes manifests (GitOps)
        ↓
Kubernetes pulls new image (rolling update, zero-downtime)
        ↓
Application runs on Kubernetes (Deployment + Service + Ingress)
        ↓
Infrastructure provisioned by Terraform (VPC, EKS cluster)
        ↓
Servers configured by Ansible (Jenkins server setup, monitoring)
```

**Deliverables:**
- GitHub repository with full source code + Jenkinsfile + Dockerfile + K8s manifests + Terraform configs + Ansible playbooks
- Documentation explaining every component and how they connect
- Working demo of a code push triggering the full pipeline automatically

---

## 📊 Full Schedule Summary

| Phase | Weeks | Course(s) | Hours |
|-------|-------|-----------|-------|
| Phase 1 | 1–2 | DevOps Prerequisites | 72 hrs |
| Phase 1 | 3–4 | Git Basics | 60 hrs |
| Phase 2 | 5–6 | Python Basics | 60 hrs |
| Phase 2 | 7–8 | Jenkins | 60 hrs |
| Phase 3 | 9–10 | Docker | 60 hrs |
| Phase 3–4 | 11–15 | Kubernetes | 150 hrs |
| Phase 5 | 16–17 | Ansible | 60 hrs |
| Phase 5 | 18–19 | Terraform | 60 hrs |
| Phase 6 | 20 | Capstone Project | 42 hrs |
| **Total** | **20 weeks** | **8 courses** | **~624 hrs** |

---

## 🔁 Weekly Habits for Success

- **Sunday:** Plan the week. Review what you learned last week. Identify any gaps.
- **Daily:** Follow the 6-hour block. Always do the lab right after the lecture — don't batch them.
- **Every 2 days:** Update your Obsidian notes with new commands and concepts.
- **Weekly:** Build one small project or mini-demo that uses what you learned.
- **Every 2 weeks:** Do a review session — go back and run through previous exercises without notes.

---

## ⚠️ Common Mistakes to Avoid

- **Watching without doing** — A lecture without an immediate lab is nearly worthless. Always follow up.
- **Moving on without understanding** — If Kubernetes pods are mysterious, don't start Ansible. Go back.
- **Not breaking things** — The best learning happens when something fails and you debug it. Intentionally misconfigure things to see what happens.
- **Skipping the fundamentals** — Everyone wants to jump to Kubernetes. Do not skip Linux and Git — they underpin everything.
- **Memorizing commands** — Understand *why* a command does what it does. You can always look up syntax; you can't look up intuition.

---

## 📚 Supplemental Resources by Topic

| Topic | Resource |
|-------|---------|
| Linux | `man` pages, `tldr` CLI tool, Linux Journey (linuxjourney.com) |
| Git | Pro Git book (free at git-scm.com/book) |
| Docker | Official docs (docs.docker.com), Play with Docker (labs.play-with-docker.com) |
| Kubernetes | Official docs (kubernetes.io/docs), Killer.sh practice exams |
| Ansible | Official docs (docs.ansible.com), Ansible for DevOps book |
| Terraform | Official docs (developer.hashicorp.com/terraform), Terraform Up & Running book |
| Jenkins | official docs (jenkins.io/doc), Jenkins Handbook |
| Python | docs.python.org, Real Python (realpython.com) |

---

*Generated: 2026-03-08 · DevOps 8-Course Mastery Roadmap · 4–5 Month Plan*
