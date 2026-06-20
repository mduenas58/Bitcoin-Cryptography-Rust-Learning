# 🐳 **Complete Guide to Docker Compose: From Basics to Production**

## **Table of Contents**
1. [What is Docker Compose?](#1-what-is-docker-compose)
2. [Installation & Setup](#2-installation--setup)
3. [docker-compose.yml Structure](#3-docker-composeyml-structure)
4. [Core Concepts](#4-core-concepts)
5. [Basic Examples](#5-basic-examples)
6. [Intermediate Examples](#6-intermediate-examples)
7. [Advanced Production Examples](#7-advanced-production-examples)
8. [Docker Compose Commands](#8-docker-compose-commands)
9. [Environment Variables & Configuration](#9-environment-variables--configuration)
10. [Networking in Compose](#10-networking-in-compose)
11. [Volumes & Data Persistence](#11-volumes--data-persistence)
12. [Health Checks & Dependencies](#12-health-checks--dependencies)
13. [Profiles & Extends](#13-profiles--extends)
14. [Monitoring & Debugging](#14-monitoring--debugging)
15. [Best Practices](#15-best-practices)
16. [Troubleshooting Guide](#16-troubleshooting-guide)

---

## **1. What is Docker Compose?**

### **Definition**
Docker Compose is a tool for defining and running multi-container Docker applications. Using a YAML file, you configure your application's services, networks, and volumes, then create and start all containers with a single command.

### **Key Benefits**
- **Single command deployment**: `docker-compose up` starts entire application stack
- **Declarative configuration**: Infrastructure as code
- **Isolation**: Each project runs in its own isolated environment
- **Reproducibility**: Same configuration works everywhere
- **Version control**: Compose files can be committed to Git
- **Development-Production parity**: Same config works in both environments

### **Use Cases**
- Local development environments
- CI/CD testing pipelines
- Single-host production deployments
- Microservices demonstration
- Complex application stacks (web + DB + cache + queue)

---

## **2. Installation & Setup**

### **Installation Methods**

#### **On Linux**
```bash
# Download latest version
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker-compose --version
```

#### **On macOS** (with Docker Desktop)
```bash
# Docker Desktop includes Compose by default
# Just install Docker Desktop from https://www.docker.com/products/docker-desktop
```

#### **On Windows** (with Docker Desktop)
```bash
# Docker Desktop for Windows includes Compose
# Install from https://www.docker.com/products/docker-desktop
```

#### **Using pip (Python)**
```bash
pip install docker-compose
```

### **Verify Installation**
```bash
docker-compose --version
# Output: docker-compose version 2.24.0, build 1110ad01
```

### **Basic Setup Directory Structure**
```bash
myapp/
├── docker-compose.yml
├── Dockerfile
├── .env
├── .env.example
├── .dockerignore
├── app/
│   ├── package.json
│   ├── server.js
│   └── ...
├── nginx/
│   └── nginx.conf
└── database/
    └── init.sql
```

---

## **3. docker-compose.yml Structure**

### **File Format Versions**
```yaml
# Version 1 (Deprecated)
version: '1'
services:
  web:
    build: .

# Version 2.x (Adds networks, volumes, depends_on)
version: '2.4'
services:
  web:
    build: .
    networks:
      - frontend

# Version 3.x (Swarm mode compatible)
version: '3.9'
services:
  web:
    build: .
    deploy:
      replicas: 3
```

### **Complete YAML Structure**
```yaml
version: '3.9'  # Use latest stable version

# Services (containers)
services:
  # Service name
  web:
    # Build configuration
    build:
      context: ./web          # Build context directory
      dockerfile: Dockerfile   # Custom Dockerfile name
      args:
        NODE_ENV: production   # Build arguments
      target: builder          # Multi-stage build target
      cache_from:
        - nginx:alpine        # Cache sources
    
    # Image (alternative to build)
    image: nginx:alpine
    
    # Container configuration
    container_name: myapp-web
    restart: unless-stopped
    hostname: web.local
    
    # Port mapping
    ports:
      - "8080:80"              # HOST:CONTAINER
      - "8443:443"
    
    # Environment variables
    environment:
      - NODE_ENV=production
      - DB_HOST=database
      - DB_PORT=5432
    
    # Environment file
    env_file:
      - .env
      - ./config/app.env
    
    # Volumes
    volumes:
      - ./src:/app/src         # Bind mount
      - web-data:/app/data     # Named volume
      - /app/node_modules      # Anonymous volume
    
    # Networks
    networks:
      - frontend
      - backend
        ipv4_address: 172.20.0.10  # Static IP
    
    # Dependencies
    depends_on:
      database:
        condition: service_healthy
      redis:
        condition: service_started
    
    # Health check
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    
    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    
    # Security
    security_opt:
      - no-new-privileges:true
    
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    
    # User
    user: "1000:1000"
    
    # Working directory
    working_dir: /app
    
    # Entrypoint and command
    entrypoint: ["docker-entrypoint.sh"]
    command: ["node", "server.js"]
    
    # Labels
    labels:
      - "com.example.description=Web Application"
      - "com.example.department=IT"
    
    # Logging
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    
    # Extra hosts (DNS entries)
    extra_hosts:
      - "host.docker.internal:host-gateway"
      - "api.local:192.168.1.100"
    
    # DNS
    dns:
      - 8.8.8.8
      - 8.8.4.4
    
    # Sysctls
    sysctls:
      - net.core.somaxconn=1024
    
    # Stop signal
    stop_signal: SIGTERM
    stop_grace_period: 30s
    
    # Init process
    init: true
    
    # Read-only root filesystem
    read_only: true
    tmpfs:
      - /tmp
      - /run

  database:
    image: postgres:15-alpine
    container_name: myapp-db
    
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    
    volumes:
      - db-data:/var/lib/postgresql/data
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql
    
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
    
    command: redis-server --appendonly yes
    
    volumes:
      - redis-data:/data
    
    networks:
      - backend

# Networks
networks:
  frontend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
          gateway: 172.20.0.1
  
  backend:
    driver: bridge
    internal: true  # No external access

# Volumes
volumes:
  web-data:
    driver: local
    driver_opts:
      type: none
      device: /data/web
      o: bind
  
  db-data:
  
  redis-data:

# Configs (Swarm mode)
configs:
  nginx_config:
    file: ./nginx/nginx.conf

# Secrets (Swarm mode)
secrets:
  db_password:
    file: ./secrets/db_password.txt
```

---

## **4. Core Concepts**

### **Services**
- Each service represents a container
- Can be built from Dockerfile or pulled from registry
- Services can scale horizontally

### **Networks**
- Services communicate through networks
- Automatic DNS resolution using service names
- Network isolation between service groups

### **Volumes**
- Persistent data storage
- Shared data between containers
- Bind mounts for development

### **Environment Variables**
- Configure services without hardcoding
- Support for .env files
- Variable substitution

### **Dependencies**
- Control startup order with `depends_on`
- Wait for health conditions
- Service orchestration

### **Profiles**
- Enable/disable services based on environment
- Development vs production configurations

---

## **5. Basic Examples**

### **Example 1: Simple Web Application**
```yaml
# docker-compose.yml
version: '3.9'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
    volumes:
      - .:/app
      - /app/node_modules
```

**Project structure:**
```bash
simple-app/
├── docker-compose.yml
├── Dockerfile
├── package.json
└── index.js
```

**Dockerfile:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

**Run:**
```bash
docker-compose up
```

---

### **Example 2: WordPress with MySQL**
```yaml
version: '3.9'

services:
  wordpress:
    image: wordpress:latest
    container_name: wp-app
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wp-data:/var/www/html
    networks:
      - wp-network
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: mysql:8.0
    container_name: wp-db
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
      MYSQL_ROOT_PASSWORD: rootpassword
    volumes:
      - db-data:/var/lib/mysql
    networks:
      - wp-network
    restart: unless-stopped

volumes:
  wp-data:
  db-data:

networks:
  wp-network:
```

**Run:**
```bash
# Start WordPress
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## **6. Intermediate Examples**

### **Example 3: Full Stack with Node.js + React + MongoDB**

```yaml
version: '3.9'

services:
  # MongoDB Database
  mongodb:
    image: mongo:6.0
    container_name: app-mongodb
    restart: unless-stopped
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_ROOT_USER}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_ROOT_PASSWORD}
      MONGO_INITDB_DATABASE: ${MONGO_DB}
    volumes:
      - mongo-data:/data/db
      - ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro
    networks:
      - backend
    healthcheck:
      test: echo 'db.runCommand("ping").ok' | mongosh localhost:27017/test --quiet
      interval: 10s
      timeout: 10s
      retries: 5
      start_period: 40s

  # Node.js Backend API
  api:
    build:
      context: ./backend
      target: development
    container_name: app-api
    restart: unless-stopped
    environment:
      - NODE_ENV=development
      - PORT=3000
      - DB_HOST=mongodb
      - DB_PORT=27017
      - DB_NAME=${MONGO_DB}
      - DB_USER=${MONGO_ROOT_USER}
      - DB_PASS=${MONGO_ROOT_PASSWORD}
      - JWT_SECRET=${JWT_SECRET}
    volumes:
      - ./backend:/app
      - /app/node_modules
    ports:
      - "3000:3000"
      - "9229:9229" # Debug port
    networks:
      - backend
      - frontend
    depends_on:
      mongodb:
        condition: service_healthy
    command: npm run dev

  # React Frontend
  frontend:
    build:
      context: ./frontend
      target: development
    container_name: app-frontend
    restart: unless-stopped
    environment:
      - REACT_APP_API_URL=http://localhost:3000
      - CHOKIDAR_USEPOLLING=true # For hot reload in Docker
    volumes:
      - ./frontend:/app
      - /app/node_modules
    ports:
      - "80:3000"
    networks:
      - frontend
    depends_on:
      - api
    command: npm start

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    container_name: app-nginx
    restart: unless-stopped
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/sites:/etc/nginx/sites-enabled:ro
    ports:
      - "8080:80"
      - "8443:443"
    networks:
      - frontend
    depends_on:
      - frontend
      - api

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: app-redis
    restart: unless-stopped
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

  # Redis Commander (Admin UI)
  redis-commander:
    image: rediscommander/redis-commander:latest
    container_name: app-redis-commander
    restart: unless-stopped
    environment:
      - REDIS_HOSTS=local:redis:6379
    ports:
      - "8081:8081"
    networks:
      - backend
    depends_on:
      redis:
        condition: service_healthy

  # Mongo Express (Admin UI)
  mongo-express:
    image: mongo-express:latest
    container_name: app-mongo-express
    restart: unless-stopped
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=${MONGO_ROOT_USER}
      - ME_CONFIG_MONGODB_ADMINPASSWORD=${MONGO_ROOT_PASSWORD}
      - ME_CONFIG_MONGODB_SERVER=mongodb
      - ME_CONFIG_BASICAUTH_USERNAME=admin
      - ME_CONFIG_BASICAUTH_PASSWORD=admin123
    ports:
      - "8082:8081"
    networks:
      - backend
    depends_on:
      mongodb:
        condition: service_healthy

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # Backend not accessible from host

volumes:
  mongo-data:
  redis-data:
```

**.env file:**
```bash
# Database
MONGO_ROOT_USER=admin
MONGO_ROOT_PASSWORD=SecurePassword123!
MONGO_DB=myapp

# JWT
JWT_SECRET=your-super-secret-jwt-key-change-this
```

---

### **Example 4: Microservices with Message Queue**

```yaml
version: '3.9'

services:
  # RabbitMQ Message Broker
  rabbitmq:
    image: rabbitmq:3-management-alpine
    container_name: ms-rabbitmq
    environment:
      RABBITMQ_DEFAULT_USER: admin
      RABBITMQ_DEFAULT_PASS: admin
      RABBITMQ_DEFAULT_VHOST: /
    ports:
      - "5672:5672"   # AMQP protocol
      - "15672:15672" # Management UI
    volumes:
      - rabbitmq-data:/var/lib/rabbitmq
    networks:
      - message-bus
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "ping"]
      interval: 30s
      timeout: 10s
      retries: 5

  # User Service (Python)
  user-service:
    build:
      context: ./services/user
      dockerfile: Dockerfile
    container_name: ms-user
    environment:
      - SERVICE_NAME=user
      - PORT=5001
      - DB_HOST=postgres-user
      - DB_PORT=5432
      - DB_NAME=userdb
      - DB_USER=postgres
      - DB_PASSWORD=postgres
      - RABBITMQ_HOST=rabbitmq
      - RABBITMQ_PORT=5672
    ports:
      - "5001:5001"
    volumes:
      - ./services/user:/app
    networks:
      - message-bus
      - user-db
    depends_on:
      rabbitmq:
        condition: service_healthy
      postgres-user:
        condition: service_healthy

  # Order Service (Node.js)
  order-service:
    build:
      context: ./services/order
      dockerfile: Dockerfile
    container_name: ms-order
    environment:
      - NODE_ENV=production
      - PORT=5002
      - DB_HOST=postgres-order
      - DB_PORT=5432
      - DB_NAME=orderdb
      - DB_USER=postgres
      - DB_PASSWORD=postgres
      - RABBITMQ_HOST=rabbitmq
      - RABBITMQ_PORT=5672
    ports:
      - "5002:5002"
    volumes:
      - ./services/order:/app
    networks:
      - message-bus
      - order-db
    depends_on:
      rabbitmq:
        condition: service_healthy
      postgres-order:
        condition: service_healthy

  # Payment Service (Go)
  payment-service:
    build:
      context: ./services/payment
      dockerfile: Dockerfile
    container_name: ms-payment
    environment:
      - PORT=5003
      - DB_HOST=postgres-payment
      - DB_PORT=5432
      - DB_NAME=paymentdb
      - DB_USER=postgres
      - DB_PASSWORD=postgres
      - RABBITMQ_HOST=rabbitmq
      - RABBITMQ_PORT=5672
    ports:
      - "5003:5003"
    volumes:
      - ./services/payment:/app
    networks:
      - message-bus
      - payment-db
    depends_on:
      rabbitmq:
        condition: service_healthy
      postgres-payment:
        condition: service_healthy

  # API Gateway
  gateway:
    build:
      context: ./gateway
      dockerfile: Dockerfile
    container_name: ms-gateway
    environment:
      - PORT=8000
      - USER_SERVICE_URL=http://user-service:5001
      - ORDER_SERVICE_URL=http://order-service:5002
      - PAYMENT_SERVICE_URL=http://payment-service:5003
    ports:
      - "8000:8000"
    networks:
      - message-bus
    depends_on:
      - user-service
      - order-service
      - payment-service

  # User Database (PostgreSQL)
  postgres-user:
    image: postgres:15-alpine
    container_name: ms-postgres-user
    environment:
      POSTGRES_DB: userdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres-user-data:/var/lib/postgresql/data
      - ./services/user/init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - user-db
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Order Database
  postgres-order:
    image: postgres:15-alpine
    container_name: ms-postgres-order
    environment:
      POSTGRES_DB: orderdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres-order-data:/var/lib/postgresql/data
    networks:
      - order-db
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Payment Database
  postgres-payment:
    image: postgres:15-alpine
    container_name: ms-postgres-payment
    environment:
      POSTGRES_DB: paymentdb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres-payment-data:/var/lib/postgresql/data
    networks:
      - payment-db
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Prometheus Monitoring
  prometheus:
    image: prom/prometheus:latest
    container_name: ms-prometheus
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    ports:
      - "9090:9090"
    networks:
      - monitoring

  # Grafana Dashboard
  grafana:
    image: grafana/grafana:latest
    container_name: ms-grafana
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_INSTALL_PLUGINS=grafana-piechart-panel
    volumes:
      - grafana-data:/var/lib/grafana
      - ./monitoring/grafana/dashboards:/etc/grafana/provisioning/dashboards
    ports:
      - "3000:3000"
    networks:
      - monitoring
    depends_on:
      - prometheus

networks:
  message-bus:
    driver: bridge
  user-db:
    driver: bridge
    internal: true
  order-db:
    driver: bridge
    internal: true
  payment-db:
    driver: bridge
    internal: true
  monitoring:
    driver: bridge

volumes:
  rabbitmq-data:
  postgres-user-data:
  postgres-order-data:
  postgres-payment-data:
  prometheus-data:
  grafana-data:
```

---

## **7. Advanced Production Examples**

### **Example 5: Production-Ready Stack with Load Balancing**

```yaml
version: '3.9'

services:
  # Load Balancer (Traefik)
  traefik:
    image: traefik:v2.10
    container_name: prod-traefik
    command:
      # Enable Docker provider
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      # Entrypoints
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      # Let's Encrypt
      - "--certificatesresolvers.letsencrypt.acme.email=admin@example.com"
      - "--certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json"
      - "--certificatesresolvers.letsencrypt.acme.httpchallenge=true"
      - "--certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=web"
      # Enable API and Dashboard
      - "--api.insecure=true"
      - "--api.dashboard=true"
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080" # Dashboard
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "traefik-data:/letsencrypt"
    networks:
      - public
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dashboard.rule=Host(`traefik.example.com`)"
      - "traefik.http.routers.dashboard.service=api@internal"
    restart: unless-stopped

  # Web Application (Scalable)
  web:
    build:
      context: ./web
      dockerfile: Dockerfile.prod
    image: ${REGISTRY:-local}/web:${TAG:-latest}
    container_name: prod-web
    environment:
      - NODE_ENV=production
      - DB_HOST=database
      - DB_PORT=5432
      - DB_NAME=${DB_NAME}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - API_URL=https://api.example.com
    volumes:
      - web-static:/app/static
      - web-media:/app/media
    networks:
      - public
      - private
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web.rule=Host(`example.com`) || Host(`www.example.com`)"
      - "traefik.http.routers.web.entrypoints=websecure"
      - "traefik.http.routers.web.tls.certresolver=letsencrypt"
      - "traefik.http.services.web.loadbalancer.server.port=3000"
      - "traefik.http.middlewares.web-compress.compress=true"
      - "traefik.http.routers.web.middlewares=web-compress"
    deploy:
      mode: replicated
      replicas: 3
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first
      rollback_config:
        parallelism: 1
        delay: 10s
        order: stop-first
      restart_policy:
        condition: any
        delay: 5s
        max_attempts: 3
        window: 120s
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # API Backend
  api:
    build:
      context: ./api
      dockerfile: Dockerfile.prod
    image: ${REGISTRY:-local}/api:${TAG:-latest}
    container_name: prod-api
    environment:
      - NODE_ENV=production
      - PORT=4000
      - DB_HOST=database
      - DB_PORT=5432
      - DB_NAME=${DB_NAME}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - JWT_SECRET=${JWT_SECRET}
    networks:
      - private
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.api.rule=Host(`api.example.com`)"
      - "traefik.http.routers.api.entrypoints=websecure"
      - "traefik.http.routers.api.tls.certresolver=letsencrypt"
      - "traefik.http.services.api.loadbalancer.server.port=4000"
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '1'
          memory: 1G
    depends_on:
      database:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:4000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Database (PostgreSQL with replication)
  database:
    image: postgres:15-alpine
    container_name: prod-database
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_REPLICATION_USER: replicator
      POSTGRES_REPLICATION_PASSWORD: ${REPLICATION_PASSWORD}
    volumes:
      - db-data:/var/lib/postgresql/data
      - ./database/postgresql.conf:/etc/postgresql/postgresql.conf:ro
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - private
    command: postgres -c config_file=/etc/postgresql/postgresql.conf
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          memory: 1G

  # Database Replica
  database-replica:
    image: postgres:15-alpine
    container_name: prod-database-replica
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - db-replica-data:/var/lib/postgresql/data
    networks:
      - private
    command: |
      bash -c "
      until pg_basebackup --host=database --username=replicator --pgdata=/var/lib/postgresql/data --wal-method=stream --write-recovery-conf
      do
        echo 'Waiting for primary database...'
        sleep 2
      done
      echo 'host replication all 0.0.0.0/0 md5' >> /var/lib/postgresql/data/pg_hba.conf
      postgres
      "
    depends_on:
      database:
        condition: service_healthy
    deploy:
      replicas: 2

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: prod-redis
    command: redis-server --appendonly yes --maxmemory 512mb --maxmemory-policy allkeys-lru
    volumes:
      - redis-data:/data
    networks:
      - private
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

  # Redis Sentinel (for HA)
  redis-sentinel:
    image: redis:7-alpine
    container_name: prod-redis-sentinel
    command: redis-sentinel /etc/redis/sentinel.conf
    volumes:
      - ./redis/sentinel.conf:/etc/redis/sentinel.conf:ro
    networks:
      - private
    depends_on:
      - redis
    deploy:
      replicas: 3

  # Elasticsearch for logging
  elasticsearch:
    image: elasticsearch:8.11.0
    container_name: prod-elasticsearch
    environment:
      - discovery.type=single-node
      - ES_JAVA_OPTS=-Xms1g -Xmx1g
      - xpack.security.enabled=false
    volumes:
      - elasticsearch-data:/usr/share/elasticsearch/data
    networks:
      - logging
    deploy:
      resources:
        limits:
          memory: 2G

  # Logstash
  logstash:
    image: logstash:8.11.0
    container_name: prod-logstash
    volumes:
      - ./logstash/logstash.conf:/usr/share/logstash/pipeline/logstash.conf:ro
    networks:
      - logging
      - private
    depends_on:
      - elasticsearch

  # Kibana
  kibana:
    image: kibana:8.11.0
    container_name: prod-kibana
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    networks:
      - logging
      - public
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.kibana.rule=Host(`logs.example.com`)"
      - "traefik.http.routers.kibana.entrypoints=websecure"
      - "traefik.http.routers.kibana.tls.certresolver=letsencrypt"
      - "traefik.http.services.kibana.loadbalancer.server.port=5601"
    depends_on:
      - elasticsearch

  # Prometheus
  prometheus:
    image: prom/prometheus:latest
    container_name: prod-prometheus
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/usr/share/prometheus/console_libraries'
      - '--web.console.templates=/usr/share/prometheus/consoles'
    networks:
      - monitoring
      - private
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.prometheus.rule=Host(`monitor.example.com`) && PathPrefix(`/prometheus`)"
      - "traefik.http.routers.prometheus.entrypoints=websecure"
      - "traefik.http.routers.prometheus.tls.certresolver=letsencrypt"
      - "traefik.http.services.prometheus.loadbalancer.server.port=9090"

  # Grafana
  grafana:
    image: grafana/grafana:latest
    container_name: prod-grafana
    environment:
      - GF_SECURITY_ADMIN_USER=${GRAFANA_ADMIN_USER:-admin}
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD:-admin}
      - GF_INSTALL_PLUGINS=grafana-piechart-panel
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
      - ./grafana/datasources:/etc/grafana/provisioning/datasources
    networks:
      - monitoring
      - public
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.grafana.rule=Host(`monitor.example.com`)"
      - "traefik.http.routers.grafana.entrypoints=websecure"
      - "traefik.http.routers.grafana.tls.certresolver=letsencrypt"
      - "traefik.http.services.grafana.loadbalancer.server.port=3000"
    depends_on:
      - prometheus

  # Backup Service
  backup:
    image: alpine:latest
    container_name: prod-backup
    volumes:
      - db-data:/backup/database:ro
      - web-media:/backup/media:ro
      - ./backup-scripts:/scripts:ro
      - backup-data:/backups
    networks:
      - private
    entrypoint: |
      sh -c "
      apk add --no-cache postgresql-client
      while true; do
        /scripts/backup.sh
        sleep 86400
      done
      "
    depends_on:
      - database

networks:
  public:
    driver: bridge
  private:
    driver: bridge
    internal: true
  logging:
    driver: bridge
  monitoring:
    driver: bridge

volumes:
  db-data:
    driver: local
  db-replica-data:
    driver: local
  redis-data:
    driver: local
  elasticsearch-data:
    driver: local
  prometheus-data:
    driver: local
  grafana-data:
    driver: local
  traefik-data:
    driver: local
  web-static:
    driver: local
  web-media:
    driver: local
  backup-data:
    driver: local
```

---

## **8. Docker Compose Commands**

### **Basic Commands**
```bash
# Start services
docker-compose up                     # Start in foreground
docker-compose up -d                  # Start in background (detached)
docker-compose up --build              # Rebuild images before starting
docker-compose up --scale web=3        # Scale web service to 3 instances

# Stop services
docker-compose down                    # Stop and remove containers
docker-compose down -v                  # Also remove volumes
docker-compose down --rmi all            # Also remove images

# Restart
docker-compose restart                  # Restart all services
docker-compose restart web               # Restart specific service

# View status
docker-compose ps                       # List containers
docker-compose ps -a                     # Include stopped containers

# Logs
docker-compose logs                     # View logs
docker-compose logs -f                   # Follow logs
docker-compose logs --tail=100 web       # Last 100 lines of web service
docker-compose logs -f --no-color        # No color output

# Execute commands
docker-compose exec web bash            # Run bash in web service
docker-compose exec -T web npm test      # Run test (no TTY)
docker-compose run web npm install       # Run one-off command
docker-compose run --rm web npm test     # Remove after run

# Build images
docker-compose build                     # Build all services
docker-compose build --no-cache web      # Build web without cache
docker-compose build --pull               # Pull base images

# Pull images
docker-compose pull                       # Pull all service images
docker-compose pull web                    # Pull specific service image

# Push images
docker-compose push                       # Push all service images
docker-compose push web                    # Push specific service image

# Configuration
docker-compose config                     # Validate and view config
docker-compose config --services           # List services
docker-compose config --volumes             # List volumes

# Images and containers
docker-compose images                      # List images used
docker-compose top                          # Show running processes

# Events
docker-compose events                      # Stream container events
docker-compose events --json                # JSON format

# Port
docker-compose port web 3000               # Show public port mapping

# Kill
docker-compose kill                         # Kill containers
docker-compose kill -s SIGINT web           # Send specific signal

# Pause/Unpause
docker-compose pause                        # Pause all services
docker-compose unpause                       # Unpause all services

# Create (without starting)
docker-compose create                       # Create containers only

# Start/Stop specific services
docker-compose start web                    # Start specific service
docker-compose stop web                      # Stop specific service
docker-compose restart web                    # Restart specific service
docker-compose rm web                         # Remove specific service

# Scale
docker-compose up --scale web=5              # Scale web to 5 instances
```

### **Advanced Commands**
```bash
# Copy files to/from container
docker-compose cp web:/app/logs ./logs       # Copy from container
docker-compose cp ./config web:/app/config   # Copy to container

# Version info
docker-compose version                        # Show version

# Help
docker-compose --help                          # General help
docker-compose COMMAND --help                   # Command-specific help

# With project name
docker-compose -p myproject up                 # Specify project name
docker-compose -f docker-compose.prod.yml up   # Use specific compose file

# Multiple compose files
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

# Environment override
docker-compose -f docker-compose.yml -f docker-compose.override.yml up

# With profiles
docker-compose --profile debug up              # Start services with profile
docker-compose --profile all up                 # Start all profiles
```

---

## **9. Environment Variables & Configuration**

### **Variable Substitution**
```yaml
# docker-compose.yml
version: '3.9'

services:
  web:
    image: ${IMAGE_NAME:-nginx}:${TAG:-latest}
    ports:
      - "${HOST_PORT:-8080}:80"
    environment:
      - NODE_ENV=${NODE_ENV:-development}
      - DATABASE_URL=postgres://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
```

### **.env File**
```bash
# .env file - loaded automatically
PROJECT_NAME=myapp
IMAGE_NAME=myapp/web
TAG=1.0.0
HOST_PORT=8080
NODE_ENV=production

# Database
DB_HOST=database
DB_PORT=5432
DB_NAME=myapp
DB_USER=postgres
DB_PASSWORD=SuperSecretPassword123!

# API Keys
STRIPE_KEY=sk_test_...
AWS_ACCESS_KEY=AKIA...
```

### **Environment File Options**
```yaml
services:
  web:
    # Method 1: Direct environment variables
    environment:
      - NODE_ENV=production
      - DEBUG=false
    
    # Method 2: From .env file
    env_file:
      - .env
      - ./config/app.env
    
    # Method 3: From variable substitution
    environment:
      - DATABASE_URL=postgres://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
```

### **Multiple Environment Configurations**
```yaml
# docker-compose.override.yml (development)
version: '3.9'

services:
  web:
    build:
      context: .
      target: development
    volumes:
      - .:/app
    environment:
      - NODE_ENV=development
    command: npm run dev
```

```yaml
# docker-compose.prod.yml (production)
version: '3.9'

services:
  web:
    build:
      context: .
      target: production
    image: registry.example.com/web:latest
    environment:
      - NODE_ENV=production
    restart: always
    deploy:
      replicas: 3
```

**Usage:**
```bash
# Development
docker-compose up

# Production
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

---

## **10. Networking in Compose**

### **Default Network Behavior**
```yaml
version: '3.9'

services:
  web:
    image: nginx
    # Automatically connected to default network
    # Can reach 'db' by hostname
    environment:
      - DB_HOST=db

  db:
    image: postgres
    # Can reach 'web' by hostname
```

### **Custom Networks**
```yaml
version: '3.9'

services:
  proxy:
    image: nginx
    networks:
      - public

  web:
    image: webapp
    networks:
      - public
      - private

  api:
    image: api
    networks:
      - private
      - database

  database:
    image: postgres
    networks:
      - database

networks:
  public:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
          gateway: 172.20.0.1
  
  private:
    driver: bridge
    internal: true  # No external access
  
  database:
    driver: bridge
    internal: true
```

### **Static IP Assignment**
```yaml
version: '3.9'

services:
  web:
    image: nginx
    networks:
      frontend:
        ipv4_address: 172.20.0.10
        ipv6_address: 2001:db8::10

networks:
  frontend:
    driver: bridge
    enable_ipv6: true
    ipam:
      config:
        - subnet: 172.20.0.0/24
          gateway: 172.20.0.1
        - subnet: 2001:db8::/64
          gateway: 2001:db8::1
```

### **Network Aliases**
```yaml
version: '3.9'

services:
  web:
    image: nginx
    networks:
      frontend:
        aliases:
          - webserver
          - app.local

  api:
    image: api
    networks:
      frontend:
        aliases:
          - api.local
      backend:
        aliases:
          - data-processor

networks:
  frontend:
  backend:
```

### **External Networks**
```yaml
version: '3.9'

services:
  web:
    image: nginx
    networks:
      - existing-network

networks:
  existing-network:
    external: true
    name: my-pre-existing-network  # Docker network must exist
```

---

## **11. Volumes & Data Persistence**

### **Volume Types**
```yaml
version: '3.9'

services:
  web:
    image: nginx
    volumes:
      # Named volume
      - web-data:/var/www/html
      
      # Bind mount (host path)
      - ./src:/app/src
      
      # Anonymous volume
      - /app/node_modules
      
      # Read-only volume
      - ./config:/app/config:ro
      
      # Volume with subpath
      - type: volume
        source: web-data
        target: /data
        volume:
          nocopy: true

volumes:
  # Named volume
  web-data:
    driver: local
    driver_opts:
      type: nfs
      o: addr=10.0.0.10,nolock,soft,rw
      device: :/path/to/dir
  
  # External volume
  existing-data:
    external: true
    name: my-existing-volume
```

### **Bind Mounts with SELinux**
```yaml
services:
  web:
    image: nginx
    volumes:
      # SELinux context
      - ./html:/usr/share/nginx/html:z  # Shared
      - ./logs:/var/log/nginx:Z          # Private
```

### **Volume Backup Strategy**
```yaml
# docker-compose.yml with backup service
services:
  database:
    image: postgres
    volumes:
      - db-data:/var/lib/postgresql/data

  backup:
    image: alpine
    volumes:
      - db-data:/backup/source:ro
      - ./backups:/backup/destination
    command: |
      sh -c "
      apk add --no-cache postgresql-client
      while true; do
        pg_dump -h database -U postgres mydb > /backup/destination/db-$(date +%Y%m%d).sql
        sleep 86400
      done
      "
    depends_on:
      - database
```

### **Volume Cleanup**
```bash
# List volumes
docker volume ls

# Remove unused volumes
docker volume prune
docker volume prune -f  # Force without confirmation

# Remove specific volume
docker volume rm volume_name

# Remove volume with compose
docker-compose down -v
```

---

## **12. Health Checks & Dependencies**

### **Service Health Checks**
```yaml
services:
  database:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 40s

  web:
    image: webapp
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

  redis:
    image: redis:7
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3
```

### **Dependency Conditions**
```yaml
services:
  web:
    build: .
    depends_on:
      database:
        condition: service_healthy
      redis:
        condition: service_healthy
      cache:
        condition: service_started
      init:
        condition: service_completed_successfully

  database:
    image: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis

  cache:
    image: memcached

  init:
    image: alpine
    command: ["sh", "-c", "echo 'Initializing...' && sleep 5"]
```

### **Wait-for-it Script**
```yaml
services:
  web:
    image: webapp
    entrypoint: >
      sh -c "
      ./wait-for-it.sh database:5432 -t 60 &&
      ./wait-for-it.sh redis:6379 -t 30 &&
      npm start
      "
    depends_on:
      - database
      - redis
```

**wait-for-it.sh:**
```bash
#!/bin/sh
# wait-for-it.sh

TIMEOUT=15
QUIET=0

echo "Waiting for $1..."

while ! nc -z $1 2>/dev/null; do
  sleep 1
done

echo "Connection to $1 established!"
```

---

## **13. Profiles & Extends**

### **Service Profiles**
```yaml
version: '3.9'

services:
  web:
    image: nginx
    profiles:
      - frontend
      - all

  api:
    image: api
    profiles:
      - backend
      - all

  database:
    image: postgres
    # No profile - always started

  adminer:
    image: adminer
    profiles:
      - debug
      - tools

  redis-commander:
    image: rediscommander/redis-commander
    profiles:
      - debug
      - tools
      - all
```

**Usage:**
```bash
# Start only default services (database)
docker-compose up

# Start with profile
docker-compose --profile frontend up
docker-compose --profile debug up

# Start multiple profiles
docker-compose --profile frontend --profile backend up

# Start all profiles
docker-compose --profile '*' up
```

### **Extends (Inheritance)**
```yaml
# docker-compose.base.yml
version: '3.9'

services:
  web-base:
    image: nginx:alpine
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: "10m"
    networks:
      - default
```

```yaml
# docker-compose.yml
version: '3.9'

services:
  web-dev:
    extends:
      file: docker-compose.base.yml
      service: web-base
    ports:
      - "8080:80"
    volumes:
      - ./src:/usr/share/nginx/html:ro

  web-prod:
    extends:
      file: docker-compose.base.yml
      service: web-base
    ports:
      - "80:80"
    deploy:
      replicas: 3
```

### **YAML Anchors (Reusability)**
```yaml
version: '3.9'

x-logging: &default-logging
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"

x-resources: &default-resources
  limits:
    cpus: '0.5'
    memory: 512M
  reservations:
    cpus: '0.25'
    memory: 256M

services:
  web:
    image: nginx
    logging: *default-logging
    deploy:
      resources: *default-resources

  api:
    image: api
    logging: *default-logging
    deploy:
      resources: *default-resources

  database:
    image: postgres
    logging: *default-logging
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
```

---

## **14. Monitoring & Debugging**

### **Logging Configuration**
```yaml
services:
  web:
    image: nginx
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        tag: "{{.ImageName}}|{{.Name}}|{{.ID}}"

  api:
    image: api
    logging:
      driver: "syslog"
      options:
        syslog-address: "tcp://logs.example.com:514"
        tag: "api"

  app:
    image: app
    logging:
      driver: "fluentd"
      options:
        fluentd-address: "localhost:24224"
        tag: "app.{{.Name}}"
```

### **Debugging with netshoot**
```yaml
services:
  web:
    image: nginx
    networks:
      - app-network

  debug:
    image: nicolaka/netshoot
    command: sleep infinity
    networks:
      - app-network
    profiles:
      - debug

networks:
  app-network:
```

**Usage:**
```bash
# Start debug container
docker-compose --profile debug up -d

# Attach to debug container
docker-compose exec debug bash

# Inside debug container
ping web
tcpdump -i eth0
nslookup database
curl http://web:80
```

### **Resource Monitoring**
```bash
# View container stats
docker-compose top
docker stats $(docker-compose ps -q)

# Check logs
docker-compose logs -f --tail=100 web

# Inspect container
docker inspect $(docker-compose ps -q web)

# Check resource usage
docker-compose exec web ps aux
docker-compose exec web free -m
docker-compose exec web df -h
```

---

## **15. Best Practices**

### **1. Version Control**
```yaml
# ✅ Always specify version
version: '3.9'

# ❌ Don't omit version
services:
  web:
    image: nginx
```

### **2. Image Tags**
```yaml
# ✅ Use specific tags
image: postgres:15.2-alpine

# ❌ Avoid 'latest' in production
image: postgres:latest
```

### **3. Resource Limits**
```yaml
# ✅ Always set resource limits
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M

# ❌ Don't leave unlimited
services:
  web:
    image: nginx
```

### **4. Health Checks**
```yaml
# ✅ Add health checks
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3

# ❌ Don't skip health checks
services:
  web:
    image: nginx
```

### **5. Security**
```yaml
# ✅ Run as non-root
services:
  web:
    user: "1000:1000"
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE

# ❌ Avoid root containers
services:
  web:
    image: nginx
```

### **6. Environment Variables**
```yaml
# ✅ Use env_file for secrets
services:
  web:
    env_file:
      - .env

# ❌ Don't hardcode secrets
services:
  web:
    environment:
      - DB_PASSWORD=password123
```

### **7. Volume Management**
```yaml
# ✅ Use named volumes for data
services:
  database:
    volumes:
      - db-data:/var/lib/postgresql/data

# ❌ Avoid anonymous volumes for important data
services:
  database:
    volumes:
      - /var/lib/postgresql/data
```

### **8. Restart Policies**
```yaml
# ✅ Appropriate restart policy
services:
  web:
    restart: unless-stopped  # For daemons
  job:
    restart: on-failure:5     # For batch jobs

# ❌ Avoid 'always' for batch jobs
services:
  batch:
    restart: always
```

### **9. Network Isolation**
```yaml
# ✅ Isolate backend services
services:
  web:
    networks:
      - public
  database:
    networks:
      - private

networks:
  public:
  private:
    internal: true
```

### **10. Configuration Validation**
```bash
# ✅ Validate before deploying
docker-compose config > /dev/null && echo "Valid"

# ❌ Don't deploy without validation
docker-compose up -d
```

---

## **16. Troubleshooting Guide**

### **Common Issues and Solutions**

#### **Issue 1: Port Already in Use**
```bash
# Error: Bind for 0.0.0.0:8080 failed: port is already allocated

# Solution 1: Find and stop process using port
sudo lsof -i :8080
sudo kill -9 <PID>

# Solution 2: Change port in docker-compose.yml
ports:
  - "8081:80"  # Use different host port

# Solution 3: Stop conflicting container
docker stop $(docker ps -q --filter publish=8080)
```

#### **Issue 2: Volume Permission Errors**
```yaml
# Error: Permission denied when writing to volume

# Solution 1: Set correct user in container
services:
  web:
    user: "${UID:-1000}:${GID:-1000}"

# Solution 2: Fix host directory permissions
sudo chown -R $USER:$USER ./data
sudo chmod -R 755 ./data

# Solution 3: Use named volumes instead
volumes:
  - app-data:/app/data
```

#### **Issue 3: Container Exit Immediately**
```bash
# Container exits right after starting

# Debug: Check logs
docker-compose logs service-name

# Debug: Run with different entrypoint
docker-compose run --entrypoint sh service-name

# Common fixes:
# - Check if command exists
# - Verify environment variables
# - Ensure dependencies are running
```

#### **Issue 4: Network Connectivity**
```bash
# Services can't communicate

# Check network configuration
docker-compose ps
docker network ls
docker network inspect project_default

# Test connectivity
docker-compose exec web ping database
docker-compose exec web nslookup database

# Fix: Ensure services on same network
services:
  web:
    networks:
      - app-network
  database:
    networks:
      - app-network
```

#### **Issue 5: Build Failures**
```bash
# Docker build fails

# Rebuild with no cache
docker-compose build --no-cache service-name

# Check build logs
docker-compose up --build service-name

# Common fixes:
# - Check Dockerfile syntax
# - Verify build context
# - Ensure base images are accessible
```

#### **Issue 6: Environment Variables Not Loading**
```bash
# Variables not available in container

# Check .env file exists
ls -la .env

# Verify variables are passed
docker-compose config | grep -A 5 environment

# Test in container
docker-compose exec web env | grep VARIABLE

# Fix: Use env_file or explicit environment
services:
  web:
    env_file:
      - .env
    environment:
      - VARIABLE=${VARIABLE}
```

#### **Issue 7: Database Connection Refused**
```yaml
# Error: Connection refused to database

# Solution 1: Add depends_on with healthcheck
services:
  web:
    depends_on:
      database:
        condition: service_healthy

# Solution 2: Wait for database in application
# Add retry logic to application code

# Solution 3: Use wait-for-it script
command: ["./wait-for-it.sh", "database:5432", "--", "npm", "start"]
```

#### **Issue 8: Out of Disk Space**
```bash
# Docker runs out of disk space

# Clean up unused resources
docker system prune -a
docker volume prune
docker image prune -a

# Check disk usage
docker system df

# Limit log size
services:
  web:
    logging:
      options:
        max-size: "10m"
        max-file: "3"
```

### **Debugging Commands Cheat Sheet**
```bash
# View all containers
docker-compose ps -a

# View logs
docker-compose logs -f --tail=100

# Check resource usage
docker stats $(docker-compose ps -q)

# Inspect a service
docker-compose exec service-name bash
docker inspect $(docker-compose ps -q service-name)

# Test network
docker-compose exec service-name ping other-service

# Check environment
docker-compose exec service-name env

# View mounted volumes
docker inspect -f '{{ .Mounts }}' container-name

# Check process list
docker-compose top

# View events
docker-compose events
```

### **Recovery Procedures**

#### **Backup and Restore Database**
```bash
# Backup PostgreSQL
docker-compose exec -T database pg_dump -U postgres dbname > backup.sql

# Restore PostgreSQL
cat backup.sql | docker-compose exec -T database psql -U postgres dbname

# Backup MySQL
docker-compose exec -T database mysqldump -u root -p dbname > backup.sql

# Restore MySQL
cat backup.sql | docker-compose exec -T database mysql -u root -p dbname
```

#### **Reset Everything**
```bash
# Stop and remove everything
docker-compose down -v --rmi all

# Clean system
docker system prune -a --volumes

# Rebuild and start
docker-compose up -d --build
```

---

## **Conclusion**

### **Key Takeaways**

1. **Docker Compose simplifies multi-container management** - Define everything in YAML, run with one command
2. **Environment-specific configurations** - Use multiple compose files and profiles
3. **Network isolation** - Control service communication with custom networks
4. **Data persistence** - Use volumes for important data
5. **Health checks** - Ensure services are truly ready
6. **Resource limits** - Prevent containers from consuming all resources
7. **Security** - Run as non-root, drop capabilities
8. **Monitoring** - Use logging and debugging tools

### **When to Use Docker Compose**

| Use Case | Recommended |
|----------|------------|
| Local development | ✅ Perfect |
| CI/CD testing | ✅ Great |
| Single-host production | ✅ Good |
| Multi-host production | ⚠️ Consider Swarm/K8s |
| Large-scale microservices | ⚠️ Consider orchestration tools |

### **Next Steps**

1. **Master Docker Compose commands**
2. **Learn Docker Swarm for multi-host orchestration**
3. **Explore Kubernetes for advanced orchestration**
4. **Implement CI/CD pipelines with Compose**
5. **Study production patterns and anti-patterns**

### **Resources**

- [Official Docker Compose Documentation](https://docs.docker.com/compose/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)
- [Docker Labs](https://github.com/docker/labs)
- [Awesome Compose](https://github.com/docker/awesome-compose)

### **Final Pro Tips**

```bash
# Always validate compose file
docker-compose config

# Use .env for environment-specific values
# Implement health checks for all services
# Set resource limits in production
# Use named volumes for persistent data
# Keep compose files in version control
# Document your compose file with comments
# Test rollback procedures regularly
```

This comprehensive guide covers everything from basic concepts to production-ready configurations. Docker Compose is an essential tool in any developer's toolkit, and mastering it will significantly improve your container workflow! 🐳