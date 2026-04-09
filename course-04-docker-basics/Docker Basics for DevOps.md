# Docker Basics for DevOps

## Course 4 – A Comprehensive Tutorial with Hands-On Labs

---

> **About This Course**
> 
> This course is designed for DevOps engineers, developers, and system administrators who want to learn Docker from first principles. You will progress from understanding Docker's purpose and installing it, through mastering containers, images, storage, and networking, to managing a Docker registry. Every module includes concept explanations, guided demonstrations, and hands-on labs with full solutions to reinforce real-world skills.

---

## Table of Contents

- [Module 1 – Setting up Docker and Basic Docker Commands](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-1--setting-up-docker-and-basic-docker-commands)
- [Module 2 – Docker Run](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-2--docker-run)
- [Module 3 – Docker Images](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-3--docker-images)
- [Module 4 – Docker Engine and Storage](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-4--docker-engine-and-storage)
- [Module 5 – Docker Networking and Registry](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-5--docker-networking-and-registry)
- [Module 6 – Conclusion](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-6--conclusion)

---

# Module 1 – Setting up Docker and Basic Docker Commands

## Module Overview

This module introduces Docker's purpose and fundamentals in modern software development and guides you through installing and setting it up on your system. You will then learn the essential commands for working with images, containers, volumes, and networks through guided demonstrations and hands-on labs.

### Learning Objectives

- Master basic Docker commands for container management and orchestration
- Follow a guided demonstration to understand the usage and syntax of common Docker commands
- Gain hands-on experience through Docker Labs to reinforce learning and practice command execution
- Understand the fundamentals of Docker and its significance in modern software development
- Explore Docker's overview, including its purpose and basic functionality
- Follow a guided demonstration to set up and install Docker on your system

---

## 1.1 Docker Overview

### The Problem Docker Solves

Before Docker, deploying software across different environments was notoriously painful. A developer would write code on their laptop, it would work perfectly, and then break in staging or production because of different OS versions, library versions, configuration differences, or missing dependencies. This became known as the **"it works on my machine"** problem.

Docker solves this by packaging an application and all of its dependencies — libraries, configuration files, runtime, system tools — into a single portable unit called a **container**. The container runs identically on any machine that has Docker installed, regardless of the underlying operating system.

### What is Docker?

**Docker** is an open-source platform that automates the building, shipping, and running of applications inside lightweight, portable containers. Docker was released in 2013 by Docker, Inc. and has since become the industry standard for containerization.

```
┌────────────────────────────────────────────────────────────────┐
│                        Docker Platform                          │
│                                                                │
│   Build          Ship           Run                            │
│   ┌──────┐      ┌──────┐      ┌──────────────────────────┐   │
│   │Docker│ ───▶ │Docker│ ───▶ │  Any Machine with Docker │   │
│   │build │      │push  │      │  ┌────────┐  ┌────────┐  │   │
│   └──────┘      └──────┘      │  │  App A │  │  App B │  │   │
│                                │  └────────┘  └────────┘  │   │
│   Dockerfile    Registry       │                           │   │
│   + Source Code (Docker Hub)   └──────────────────────────┘   │
└────────────────────────────────────────────────────────────────┘
```

### Containers vs. Virtual Machines

Understanding the difference between containers and VMs is fundamental to understanding Docker's value proposition.

```
Virtual Machines                     Containers
┌──────────────────────┐             ┌──────────────────────┐
│    Infrastructure    │             │    Infrastructure    │
├──────────────────────┤             ├──────────────────────┤
│    Host OS           │             │    Host OS           │
├──────────────────────┤             ├──────────────────────┤
│    Hypervisor        │             │    Docker Engine     │
├──────┬───────┬───────┤             ├──────┬───────┬───────┤
│Guest │Guest  │Guest  │             │ App  │ App   │ App   │
│ OS   │ OS    │ OS    │             │  A   │  B    │  C    │
│ App A│ App B │ App C │             │      │       │       │
└──────┴───────┴───────┘             └──────┴───────┴───────┘
  GBs per VM, minutes to boot          MBs per container, seconds to start
```

|Feature|Virtual Machines|Docker Containers|
|---|---|---|
|**Startup time**|1–5 minutes|Milliseconds to seconds|
|**Disk size**|Gigabytes|Megabytes|
|**OS**|Full OS per VM|Shared host OS kernel|
|**Isolation**|Strong (hypervisor)|Process-level (namespaces)|
|**Portability**|Limited (heavy images)|High (lightweight images)|
|**Performance**|Near-native but overhead|Near-native, minimal overhead|
|**Density**|Tens per host|Hundreds per host|

### Core Docker Concepts

|Concept|Description|
|---|---|
|**Image**|A read-only template that defines what goes into a container|
|**Container**|A running instance of an image — isolated, portable, ephemeral|
|**Dockerfile**|A text script of instructions to build a Docker image|
|**Docker Hub**|The public registry where images are stored and shared|
|**Docker Engine**|The background service that builds and runs containers|
|**Docker Compose**|A tool for defining and running multi-container applications|
|**Volume**|Persistent storage that exists independently of containers|
|**Network**|Virtual network enabling containers to communicate|

### Docker's Role in Modern Software Development

Docker has fundamentally changed how software is built and delivered:

- **CI/CD Pipelines**: Build once, deploy anywhere — the same image goes through dev, test, staging, and production
- **Microservices**: Each service runs in its own isolated container with its own dependencies
- **Developer Onboarding**: New developers can get a full environment running with a single command
- **Cloud-Native Apps**: Cloud providers offer native container services (AWS ECS, Azure Container Instances, GKE)
- **Kubernetes**: The industry-standard container orchestrator uses Docker images as its deployment unit

---

## 1.2 Getting Started with Docker

### How Docker Works

The Docker platform consists of three major pieces that work together:

```
                        ┌─────────────────────────┐
                        │      Docker Daemon       │
                        │      (dockerd)           │
  ┌──────────────┐      │                         │      ┌────────────────┐
  │  Docker CLI  │─────▶│  REST API               │─────▶│  Docker Hub    │
  │  (docker)    │      │                         │      │  (Registry)    │
  └──────────────┘      │  Container Runtime      │      └────────────────┘
                        │  Image Builder          │
                        │  Volume Manager         │
                        │  Network Manager        │
                        └─────────────────────────┘
```

- **Docker CLI** (`docker`) — The command you type; sends instructions to the daemon
- **Docker Daemon** (`dockerd`) — The background service that does all the actual work
- **Docker Registry** — Where images are stored (Docker Hub is the default public registry)

### The Docker Workflow

```
Write           Build            Push             Pull & Run
┌──────────┐   ┌──────────┐   ┌──────────┐     ┌──────────┐
│Dockerfile│──▶│  Image   │──▶│ Registry │────▶│Container │
└──────────┘   └──────────┘   └──────────┘     └──────────┘
 Instructions   Snapshot of     Central          Running
 for building   app + deps      storage          instance
```

---

## 1.3 Demo: Setup and Install Docker

### Installing Docker on Linux (Ubuntu/Debian)

```bash
# Step 1: Update the package index
sudo apt-get update

# Step 2: Install prerequisites
sudo apt-get install -y \
  ca-certificates \
  curl \
  gnupg \
  lsb-release

# Step 3: Add Docker's official GPG key
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Step 4: Add the Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Step 5: Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin

# Step 6: Start and enable the Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Step 7: Add your user to the docker group (no more sudo!)
sudo usermod -aG docker $USER
newgrp docker

# Step 8: Verify the installation
docker --version
docker run hello-world
```

### Installing Docker on macOS

```bash
# Option 1: Docker Desktop (recommended for Mac)
# Download from: https://www.docker.com/products/docker-desktop/
# - Intel Mac: docker-desktop.dmg
# - Apple Silicon: docker-desktop-arm64.dmg
# Install the .dmg and start Docker Desktop from Applications

# Option 2: Homebrew
brew install --cask docker

# Verify
docker --version
docker info
```

### Installing Docker on Windows

```powershell
# Option 1: Docker Desktop for Windows (recommended)
# Download from: https://www.docker.com/products/docker-desktop/
# Requires WSL2 (Windows Subsystem for Linux 2)

# Enable WSL2 first:
wsl --install

# Then install Docker Desktop and enable WSL2 backend in settings

# Option 2: Using Winget
winget install Docker.DockerDesktop

# Verify (in PowerShell or Command Prompt)
docker --version
docker run hello-world
```

### Verifying the Installation

```bash
# Check Docker version
docker --version
# Docker version 24.0.x, build xxxxxxx

# Get detailed system information
docker info

# Run the hello-world container (the classic first test)
docker run hello-world
# This will:
# 1. Check if hello-world image exists locally (it won't)
# 2. Pull it from Docker Hub
# 3. Create a container from it
# 4. Run it (it prints a message and exits)

# Check Docker service status (Linux)
sudo systemctl status docker
```

---

## 1.4 Basic Docker Commands

### Image Commands

Images are the blueprints for containers. Before you can run a container, you need an image.

```bash
# ─── PULLING IMAGES ───────────────────────────────────────────

# Pull the latest version of an image
docker pull nginx

# Pull a specific version (tag)
docker pull nginx:1.25
docker pull ubuntu:22.04
docker pull python:3.11-alpine

# Pull from a specific registry
docker pull gcr.io/google-containers/pause:3.9

# ─── LISTING IMAGES ───────────────────────────────────────────

# List all locally stored images
docker images
# REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
# nginx        latest    a6bd71f48f68   2 weeks ago    187MB
# ubuntu       22.04     08d22c0ceb15   3 weeks ago    77.8MB

# Alternative command (same result)
docker image ls

# Show all images including intermediate layers
docker images -a

# Show only image IDs
docker images -q

# Filter images
docker images --filter "dangling=true"   # Untagged images
docker images nginx                       # Only nginx images

# ─── INSPECTING IMAGES ────────────────────────────────────────

# Get detailed JSON metadata about an image
docker inspect nginx

# Get specific fields using Go template
docker inspect nginx --format='{{.Config.ExposedPorts}}'
docker inspect nginx --format='{{.Config.Env}}'

# View image layers and history
docker history nginx

# ─── REMOVING IMAGES ──────────────────────────────────────────

# Remove a specific image
docker rmi nginx

# Remove by image ID
docker rmi a6bd71f48f68

# Force remove (even if containers depend on it)
docker rmi -f nginx

# Remove all unused images (not referenced by any container)
docker image prune

# Remove ALL images (use with caution!)
docker rmi $(docker images -q)

# Search Docker Hub for images
docker search nginx
docker search --filter "is-official=true" python
```

### Container Commands

