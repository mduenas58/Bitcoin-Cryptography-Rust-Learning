# Complete DevOps Tutorial: Building, Containerizing, and Orchestrating Node.js Applications

## **Lab Overview**
This comprehensive lab will guide you through the entire lifecycle of a Node.js application - from development to deployment. You'll learn how to build Node.js applications, manage dependencies with npm, containerize with Docker, orchestrate with Kubernetes, and establish CI/CD pipelines using GitHub and Jenkins.

**Duration:** 4-6 hours  
**Prerequisites:** Basic knowledge of JavaScript, command line, and cloud concepts

---

## **Part 1: Node.js Application Development & npm Fundamentals**

### **1.1 Setting Up the Development Environment**

First, ensure you have Node.js and npm installed:

```bash
# Check if Node.js and npm are installed
node --version
npm --version

# If not installed, download from https://nodejs.org/ (LTS version recommended)
```

### **1.2 Creating Your First Node.js Application**

Let's build a simple REST API for a task management system:

```bash
# Create project directory
mkdir task-manager-app
cd task-manager-app

# Initialize npm project
npm init -y
```

This creates a `package.json` file. Let's understand its structure:

```json
{
  "name": "task-manager-app",
  "version": "1.0.0",
  "description": "A simple task management API",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "jest"
  },
  "keywords": ["nodejs", "rest-api", "tutorial"],
  "author": "Your Name",
  "license": "MIT"
}
```

### **1.3 Installing Dependencies**

```bash
# Install production dependencies
npm install express body-parser cors

# Install development dependencies
npm install --save-dev nodemon jest supertest

# View installed packages
npm list --depth=0
```

**Understanding package.json:**
- `dependencies`: Required for the app to run in production
- `devDependencies`: Only needed during development
- `scripts`: Custom commands you can run with `npm run <script-name>`

### **1.4 Building the Application**

Create `server.js`:

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database
let tasks = [
  { id: 1, title: 'Learn Node.js', completed: false },
  { id: 2, title: 'Build a REST API', completed: false }
];

// Routes
app.get('/', (req, res) => {
  res.json({ message: 'Task Manager API is running' });
});

// GET all tasks
app.get('/api/tasks', (req, res) => {
  res.json(tasks);
});

// GET single task
app.get('/api/tasks/:id', (req, res) => {
  const task = tasks.find(t => t.id === parseInt(req.params.id));
  if (!task) return res.status(404).json({ error: 'Task not found' });
  res.json(task);
});

// POST new task
app.post('/api/tasks', (req, res) => {
  const task = {
    id: tasks.length + 1,
    title: req.body.title,
    completed: false
  };
  tasks.push(task);
  res.status(201).json(task);
});

// PUT update task
app.put('/api/tasks/:id', (req, res) => {
  const task = tasks.find(t => t.id === parseInt(req.params.id));
  if (!task) return res.status(404).json({ error: 'Task not found' });
  
  task.title = req.body.title || task.title;
  task.completed = req.body.completed !== undefined ? req.body.completed : task.completed;
  
  res.json(task);
});

