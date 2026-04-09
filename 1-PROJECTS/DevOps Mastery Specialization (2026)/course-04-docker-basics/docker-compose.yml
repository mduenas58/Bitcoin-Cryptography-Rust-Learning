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