```bash
# ─── CREATING AND RUNNING CONTAINERS ──────────────────────────

# Run a container (pull image if needed, create, start)
docker run nginx

# Run in detached/background mode (-d)
docker run -d nginx

# Run with a custom name
docker run -d --name my-nginx nginx

# Run interactively with a terminal (-it)
docker run -it ubuntu:22.04 bash

# Run and remove container when it exits (--rm)
docker run --rm ubuntu:22.04 echo "Hello, Docker!"

# ─── LISTING CONTAINERS ───────────────────────────────────────

# List running containers
docker ps
# CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
# a3b7c9d1e2f4   nginx   ...       1 min     Up 1m    80/tcp  my-nginx

# List all containers (running and stopped)
docker ps -a

# Show only container IDs
docker ps -q

# Show container sizes
docker ps -s

# ─── STARTING AND STOPPING ────────────────────────────────────

# Stop a running container (sends SIGTERM, waits 10s, then SIGKILL)
docker stop my-nginx

# Start a stopped container
docker start my-nginx

# Restart a container
docker restart my-nginx

# Kill a container immediately (SIGKILL, no graceful shutdown)
docker kill my-nginx

# Pause a container (freeze, not stop)
docker pause my-nginx
docker unpause my-nginx

# ─── CONTAINER INTERACTION ────────────────────────────────────

# Attach to a running container's stdout
docker attach my-nginx

# Execute a command in a running container
docker exec my-nginx ls /etc/nginx

# Open an interactive shell in a running container
docker exec -it my-nginx bash
docker exec -it my-nginx sh       # If bash isn't available

# Copy files to/from containers
docker cp my-nginx:/etc/nginx/nginx.conf ./nginx.conf   # Container to host
docker cp ./nginx.conf my-nginx:/etc/nginx/nginx.conf   # Host to container

# ─── LOGS AND MONITORING ──────────────────────────────────────

# View container logs
docker logs my-nginx

# Follow logs in real time
docker logs -f my-nginx

# Show last 50 lines
docker logs --tail 50 my-nginx

# Show logs with timestamps
docker logs -t my-nginx

# Show logs since a specific time
docker logs --since 2024-01-01T12:00:00 my-nginx

# View container resource usage
docker stats
docker stats my-nginx            # Specific container
docker stats --no-stream         # One-time snapshot

# Get detailed container metadata
docker inspect my-nginx

# View running processes inside a container
docker top my-nginx

# ─── REMOVING CONTAINERS ──────────────────────────────────────

# Remove a stopped container
docker rm my-nginx

# Force remove a running container
docker rm -f my-nginx

# Remove all stopped containers
docker container prune

# Remove all containers (stopped and running)
docker rm -f $(docker ps -aq)

# ─── SYSTEM COMMANDS ──────────────────────────────────────────

# Show Docker disk usage
docker system df

# Remove everything unused (containers, images, networks, volumes)
docker system prune

# Prune everything including volumes (DESTRUCTIVE!)
docker system prune --volumes -a
```

### How Containers Work

When you run `docker run nginx`, Docker performs these steps:

```
1. Check local image cache
   └── Image found?  → Skip to step 4
   └── Not found?    → Continue to step 2

2. Pull the image from Docker Hub
   └── Pulls all image layers
   └── Caches layers locally for reuse

3. Create a container from the image
   └── Allocates writable layer on top of read-only image layers
   └── Assigns a unique container ID

4. Set up networking
   └── Assigns an internal IP address
   └── Sets up NAT rules if ports are published

5. Start the container process
   └── Runs the CMD or ENTRYPOINT defined in the image
   └── Container is now "Running"

6. Attach to output (unless -d flag used)
   └── Streams stdout/stderr to your terminal
```

### Command Planning Pattern

A useful mental model for Docker commands follows this pattern:

```
docker [management-command] [subcommand] [options] [arguments]

Management commands group related operations:
  docker container   →  manage containers
  docker image       →  manage images
  docker volume      →  manage volumes
  docker network     →  manage networks
  docker system      →  manage Docker system

Old-style (still valid):           New-style (preferred):
  docker ps            =             docker container ls
  docker rm            =             docker container rm
  docker images        =             docker image ls
  docker rmi           =             docker image rm
  docker run           =             docker container run
```

---

## 🧪 Hands-on Lab: Basic Docker Commands

### Lab Objectives

- Install and verify Docker on your system
- Pull, inspect, and manage Docker images
- Create, run, monitor, and remove containers
- Practice essential Docker commands

### Lab Duration: 60 minutes

---

### Exercise 1: First Steps with Docker

```bash
# 1. Verify Docker is installed and running
docker --version
docker info | head -20

# 2. Run the official hello-world test container
docker run hello-world

# 3. See that the container exited
docker ps         # Running only — hello-world won't appear
docker ps -a      # All containers — hello-world is here, "Exited"

# 4. Pull the Ubuntu image explicitly
docker pull ubuntu:22.04

# 5. Confirm it's in your local cache
docker images

# 6. Run Ubuntu interactively
docker run -it --name my-ubuntu ubuntu:22.04 bash

# Inside the container, run some commands:
cat /etc/os-release
hostname
ps aux
ls /
exit

# 7. The container stopped when you exited
docker ps -a     # Shows my-ubuntu as Exited

# 8. Restart it and attach
docker start my-ubuntu
docker exec -it my-ubuntu bash
exit

# 9. Clean up
docker rm my-ubuntu
docker images
```

---

### Exercise 2: Working with Nginx

```bash
# 1. Pull nginx and explore it
docker pull nginx:latest
docker history nginx:latest    # View image layers
docker inspect nginx:latest | python3 -m json.tool | head -60

# 2. Run nginx in the background
docker run -d --name webserver -p 8080:80 nginx:latest

# 3. Verify it's running
docker ps
curl http://localhost:8080    # Should return nginx welcome page

# 4. Watch the logs
docker logs webserver
# Generate some traffic then watch
curl http://localhost:8080 && curl http://localhost:8080/notfound
docker logs webserver        # Shows access log entries

# 5. Check resource usage
docker stats webserver --no-stream

# 6. Execute commands inside the running container
docker exec webserver nginx -v
docker exec -it webserver bash
# Inside:
ls /etc/nginx/
cat /etc/nginx/nginx.conf
echo "<h1>Hello from Docker!</h1>" > /usr/share/nginx/html/index.html
exit

# 7. Test the change
curl http://localhost:8080   # Should now say "Hello from Docker!"

# 8. Copy the config out
docker cp webserver:/etc/nginx/nginx.conf ./nginx.conf
cat nginx.conf

# 9. Stop and remove the container
docker stop webserver
docker rm webserver

# 10. Image is still there
docker images nginx
```

---

### Exercise 3: Image and Container Cleanup

```bash
# 1. Pull several images for cleanup practice
docker pull alpine:latest
docker pull busybox:latest
docker pull redis:7-alpine

# 2. Create several containers (some running, some stopped)
docker run -d --name redis-test redis:7-alpine
docker run --name alpine-test alpine:latest echo "done"
docker run --name busybox-test busybox:latest echo "done"

# 3. View current state
docker ps -a
docker images

# 4. Clean up stopped containers only
docker container prune
# Confirms removal of alpine-test and busybox-test

docker ps -a   # Only redis-test remains (it's still running)

# 5. Stop and remove redis-test
docker stop redis-test
docker rm redis-test

# 6. View image disk usage
docker system df

# 7. Remove unused images
docker image prune        # Removes dangling (untagged) images
docker images             # Specific images remain

# 8. Remove specific images
docker rmi alpine:latest busybox:latest redis:7-alpine

# 9. Final state
docker images   # Should be back to just base images
```

---

# Module 2 – Docker Run

## Module Overview

This module focuses on the essential Docker Run command for container instantiation. Participants learn how to use Docker Run to launch and manage containers efficiently, and explore advanced features to customize container execution.

### Learning Objectives

- Understand the Docker Run command and its significance in launching and managing Docker containers
- Explore advanced Docker Run features and functionalities for customizing container execution
- Practice Docker Run commands through hands-on labs to gain proficiency in container deployment and management

---

## 2.1 Docker Run In Depth

The `docker run` command is arguably the most important Docker command. It combines `docker pull` + `docker create` + `docker start` into a single operation, with a vast number of options for customizing container behavior.

### Command Syntax

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

### Detached vs. Foreground Mode

```bash
# Foreground mode (default) - container output goes to your terminal
docker run nginx
# Ctrl+C to stop

# Detached mode (-d) - runs in background
docker run -d nginx

# Detached + interactive terminal (-dit) - background with terminal attached
docker run -dit ubuntu bash
```

### Port Mapping

```bash
# Map host port to container port: -p <hostPort>:<containerPort>
docker run -d -p 8080:80 nginx
# Access at http://localhost:8080 → routes to container's port 80

# Map a different host port
docker run -d -p 3000:80 nginx

# Map multiple ports
docker run -d -p 8080:80 -p 8443:443 nginx

# Map to all interfaces (any available port on host)
docker run -d -p 80 nginx
docker ps   # Shows the randomly assigned host port, e.g. 0.0.0.0:49157->80/tcp

# Bind to a specific host IP
docker run -d -p 127.0.0.1:8080:80 nginx   # Only localhost can access

# Map a UDP port
docker run -d -p 5353:53/udp some-dns-server
```

### Volume Mounting

```bash
# Mount a host directory into the container (bind mount)
docker run -d -v /host/path:/container/path nginx
docker run -d -v $(pwd)/html:/usr/share/nginx/html nginx

# Read-only bind mount
docker run -d -v $(pwd)/config:/etc/nginx:ro nginx

# Named volume (Docker manages the storage location)
docker run -d -v my-data:/var/lib/mysql mysql:8

# Create a temporary in-memory filesystem
docker run --tmpfs /tmp nginx
```

### Environment Variables

```bash
# Set a single environment variable (-e)
docker run -d -e MYSQL_ROOT_PASSWORD=secret mysql:8

# Set multiple environment variables
docker run -d \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=myapp \
  -e MYSQL_USER=appuser \
  -e MYSQL_PASSWORD=apppassword \
  mysql:8

# Load environment variables from a file (--env-file)
# Create a .env file:
cat > app.env << 'EOF'
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp
API_KEY=super-secret-key
EOF

docker run -d --env-file app.env myapp:latest
```

### Container Naming and Hostname

```bash
# Assign a custom name (otherwise Docker generates one randomly)
docker run -d --name my-database mysql:8

# Set the container's hostname (what the container sees as its hostname)
docker run -it --hostname webserver01 ubuntu bash
# Inside: hostname → webserver01

# Set both name and hostname
docker run -d --name web01 --hostname webserver01 nginx
```

### Resource Constraints

