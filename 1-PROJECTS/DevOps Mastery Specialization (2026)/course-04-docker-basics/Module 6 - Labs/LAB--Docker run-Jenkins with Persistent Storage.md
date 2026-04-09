# Docker Run Lab: Jenkins with Persistent Storage

## Lab Overview
In this lab, you'll learn how to use the `docker run` command to deploy a Jenkins container with persistent storage. You'll understand volume mounting, port mapping, and container management.

**Time Required:** 30-45 minutes  
**Prerequisites:** Docker installed on your system, basic command line knowledge

## Learning Objectives
By the end of this lab, you will be able to:
- Run a container using the `docker run` command
- Configure port mapping for container accessibility
- Implement persistent storage using Docker volumes
- Manage container lifecycle
- Access and verify Jenkins installation

## Lab Environment Setup

### Step 1: Verify Docker Installation
```bash
# Check Docker version
docker --version

# Verify Docker is running
docker info

# Check available disk space for volumes
df -h
```

### Step 2: Create Persistent Storage Directory
```bash
# Create a directory for Jenkins data on your host
mkdir -p ~/jenkins_home

# Set proper permissions (Linux/Mac)
chmod 777 ~/jenkins_home

# For Linux, you might need to set ownership
sudo chown -R 1000:1000 ~/jenkins_home
```

## Main Lab Exercises

### Exercise 1: Basic Jenkins Container Run

#### Step 1.1: Pull Jenkins Image
```bash
# Pull the official Jenkins LTS image
docker pull jenkins/jenkins:lts

# Verify the image is downloaded
docker images | grep jenkins
```

#### Step 1.2: Run Basic Container (Without Persistence)
```bash
# Run Jenkins container
docker run -d \
  --name jenkins-test \
  -p 8080:8080 \
  -p 50000:50000 \
  jenkins/jenkins:lts

# Check if container is running
docker ps

# View container logs
docker logs jenkins-test
```

#### Step 1.3: Access Jenkins
```bash
# Get the initial admin password
docker exec jenkins-test cat /var/jenkins_home/secrets/initialAdminPassword

# Access Jenkins in browser
echo "Open http://localhost:8080 in your browser"
```

### Exercise 2: Jenkins with Persistent Storage

#### Step 2.1: Remove Previous Container
```bash
# Stop and remove the test container
docker stop jenkins-test
docker rm jenkins-test
```

#### Step 2.2: Run with Volume Mounting
```bash
# Run Jenkins with persistent storage
docker run -d \
  --name jenkins-prod \
  -p 8080:8080 \
  -p 50000:50000 \
  -v ~/jenkins_home:/var/jenkins_home \
  -e JAVA_OPTS="-Djenkins.install.runSetupWizard=false" \
  jenkins/jenkins:lts

# Verify container is running
docker ps

# Check volume mounting
docker inspect jenkins-prod | grep -A 10 "Mounts"
```

#### Step 2.3: Verify Persistence
```bash
# List contents of mounted volume
ls -la ~/jenkins_home

# Create a test file in the container
docker exec jenkins-prod touch /var/jenkins_home/test-persistence.txt

# Verify file exists on host
ls -la ~/jenkins_home/test-persistence.txt
```

### Exercise 3: Advanced Configuration

#### Step 3.1: Run with Custom Network and Resource Limits
```bash
# Create a custom network
docker network create jenkins-network

# Run container with advanced options
docker run -d \
  --name jenkins-advanced \
  -p 8081:8080 \
  -p 50001:50000 \
  -v ~/jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --network jenkins-network \
  --memory="2g" \
  --cpus="1.5" \
  --restart unless-stopped \
  -e JAVA_OPTS="-Xmx2048m" \
  -e JENKINS_OPTS="--prefix=/jenkins" \
  jenkins/jenkins:lts

# Verify resource constraints
docker stats jenkins-advanced --no-stream
```

#### Step 3.2: Test Container Resilience
```bash
# Stop the container
docker stop jenkins-advanced

# Start it again
docker start jenkins-advanced

# Verify Jenkins data persists (check if plugins/jobs are still there)
docker exec jenkins-advanced ls -la /var/jenkins_home
```

### Exercise 4: Data Management and Backup

#### Step 4.1: Create Backup of Jenkins Data
```bash
# Create backup directory
mkdir -p ~/jenkins_backup

# Backup Jenkins home
docker run --rm \
  -v ~/jenkins_home:/source \
  -v ~/jenkins_backup:/backup \
  alpine tar czf /backup/jenkins-backup-$(date +%Y%m%d).tar.gz -C /source .

# List backups
ls -la ~/jenkins_backup/
```

