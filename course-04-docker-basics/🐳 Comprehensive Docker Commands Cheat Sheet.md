# 🐳 **Comprehensive Docker Commands Cheat Sheet**

## **Table of Contents**
1. [Container Management](#1-container-management)
2. [Image Management](#2-image-management)
3. [Docker Hub/Registry](#3-docker-hubregistry)
4. [Network Management](#4-network-management)
5. [Volume Management](#5-volume-management)
6. [Docker Compose](#6-docker-compose)
7. [Dockerfile Instructions](#7-dockerfile-instructions)
8. [System Management](#8-system-management)
9. [Docker Swarm](#9-docker-swarm)
10. [Docker Buildx](#10-docker-buildx)
11. [Security & Best Practices](#11-security--best-practices)
12. [Troubleshooting & Debugging](#12-troubleshooting--debugging)

---

## **1. Container Management**

### **Basic Container Operations**
```bash
# Create and start a container
docker run nginx:alpine
docker run -d nginx:alpine                    # Run in background
docker run -it ubuntu bash                     # Interactive with terminal
docker run --rm nginx:alpine                    # Remove after exit
docker run --name my-nginx nginx:alpine         # Assign custom name

# Port mapping
docker run -p 8080:80 nginx:alpine              # Map port 8080 host -> 80 container
docker run -p 8080:80 -p 8443:443 nginx:alpine  # Multiple ports

# Environment variables
docker run -e MY_VAR=value nginx:alpine
docker run --env-file .env nginx:alpine

# Resource limits
docker run --memory="256m" --cpus="1.5" nginx:alpine
docker run --memory="256m" --memory-swap="512m" nginx:alpine

# Restart policies
docker run --restart=always nginx:alpine        # Always restart
docker run --restart=on-failure:5 nginx:alpine  # Max 5 retries
docker run --restart=unless-stopped nginx:alpine

# Working directory and user
docker run -w /app -u 1000:1000 nginx:alpine

# Container operations
docker ps                                       # List running containers
docker ps -a                                     # List all containers
docker ps -q                                      # List only IDs
docker ps --filter "status=exited"                # Filter by status

docker start container_name                      # Start stopped container
docker stop container_name                        # Graceful stop
docker kill container_name                         # Force stop
docker restart container_name                       # Restart

docker pause container_name                        # Pause processes
docker unpause container_name                       # Unpause

docker rm container_name                            # Remove container
docker rm -f container_name                          # Force remove running
docker container prune                                # Remove all stopped

docker rename old_name new_name                      # Rename container

docker wait container_name                            # Block until container stops
```

### **Inspecting Containers**
```bash
docker logs container_name                          # View logs
docker logs -f container_name                         # Follow logs
docker logs --tail 100 container_name                  # Last 100 lines
docker logs --since 2024-01-01 container_name           # Logs since date

docker inspect container_name                          # Detailed info
docker inspect -f '{{.NetworkSettings.IPAddress}}' container_name

docker top container_name                               # Running processes
docker stats                                            # Live resource usage
docker stats --no-stream                                 # One-time stats

docker port container_name                               # Port mappings
docker diff container_name                                # Filesystem changes

docker exec -it container_name bash                       # Execute command
docker exec -it container_name sh                          # If bash not available
docker exec -e VAR=value container_name env                 # With environment

docker cp file.txt container_name:/path/                   # Copy to container
docker cp container_name:/path/file.txt ./                  # Copy from container

docker attach container_name                                # Attach to running container
docker container update --restart=always container_name     # Update container config
```

---

## **2. Image Management**

### **Image Operations**
```bash
# Listing and searching
docker images                                          # List images
docker images -a                                        # All images (including intermediates)
docker images --filter "dangling=true"                   # Filter dangling
docker images --format "table {{.Repository}}\t{{.Tag}}"  # Custom format

docker search nginx                                      # Search Docker Hub
docker search --filter "stars=100" nginx                  # Search by stars

# Pulling and pushing
docker pull nginx:alpine                                 # Pull image
docker pull --platform linux/arm64 nginx:alpine          # Pull for specific platform
docker pull --all-tags nginx                              # Pull all tags

docker push username/image:tag                           # Push to registry

# Building images
docker build -t myapp:latest .                           # Build from Dockerfile
docker build -t myapp:latest -f Dockerfile.prod .         # Custom Dockerfile
docker build --no-cache -t myapp:latest .                  # Build without cache
docker build --build-arg VERSION=1.0 -t myapp:latest .     # Build args
docker build --target builder -t myapp:latest .            # Multi-stage specific stage
docker build --platform linux/amd64,linux/arm64 .          # Multi-platform build

# Tagging
docker tag myapp:latest username/myapp:latest            # Tag image
docker tag myapp:latest username/myapp:v1.0.0             # Version tag

# Removing
docker rmi image_name                                    # Remove image
docker rmi -f image_name                                  # Force remove
docker image prune                                        # Remove dangling images
docker image prune -a                                      # Remove all unused images

# Saving and loading
docker save -o myimage.tar myapp:latest                  # Save image to file
docker load -i myimage.tar                                # Load image from file

docker export -o container.tar container_name             # Export container
docker import container.tar newimage:latest                # Import as image

# History and layers
docker history myapp:latest                               # Show image layers
docker history --no-trunc myapp:latest                     # Full output
```

---

## **3. Docker Hub/Registry**

```bash
# Login/Logout
docker login                                             # Login to Docker Hub
docker login -u username -p password
docker logout

# Registry operations
docker pull registry:2                                   # Run private registry
docker run -d -p 5000:5000 --name registry registry:2

docker tag myapp:latest localhost:5000/myapp:latest      # Tag for local registry
docker push localhost:5000/myapp:latest                   # Push to local registry
docker pull localhost:5000/myapp:latest                    # Pull from local registry

# Registry inspection
docker manifest inspect nginx:alpine                      # Inspect manifest
docker manifest inspect --verbose nginx:alpine             # Verbose output
```

---

## **4. Network Management**

### **Network Types**
```bash
# Bridge (default) - isolated network on single host
# Host - uses host's networking directly
# Overlay - multi-host networking (Swarm)
# Macvlan - assign MAC addresses to containers
# None - no networking
```

### **Network Commands**
```bash
# List networks
docker network ls                                         # List all networks
docker network ls --filter "driver=bridge"                 # Filter by driver

# Create networks
docker network create my-network                          # Default bridge
docker network create --driver bridge my-network

docker network create \
  --driver bridge \
  --subnet 172.20.0.0/16 \
  --gateway 172.20.0.1 \
  --ip-range 172.20.10.0/24 \
  my-custom-network

docker network create \
  --driver overlay \
  --subnet 10.10.0.0/16 \
  --attachable \
  my-swarm-network

# Inspect
docker network inspect my-network                         # Network details
docker network inspect -f '{{range .Containers}}{{.Name}}{{end}}' my-network

# Connect/Disconnect
docker network connect my-network container_name          # Connect container
docker network connect --ip 172.20.0.10 my-network container_name  # With specific IP
docker network connect --alias db my-network container_name        # With alias

docker network disconnect my-network container_name       # Disconnect
docker network disconnect -f my-network container_name    # Force disconnect

# Remove
docker network rm my-network                              # Remove network
docker network prune                                       # Remove unused networks
docker network prune --filter "until=24h"                  # Filter by age
```

---

## **5. Volume Management**

### **Volume Types**
```bash
# Volumes - managed by Docker (/var/lib/docker/volumes/)
# Bind mounts - any directory on host
# tmpfs mounts - in-memory (Linux only)
# Named pipes - for Windows containers
```

### **Volume Commands**
```bash
# Create and manage volumes
docker volume create my-volume                            # Create volume
docker volume create --driver local \
  --opt type=btrfs \
  --opt device=/dev/sda2 \
  my-volume

docker volume ls                                          # List volumes
docker volume ls --filter "dangling=true"                  # Filter
docker volume inspect my-volume                            # Inspect volume

# Run with volumes
docker run -v my-volume:/app/data nginx:alpine            # Named volume
docker run -v /host/path:/container/path nginx:alpine     # Bind mount
docker run --mount type=bind,src=/host,dst=/container nginx:alpine
docker run --mount type=volume,src=my-volume,dst=/data nginx:alpine
docker run --mount type=tmpfs,dst=/app/cache nginx:alpine # tmpfs mount

# Volume options
docker run -v my-volume:/data:ro nginx:alpine             # Read-only
docker run -v my-volume:/data:z nginx:alpine              # SELinux relabel

# Backup and restore
docker run --rm -v my-volume:/data -v $(pwd):/backup alpine \
  tar czf /backup/backup.tar.gz -C /data .                # Backup

docker run --rm -v my-volume:/data -v $(pwd):/backup alpine \
  tar xzf /backup/backup.tar.gz -C /data                  # Restore

# Remove
docker volume rm my-volume                                # Remove volume
docker volume prune                                        # Remove unused volumes
docker volume prune --filter "label=keep=false"            # Filter by label
```

---

## **6. Docker Compose**

### **Basic Commands**
```bash
# Start and stop
docker-compose up                                         # Create and start
docker-compose up -d                                       # Detached mode
docker-compose down                                        # Stop and remove
docker-compose down -v                                      # Remove volumes too
docker-compose down --rmi all                                # Remove images too

docker-compose start                                       # Start services
docker-compose stop                                         # Stop services
docker-compose restart                                       # Restart services
docker-compose pause                                         # Pause services
docker-compose unpause                                       # Unpause services

# Build
docker-compose build                                       # Build images
docker-compose build --no-cache                             # Build without cache
docker-compose build --pull                                  # Pull latest base images

# Logs
docker-compose logs                                        # View logs
docker-compose logs -f                                       # Follow logs
docker-compose logs --tail=100 service_name                  # Last 100 lines

# Exec and run
docker-compose exec web bash                               # Execute in service
docker-compose run web npm install                         # Run one-off command

# Scale
docker-compose up --scale web=3                            # Scale service

# Configuration
docker-compose config                                      # Validate and view
docker-compose config --services                            # List services
docker-compose config --volumes                              # List volumes

# Images and containers
docker-compose images                                      # List images used
docker-compose ps                                           # List containers
docker-compose top                                          # Running processes

# Events
docker-compose events                                      # Stream events
docker-compose events --json                                # JSON format
```

### **docker-compose.yml Example**
```yaml
version: '3.8'

services:
  web:
    build: 
      context: .
      dockerfile: Dockerfile
      args:
        NODE_ENV: production
    image: myapp:latest
    container_name: myapp-web
    ports:
      - "8080:80"
      - "8443:443"
    environment:
      - NODE_ENV=production
      - DB_HOST=db
    env_file:
      - .env
    volumes:
      - ./src:/app/src
      - /app/node_modules
      - web-data:/app/data
    networks:
      - frontend
      - backend
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
      restart_policy:
        condition: on-failure

  db:
    image: postgres:15-alpine
    container_name: myapp-db
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: myapp-redis
    networks:
      - backend

volumes:
  web-data:
    driver: local
  db-data:

networks:
  frontend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
  backend:
    driver: bridge
    internal: true
```

---

## **7. Dockerfile Instructions**

### **Complete Dockerfile Reference**
```dockerfile
# Base images
FROM alpine:3.19                              # Latest stable Alpine
FROM ubuntu:22.04                              # Ubuntu LTS
FROM node:20-alpine                             # Node.js with Alpine
FROM python:3.11-slim                            # Python slim
FROM nginx:alpine                                 # Nginx with Alpine
FROM scratch                                      # Empty image

# Metadata
LABEL maintainer="user@example.com"
LABEL version="1.0"
LABEL description="My application"

# Environment variables
ENV NODE_ENV=production
ENV APP_HOME=/app
ENV PATH="${APP_HOME}/bin:${PATH}"

# Arguments (build-time)
ARG VERSION=latest
ARG DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR ${APP_HOME}

# Copy files
COPY package*.json ./                           # Copy specific files
COPY . .                                         # Copy everything
COPY --chown=node:node . .                       # With ownership
COPY --chmod=755 script.sh .                      # With permissions

# Copy from previous stage (multi-stage)
COPY --from=builder /app/dist ./dist

# Run commands
RUN apt-get update && apt-get install -y \
    curl \
    nginx \
    && rm -rf /var/lib/apt/lists/*

RUN npm ci --only=production

# User management
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

# Ports
EXPOSE 8080
EXPOSE 8443/tcp

# Volumes
VOLUME ["/data", "/config"]

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Entrypoint and Command
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["node", "server.js"]

# Init process
STOPSIGNAL SIGTERM

# Shell form vs Exec form
CMD node server.js                    # Shell form (runs with /bin/sh -c)
CMD ["node", "server.js"]              # Exec form (preferred)

# Onbuild (deprecated, avoid using)
ONBUILD RUN npm install

# Cache mounts (BuildKit)
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y curl
```

### **Multi-stage Build Example**
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## **8. System Management**

```bash
# Docker system info
docker version                                       # Version info
docker version --format '{{.Server.Version}}'        # Custom format

docker info                                          # System-wide info
docker info --format '{{.ServerVersion}}'

# Disk usage
docker system df                                     # Disk usage
docker system df -v                                   # Detailed usage
docker system df --format 'table {{.Type}}\t{{.Size}}'

# Cleanup
docker system prune                                   # Clean everything unused
docker system prune -a                                 # Including unused images
docker system prune --volumes                           # Including volumes
docker system prune --filter "until=24h"                 # Filter by time

# Events
docker events                                         # Real-time events
docker events --filter 'event=create'                  # Filter events
docker events --since '2024-01-01T00:00:00'            # Since timestamp

# Context (multi-environment)
docker context ls                                      # List contexts
docker context create my-context --docker host=ssh://user@host
docker context use my-context
docker context inspect

# Stats
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}"
```

---

## **9. Docker Swarm**

```bash
# Initialize Swarm
docker swarm init                                     # Initialize swarm
docker swarm init --advertise-addr 192.168.1.10

docker swarm join-token manager                       # Get manager token
docker swarm join-token worker                         # Get worker token

# Join cluster
docker swarm join --token TOKEN 192.168.1.10:2377     # Join as worker/manager

# Node management
docker node ls                                         # List nodes
docker node inspect node1                               # Inspect node
docker node promote node2                                # Promote to manager
docker node demote node2                                  # Demote to worker
docker node update --availability drain node1            # Drain node
docker node rm node1                                      # Remove node

# Service management
docker service create --name web --replicas 3 nginx     # Create service
docker service create \
  --name web \
  --publish 8080:80 \
  --replicas 5 \
  --network my-network \
  --mount type=volume,source=data,target=/data \
  --limit-memory 256m \
  --limit-cpu 0.5 \
  nginx:alpine

docker service ls                                       # List services
docker service ps web                                    # List service tasks
docker service logs web                                  # Service logs
docker service inspect web                               # Service details

docker service scale web=10                             # Scale service
docker service update --image nginx:1.25 web            # Update image
docker service update --force web                       # Force restart
docker service update --rollback web                    # Rollback update

docker service rm web                                    # Remove service

# Stack (Compose in Swarm)
docker stack deploy -c docker-compose.yml myapp         # Deploy stack
docker stack ls                                          # List stacks
docker stack services myapp                              # Stack services
docker stack ps myapp                                     # Stack tasks
docker stack rm myapp                                     # Remove stack

# Secrets and configs
echo "mysecret" | docker secret create db_password -    # Create secret
docker secret ls                                          # List secrets
docker secret inspect db_password                         # Inspect secret
docker secret rm db_password                               # Remove secret

docker config create nginx.conf ./nginx.conf             # Create config
docker config ls                                          # List configs
docker config inspect nginx.conf                           # Inspect config
```

---

## **10. Docker Buildx**

```bash
# Enable Buildx
docker buildx create --name mybuilder                    # Create builder
docker buildx use mybuilder                               # Use builder
docker buildx inspect --bootstrap                          # Bootstrap
docker buildx ls                                           # List builders

# Multi-platform builds
docker buildx build \
  --platform linux/amd64,linux/arm64,linux/arm/v7 \
  -t username/app:latest \
  --push \
  .

# With caching
docker buildx build \
  --cache-from type=registry,ref=username/app:cache \
  --cache-to type=inline \
  -t username/app:latest \
  --push \
  .

# Bake (HCL/JSON build definition)
docker buildx bake                                         # Build from bake file
docker buildx bake -f docker-bake.hcl                       # Custom file
```

**docker-bake.hcl example:**
```hcl
group "default" {
  targets = ["app", "web"]
}

target "app" {
  context = "."
  dockerfile = "Dockerfile.app"
  tags = ["username/app:latest"]
  platforms = ["linux/amd64", "linux/arm64"]
}

target "web" {
  context = "web"
  dockerfile = "Dockerfile.web"
  tags = ["username/web:latest"]
}
```

---

## **11. Security & Best Practices**

```bash
# Security scanning
docker scan nginx:alpine                                 # Scan for vulnerabilities
docker scan --file Dockerfile nginx:alpine                # Scan with Dockerfile

docker scout quickview nginx:alpine                       # Docker Scout quick view
docker scout cves nginx:alpine                             # List CVEs
docker scout recommendations nginx:alpine                   # Get recommendations

# Security commands
docker run --security-opt=no-new-privileges:true nginx   # No new privileges
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE     # Drop all, add specific
docker run --read-only nginx                              # Read-only root fs
docker run --tmpfs /tmp                                    # Temp filesystem

# Secret management (don't use ENV for secrets!)
docker run --secret id=db_password,src=db_password.txt    # Secret mount (Swarm)

# Image signing and verification
docker trust sign username/app:latest                     # Sign image
docker trust inspect username/app:latest                   # Inspect signatures
docker trust revoke username/app:latest                     # Revoke signature

# Content trust
export DOCKER_CONTENT_TRUST=1                             # Enable content trust
docker pull username/app:latest                            # Only signed images

# User namespace remapping
# /etc/docker/daemon.json
{
  "userns-remap": "default"
}
```

### **Security Best Practices Checklist**
```bash
# ✅ Use specific tags, never 'latest' in production
docker pull nginx:1.25.3-alpine

# ✅ Run as non-root user
docker run --user 1000:1000 nginx

# ✅ Read-only root filesystem
docker run --read-only --tmpfs /tmp --tmpfs /run nginx

# ✅ Drop all capabilities, add only needed
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE nginx

# ✅ Use secrets, not environment variables
# ✅ Scan images regularly
# ✅ Sign and verify images
# ✅ Use minimal base images
# ✅ Multi-stage builds
```

---

## **12. Troubleshooting & Debugging**

```bash
# Debug containers
docker logs container_name                               # Check logs
docker logs --tail 50 --follow --timestamps container_name

docker inspect container_name                            # Full details
docker inspect -f '{{.State.Running}}' container_name    # Check if running

docker exec -it container_name sh                        # Shell access
docker exec container_name ps aux                         # Check processes
docker exec container_name netstat -tulpn                  # Check ports

docker stats --no-stream container_name                   # Resource usage

# Debug images
docker history image_name                                # Check layers
docker run -it --entrypoint sh image_name                # Override entrypoint

# Network debugging
docker network inspect network_name                      # Network details
docker run --rm --network container:container_name nicolaka/netshoot

# With netshoot toolkit
docker run -it --network container:container_name nicolaka/netshoot \
  tcpdump -i eth0

# Common diagnostics
docker system df                                         # Check disk usage
docker events --since '5m'                               # Recent events
docker info                                               # System info

# Debug daemon
dockerd --debug                                          # Start daemon in debug
journalctl -u docker.service -f                          # View systemd logs

# Checkpoint/Restore
docker checkpoint create container_name checkpoint       # Create checkpoint
docker start --checkpoint checkpoint container_name      # Restore from checkpoint

# Export/Import for debugging
docker export container_name > container.tar
tar -tvf container.tar                                   # Inspect filesystem

# Container forensics
docker diff container_name                               # Filesystem changes
docker cp container_name:/path/to/file ./                 # Extract specific file

# Plugin debugging
docker plugin ls                                          # List plugins
docker plugin inspect plugin_name                         # Inspect plugin
```

### **Common Issues Quick Reference**

| Problem | Diagnostic Commands | Solution |
|---------|-------------------|----------|
| **Container exits immediately** | `docker logs <container>` | Check logs for errors |
| **Port already in use** | `netstat -tulpn \| grep <port>` | Change port or stop process |
| **Out of disk space** | `docker system df` | `docker system prune -a` |
| **Network issues** | `docker network inspect` | Check network config |
| **Permission denied** | `docker inspect --format='{{.Config.User}}'` | Use `--user` flag |
| **Image not found** | `docker search <image>` | Check registry/tag |
| **DNS resolution fails** | `docker exec <container> cat /etc/resolv.conf` | Add `--dns` flag |
| **Slow performance** | `docker stats` | Check resource limits |

---

## **Quick Reference Card**

### **Most Used Commands**
```bash
# Containers
docker run -d -p 8080:80 --name web nginx
docker ps
docker stop web && docker rm web

# Images
docker build -t myapp .
docker images
docker rmi myapp

# Compose
docker-compose up -d
docker-compose down
docker-compose logs -f

# System
docker system df
docker system prune -a
```

### **Aliases for Productivity**
```bash
alias d='docker'
alias dc='docker-compose'
alias dps='docker ps'
alias dis='docker images'
alias dex='docker exec -it'
alias dlog='docker logs -f'
alias dprune='docker system prune -af'
alias dstats='docker stats --no-stream'
```

### **Formatting Examples**
```bash
# Custom output formats
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
docker images --format "{{.Repository}}:{{.Tag}}\t{{.Size}}"
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

---

## **Environment Variables**

```bash
# Docker CLI
export DOCKER_HOST="tcp://192.168.1.10:2375"           # Remote Docker
export DOCKER_TLS_VERIFY="1"                            # TLS verification
export DOCKER_CERT_PATH="/path/to/certs"                 # Cert path
export DOCKER_CONTENT_TRUST="1"                          # Content trust

# BuildKit
export DOCKER_BUILDKIT=1                                 # Enable BuildKit
export BUILDKIT_PROGRESS=plain                            # Build output

# Compose
export COMPOSE_PROJECT_NAME="myproject"                  # Project name
export COMPOSE_FILE="docker-compose.yml:docker-compose.prod.yml"  # Multiple files
export COMPOSE_PROFILES="debug"                           # Enable profiles
```

---

## **Conclusion**

This comprehensive cheat sheet covers **95% of daily Docker operations**. For specific scenarios:

- 📚 Bookmark this guide
- 🏷️ Print the quick reference card
- 🔧 Customize aliases for your workflow
- 📖 Refer to official docs for advanced topics

**Pro Tips:**
- Always use specific tags in production
- Implement proper security practices
- Regular cleanup with `docker system prune`
- Use BuildKit for faster builds
- Monitor with `docker stats` and `docker events`

**Need more help?** Run `docker COMMAND --help` or visit [docs.docker.com](https://docs.docker.com)