```bash
# Limit CPU usage (number of CPUs)
docker run -d --cpus="1.5" nginx        # Max 1.5 CPU cores

# Set CPU shares (relative weight, default 1024)
docker run -d --cpu-shares=512 nginx    # Gets half the default CPU priority

# Limit memory
docker run -d --memory="512m" nginx     # Max 512 MB RAM
docker run -d --memory="2g" nginx       # Max 2 GB RAM

# Set memory + swap limit
docker run -d --memory="512m" --memory-swap="1g" nginx

# Limit both CPU and memory
docker run -d \
  --name constrained-app \
  --cpus="0.5" \
  --memory="256m" \
  nginx
```

### Restart Policies

```bash
# no (default): Do not restart if the container exits
docker run -d --restart=no nginx

# always: Always restart the container
docker run -d --restart=always nginx

# on-failure: Restart only if the container exits with a non-zero status
docker run -d --restart=on-failure nginx

# on-failure with max retry count
docker run -d --restart=on-failure:5 nginx

# unless-stopped: Always restart unless manually stopped
docker run -d --restart=unless-stopped nginx
```

### User and Permissions

```bash
# Run as a specific user (by name or UID)
docker run -it --user nginx nginx sh
docker run -it --user 1001 ubuntu bash

# Run as a specific user:group
docker run -it --user 1001:1001 ubuntu bash

# Read-only root filesystem (security best practice)
docker run -d --read-only nginx

# Drop all Linux capabilities (most secure)
docker run -d --cap-drop ALL nginx

# Add specific capabilities
docker run -d --cap-add NET_ADMIN ubuntu

# Run privileged (full host access — avoid in production)
docker run -d --privileged ubuntu   # ⚠️ Security risk
```

### Networking Options

```bash
# Connect to a specific network
docker run -d --network my-network nginx

# Use host networking (container shares host network stack)
docker run -d --network host nginx   # Access at host IP:80 (not localhost:port)

# Disable all networking
docker run -d --network none nginx

# Publish all exposed ports
docker run -d -P nginx   # Maps all EXPOSE ports to random host ports
docker ps   # Shows assigned ports
```

### Other Useful Options

```bash
# Set working directory inside the container
docker run -it -w /app python:3.11 bash

# Override the ENTRYPOINT
docker run --entrypoint /bin/sh nginx

# Run as a one-off command (remove container when done)
docker run --rm ubuntu:22.04 cat /etc/os-release

# Limit container to a specific number of processes
docker run -d --pids-limit=50 nginx

# Add host-to-IP mappings (like /etc/hosts entries)
docker run -d --add-host=db.local:192.168.1.100 myapp

# Set labels (metadata on the container)
docker run -d \
  --label app=nginx \
  --label version=1.0 \
  --label environment=production \
  nginx
```

---

## 🧪 Hands-on Lab: Docker Run Commands

### Lab Objectives

- Use port mapping to expose containerized applications
- Set environment variables for container configuration
- Apply resource constraints to containers
- Configure restart policies
- Practice advanced Docker Run options

### Lab Duration: 60 minutes

---

### Exercise 1: Port Mapping and Web Servers

```bash
# 1. Run nginx on multiple host ports simultaneously
docker run -d --name nginx-8080 -p 8080:80 nginx:latest
docker run -d --name nginx-8090 -p 8090:80 nginx:latest

# 2. Verify both are running and accessible
docker ps
curl http://localhost:8080
curl http://localhost:8090

# 3. Run Apache on another port
docker run -d --name apache-8070 -p 8070:80 httpd:2.4

# 4. Check all three
curl http://localhost:8070     # Apache default page
curl http://localhost:8080     # Nginx default page
curl http://localhost:8090     # Nginx default page

# 5. Check port assignments
docker port nginx-8080
docker port apache-8070

# 6. Stop and remove
docker stop nginx-8080 nginx-8090 apache-8070
docker rm nginx-8080 nginx-8090 apache-8070
```

---

### Exercise 2: MySQL with Environment Variables

```bash
# 1. Run MySQL with required environment variables
docker run -d \
  --name mysql-lab \
  -e MYSQL_ROOT_PASSWORD=MyR00tPassw0rd \
  -e MYSQL_DATABASE=labdb \
  -e MYSQL_USER=labuser \
  -e MYSQL_PASSWORD=labpassword \
  -p 3306:3306 \
  mysql:8

# 2. Wait for MySQL to initialize (check logs)
docker logs -f mysql-lab
# Wait until you see: ready for connections

# 3. Connect to MySQL
docker exec -it mysql-lab mysql -u labuser -plabpassword labdb

# Inside MySQL:
SHOW DATABASES;
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100));
INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');
SELECT * FROM users;
EXIT;

# 4. Verify environment variables are set
docker inspect mysql-lab | grep -A 20 '"Env"'

# 5. Use --env-file for cleaner configuration
cat > mysql.env << 'EOF'
MYSQL_ROOT_PASSWORD=MyR00tPassw0rd
MYSQL_DATABASE=labdb2
MYSQL_USER=labuser2
MYSQL_PASSWORD=labpassword2
EOF

docker run -d \
  --name mysql-lab2 \
  --env-file mysql.env \
  -p 3307:3306 \
  mysql:8

# 6. Clean up
docker stop mysql-lab mysql-lab2
docker rm mysql-lab mysql-lab2
rm mysql.env
```

---

### Exercise 3: Resource Constraints and Restart Policies

```bash
# 1. Run a container with resource limits
docker run -d \
  --name limited-nginx \
  --cpus="0.5" \
  --memory="128m" \
  --memory-swap="256m" \
  -p 8080:80 \
  nginx:latest

# 2. Monitor resource usage
docker stats limited-nginx --no-stream

# 3. Inspect the constraints
docker inspect limited-nginx | grep -E '"Memory|NanoCpus|MemorySwap"'

# 4. Test restart policy
docker run -d \
  --name auto-restart \
  --restart=unless-stopped \
  -p 8090:80 \
  nginx:latest

# Stop and verify it restarts
docker stop auto-restart
docker ps       # It's stopped (unless-stopped respects manual stop)
docker start auto-restart
docker ps       # Running again

# 5. Clean up
docker stop limited-nginx auto-restart
docker rm limited-nginx auto-restart
```

---

# Module 3 – Docker Images

## Module Overview

This module explores Docker Images and their significance in containerization. Participants learn to create custom Docker Images using Dockerfiles, manage images, use environment variables, and understand the difference between CMD and ENTRYPOINT.

### Learning Objectives

- Grasp the concept of Docker Images and their role in containerization
- Acquire practical skills in creating custom Docker Images through guided demonstrations
- Gain proficiency in managing Docker Images and understanding the use of environment variables, commands, and entrypoints through hands-on labs

---

## 3.1 Docker Images In Depth

### What is a Docker Image?

A Docker image is a **read-only, layered filesystem snapshot** that contains everything needed to run an application: the OS filesystem, application code, libraries, environment variables, and configuration files. Think of an image as a class in object-oriented programming — you can create many container instances from one image.

### The Layer Architecture

Images are built from stacked, read-only layers. Each instruction in a Dockerfile creates a new layer. Only changed layers need to be downloaded when updating an image, making Docker extremely efficient.

```
┌─────────────────────────────────────────────────┐
│          Container Layer (Read/Write)            │  ← Your running container writes here
├─────────────────────────────────────────────────┤
│   Layer 4: COPY app/ /app  (3 MB)               │  ← Application code
├─────────────────────────────────────────────────┤
│   Layer 3: RUN pip install -r requirements.txt  │  ← Python dependencies
├─────────────────────────────────────────────────┤
│   Layer 2: COPY requirements.txt /app/          │  ← Requirements file
├─────────────────────────────────────────────────┤
│   Layer 1: FROM python:3.11-slim  (123 MB)      │  ← Base OS + Python
└─────────────────────────────────────────────────┘

Multiple containers share the same read-only layers → huge space savings
```

### The Dockerfile

A **Dockerfile** is a text file containing a series of instructions that Docker executes in order to build an image. Each instruction creates a new read-only layer.

#### Complete Dockerfile Reference

```dockerfile
# ─── FROM ─────────────────────────────────────────────────────
# Every Dockerfile must begin with FROM
# Specifies the base (parent) image to start from
FROM ubuntu:22.04
FROM python:3.11-slim          # Smaller image
FROM scratch                   # Empty image (for fully static binaries)

# ─── LABEL ────────────────────────────────────────────────────
# Adds metadata to the image
LABEL maintainer="devops@company.com"
LABEL version="1.0"
LABEL description="My application image"

# ─── ARG ──────────────────────────────────────────────────────
# Build-time variables (not available at runtime)
ARG APP_VERSION=1.0
ARG BUILD_DATE

# ─── ENV ──────────────────────────────────────────────────────
# Sets environment variables (available at runtime too)
ENV APP_HOME=/opt/app
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# ─── RUN ──────────────────────────────────────────────────────
# Executes commands during image build
RUN apt-get update && apt-get install -y \
    curl \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*   # Clean up to reduce layer size

# Shell form (runs in /bin/sh -c)
RUN echo "Building..."

# Exec form (runs directly, no shell interpretation)
RUN ["apt-get", "update"]

# ─── WORKDIR ──────────────────────────────────────────────────
# Sets the working directory for subsequent instructions
# Creates the directory if it doesn't exist
WORKDIR /opt/app

# ─── COPY ─────────────────────────────────────────────────────
# Copies files/directories from build context to image
COPY . .                         # Copy everything from current directory
COPY requirements.txt /app/      # Copy specific file
COPY --chown=user:group file /   # Set ownership while copying

# ─── ADD ──────────────────────────────────────────────────────
# Like COPY but also supports URLs and auto-extracts tar files
ADD https://example.com/app.tar.gz /opt/
# Note: COPY is preferred over ADD unless you need URL/tar features

# ─── USER ─────────────────────────────────────────────────────
# Sets the user for subsequent instructions and container runtime
RUN useradd -m -r appuser
USER appuser

# ─── EXPOSE ───────────────────────────────────────────────────
# Documents which ports the container listens on (informational)
EXPOSE 8080
EXPOSE 443/tcp

# ─── VOLUME ───────────────────────────────────────────────────
# Creates a mount point for external volumes
VOLUME ["/data", "/var/log"]

# ─── CMD ──────────────────────────────────────────────────────
# Default command to run when container starts
# Can be overridden by command line arguments to docker run
CMD ["python", "app.py"]
CMD ["nginx", "-g", "daemon off;"]

# ─── ENTRYPOINT ───────────────────────────────────────────────
# Sets the command that ALWAYS runs (harder to override)
# CMD arguments are passed to ENTRYPOINT
ENTRYPOINT ["python", "app.py"]
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# ─── HEALTHCHECK ──────────────────────────────────────────────
# Tells Docker how to test if the container is healthy
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# ─── ONBUILD ──────────────────────────────────────────────────
# Adds a trigger instruction executed when image is used as base
ONBUILD COPY . /app
ONBUILD RUN npm install

# ─── STOPSIGNAL ───────────────────────────────────────────────
# Sets the system call signal to stop the container
STOPSIGNAL SIGTERM
```