#### Step 4.2: Test Data Restoration
```bash
# Stop current Jenkins container
docker stop jenkins-advanced
docker rm jenkins-advanced

# Restore from backup
docker run --rm \
  -v ~/jenkins_home:/target \
  -v ~/jenkins_backup:/backup \
  alpine sh -c "rm -rf /target/* && tar xzf /backup/jenkins-backup-*.tar.gz -C /target"

# Start new container with restored data
docker run -d \
  --name jenkins-restored \
  -p 8082:8080 \
  -v ~/jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

### Exercise 5: Docker Run Command Breakdown

#### Step 5.1: Analyze Each Parameter
```bash
# Create a complex run command and understand each part
docker run -d \
  --name jenkins-production \           # Container name
  --restart always \                     # Restart policy
  -p 80:8080 \                           # Port mapping (host:container)
  -p 50000:50000 \                        # Jenkins agent port
  -v jenkins-data:/var/jenkins_home \     # Named volume
  -v jenkins-logs:/var/log/jenkins \       # Separate logs volume
  -e JENKINS_OPTS="--httpPort=8080" \      # Environment variables
  --network jenkins-net \                  # Custom network
  --memory="2g" \                          # Memory limit
  --cpus="2" \                             # CPU limit
  --read-only \                            # Read-only root filesystem
  --tmpfs /tmp \                            # Temporary filesystem
  --health-cmd="curl -f http://localhost:8080 || exit 1" \  # Health check
  --health-interval=5m \                     # Health check interval
  --health-timeout=10s \                      # Health check timeout
  --health-retries=3 \                         # Health check retries
  jenkins/jenkins:lts                          # Image name
```

## Troubleshooting Exercises

### Exercise 6: Common Issues and Solutions

#### Scenario 1: Permission Denied
```bash
# Simulate permission issue
mkdir ~/jenkins_restricted
chmod 000 ~/jenkins_restricted

# Try to run with this directory
docker run -d \
  --name jenkins-permission-test \
  -v ~/jenkins_restricted:/var/jenkins_home \
  jenkins/jenkins:lts

# Check logs
docker logs jenkins-permission-test

# Fix permissions
chmod 777 ~/jenkins_restricted
```

#### Scenario 2: Port Conflict
```bash
# Run container on port 8080 (might conflict)
docker run -d --name jenkins-port-test -p 8080:8080 jenkins/jenkins:lts

# If port is in use, check
sudo lsof -i :8080

# Solution: Use different port
docker run -d --name jenkins-port-fixed -p 8083:8080 jenkins/jenkins:lts
```

## Verification Checklist

Run these commands to verify your setup:

```bash
# Check container status
docker ps -a | grep jenkins

# Check logs for errors
docker logs jenkins-prod --tail 50

# Verify volume mounting
docker volume ls
docker volume inspect jenkins_home

# Test Jenkins accessibility
curl -I http://localhost:8080

# Check resource usage
docker stats --no-stream $(docker ps -q --filter "name=jenkins")

# Verify data persistence
docker exec jenkins-prod ls -la /var/jenkins_home/
ls -la ~/jenkins_home/
```

## Cleanup

```bash
# Stop all Jenkins containers
docker stop $(docker ps -q --filter "name=jenkins")

# Remove all Jenkins containers
docker rm $(docker ps -aq --filter "name=jenkins")

# Remove volumes (optional - CAREFUL: this deletes all Jenkins data)
docker volume rm jenkins-data jenkins-logs

# Remove networks
docker network rm jenkins-network

# Remove backup files (optional)
rm -rf ~/jenkins_backup/*
```

## Summary Questions

1. What is the purpose of `-v` flag in the docker run command?
2. Why do we map port 8080 and 50000?
3. How does data persistence work with Docker volumes?
4. What happens if you restart the container without volume mounting?
5. How would you access Jenkins if it's running on a remote server?

## Additional Challenges

1. **Challenge 1:** Configure Jenkins with SSL using custom certificates
2. **Challenge 2:** Set up multiple Jenkins agents using different containers
3. **Challenge 3:** Create a docker-compose file that replicates this setup
4. **Challenge 4:** Implement automated backups using cron jobs
5. **Challenge 5:** Set up monitoring for your Jenkins container

## Reference: Docker Run Options Used

| Option | Description | Example |
|--------|-------------|---------|
| `-d` | Detached mode | `docker run -d` |
| `--name` | Assign container name | `--name jenkins` |
| `-p` | Publish port | `-p 8080:8080` |
| `-v` | Mount volume | `-v ~/jenkins_home:/var/jenkins_home` |
| `-e` | Set environment variables | `-e JAVA_OPTS="-Xmx512m"` |
| `--restart` | Restart policy | `--restart unless-stopped` |
| `--memory` | Memory limit | `--memory="2g"` |
| `--cpus` | CPU limit | `--cpus="1.5"` |
| `--network` | Network connection | `--network jenkins-network` |

## Troubleshooting Tips

1. **Container exits immediately:** Check logs with `docker logs [container-name]`
2. **Cannot access Jenkins:** Verify port mapping and firewall settings
3. **Permission errors:** Ensure proper ownership of mounted directories
4. **Out of memory:** Check container logs and increase memory limit
5. **Plugin installation fails:** Verify internet connectivity and proxy settings

This lab provides hands-on experience with Docker's `run` command using Jenkins as a practical example, focusing on data persistence and container management best practices.