// DELETE task
app.delete('/api/tasks/:id', (req, res) => {
  const index = tasks.findIndex(t => t.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'Task not found' });
  
  tasks.splice(index, 1);
  res.status(204).send();
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

### **1.5 Adding Tests**

Create `server.test.js`:

```javascript
const request = require('supertest');
const app = require('./server');

describe('Task Manager API', () => {
  test('GET /api/tasks should return all tasks', async () => {
    const response = await request(app).get('/api/tasks');
    expect(response.statusCode).toBe(200);
    expect(Array.isArray(response.body)).toBeTruthy();
  });

  test('POST /api/tasks should create new task', async () => {
    const newTask = { title: 'Test task' };
    const response = await request(app)
      .post('/api/tasks')
      .send(newTask);
    expect(response.statusCode).toBe(201);
    expect(response.body.title).toBe(newTask.title);
  });
});
```

### **1.6 Understanding package-lock.json**

```bash
# After installing dependencies, examine package-lock.json
cat package-lock.json
```

The `package-lock.json` ensures consistent installs across environments by locking dependency versions.

---

## **Part 2: Version Control with GitHub**

### **2.1 Initialize Git Repository**

```bash
# Initialize git
git init

# Create .gitignore file
cat > .gitignore << EOF
node_modules/
.env
*.log
coverage/
dist/
.DS_Store
EOF

# Add and commit files
git add .
git commit -m "Initial commit: Task Manager API"
```

### **2.2 Create GitHub Repository**

1. Go to [GitHub](https://github.com) and create a new repository
2. Link and push your local repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/task-manager-app.git
git branch -M main
git push -u origin main
```

### **2.3 Implement Branching Strategy**

```bash
# Create development branch
git checkout -b develop

# Create feature branch
git checkout -b feature/add-user-authentication

# Make changes and commit
git add .
git commit -m "Add user authentication middleware"

# Merge back to develop
git checkout develop
git merge feature/add-user-authentication

# Push to GitHub
git push origin develop
```

---

## **Part 3: Docker Containerization**

### **3.1 Understanding Docker Basics**

First, ensure Docker is installed:
```bash
docker --version
docker-compose --version
```

### **3.2 Creating Dockerfile**

Create `Dockerfile` in your project root:

```dockerfile
# Multi-stage build for optimized image size

# Build stage
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Runtime stage
FROM node:18-alpine

RUN apk add --no-cache tini

WORKDIR /app

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Copy from builder
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --chown=nodejs:nodejs . .

# Use tini as init system
ENTRYPOINT ["/sbin/tini", "--"]

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000', (r) => {r.statusCode === 200 ? process.exit(0) : process.exit(1)})"

# Start application
CMD ["node", "server.js"]
```

### **3.3 Building and Testing Docker Image**

```bash
# Build the image
docker build -t task-manager-app:latest .

# Run container locally
docker run -p 3000:3000 -d --name task-manager task-manager-app:latest

# Check logs
docker logs task-manager

# Test the application
curl http://localhost:3000/api/tasks

# Stop and remove container
docker stop task-manager
docker rm task-manager
```

### **3.4 Docker Compose for Development**

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      target: builder
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - PORT=3000
    volumes:
      - ./:/app
      - /app/node_modules
    command: npm run dev

  # Add MongoDB service (optional)
  mongodb:
    image: mongo:6.0
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=password
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

### **3.5 Docker Best Practices**

```bash
# Tag your image properly
docker tag task-manager-app:latest YOUR_DOCKERHUB_USERNAME/task-manager-app:v1.0.0

# Login to Docker Hub
docker login

# Push to registry
docker push YOUR_DOCKERHUB_USERNAME/task-manager-app:v1.0.0

# Scan for vulnerabilities
docker scan task-manager-app:latest
```

---

## **Part 4: Kubernetes Orchestration**

### **4.1 Setting Up Kubernetes Environment**

For local development, use Minikube or Docker Desktop's Kubernetes:

```bash
# Start Minikube
minikube start --cpus=4 --memory=8192

# Verify cluster
kubectl cluster-info
kubectl get nodes
```

### **4.2 Creating Kubernetes Manifests**

Create `k8s/namespace.yaml`:
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: task-manager
```

Create `k8s/configmap.yaml`:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: task-manager-config
  namespace: task-manager
data:
  NODE_ENV: "production"
  PORT: "3000"
  API_VERSION: "v1"
```

Create `k8s/secret.yaml`:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: task-manager-secrets
  namespace: task-manager
type: Opaque
data:
  # Base64 encoded values (echo -n 'your-value' | base64)
  DATABASE_URL: bW9uZ29kYjovL2FkbWluOnBhc3N3b3JkQG1vbmdvZGI6MjcwMTcvdGFza21hbmFnZXI=
  JWT_SECRET: c3VwZXItc2VjcmV0LWtleS1mb3Itand0
```

Create `k8s/deployment.yaml`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: task-manager
  namespace: task-manager
  labels:
    app: task-manager
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: task-manager
  template:
    metadata:
      labels:
        app: task-manager
    spec:
      containers:
      - name: app
        image: YOUR_DOCKERHUB_USERNAME/task-manager-app:v1.0.0
        imagePullPolicy: Always
        ports:
        - containerPort: 3000
        envFrom:
        - configMapRef:
            name: task-manager-config
        - secretRef:
            name: task-manager-secrets
        resources:
          requests:
            memory: "128Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
```

Create `k8s/service.yaml`:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: task-manager-service
  namespace: task-manager
spec:
  selector:
    app: task-manager
  ports:
  - port: 80
    targetPort: 3000
  type: ClusterIP
```

Create `k8s/ingress.yaml`:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: task-manager-ingress
  namespace: task-manager
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: task-manager.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: task-manager-service
            port:
              number: 80
```

Create `k8s/hpa.yaml` (Horizontal Pod Autoscaler):
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: task-manager-hpa
  namespace: task-manager
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: task-manager
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

### **4.3 Deploying to Kubernetes**

```bash
# Create namespace and deploy resources
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml

# Check deployment status
kubectl get all -n task-manager
kubectl get pods -n task-manager -w

# Scale deployment manually (if HPA not used)
kubectl scale deployment task-manager -n task-manager --replicas=5

# Port forwarding for local access
kubectl port-forward -n task-manager service/task-manager-service 8080:80

# Check logs
kubectl logs -n task-manager -l app=task-manager
```

### **4.4 Advanced Kubernetes Operations**

```bash
# Exec into a pod
kubectl exec -it -n task-manager deployment/task-manager -- /bin/sh

# View resource usage
kubectl top pods -n task-manager

# Rolling update
kubectl set image deployment/task-manager -n task-manager app=YOUR_DOCKERHUB_USERNAME/task-manager-app:v1.0.1

# Rollback if needed
kubectl rollout undo deployment/task-manager -n task-manager

# View rollout history
kubectl rollout history deployment/task-manager -n task-manager
```

---

## **Part 5: Jenkins Pipeline CI/CD**

### **5.1 Setting Up Jenkins**

Using Docker to run Jenkins:

```bash
# Create Docker network
docker network create jenkins

# Run Jenkins container
docker run -d \
  --name jenkins \
  --network jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts

# Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Access Jenkins at `http://localhost:8080` and complete the setup.

### **5.2 Install Required Plugins**

Install these plugins via Jenkins Dashboard:
- GitHub Integration
- Docker Pipeline
- Kubernetes CLI
- Blue Ocean (optional, better UI)
- NodeJS Plugin

### **5.3 Configure Jenkins Credentials**

Add credentials for:
1. GitHub (username/password or token)
2. Docker Hub (username/password)
3. Kubernetes config file

### **5.4 Create Jenkins Pipeline**

Create `Jenkinsfile` in your project root:

```groovy
pipeline {
    agent any
    
    tools {
        nodejs 'NodeJS-18'  // Configure this in Jenkins tools
    }
    
    environment {
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_IMAGE = 'yourusername/task-manager-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
        K8S_NAMESPACE = 'task-manager'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/yourusername/task-manager-app.git',
                    credentialsId: 'github-credentials'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'npm ci'
            }
        }
        
        stage('Lint') {
            steps {
                sh 'npm run lint || true'  // Add linting script
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('Build and Tag Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
        
        stage('Security Scan') {
            steps {
                sh "docker scan ${DOCKER_IMAGE}:${DOCKER_TAG} || true"
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig([credentialsId: 'kubeconfig']) {
                        sh """
                            sed -i 's|image: .*|image: ${DOCKER_IMAGE}:${DOCKER_TAG}|' k8s/deployment.yaml
                            kubectl apply -f k8s/namespace.yaml
                            kubectl apply -f k8s/configmap.yaml
                            kubectl apply -f k8s/secret.yaml
                            kubectl apply -f k8s/deployment.yaml
                            kubectl apply -f k8s/service.yaml
                            kubectl apply -f k8s/hpa.yaml
                            kubectl rollout status deployment/task-manager -n ${K8S_NAMESPACE}
                        """
                    }
                }
            }
        }
        
        stage('Smoke Test') {
            steps {
                script {
                    def podName = sh(script: "kubectl get pods -n ${K8S_NAMESPACE} -l app=task-manager -o jsonpath='{.items[0].metadata.name}'", returnStdout: true).trim()
                    sh "kubectl port-forward -n ${K8S_NAMESPACE} pod/${podName} 8080:3000 &"
                    sleep(5)
                    sh "curl --fail http://localhost:8080/api/tasks || exit 1"
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
            // Send notification (Slack, email, etc.)
        }
        failure {
            echo 'Pipeline failed!'
            // Send failure notification
        }
        always {
            cleanWs()  // Clean workspace
        }
    }
}
```

### **5.5 Multi-Branch Pipeline Configuration**

1. In Jenkins, create a new Pipeline job
2. Select "Multibranch Pipeline"
3. Add GitHub repository URL
4. Jenkins will automatically discover branches and create pipelines

### **5.6 Webhook Configuration for Automatic Triggers**

In GitHub repository settings:
1. Go to Settings > Webhooks
2. Add webhook: `http://JENKINS_URL:8080/github-webhook/`
3. Select "Just the push event"

---

## **Part 6: Monitoring and Logging**

### **6.1 Add Health Check Endpoint**

Update `server.js`:

```javascript
// Health check endpoints
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy', timestamp: new Date().toISOString() });
});

app.get('/ready', (req, res) => {
  // Check database connection, etc.
  res.status(200).json({ status: 'ready', timestamp: new Date().toISOString() });
});

// Metrics endpoint for Prometheus
app.get('/metrics', (req, res) => {
  res.json({
    uptime: process.uptime(),
    memoryUsage: process.memoryUsage(),
    cpuUsage: process.cpuUsage(),
    tasksCount: tasks.length
  });
});
```

### **6.2 Implement Structured Logging**

Install Winston:

```bash
npm install winston
```

Create `logger.js`:

```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
    new winston.transports.Console({
      format: winston.format.simple()
    })
  ]
});

module.exports = logger;
```

---

## **Part 7: Advanced Topics & Best Practices**

### **7.1 Git Hooks with Husky**

```bash
npm install --save-dev husky lint-staged

# Add to package.json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "pre-push": "npm test"
    }
  },
  "lint-staged": {
    "*.js": ["eslint --fix", "git add"]
  }
}
```

### **7.2 Semantic Versioning**

Follow semantic versioning for releases:
- **Major**: Incompatible API changes
- **Minor**: Backward-compatible functionality
- **Patch**: Backward-compatible bug fixes

```bash
npm version patch  # 1.0.0 -> 1.0.1
npm version minor  # 1.0.1 -> 1.1.0
npm version major  # 1.1.0 -> 2.0.0
```

### **7.3 Security Best Practices**

```bash
# Audit dependencies
npm audit
npm audit fix

# Use Snyk for security
npm install -g snyk
snyk test
snyk monitor

# Scan Docker images
trivy image yourusername/task-manager-app:latest
```

### **7.4 Performance Optimization**

```bash
# Use Alpine-based images
node:18-alpine

# Implement caching in Dockerfile
COPY package*.json ./
RUN npm ci && npm cache clean --force

# Use multi-stage builds
# Already implemented in our Dockerfile

# Enable gzip compression
npm install compression
```

---

## **Part 8: Troubleshooting Guide**

### **Common Issues and Solutions**

1. **Node.js version mismatch**
```bash
nvm use  # Use .nvmrc file
node --version
```

2. **Docker build fails**
```bash
docker system prune
docker build --no-cache -t app .
```

3. **Kubernetes pod stuck in pending**
```bash
kubectl describe pod <pod-name> -n task-manager
kubectl get events -n task-manager --sort-by='.lastTimestamp'
```

4. **Jenkins pipeline fails**
- Check Jenkins system log
- Verify credentials are valid
- Ensure Docker socket permissions

### **Debugging Commands**

```bash
# Debug Node.js
node --inspect server.js

# Debug Docker
docker logs <container-id>
docker exec -it <container-id> sh

# Debug Kubernetes
kubectl describe <resource>
kubectl logs <pod-name>
kubectl exec -it <pod-name> -- /bin/sh
```

---

## **Conclusion**

Congratulations! You've successfully:
- ✅ Built a Node.js application with npm
- ✅ Managed dependencies and scripts
- ✅ Version-controlled with Git and GitHub
- ✅ Containerized with Docker
- ✅ Orchestrated with Kubernetes
- ✅ Automated CI/CD with Jenkins
- ✅ Implemented monitoring and logging

## **Next Steps**

1. Add a database (MongoDB, PostgreSQL)
2. Implement authentication (JWT, OAuth)
3. Add message queue (RabbitMQ, Kafka)
4. Implement service mesh (Istio)
5. Add canary deployments
6. Implement GitOps with ArgoCD
7. Add chaos engineering experiments

## **Resources**

- [Node.js Documentation](https://nodejs.org/docs)
- [npm Documentation](https://docs.npmjs.com)
- [Docker Documentation](https://docs.docker.com)
- [Kubernetes Documentation](https://kubernetes.io/docs)
- [Jenkins Handbook](https://www.jenkins.io/doc)

**Remember**: Always follow the principle of least privilege, implement security scanning, and maintain proper documentation. Happy coding! 🚀