### Dockerfile Best Practices

```dockerfile
# ✅ 1. Use specific version tags (avoid 'latest' in production)
FROM node:18.17-alpine3.18      # Pin exact version

# ✅ 2. Combine RUN commands to reduce layers
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       curl \
       git \
    && rm -rf /var/lib/apt/lists/*

# ❌ Avoid separate RUN commands for the same package operation
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
# This creates 3 layers and doesn't clean up

# ✅ 3. Use .dockerignore to exclude unnecessary files
# .dockerignore:
# .git
# node_modules
# *.log
# .env
# __pycache__

# ✅ 4. Order instructions from least to most frequently changed
# (Docker caches layers; stable layers should come first)
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .        # Stable: rarely changes
RUN pip install -r requirements.txt
COPY . .                       # Volatile: changes often

# ✅ 5. Use non-root user
RUN useradd -m -u 1001 appuser
USER appuser

# ✅ 6. Set WORKDIR explicitly (don't use cd in RUN)
WORKDIR /opt/app

# ✅ 7. Use multi-stage builds for smaller production images
FROM node:18 AS builder
WORKDIR /build
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine AS production
COPY --from=builder /build/dist /usr/share/nginx/html
# Final image only contains the built files + nginx, not Node.js!
```

---

## 3.2 Demo: Creating a New Docker Image

### Example 1: A Simple Flask Web Application

**Project structure:**

```
my-flask-app/
├── Dockerfile
├── requirements.txt
├── app.py
└── .dockerignore
```

**`app.py`:**

```python
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Docker!',
        'version': os.getenv('APP_VERSION', '1.0'),
        'environment': os.getenv('APP_ENV', 'development')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

**`requirements.txt`:**

```
flask==3.0.0
gunicorn==21.2.0
```

**`Dockerfile`:**

```dockerfile
# Build stage — install dependencies
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage — minimal final image
FROM python:3.11-slim

LABEL maintainer="devops@company.com"
LABEL version="1.0"

# Create non-root user
RUN useradd -m -r -u 1001 appuser

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY app.py .

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PATH=/root/.local/bin:$PATH
ENV PORT=5000
ENV APP_VERSION=1.0
ENV APP_ENV=production

# Document the exposed port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

# Switch to non-root user
USER appuser

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
```

**`.dockerignore`:**

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.log
.git
.gitignore
.env
.venv
venv/
```

**Building and running:**

```bash
# Build the image
docker build -t my-flask-app:1.0 .

# Build with a build argument
docker build --build-arg APP_VERSION=2.0 -t my-flask-app:2.0 .

# Run the container
docker run -d --name flask-app -p 5000:5000 my-flask-app:1.0

# Test it
curl http://localhost:5000
curl http://localhost:5000/health

# Override environment variable at runtime
docker run -d --name flask-dev \
  -e APP_ENV=development \
  -e APP_VERSION=dev-build \
  -p 5001:5000 \
  my-flask-app:1.0
curl http://localhost:5001
```

### Example 2: A Node.js Application

**`Dockerfile`:**

```dockerfile
FROM node:18-alpine

# Set working directory
WORKDIR /usr/src/app

# Install dependencies first (layer caching optimization)
COPY package*.json ./
RUN npm ci --only=production

# Copy application code
COPY . .

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://localhost:3000/health || exit 1

CMD ["node", "server.js"]
```

---

## 3.3 Environment Variables

Environment variables are a fundamental way to configure containerized applications without modifying code or rebuilding images. They follow the **12-Factor App** methodology's principle of storing config in the environment.

### Defining ENV in Dockerfile

```dockerfile
# Set at build time — these become defaults
ENV DATABASE_URL=postgres://localhost/mydb
ENV DEBUG=false
ENV PORT=8080
ENV MAX_WORKERS=4

# Multiple ENV on one line (creates a single layer)
ENV APP_NAME=myapp \
    APP_VERSION=1.0 \
    LOG_LEVEL=info
```

### Overriding ENV at Runtime

```bash
# Override at docker run time with -e
docker run -e PORT=9090 -e DEBUG=true myapp:latest

# Environment variables at runtime always override Dockerfile ENV defaults
docker run -e DATABASE_URL=postgres://prod-db/mydb myapp:latest

# Load from file
docker run --env-file production.env myapp:latest
```

### Using ARG vs ENV

```dockerfile
# ARG: Build-time only, NOT available in running container
ARG BUILD_NUMBER
ARG GIT_COMMIT=unknown

# Use ARG in build commands
RUN echo "Building commit: $GIT_COMMIT"

# ARG can be passed to docker build with --build-arg
# docker build --build-arg BUILD_NUMBER=42 --build-arg GIT_COMMIT=abc123 .

# ENV: Available BOTH during build and at container runtime
ENV NODE_ENV=production
ENV DATABASE_URL=postgres://db/mydb
```

### Environment Variable Patterns

```bash
# Pattern 1: Override at runtime (12-Factor App)
docker run -e DB_HOST=prod-db.internal -e DB_PASS=secret myapp

# Pattern 2: Read from host environment
docker run -e DB_HOST -e DB_PASS myapp
# (reads DB_HOST and DB_PASS from your current shell environment)

# Pattern 3: File-based configuration
cat > prod.env << 'EOF'
DB_HOST=prod-db.internal
DB_PORT=5432
DB_NAME=myapp_prod
DB_USER=myapp
DB_PASS=secretpassword
CACHE_HOST=redis.internal
LOG_LEVEL=warning
EOF
docker run --env-file prod.env myapp
```

---

## 3.4 Commands vs. Entrypoint

Understanding the difference between `CMD` and `ENTRYPOINT` is crucial for building flexible, production-quality images.

### CMD — Default Command (Overridable)

`CMD` provides default arguments for the container. The user can **completely replace** CMD at runtime.

```dockerfile
FROM ubuntu:22.04
CMD ["echo", "Hello, World!"]
```

```bash
docker build -t cmd-demo .
docker run cmd-demo                    # Runs: echo "Hello, World!"
docker run cmd-demo echo "Different!"  # Overrides CMD entirely
docker run cmd-demo ls /tmp            # Overrides CMD entirely
```

### ENTRYPOINT — Fixed Command (Always Runs)

`ENTRYPOINT` sets the command that **always executes** when the container starts. Arguments from `docker run` or `CMD` are **appended** to ENTRYPOINT.

```dockerfile
FROM ubuntu:22.04
ENTRYPOINT ["echo"]
CMD ["Hello, World!"]
```

```bash
docker build -t ep-demo .
docker run ep-demo                      # Runs: echo "Hello, World!"
docker run ep-demo "Custom message"     # Runs: echo "Custom message"
docker run ep-demo -n "No newline"      # Runs: echo -n "No newline"
# To override ENTRYPOINT, use --entrypoint flag:
docker run --entrypoint /bin/ls ep-demo /tmp
```

### CMD + ENTRYPOINT Together (The Power Pattern)

```dockerfile
FROM python:3.11-slim
COPY app.py .

ENTRYPOINT ["python", "app.py"]   # Always runs python app.py
CMD ["--port", "8080"]            # Default: python app.py --port 8080
```

```bash
docker run myapp                              # python app.py --port 8080
docker run myapp --port 9090                  # python app.py --port 9090
docker run myapp --port 9090 --debug          # python app.py --port 9090 --debug
```

### Using Shell Scripts as ENTRYPOINT

A common pattern for complex initialization:

```bash
# entrypoint.sh
#!/bin/bash
set -e

# Run any initialization
echo "Starting container..."

# Wait for database
until pg_isready -h "$DB_HOST" -p "${DB_PORT:-5432}"; do
  echo "Waiting for database..."
  sleep 2
done

# Run migrations
python manage.py migrate

# Execute the main command
exec "$@"
```

```dockerfile
FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "app:app"]
```

### Summary Table

|Feature|CMD|ENTRYPOINT|
|---|---|---|
|Sets default command|✅|✅|
|Can be overridden by `docker run args`|✅ (replaced)|❌ (arguments are appended)|
|Override with flag|N/A|`--entrypoint`|
|When to use|Default arguments|The executable itself|

---

## 🧪 Hands-on Lab: Docker Images

### Lab Duration: 90 minutes

---

### Exercise 1: Build a Custom Web Server Image

```bash
# Create project directory
mkdir custom-nginx && cd custom-nginx

# Create a custom HTML page
mkdir html
cat > html/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Docker App</title>
  <style>
    body { font-family: sans-serif; background: #f0f4f8; display: flex;
           align-items: center; justify-content: center; min-height: 100vh; }
    .card { background: white; padding: 2rem; border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,.1); text-align: center; }
    h1 { color: #2c5282; }
    p { color: #4a5568; }
  </style>
</head>
<body>
  <div class="card">
    <h1>🐳 Hello from Docker!</h1>
    <p>This page is served from a custom Docker image.</p>
    <p>Built with love and Dockerfiles.</p>
  </div>
</body>
</html>
EOF

# Create a custom nginx config
cat > nginx.conf << 'EOF'
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /health {
        return 200 'OK';
        add_header Content-Type text/plain;
    }
}
EOF

# Write the Dockerfile
cat > Dockerfile << 'EOF'
FROM nginx:1.25-alpine

LABEL maintainer="lab@docker.com"
LABEL description="Custom nginx web server"

# Remove default nginx config and content
RUN rm /etc/nginx/conf.d/default.conf
RUN rm -rf /usr/share/nginx/html/*

# Copy our custom files
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY html/ /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=15s --timeout=3s \
  CMD wget -qO- http://localhost/health || exit 1

CMD ["nginx", "-g", "daemon off;"]
EOF

# Build the image
docker build -t custom-nginx:1.0 .

# Verify the image was created
docker images custom-nginx

# View the image layers
docker history custom-nginx:1.0

# Run it
docker run -d --name my-webserver -p 8080:80 custom-nginx:1.0

# Test it
curl http://localhost:8080
curl http://localhost:8080/health

# Check health status
docker inspect --format='{{.State.Health.Status}}' my-webserver

# Clean up
docker stop my-webserver && docker rm my-webserver
cd ..
```

---

### Exercise 2: CMD vs ENTRYPOINT Exploration

```bash
mkdir cmd-ep-lab && cd cmd-ep-lab

# ── Test CMD ─────────────────────────────────────────────────
cat > Dockerfile.cmd << 'EOF'
FROM alpine:latest
CMD ["echo", "This is the default CMD message"]
EOF

docker build -f Dockerfile.cmd -t cmd-test .

echo "Running with default CMD:"
docker run --rm cmd-test

echo "Overriding CMD:"
docker run --rm cmd-test echo "I replaced the CMD!"

echo "Running a different command entirely:"
docker run --rm cmd-test ls /etc

# ── Test ENTRYPOINT ──────────────────────────────────────────
cat > Dockerfile.ep << 'EOF'
FROM alpine:latest
ENTRYPOINT ["echo", "ENTRYPOINT says:"]
CMD ["default CMD appended here"]
EOF

docker build -f Dockerfile.ep -t ep-test .

echo "Running with ENTRYPOINT + CMD:"
docker run --rm ep-test

echo "CMD argument replaced by user input:"
docker run --rm ep-test "This was passed by the user"

echo "Overriding ENTRYPOINT with --entrypoint:"
docker run --rm --entrypoint ls ep-test /bin

# ── Real-world ENTRYPOINT pattern ────────────────────────────
cat > docker-entrypoint.sh << 'EOF'
#!/bin/sh
set -e
echo "Container starting..."
echo "Arguments received: $@"
exec "$@"
EOF
chmod +x docker-entrypoint.sh

cat > Dockerfile.real << 'EOF'
FROM alpine:latest
COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["sh", "-c", "echo 'Default: running shell'"]
EOF

docker build -f Dockerfile.real -t real-ep-test .
docker run --rm real-ep-test
docker run --rm real-ep-test echo "Custom command"
docker run --rm real-ep-test ls /etc/alpine-release

# Clean up
cd ..
docker rmi cmd-test ep-test real-ep-test
```

---

# Module 4 – Docker Engine and Storage

## Module Overview

This module provides deep insight into Docker's core components and storage mechanisms, including the Docker Engine's architecture, volumes, bind mounts, and storage drivers.

### Learning Objectives

- Understand the components and architecture of Docker Engine, including its role in containerization
- Explore Docker Storage concepts, including volumes, bind mounts, and storage drivers
- Gain practical experience in managing Docker storage through hands-on labs

---

## 4.1 Docker Engine

### Docker Engine Architecture

Docker Engine is a client-server application consisting of three major components:

```
┌──────────────────────────────────────────────────────────────────┐
│                         Docker Engine                            │
│                                                                  │
│  ┌────────────────┐    REST API    ┌─────────────────────────┐  │
│  │  Docker CLI    │ ────────────▶  │     Docker Daemon       │  │
│  │  (docker)      │ ◀────────────  │     (dockerd)           │  │
│  └────────────────┘                │                         │  │
│                                    │  ┌──────────────────┐   │  │
│  ┌────────────────┐                │  │   containerd     │   │  │
│  │  Docker API    │                │  │  (container      │   │  │
│  │  Clients       │                │  │   lifecycle)     │   │  │
│  └────────────────┘                │  └────────┬─────────┘   │  │
│                                    │           │              │  │
│                                    │  ┌────────▼─────────┐   │  │
│                                    │  │   runc           │   │  │
│                                    │  │  (OCI runtime)   │   │  │
│                                    │  └──────────────────┘   │  │
│                                    └─────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

#### Docker CLI (`docker`)

The command-line tool users interact with. It translates commands into API calls to the Docker daemon.

#### Docker Daemon (`dockerd`)

The background service that manages Docker objects: images, containers, networks, volumes. It listens for API requests and delegates container execution to `containerd`.

#### containerd

A high-level container runtime that manages the complete container lifecycle — image pull/push, container execution, snapshot management, and network attachment. Containerd is also a standalone CNCF project.

#### runc

The low-level OCI (Open Container Initiative) runtime that actually creates and runs containers using Linux kernel features: **namespaces** and **cgroups**.

### Linux Kernel Features That Make Containers Work

#### Namespaces — Isolation

Namespaces isolate container processes from the host and from each other:

|Namespace|What it Isolates|
|---|---|
|**PID**|Process IDs (container sees its own process tree)|
|**Network**|Network interfaces, routing, ports|
|**Mount**|Filesystem mount points|
|**UTS**|Hostname and domain name|
|**IPC**|Inter-process communication|
|**User**|User and group IDs|

#### cgroups — Resource Control

Control Groups (cgroups) limit and account for resource usage:

- **CPU**: Limit the CPU time a container can use
- **Memory**: Cap the amount of RAM a container can allocate
- **Block I/O**: Throttle disk read/write speeds
- **Network**: Limit network bandwidth

```bash
# You can see cgroup limits applied to a container
cat /sys/fs/cgroup/memory/docker/<container-id>/memory.limit_in_bytes
```

### Docker Daemon Configuration

The Docker daemon is configured via `/etc/docker/daemon.json`:

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "data-root": "/var/lib/docker",
  "default-address-pools": [
    {"base": "172.17.0.0/12", "size": 24}
  ],
  "insecure-registries": [],
  "registry-mirrors": [],
  "live-restore": true
}
```

```bash
# Reload daemon config without restart
sudo kill -HUP $(pidof dockerd)

# Or restart the service
sudo systemctl restart docker

# Check daemon status
sudo systemctl status docker

# View daemon logs
sudo journalctl -u docker -f
```

---

## 4.2 Docker Storage

### Understanding the Container Filesystem

Every container gets a writable layer on top of the read-only image layers. This is the **Copy-on-Write (CoW)** mechanism:

```
When a container modifies a file:
1. Docker checks all image layers for the file
2. Copies the file up to the writable container layer
3. Modifies the copy in the container layer
4. Reads/writes go to the container layer copy

This means:
✅ Multiple containers sharing an image don't waste space
✅ Read performance is excellent
⚠️ Write performance is slower than native (CoW overhead)
⚠️ Data is lost when the container is removed
```

### Three Storage Options

```
┌──────────────────────────────────────────────────────────────────┐
│                          HOST MACHINE                            │
│                                                                  │
│  /var/lib/docker/volumes/   /some/host/path   memory (RAM)      │
│  ┌─────────────────────┐   ┌──────────────┐  ┌──────────────┐  │
│  │    Docker Volume     │   │  Bind Mount  │  │   tmpfs      │  │
│  │  (Docker managed)    │   │ (user path)  │  │   Mount      │  │
│  └──────────┬───────────┘   └──────┬───────┘  └──────┬───────┘  │
│             │                      │                  │          │
│  ┌──────────▼──────────────────────▼──────────────────▼───────┐ │
│  │                      Container                              │ │
│  │          /data            /app           /tmp              │ │
│  └─────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

### 1. Docker Volumes (Recommended)

Docker volumes are managed by Docker and stored in `/var/lib/docker/volumes/`. They are the preferred mechanism for persisting container data.

```bash
# ─── CREATING VOLUMES ─────────────────────────────────────────

# Create a named volume
docker volume create my-data

# List all volumes
docker volume ls

# Inspect a volume
docker volume inspect my-data

# ─── USING VOLUMES ────────────────────────────────────────────

# Mount a named volume (-v or --mount)
docker run -d \
  --name db \
  -v my-data:/var/lib/postgresql/data \
  postgres:15

# Using --mount syntax (more explicit, recommended)
docker run -d \
  --name db \
  --mount type=volume,source=my-data,target=/var/lib/postgresql/data \
  postgres:15

# Multiple volumes
docker run -d \
  -v my-data:/data \
  -v my-logs:/var/log/app \
  myapp

# ─── MANAGING VOLUMES ─────────────────────────────────────────

# Remove a volume
docker volume rm my-data

# Remove all unused volumes
docker volume prune

# Back up a volume
docker run --rm \
  -v my-data:/source:ro \
  -v $(pwd):/backup \
  alpine tar czf /backup/my-data-backup.tar.gz -C /source .

# Restore a volume from backup
docker volume create restored-data
docker run --rm \
  -v restored-data:/target \
  -v $(pwd):/backup:ro \
  alpine tar xzf /backup/my-data-backup.tar.gz -C /target
```

### 2. Bind Mounts

Bind mounts map a specific path on the host machine to a path in the container. The host directory must already exist.

```bash
# Mount current directory into container
docker run -d \
  --name nginx-dev \
  -v $(pwd)/html:/usr/share/nginx/html \
  -p 8080:80 \
  nginx:latest

# Now changes to files in ./html/ are immediately reflected in the container

# Read-only bind mount (container can't write to it)
docker run -d \
  -v $(pwd)/config:/etc/nginx:ro \
  nginx:latest

# Using --mount syntax
docker run -d \
  --mount type=bind,source=$(pwd)/html,target=/usr/share/nginx/html \
  -p 8080:80 \
  nginx:latest
```

**When to use bind mounts:**

- Development environments (share source code with container)
- Sharing host configuration files with containers
- When the host path matters (log collection, sharing with other tools)

**When to use volumes:**

- Production database storage
- Sharing data between containers
- When portability matters (works the same on any Docker host)

### 3. tmpfs Mounts (In-Memory)

tmpfs mounts store data in the host's memory (RAM), never written to disk. Data is lost when the container stops.

```bash
# Create a tmpfs mount
docker run -d \
  --tmpfs /tmp \
  --tmpfs /run:rw,noexec,nosuid,size=65536k \
  nginx:latest

# Using --mount syntax
docker run -d \
  --mount type=tmpfs,target=/tmp,tmpfs-size=100m \
  nginx:latest
```

**Use cases:** Sensitive data that should never touch disk, high-performance temporary file operations, session data.

### Storage Drivers

The **storage driver** controls how image layers are managed and how the container's writable layer is implemented.

|Driver|Description|Best For|
|---|---|---|
|**overlay2**|Modern, efficient; uses OverlayFS|Default on modern Linux (recommended)|
|**overlay**|Older version of overlay2|Older kernels|
|**devicemapper**|Uses device-mapper (loop or direct)|Older Linux, RHEL/CentOS|
|**btrfs**|Uses Btrfs filesystem features|Systems running Btrfs|
|**zfs**|Uses ZFS filesystem features|Systems running ZFS|

```bash
# Check current storage driver
docker info | grep "Storage Driver"

# View how overlay2 stores data
ls /var/lib/docker/overlay2/
```

---

## 🧪 Hands-on Lab: Docker Storage

### Lab Duration: 60 minutes

---

### Exercise 1: Demonstrate Container Data Impermanence

```bash
# 1. Run a container and write some data
docker run -it --name data-test ubuntu:22.04 bash

# Inside the container:
echo "This data will be lost!" > /tmp/important-data.txt
cat /tmp/important-data.txt
exit

# 2. The container stopped but still exists
docker ps -a | grep data-test

# 3. Start it again and check the data
docker start -ai data-test
cat /tmp/important-data.txt    # Data persists while container exists
exit

# 4. Now remove the container
docker rm data-test

# 5. Create a fresh container from the same image
docker run -it --rm ubuntu:22.04 bash
cat /tmp/important-data.txt    # FILE NOT FOUND — data is gone!
exit
```

---

### Exercise 2: Persistent Data with Docker Volumes

```bash
# 1. Create a volume for database storage
docker volume create postgres-data
docker volume ls
docker volume inspect postgres-data

# 2. Run PostgreSQL using the volume
docker run -d \
  --name my-postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=myapp \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15

# Wait for Postgres to initialize
sleep 5
docker logs my-postgres | tail -5

# 3. Create a table and insert data
docker exec -it my-postgres psql -U postgres -d myapp -c "
  CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
  );
  INSERT INTO customers (name, email)
  VALUES
    ('Alice Smith', 'alice@example.com'),
    ('Bob Jones', 'bob@example.com'),
    ('Carol White', 'carol@example.com');
"

# 4. Verify the data
docker exec -it my-postgres psql -U postgres -d myapp -c "SELECT * FROM customers;"

# 5. Delete the container (but the volume persists!)
docker stop my-postgres
docker rm my-postgres

# 6. Verify the volume still exists
docker volume ls          # postgres-data is still there

# 7. Create a new PostgreSQL container using the SAME volume
docker run -d \
  --name my-postgres-v2 \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=myapp \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15

sleep 5

# 8. Check that the data survived!
docker exec -it my-postgres-v2 psql -U postgres -d myapp -c "SELECT * FROM customers;"
# All 3 customers are still there! ✅

# 9. Clean up
docker stop my-postgres-v2
docker rm my-postgres-v2
docker volume rm postgres-data
```

---

### Exercise 3: Bind Mount for Development

```bash
# 1. Create a simple web project
mkdir dev-project && cd dev-project
mkdir site

cat > site/index.html << 'EOF'
<!DOCTYPE html>
<html>
<body>
  <h1>Development Server</h1>
  <p>Edit index.html on your host — changes appear immediately!</p>
</body>
</html>
EOF

# 2. Run nginx with bind mount
docker run -d \
  --name dev-server \
  -v $(pwd)/site:/usr/share/nginx/html \
  -p 8080:80 \
  nginx:latest

# 3. Test the page
curl http://localhost:8080

# 4. Edit the file on your host (without restarting the container)
cat >> site/index.html << 'EOF'
<p style="color: green;">This line was added without restarting the container!</p>
EOF

# 5. Check the change took effect immediately
curl http://localhost:8080    # Updated content!

# 6. Create a new page
cat > site/about.html << 'EOF'
<html><body><h1>About Page</h1></body></html>
EOF
curl http://localhost:8080/about.html    # Works immediately!

# 7. Clean up
docker stop dev-server && docker rm dev-server
cd ..
rm -rf dev-project
```

---

# Module 5 – Docker Networking and Registry

## Module Overview

This module covers essential networking and registry concepts in Docker environments. Participants learn about Docker networking modes, configure container communication, and interact with Docker Registry for storing and distributing images.

### Learning Objectives

- Understand Docker Networking and its role in facilitating communication between Docker containers
- Gain practical experience in configuring and managing Docker Networking through hands-on labs
- Explore Docker Registry and its significance in storing and distributing Docker images

---

## 5.1 Docker Networking

### Docker's Network Architecture

When Docker is installed, it creates three default networks automatically. Every container you run connects to one of these (or a custom network):

```bash
docker network ls
# NETWORK ID     NAME      DRIVER    SCOPE
# abc123def456   bridge    bridge    local
# def456ghi789   host      host      local
# ghi789jkl012   none      null      local
```

### Network Drivers

#### 1. Bridge Network (Default)

The **bridge** network is the default for standalone containers. Docker creates a virtual bridge (`docker0`) on the host, and containers connect to it via virtual ethernet pairs. Containers on the same bridge network can communicate; they're isolated from containers on other networks.

```
Host
├── docker0 (172.17.0.1)  ← Virtual bridge
│   ├── Container A (172.17.0.2)
│   ├── Container B (172.17.0.3)
│   └── Container C (172.17.0.4)
```

```bash
# Containers on the DEFAULT bridge network use IP addresses to find each other
docker run -d --name app1 nginx
docker run -d --name app2 nginx

# Get app1's IP
docker inspect app1 | grep IPAddress

# From app2, ping app1 by IP (works)
docker exec app2 ping 172.17.0.2    # ✅ Works by IP

# By container name (does NOT work on default bridge)
docker exec app2 ping app1          # ❌ Fails! Default bridge has no DNS

# SOLUTION: Use custom bridge networks (they have DNS)
docker network create my-app-network

docker run -d --name web --network my-app-network nginx
docker run -d --name db --network my-app-network postgres:15 -e POSTGRES_PASSWORD=pass

# Now containers can find each other by NAME
docker exec web ping db             # ✅ Works! Custom bridges have DNS
docker exec web curl http://web/    # ✅ Works! Can reference self too
```

#### 2. Host Network

Containers with the **host** network share the host machine's network stack directly. No network isolation — the container uses the host's IP and ports.

```bash
# Container uses host's ports directly (no -p mapping needed)
docker run -d --network host nginx

# Now nginx is at HOST_IP:80, not via port mapping
curl http://localhost:80    # Works directly

# Use cases: maximum network performance, network tooling that needs host access
# Avoid in: multi-tenant environments, security-sensitive deployments
```

#### 3. None Network (No Networking)

Completely disables networking for the container.

```bash
docker run --network none -it alpine sh
# Inside container:
ping 8.8.8.8    # Fails — no network!
ifconfig        # Only loopback (lo)
```

#### 4. Overlay Network (Swarm/Multi-Host)

Overlay networks span multiple Docker hosts, enabling containers on different machines to communicate as if they were on the same network. Used in Docker Swarm mode.

```bash
# Requires Swarm mode
docker swarm init
docker network create --driver overlay my-overlay
```

#### 5. Macvlan Network

Assigns a MAC address to containers, making them appear as physical devices on the network.

```bash
docker network create \
  --driver macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 \
  my-macvlan
```

### Creating and Managing Networks

```bash
# ─── CREATE ───────────────────────────────────────────────────

# Create a custom bridge network (default driver)
docker network create my-network

# Create with specific subnet and gateway
docker network create \
  --driver bridge \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1 \
  --ip-range=172.20.240.0/20 \
  custom-net

# ─── CONNECT / DISCONNECT ─────────────────────────────────────

# Connect a running container to a network
docker network connect my-network my-container

# Disconnect a container from a network
docker network disconnect my-network my-container

# Connect with a specific IP
docker network connect --ip 172.20.0.10 custom-net my-container

# ─── INSPECT ──────────────────────────────────────────────────

# View network details (subnets, connected containers)
docker network inspect my-network

# ─── REMOVE ───────────────────────────────────────────────────

# Remove a network (all containers must be disconnected first)
docker network rm my-network

# Remove all unused networks
docker network prune
```

### Container Communication Patterns

#### Pattern 1: Single Custom Network

```bash
# All services on one network — can find each other by name
docker network create app-net

docker run -d --name redis --network app-net redis:7-alpine
docker run -d --name postgres \
  --network app-net \
  -e POSTGRES_PASSWORD=pass \
  postgres:15
docker run -d --name backend \
  --network app-net \
  -e REDIS_URL=redis://redis:6379 \
  -e DATABASE_URL=postgres://postgres:pass@postgres/mydb \
  mybackend:latest
docker run -d --name frontend \
  --network app-net \
  -p 80:80 \
  myfrontend:latest

# frontend → backend (by name "backend")
# backend → redis (by name "redis")
# backend → postgres (by name "postgres")
```

#### Pattern 2: Multiple Networks for Isolation

```bash
# Create networks for different tiers
docker network create frontend-net   # Frontend ↔ Backend
docker network create backend-net    # Backend ↔ Database

# Database only on backend-net (not reachable from frontend directly)
docker run -d --name db \
  --network backend-net \
  postgres:15

# Backend on BOTH networks (bridges the tiers)
docker run -d --name api \
  --network backend-net \
  myapi:latest
docker network connect frontend-net api   # Also on frontend-net

# Frontend only on frontend-net (can't reach db directly)
docker run -d --name web \
  --network frontend-net \
  -p 80:80 \
  myfrontend:latest
```

### Publishing Ports

```bash
# Map host port to container port
docker run -d -p 8080:80 nginx

# Map all exposed ports to random host ports
docker run -d -P nginx
docker ps   # Shows: 0.0.0.0:49153->80/tcp

# Check port mappings for a container
docker port my-container

# Bind to a specific host interface
docker run -d -p 127.0.0.1:8080:80 nginx   # Only localhost

# Map UDP port
docker run -d -p 5353:53/udp dns-server
```

---

## 🧪 Hands-on Lab: Docker Networking

### Lab Duration: 60 minutes

---

### Exercise 1: Default vs. Custom Bridge Networks

```bash
# ── Part A: Default Bridge (no DNS) ───────────────────────────

# Run two containers on the default bridge
docker run -d --name ping-target nginx:alpine
docker run -d --name ping-source alpine sleep 3600

# Get the IP of ping-target
TARGET_IP=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ping-target)
echo "ping-target IP: $TARGET_IP"

# Communicate by IP (works)
docker exec ping-source ping -c 3 $TARGET_IP

# Communicate by name (fails on default bridge!)
docker exec ping-source ping -c 3 ping-target    # Should fail

# Clean up Part A
docker stop ping-target ping-source
docker rm ping-target ping-source

# ── Part B: Custom Bridge (DNS works) ─────────────────────────

# Create a custom network
docker network create lab-network

# Run containers on the custom network
docker run -d --name server --network lab-network nginx:alpine
docker run -d --name client --network lab-network alpine sleep 3600

# Communicate by NAME (works on custom network!)
docker exec client ping -c 3 server        # DNS resolution works!
docker exec client wget -qO- http://server # HTTP by name works!

# Inspect the network
docker network inspect lab-network

# Clean up
docker stop server client
docker rm server client
docker network rm lab-network
```

---

### Exercise 2: Multi-Container Application with Custom Networks

```bash
# Create a two-tier app: web server + backend API

# Create network
docker network create webapp-net

# Run a simple "API" (we'll use a basic HTTP echo server)
docker run -d \
  --name backend-api \
  --network webapp-net \
  --expose 8080 \
  ealen/echo-server   # A simple HTTP echo server

# Run nginx as a frontend proxy
mkdir nginx-proxy-lab

cat > nginx-proxy-lab/default.conf << 'EOF'
server {
    listen 80;

    location / {
        return 200 'Frontend is running!\n';
        add_header Content-Type text/plain;
    }

    location /api/ {
        proxy_pass http://backend-api:8080/;
        proxy_set_header Host $host;
    }
}
EOF

docker run -d \
  --name frontend-web \
  --network webapp-net \
  -v $(pwd)/nginx-proxy-lab/default.conf:/etc/nginx/conf.d/default.conf \
  -p 8080:80 \
  nginx:latest

# Test
curl http://localhost:8080/
curl http://localhost:8080/api/

# Verify containers can reach each other by name
docker exec frontend-web ping -c 2 backend-api

# Clean up
docker stop frontend-web backend-api
docker rm frontend-web backend-api
docker network rm webapp-net
rm -rf nginx-proxy-lab
```

---

## 5.2 Docker Registry

### What is a Docker Registry?

A **Docker Registry** is a storage and distribution system for Docker images. It is the central repository that:

- Stores Docker images organized into repositories
- Allows pushing (uploading) and pulling (downloading) images
- Controls access to images (public or private)

```
Developer                Registry                  Server
   │                         │                       │
   │ docker build            │                       │
   │ docker push ──────────▶ │                       │
   │ (upload image)          │                       │
   │                         │ docker pull ◀─────────│
   │                         │ (download image)      │
   │                         │                       │
```

### Registry Types

|Registry|Description|Use Case|
|---|---|---|
|**Docker Hub**|Public registry; free tier available|Open-source projects, learning|
|**Amazon ECR**|AWS managed private registry|AWS deployments|
|**Google Artifact Registry**|GCP managed private registry|GCP deployments|
|**Azure Container Registry**|Azure managed private registry|Azure deployments|
|**GitHub Container Registry**|GitHub-integrated registry|GitHub-based CI/CD|
|**GitLab Registry**|Built into GitLab|GitLab CI/CD|
|**Harbor**|Open-source self-hosted enterprise registry|Self-hosted, air-gapped|
|**Registry (official)**|Docker's own open-source registry image|Local/private registry|

### Working with Docker Hub

```bash
# ─── LOGIN ────────────────────────────────────────────────────
docker login
# Username: your-dockerhub-username
# Password: your-dockerhub-password

# Login to a specific registry
docker login registry.example.com
docker login -u username -p password registry.example.com

# ─── TAGGING IMAGES ───────────────────────────────────────────
# Image names follow this format:
# [registry/][username/]repository[:tag]

# Examples:
# nginx                           → Docker Hub official image
# myusername/myapp:1.0            → Docker Hub user image
# registry.example.com/myapp:1.0 → Private registry image

# Tag a local image for pushing to Docker Hub
docker tag my-flask-app:1.0 yourusername/my-flask-app:1.0

# Tag with multiple tags (latest + version)
docker tag my-flask-app:1.0 yourusername/my-flask-app:latest

# ─── PUSHING IMAGES ───────────────────────────────────────────
docker push yourusername/my-flask-app:1.0
docker push yourusername/my-flask-app:latest

# ─── PULLING IMAGES ───────────────────────────────────────────
docker pull yourusername/my-flask-app:1.0

# Pull from a private registry
docker pull registry.example.com/myteam/myapp:v2.0

# ─── SEARCHING ────────────────────────────────────────────────
docker search nginx
docker search --filter "is-official=true" python
docker search --limit 10 ubuntu
```

### Running a Local Private Registry

You can run your own Docker Registry using the official `registry` image — useful for air-gapped environments, local development, or testing.

```bash
# ─── BASIC LOCAL REGISTRY ─────────────────────────────────────

# Pull and start the registry
docker run -d \
  --name local-registry \
  -p 5000:5000 \
  --restart unless-stopped \
  registry:2

# Verify it's running
curl http://localhost:5000/v2/
# Should return: {}

# ─── PUSH TO LOCAL REGISTRY ───────────────────────────────────

# Pull a public image
docker pull nginx:latest

# Tag it for your local registry
docker tag nginx:latest localhost:5000/my-nginx:1.0

# Push to your local registry
docker push localhost:5000/my-nginx:1.0

# ─── PULL FROM LOCAL REGISTRY ─────────────────────────────────

# Remove the local copy
docker rmi nginx:latest localhost:5000/my-nginx:1.0

# Pull from your local registry
docker pull localhost:5000/my-nginx:1.0

# Run from your local registry
docker run -d -p 8080:80 localhost:5000/my-nginx:1.0

# ─── BROWSE THE REGISTRY ──────────────────────────────────────

# List all repositories
curl http://localhost:5000/v2/_catalog

# List tags for a repository
curl http://localhost:5000/v2/my-nginx/tags/list

# ─── REGISTRY WITH PERSISTENT STORAGE ────────────────────────

# Run registry with a volume (data survives restarts)
docker volume create registry-data

docker run -d \
  --name persistent-registry \
  -p 5000:5000 \
  --restart unless-stopped \
  -v registry-data:/var/lib/registry \
  registry:2
```

### Registry with Authentication (Basic Auth)

```bash
# Create a password file using htpasswd
mkdir registry-auth

docker run --rm \
  --entrypoint htpasswd \
  httpd:2 \
  -Bbn registryuser registrypassword > registry-auth/htpasswd

# Run registry with authentication
docker run -d \
  --name secure-registry \
  -p 5001:5000 \
  -v $(pwd)/registry-auth:/auth \
  -e REGISTRY_AUTH=htpasswd \
  -e REGISTRY_AUTH_HTPASSWD_REALM="Registry Realm" \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
  registry:2

# Test authentication
curl http://localhost:5001/v2/    # Should return 401 Unauthorized

docker login localhost:5001 -u registryuser -p registrypassword

curl http://localhost:5001/v2/    # Should return {} now

# Push to authenticated registry
docker tag nginx:latest localhost:5001/nginx:latest
docker push localhost:5001/nginx:latest
```

### Image Tagging Strategy

Good tagging makes your registry organized and deployments predictable:

```bash
# Strategy 1: Semantic versioning
docker tag myapp:latest myrepo/myapp:1.2.3
docker tag myapp:latest myrepo/myapp:1.2
docker tag myapp:latest myrepo/myapp:1
docker tag myapp:latest myrepo/myapp:latest

# Strategy 2: Git-based tags (used in CI/CD)
GIT_SHA=$(git rev-parse --short HEAD)
docker tag myapp:latest myrepo/myapp:$GIT_SHA

# Strategy 3: Environment-based tags
docker tag myapp:latest myrepo/myapp:production
docker tag myapp:latest myrepo/myapp:staging

# Strategy 4: Combined
docker tag myapp:latest myrepo/myapp:1.2.3-$GIT_SHA
```

---

## 🧪 Hands-on Lab: Docker Registry

### Lab Duration: 60 minutes

---

### Exercise 1: Push and Pull from Docker Hub

```bash
# Step 1: Log in to Docker Hub
docker login

# Step 2: Build a custom image
mkdir dockerhub-lab && cd dockerhub-lab

cat > index.html << 'EOF'
<html><body><h1>My Custom Image on Docker Hub!</h1></body></html>
EOF

cat > Dockerfile << 'EOF'
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
LABEL description="My first Docker Hub image"
EOF

docker build -t my-first-push:1.0 .

# Step 3: Tag for Docker Hub (replace YOUR_USERNAME)
YOUR_USERNAME="yourusername"
docker tag my-first-push:1.0 ${YOUR_USERNAME}/my-first-push:1.0
docker tag my-first-push:1.0 ${YOUR_USERNAME}/my-first-push:latest

# Step 4: Push to Docker Hub
docker push ${YOUR_USERNAME}/my-first-push:1.0
docker push ${YOUR_USERNAME}/my-first-push:latest

# Step 5: Remove local copies
docker rmi my-first-push:1.0 ${YOUR_USERNAME}/my-first-push:1.0 ${YOUR_USERNAME}/my-first-push:latest

# Step 6: Pull from Docker Hub
docker pull ${YOUR_USERNAME}/my-first-push:1.0

# Step 7: Run it
docker run -d --name pulled-container -p 8080:80 ${YOUR_USERNAME}/my-first-push:1.0
curl http://localhost:8080

# Clean up
docker stop pulled-container && docker rm pulled-container
cd .. && rm -rf dockerhub-lab
```

---

### Exercise 2: Set Up a Local Registry

```bash
# Step 1: Start a local registry with persistent storage
docker volume create my-registry-data

docker run -d \
  --name my-local-registry \
  -p 5000:5000 \
  --restart unless-stopped \
  -v my-registry-data:/var/lib/registry \
  registry:2

# Step 2: Verify the registry is running
curl http://localhost:5000/v2/
# Should output: {}

# Step 3: Pull a public image and push to local registry
docker pull alpine:latest
docker tag alpine:latest localhost:5000/alpine:latest
docker push localhost:5000/alpine:latest

docker pull python:3.11-slim
docker tag python:3.11-slim localhost:5000/python:3.11-slim
docker push localhost:5000/python:3.11-slim

# Step 4: Browse the registry catalog
echo "All repositories in local registry:"
curl -s http://localhost:5000/v2/_catalog | python3 -m json.tool

echo "Tags for alpine:"
curl -s http://localhost:5000/v2/alpine/tags/list | python3 -m json.tool

# Step 5: Delete local copies and pull from local registry
docker rmi localhost:5000/alpine:latest
docker pull localhost:5000/alpine:latest
docker run --rm localhost:5000/alpine:latest echo "Pulled from local registry!"

# Step 6: Build and push a custom image to local registry
mkdir local-reg-lab && cd local-reg-lab

cat > Dockerfile << 'EOF'
FROM alpine:latest
RUN apk add --no-cache curl
LABEL registry=local
CMD ["echo", "Hello from local registry!"]
EOF

docker build -t localhost:5000/my-custom-alpine:1.0 .
docker push localhost:5000/my-custom-alpine:1.0

# Verify
curl -s http://localhost:5000/v2/_catalog | python3 -m json.tool

# Run from local registry
docker run --rm localhost:5000/my-custom-alpine:1.0

# Clean up
cd .. && rm -rf local-reg-lab
docker stop my-local-registry && docker rm my-local-registry
docker volume rm my-registry-data
```

---

# Module 6 – Conclusion

## Course Summary

Congratulations on completing **Docker Basics for DevOps**! Here is a comprehensive review of everything you have learned throughout this course.

---

## Key Concepts Recap

### Module 1: Setting Up Docker and Basic Commands

**Docker** is an open-source platform that automates the building, shipping, and running of applications inside lightweight, portable containers. Containers solve the "it works on my machine" problem by packaging applications with all their dependencies.

Containers differ from VMs in that they share the host OS kernel, starting in milliseconds and using megabytes rather than gigabytes. The Docker Engine consists of the CLI, daemon (dockerd), containerd, and runc — leveraging Linux namespaces for isolation and cgroups for resource control.

Core commands to internalize: `docker run`, `docker ps`, `docker images`, `docker pull`, `docker stop`, `docker rm`, `docker rmi`, `docker logs`, `docker exec`.

---

### Module 2: Docker Run

`docker run` is the central command of Docker. Its key options include `-d` (detached/background), `-p` (port mapping), `-v` (volumes), `-e` (environment variables), `--name` (naming), `--rm` (auto-remove), `--network` (networking), `--cpus` and `--memory` (resource limits), and `--restart` (restart policy).

Port mapping with `-p hostPort:containerPort` routes external traffic into the container. Environment variables with `-e KEY=VALUE` or `--env-file` are the standard way to configure containers at runtime without rebuilding images.

---

### Module 3: Docker Images

Docker images are **layered, read-only snapshots** built from Dockerfiles. Each Dockerfile instruction creates a new layer, and layers are cached and reused, making builds fast and efficient.

Critical Dockerfile instructions: `FROM` (base image), `RUN` (execute commands), `COPY` (add files), `ENV` (environment variables), `WORKDIR` (working directory), `EXPOSE` (document ports), `CMD` (default command — overridable), `ENTRYPOINT` (fixed executable — CMD arguments are appended).

The distinction between `CMD` and `ENTRYPOINT` is fundamental: CMD provides overridable defaults, while ENTRYPOINT defines the fixed executable. Together, ENTRYPOINT + CMD creates the most flexible container configuration pattern.

Best practices include pinning image versions, combining RUN commands, using `.dockerignore`, ordering layers from stable to volatile, using multi-stage builds, and running as a non-root user.

---

### Module 4: Docker Engine and Storage

The Docker Engine uses Linux **namespaces** for isolation (PID, network, mount, UTS, IPC, user) and **cgroups** for resource limiting (CPU, memory, I/O). The daemon (`dockerd`) manages all Docker objects and delegates container execution to `containerd` and `runc`.

Three storage mechanisms exist: **Volumes** (Docker-managed, recommended for production data, live in `/var/lib/docker/volumes/`), **Bind Mounts** (map specific host paths into containers, ideal for development), and **tmpfs mounts** (in-memory, non-persistent, for sensitive temporary data).

Volumes are preferred for: database storage, sharing data between containers, and portability. Bind mounts are preferred for: development workflows, sharing source code, and host-managed configuration.

---

### Module 5: Docker Networking and Registry

Docker provides five network drivers: **bridge** (default, isolated virtual network), **host** (shares host network stack), **none** (no networking), **overlay** (multi-host Swarm networks), and **macvlan** (physical network integration).

Custom bridge networks are almost always preferred over the default bridge because they provide **automatic DNS resolution** — containers can reach each other by name rather than by ephemeral IP address.

A **Docker Registry** stores and distributes images. Docker Hub is the public default. Private registries (ECR, GCR, ACR, Harbor, or self-hosted with the `registry:2` image) are used for proprietary or internal images. The workflow is: `docker build` → `docker tag` → `docker push` → `docker pull` → `docker run`.

---

## Docker Quick Reference Card

```bash
# ═══════════════════════════════════════════════
#            IMAGES
# ═══════════════════════════════════════════════
docker pull IMAGE[:TAG]                # Download image
docker images                          # List local images
docker build -t NAME:TAG .             # Build image from Dockerfile
docker tag SOURCE TARGET               # Tag an image
docker push IMAGE[:TAG]                # Push to registry
docker rmi IMAGE                       # Remove image
docker image prune                     # Remove unused images
docker history IMAGE                   # View image layers
docker inspect IMAGE                   # Detailed image info

# ═══════════════════════════════════════════════
#            CONTAINERS
# ═══════════════════════════════════════════════
docker run -d --name NAME -p HP:CP IMAGE    # Run in background
docker run -it IMAGE bash                   # Interactive shell
docker run --rm IMAGE COMMAND               # Run and auto-remove
docker ps                                   # Running containers
docker ps -a                                # All containers
docker stop CONTAINER                       # Graceful stop
docker start CONTAINER                      # Start stopped container
docker restart CONTAINER                    # Restart
docker rm CONTAINER                         # Remove container
docker rm -f CONTAINER                      # Force remove
docker container prune                      # Remove all stopped

# ═══════════════════════════════════════════════
#            INTERACTION
# ═══════════════════════════════════════════════
docker exec -it CONTAINER bash         # Shell into container
docker exec CONTAINER COMMAND          # Run command in container
docker logs CONTAINER                  # View logs
docker logs -f CONTAINER               # Follow logs
docker cp SRC CONTAINER:DEST           # Copy to container
docker cp CONTAINER:SRC DEST           # Copy from container
docker top CONTAINER                   # Processes in container
docker stats CONTAINER                 # Resource usage
docker inspect CONTAINER               # Detailed info
docker port CONTAINER                  # Port mappings

# ═══════════════════════════════════════════════
#            VOLUMES
# ═══════════════════════════════════════════════
docker volume create NAME              # Create volume
docker volume ls                       # List volumes
docker volume inspect NAME             # Volume details
docker volume rm NAME                  # Remove volume
docker volume prune                    # Remove unused volumes
# Use with: -v NAME:/path  or  --mount type=volume,...

# ═══════════════════════════════════════════════
#            NETWORKS
# ═══════════════════════════════════════════════
docker network create NAME             # Create network
docker network ls                      # List networks
docker network inspect NAME            # Network details
docker network connect NET CONTAINER   # Connect container to network
docker network disconnect NET CONT     # Disconnect
docker network rm NAME                 # Remove network
docker network prune                   # Remove unused networks

# ═══════════════════════════════════════════════
#            SYSTEM
# ═══════════════════════════════════════════════
docker info                            # Docker system info
docker system df                       # Disk usage
docker system prune                    # Remove all unused resources
docker system prune -a --volumes       # Full cleanup (DESTRUCTIVE)
docker login [REGISTRY]                # Log in to registry
docker logout [REGISTRY]               # Log out
```

---

## Docker Run Options Reference

```bash
docker run \
  -d                          # Detached (background) mode
  -it                         # Interactive + TTY (for shell access)
  --rm                        # Auto-remove when container exits
  --name my-container         # Assign a name
  -p 8080:80                  # Port map: hostPort:containerPort
  -P                          # Publish all exposed ports to random host ports
  -v volume:/path             # Named volume mount
  -v /host/path:/container    # Bind mount
  --mount type=volume,...     # Explicit mount (alternative to -v)
  -e KEY=VALUE                # Environment variable
  --env-file ./config.env     # Load env vars from file
  --network my-net            # Specify network
  --hostname myhost           # Set container hostname
  --restart unless-stopped    # Restart policy
  --cpus="1.0"                # CPU limit
  --memory="512m"             # Memory limit
  --user 1001:1001            # Run as user:group
  --read-only                 # Read-only root filesystem
  --workdir /app              # Set working directory
  --entrypoint /bin/sh        # Override ENTRYPOINT
  IMAGE [COMMAND] [ARGS...]   # Image and optional command
```

---

## Common Dockerfile Patterns

```dockerfile
# ── PATTERN 1: Simple application ──────────────────────────────
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]

# ── PATTERN 2: Multi-stage build ──────────────────────────────
FROM node:18 AS builder
WORKDIR /build
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /build/dist /usr/share/nginx/html

# ── PATTERN 3: Non-root user (security) ───────────────────────
FROM ubuntu:22.04
RUN useradd -m -r -u 1001 appuser
WORKDIR /app
COPY --chown=appuser:appuser . .
USER appuser
CMD ["./app"]

# ── PATTERN 4: Init script as ENTRYPOINT ──────────────────────
FROM python:3.11-slim
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "app:app"]

# ── PATTERN 5: With healthcheck ───────────────────────────────
FROM nginx:alpine
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -qO- http://localhost/ || exit 1
```

---

## Recommended Next Steps

**Immediate Next Skills:**

- **Docker Compose** — Define and run multi-container applications with a single `docker-compose.yml` file
- **Docker Secrets** — Manage sensitive data (passwords, certificates) securely
- **Multi-stage builds** — Create lean production images by separating build and runtime stages
- **BuildKit** — Docker's advanced image builder with parallel builds and better caching

**Intermediate Topics:**

- **Container security** — Image scanning (Trivy, Snyk), rootless Docker, AppArmor/seccomp profiles
- **Kubernetes** — Container orchestration for running Docker containers at scale
- **Docker Swarm** — Docker's built-in clustering and orchestration solution
- **CI/CD integration** — GitHub Actions, GitLab CI, Jenkins pipelines using Docker

**Advanced Topics:**

- **Custom registry** — Harbor for enterprise-grade image management
- **Image optimization** — Distroless images, Alpine-based builds, layer squashing
- **Container monitoring** — Prometheus + cAdvisor, Datadog, Grafana dashboards
- **Service mesh** — Istio or Linkerd for advanced microservices networking

**Certifications:**

- **Docker Certified Associate (DCA)** — Official Docker certification
- **CKAD** — Certified Kubernetes Application Developer (builds on Docker skills)
- **CKA** — Certified Kubernetes Administrator

---

## Resources

### Official Documentation

- [Docker Documentation](https://docs.docker.com/) — Complete official reference
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/) — All Dockerfile instructions
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/) — All CLI commands
- [Docker Hub](https://hub.docker.com/) — Browse official and community images

### Learning Platforms

- [Play with Docker](https://labs.play-with-docker.com/) — Free browser-based Docker environment
- [Killercoda Docker Scenarios](https://killercoda.com/playgrounds/scenario/docker) — Interactive labs
- [Docker Labs on GitHub](https://github.com/docker/labs) — Official Docker training labs

### Community

- [Docker Community Forums](https://forums.docker.com/)
- [Docker Slack Community](https://dockr.ly/slack)
- [r/docker on Reddit](https://www.reddit.com/r/docker/)
- [Awesome Docker](https://github.com/veggiemonk/awesome-docker) — Curated Docker resources

---

_This tutorial was created to provide a comprehensive introduction to Docker for DevOps practitioners. All examples are based on Docker Engine 24.x and have been validated on Ubuntu 22.04, macOS, and Windows with Docker Desktop. Images referenced are from Docker Hub and are provided for educational purposes._