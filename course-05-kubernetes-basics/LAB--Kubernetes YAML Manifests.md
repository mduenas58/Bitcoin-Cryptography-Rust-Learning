# **Kubernetes YAML Manifests Deep Dive: Pods & Deployments**

## **1. Pod Manifest Fundamentals**

### **Basic Pod Structure**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: basic-pod
  namespace: default
  labels:
    app: myapp
    tier: frontend
  annotations:
    description: "Basic pod example"
    kubernetes.io/created-by: "manual"
spec:
  containers:
  - name: main-container
    image: nginx:1.21
    imagePullPolicy: IfNotPresent
```

### **Complete Pod Manifest with All Options**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: comprehensive-pod
  namespace: production
  labels:
    app: ecommerce
    component: api
    version: "2.1.0"
    environment: production
    managed-by: kubectl
  annotations:
    iam.amazonaws.com/role: app-role
    prometheus.io/scrape: "true"
    prometheus.io/port: "9100"
    prometheus.io/path: "/metrics"
    sidecar.istio.io/inject: "true"
    backup.velero.io/backup-volumes: "data-volume"
spec:
  # Pod-level configurations
  restartPolicy: Always  # Options: Always, OnFailure, Never
  terminationGracePeriodSeconds: 30
  activeDeadlineSeconds: 3600  # Pod will be killed after 1 hour
  nodeSelector:
    disktype: ssd
    gpu: "true"
  
  # Image pull secrets
  imagePullSecrets:
  - name: registry-credentials
  
  # Service Account
  serviceAccountName: app-service-account
  automountServiceAccountToken: false
  
  # Security Context (Pod-level)
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
    supplementalGroups: [1000, 2000]
  
  # Containers
  containers:
  - name: web-server
    image: nginx:1.21-alpine
    imagePullPolicy: IfNotPresent  # Always, Never, IfNotPresent
    
    # Container Ports
    ports:
    - name: http
      containerPort: 80
      protocol: TCP
    - name: metrics
      containerPort: 9100
      protocol: TCP
    
    # Environment Variables
    env:
    - name: NODE_ENV
      value: "production"
    - name: DATABASE_HOST
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: database.host
    - name: API_KEY
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: api-key
    - name: POD_IP
      valueFrom:
        fieldRef:
          fieldPath: status.podIP
    - name: NODE_NAME
      valueFrom:
        fieldRef:
          fieldPath: spec.nodeName
    
    # Environment Variables from ConfigMap
    envFrom:
    - configMapRef:
        name: app-config
    - secretRef:
        name: app-secrets
    
    # Resource Limits & Requests
    resources:
      requests:
        memory: "128Mi"
        cpu: "250m"  # 250 millicores (0.25 CPU)
        ephemeral-storage: "1Gi"
      limits:
        memory: "256Mi"
        cpu: "500m"
        ephemeral-storage: "2Gi"
        hugepages-2Mi: "100Mi"
    
    # Liveness and Readiness Probes
    livenessProbe:
      httpGet:
        path: /healthz
        port: 80
        scheme: HTTP
        httpHeaders:
        - name: Custom-Header
          value: Awesome
      initialDelaySeconds: 30
      periodSeconds: 10
      timeoutSeconds: 5
      successThreshold: 1
      failureThreshold: 3
    
    readinessProbe:
      tcpSocket:
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 10
      failureThreshold: 3
      successThreshold: 1
    
    startupProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 10
      periodSeconds: 5
      failureThreshold: 30  # 30 * 5 = 150s max startup time
    
    # Lifecycle Hooks
    lifecycle:
      postStart:
        exec:
          command: ["/bin/sh", "-c", "echo 'Container started' > /tmp/startup.log"]
      preStop:
        httpGet:
          path: /graceful-shutdown
          port: 80
          scheme: HTTP
    
    # Security Context (Container-level)
    securityContext:
      allowPrivilegeEscalation: false
      privileged: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
        add:
        - NET_BIND_SERVICE
      seLinuxOptions:
        level: "s0:c123,c456"
    
    # Volume Mounts
    volumeMounts:
    - name: config-volume
      mountPath: /etc/nginx/conf.d
      readOnly: true
    - name: data-volume
      mountPath: /var/www/html
    - name: secrets-volume
      mountPath: /etc/secrets
      readOnly: true
    - name: emptydir-volume
      mountPath: /tmp/cache
    - name: hostpath-volume
      mountPath: /host/data
      readOnly: true
    
    # Command and Arguments
    command: ["nginx"]  # Overrides ENTRYPOINT
    args: ["-g", "daemon off;"]  # Overrides CMD
    
    # Working Directory
    workingDir: /usr/share/nginx/html
    
    # stdin and tty
    stdin: true
    tty: true
  
  # Init Containers
  initContainers:
  - name: init-db
    image: busybox:1.28
    command: ['sh', '-c', 'until nslookup db-service; do echo waiting for db; sleep 2; done']
  - name: init-config
    image: busybox:1.28
    command: ['sh', '-c', 'cp /config-temp/* /config-dest/']
    volumeMounts:
    - name: config-temp
      mountPath: /config-temp
    - name: config-dest
      mountPath: /config-dest
  
  # Volumes
  volumes:
  - name: config-volume
    configMap:
      name: nginx-config
      items:
      - key: nginx.conf
        path: nginx.conf
      - key: default.conf
        path: sites-enabled/default.conf
  
  - name: data-volume
    persistentVolumeClaim:
      claimName: app-data-pvc
  
  - name: secrets-volume
    secret:
      secretName: app-tls-secret
      items:
      - key: tls.crt
        path: tls.crt
      - key: tls.key
        path: tls.key
  
  - name: emptydir-volume
    emptyDir:
      medium: Memory
      sizeLimit: 100Mi
  
  - name: hostpath-volume
    hostPath:
      path: /mnt/data
      type: DirectoryOrCreate
  
  - name: config-temp
    configMap:
      name: init-config
  
  - name: config-dest
    emptyDir: {}
  
  # Topology Spread Constraints
  topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        app: myapp
  
  # Affinity and Anti-Affinity
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/arch
            operator: In
            values:
            - amd64
            - arm64
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
    
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: security
            operator: In
            values:
            - S1
        topologyKey: topology.kubernetes.io/zone
    
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values:
              - myapp
          topologyKey: kubernetes.io/hostname
  
  # Tolerations
  tolerations:
  - key: "node.kubernetes.io/unreachable"
    operator: "Exists"
    effect: "NoExecute"
    tolerationSeconds: 300
  - key: "dedicated"
    operator: "Equal"
    value: "gpu"
    effect: "NoSchedule"
  
  # Priority and Preemption
  priorityClassName: high-priority
  
  # DNS Config
  dnsConfig:
    nameservers:
      - 1.2.3.4
    searches:
      - ns1.svc.cluster-domain.example
      - my.dns.search.suffix
    options:
      - name: ndots
        value: "2"
      - name: edns0
  
  # Host Aliases
  hostAliases:
  - ip: "192.168.1.100"
    hostnames:
    - "foo.local"
    - "bar.local"
```

## **2. Deployment Manifest Deep Dive**

### **Basic Deployment Structure**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
  namespace: production
  labels:
    app: web
    environment: production
spec:
  # Replica Management
  replicas: 3
  revisionHistoryLimit: 10
  
  # Strategy
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%  # Can also be integer like 1
      maxUnavailable: 25%
  
  # Selector (MUST match template labels)
  selector:
    matchLabels:
      app: web
      component: frontend
    
    # Advanced selector
    matchExpressions:
    - {key: environment, operator: In, values: [production, staging]}
    - {key: version, operator: NotIn, values: [deprecated]}
  
  # Pod Template
  template:
    metadata:
      labels:
        app: web
        component: frontend
        version: "2.1.0"
      annotations:
        sidecar.istio.io/inject: "true"
        prometheus.io/scrape: "true"
    
    spec:
      containers:
      - name: nginx
        image: nginx:1.21-alpine
        ports:
        - containerPort: 80
        
        # Resources
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
        
        # Probes
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 15
          periodSeconds: 20
        
        readinessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
```

### **Advanced Deployment Configuration**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: advanced-deployment
  namespace: production
  annotations:
    deployment.kubernetes.io/revision: "1"
spec:
  # Replica Management
  replicas: 5
  minReadySeconds: 30  # Pod must be ready for 30s before considered available
  progressDeadlineSeconds: 600  # Deployment fails if not progressing in 10min
  revisionHistoryLimit: 10  # Keep last 10 ReplicaSets for rollback
  
  # Update Strategy
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1  # Maximum pods that can be created over desired
      maxUnavailable: 0  # No pods unavailable during update (blue-green like)
  
  # Pod Disruption Budget (created separately but related)
  # pdb.yaml
  # apiVersion: policy/v1
  # kind: PodDisruptionBudget
  # spec:
  #   minAvailable: 3
  #   selector:
  #     matchLabels:
  #       app: critical-app
  
  selector:
    matchLabels:
      app: critical-app
      tier: backend
  
  template:
    metadata:
      labels:
        app: critical-app
        tier: backend
        version: "3.2.1"
      annotations:
        checksum/config: "abc123"  # Triggers rollout on config change
    
    spec:
      # Pod Priority
      priorityClassName: high-priority
      
      # Termination Grace Period
      terminationGracePeriodSeconds: 60
      
      # Share Process Namespace
      shareProcessNamespace: true
      
      # Host Networking (use with caution)
      hostNetwork: false
      hostPID: false
      hostIPC: false
      
      # DNS Policy
      dnsPolicy: ClusterFirst
      
      # Node Selector
      nodeSelector:
        node-type: optimized
        kubernetes.io/os: linux
      
      # Service Account
      serviceAccountName: app-service-account
      automountServiceAccountToken: true
      
      # Image Pull Secrets
      imagePullSecrets:
      - name: private-registry-secret
      
      # Security Context (Pod-level)
      securityContext:
        runAsUser: 1000
        runAsGroup: 1000
        fsGroup: 2000
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      
      # Multiple Containers
      containers:
      - name: app
        image: myapp:3.2.1
        imagePullPolicy: IfNotPresent
        
        # Ports
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
        - name: metrics
          containerPort: 9090
          protocol: TCP
        - name: grpc
          containerPort: 50051
          protocol: TCP
        
        # Environment Variables with Complex ConfigMaps
        env:
        - name: CONFIG_MAP_VALUE
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: app.config
              optional: true  # Pod can start without this
        - name: SECRET_VALUE
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database.password
              optional: false  # Pod will fail without this
        
        envFrom:
        - configMapRef:
            name: environment-config
        - secretRef:
            name: sensitive-config
        
        # Resources with Quality of Service Classes
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
            ephemeral-storage: "1Gi"
            hugepages-2Mi: "64Mi"
          limits:
            memory: "512Mi"
            cpu: "500m"
            ephemeral-storage: "2Gi"
            hugepages-2Mi: "128Mi"
        
        # Advanced Probes
        livenessProbe:
          httpGet:
            path: /health/live
            port: 8080
            scheme: HTTP
            httpHeaders:
            - name: X-Custom-Header
              value: HealthCheck
          initialDelaySeconds: 45
          periodSeconds: 10
          timeoutSeconds: 5
          successThreshold: 1
          failureThreshold: 3
        
        readinessProbe:
          tcpSocket:
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 5
          successThreshold: 1
          failureThreshold: 3
        
        startupProbe:
          exec:
            command:
            - /bin/sh
            - -c
            - |
              # Check if application is initialized
              curl -f http://localhost:8080/startup || exit 1
          initialDelaySeconds: 10
          periodSeconds: 5
          failureThreshold: 30
        
        # Lifecycle Hooks
        lifecycle:
          postStart:
            exec:
              command:
              - /bin/sh
              - -c
              - |
                echo "Application started at $(date)" >> /var/log/startup.log
                # Perform initialization tasks
          preStop:
            httpGet:
              path: /prestop
              port: 8080
              httpHeaders:
              - name: Termination
                value: graceful
        
        # Security Context (Container-level)
        securityContext:
          allowPrivilegeEscalation: false
          privileged: false
          readOnlyRootFilesystem: true
          capabilities:
            drop: ["ALL"]
            add: ["NET_BIND_SERVICE"]
          seLinuxOptions:
            level: "s0:c123,c456"
          appArmorProfile: runtime/default
        
        # Volume Mounts
        volumeMounts:
        - name: config
          mountPath: /etc/config
          readOnly: true
        - name: data
          mountPath: /var/data
        - name: tmp
          mountPath: /tmp
          mountPropagation: HostToContainer
        
        # Command and Args
        command: ["/app/start.sh"]
        args: ["--config", "/etc/config/app.yaml", "--log-level", "info"]
        
        # stdin and tty
        stdin: false
        tty: false
        
        # Working Directory
        workingDir: /app
        
        # Termination Message
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      
      # Sidecar Container
      - name: sidecar
        image: fluentd:latest
        command: ["fluentd"]
        args: ["-c", "/fluentd/etc/fluent.conf"]
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: fluentd-config
          mountPath: /fluentd/etc
      
      # Init Containers
      initContainers:
      - name: init-migrations
        image: postgres:13-alpine
        command: ['sh', '-c', 'until pg_isready -h database; do sleep 2; done && psql -h database -U app -d appdb -f /migrations/init.sql']
        volumeMounts:
        - name: migration-scripts
          mountPath: /migrations
      
      - name: init-cache
        image: redis:alpine
        command: ['sh', '-c', 'redis-cli -h redis ping || exit 1']
      
      # Volumes
      volumes:
      - name: config
        configMap:
          name: app-config-map
          defaultMode: 0644
      
      - name: data
        persistentVolumeClaim:
          claimName: app-data-pvc
          readOnly: false
      
      - name: tmp
        emptyDir:
          medium: Memory
          sizeLimit: 100Mi
      
      - name: varlog
        emptyDir: {}
      
      - name: fluentd-config
        configMap:
          name: fluentd-config
      
      - name: migration-scripts
        configMap:
          name: db-migrations
      
      # Affinity Rules
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/arch
                operator: In
                values: [amd64]
              - key: node.kubernetes.io/instance-type
                operator: NotIn
                values: [t2.nano, t2.micro]
          
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            preference:
              matchExpressions:
              - key: spot-instance
                operator: In
                values: ["false"]
          - weight: 50
            preference:
              matchExpressions:
              - key: zone
                operator: In
                values: [us-east-1a]
        
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values: [cache]
            topologyKey: kubernetes.io/hostname
        
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values: [web]
            topologyKey: topology.kubernetes.io/zone
          
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values: [web]
              topologyKey: kubernetes.io/hostname
      
      # Tolerations
      tolerations:
      - key: "node.kubernetes.io/not-ready"
        operator: "Exists"
        effect: "NoExecute"
        tolerationSeconds: 300
      - key: "node.kubernetes.io/unreachable"
        operator: "Exists"
        effect: "NoExecute"
        tolerationSeconds: 300
      - key: "dedicated"
        operator: "Equal"
        value: "gpu-team"
        effect: "NoSchedule"
      
      # Topology Spread Constraints
      topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: ScheduleAnyway
        labelSelector:
          matchLabels:
            app: web
      
      - maxSkew: 2
        topologyKey: kubernetes.io/hostname
        whenUnsatisfiable: DoNotSchedule
        labelSelector:
          matchLabels:
            app: web
  
  # Deployment Pause/Resume
  # paused: true  # Can be set to pause rollout
  
  # Rollback To (can be set after deployment)
  # rollbackTo:
  #   revision: 3
```

## **3. Multi-Container Pod Patterns**

### **Sidecar Pattern**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sidecar-pod
spec:
  containers:
  - name: main-app
    image: myapp:latest
    ports:
    - containerPort: 8080
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/app
    - name: shared-data
      mountPath: /tmp/shared
  
  - name: log-collector
    image: fluentd:latest
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/app
    - name: fluentd-config
      mountPath: /etc/fluentd
  
  - name: config-watcher
    image: jwilder/dockerize
    command: ['dockerize', '-wait', 'http://main-app:8080/health', '-timeout', '60s']
  
  volumes:
  - name: shared-logs
    emptyDir: {}
  - name: shared-data
    emptyDir: {}
  - name: fluentd-config
    configMap:
      name: fluentd-config
```

### **Ambassador Pattern**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ambassador-pod
spec:
  containers:
  - name: main-app
    image: myapp:latest
    env:
    - name: DATABASE_HOST
      value: localhost
    - name: DATABASE_PORT
      value: "5432"
  
  - name: proxy
    image: envoyproxy/envoy:latest
    ports:
    - containerPort: 5432
      name: postgres-proxy
    volumeMounts:
    - name: envoy-config
      mountPath: /etc/envoy
    command: ["envoy"]
    args: ["-c", "/etc/envoy/envoy.yaml", "--service-cluster", "database-proxy"]
  
  volumes:
  - name: envoy-config
    configMap:
      name: envoy-config
```

### **Adapter Pattern**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: adapter-pod
spec:
  containers:
  - name: main-app
    image: myapp:legacy
    ports:
    - containerPort: 8080
  
  - name: metrics-adapter
    image: prometheus/node-exporter
    ports:
    - containerPort: 9100
    args:
    - "--path.procfs=/host/proc"
    - "--path.sysfs=/host/sys"
    - "--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($|/)"
    volumeMounts:
    - name: proc
      mountPath: /host/proc
      readOnly: true
    - name: sys
      mountPath: /host/sys
      readOnly: true
  
  volumes:
  - name: proc
    hostPath:
      path: /proc
  - name: sys
    hostPath:
      path: /sys
```

## **4. Production-Ready Deployment Patterns**

### **Blue-Green Deployment Strategy**
```yaml
# blue-deployment.yaml (current)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-blue
  labels:
    version: blue
    track: stable
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: blue
  template:
    metadata:
      labels:
        app: myapp
        version: blue
        track: stable
    spec:
      containers:
      - name: app
        image: myapp:v1.0
        ports:
        - containerPort: 80
---
# green-deployment.yaml (new)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-green
  labels:
    version: green
    track: canary
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: green
  template:
    metadata:
      labels:
        app: myapp
        version: green
        track: canary
    spec:
      containers:
      - name: app
        image: myapp:v2.0
        ports:
        - containerPort: 80
---
# service.yaml (routes traffic)
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: myapp
    version: blue  # Switch to green after testing
  ports:
  - port: 80
    targetPort: 80
```

### **Canary Deployment**
```yaml
# stable-deployment.yaml (90% traffic)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-stable
spec:
  replicas: 9
  selector:
    matchLabels:
      app: myapp
      track: stable
  template:
    metadata:
      labels:
        app: myapp
        track: stable
    spec:
      containers:
      - name: app
        image: myapp:v1.0
---
# canary-deployment.yaml (10% traffic)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-canary
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
      track: canary
  template:
    metadata:
      labels:
        app: myapp
        track: canary
    spec:
      containers:
      - name: app
        image: myapp:v2.0
---
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: myapp
  ports:
  - port: 80
```

### **Stateful Application Deployment**
```yaml
apiVersion: apps/v1
kind: StatefulSet  # Similar to Deployment but for stateful apps
metadata:
  name: mysql
spec:
  serviceName: mysql
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: root-password
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: "ssd"
      resources:
        requests:
          storage: 10Gi
```

## **5. Advanced Features & Best Practices**

### **Pod Disruption Budget**
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: app-pdb
spec:
  minAvailable: 2  # At least 2 pods must be available
  # OR
  maxUnavailable: 1  # At most 1 pod can be unavailable
  selector:
    matchLabels:
      app: critical-app
```

### **Horizontal Pod Autoscaler**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app-deployment
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
  - type: Pods
    pods:
      metric:
        name: packets-per-second
      target:
        type: AverageValue
        averageValue: 1k
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 60
```

### **Pod Security Standards**
```yaml
# Pod Security Admission (PSA) Labels
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: baseline
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/audit-version: latest
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/warn-version: latest
---
# Privileged Pod (use sparingly)
apiVersion: v1
kind: Pod
metadata:
  name: privileged-pod
  namespace: privileged-namespace
spec:
  containers:
  - name: debug
    image: busybox
    command: ["sleep", "3600"]
    securityContext:
      privileged: true
      capabilities:
        add: ["SYS_ADMIN", "NET_ADMIN"]
      allowPrivilegeEscalation: true
```

### **Resource Quotas**
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-quota
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    limits.cpu: "20"
    limits.memory: 40Gi
    requests.storage: 100Gi
    persistentvolumeclaims: "10"
    services.loadbalancers: "2"
    services.nodeports: "5"
    pods: "50"
    count/deployments.apps: "10"
    count/statefulsets.apps: "5"
    count/jobs.batch: "5"
```

## **6. Troubleshooting & Debugging Manifests**

### **Common Issues and Solutions:**

1. **Image Pull Errors:**
```yaml
# Solution: Add imagePullSecrets
spec:
  imagePullSecrets:
  - name: docker-registry-secret
```

2. **CrashLoopBackOff:**
```yaml
# Add proper probes and logs
spec:
  containers:
  - name: app
    livenessProbe:
      failureThreshold: 3
      initialDelaySeconds: 30
    readinessProbe:
      failureThreshold: 3
      initialDelaySeconds: 5
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: FallbackToLogsOnError
```

3. **Resource Issues:**
```yaml
# Set proper resource requests/limits
spec:
  containers:
  - name: app
    resources:
      requests:
        memory: "128Mi"
        cpu: "100m"
      limits:
        memory: "256Mi"
        cpu: "200m"
```

### **Debug Commands:**
```bash
# Check pod status
kubectl describe pod <pod-name>

# View pod logs
kubectl logs <pod-name> -c <container-name>

# Debug with exec
kubectl exec -it <pod-name> -- /bin/sh

# Get YAML of running pod
kubectl get pod <pod-name> -o yaml

# Check events
kubectl get events --sort-by='.lastTimestamp'

# Validate YAML
kubectl apply --dry-run=client -f pod.yaml
kubectl apply --dry-run=server -f pod.yaml
```

## **7. YAML Generation Best Practices**

### **Use Kustomize:**
```yaml
# kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
- deployment.yaml
- service.yaml
- configmap.yaml

commonLabels:
  app: myapp
  environment: production

patchesStrategicMerge:
- patch.yaml

images:
- name: nginx
  newTag: 1.21-alpine
```

### **Helm Templates:**
```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Chart.Name }}
  labels:
    {{- include "mychart.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "mychart.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "mychart.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
```

### **Generate Manifests Programmatically:**
```python
# Python script to generate YAML
import yaml

def generate_deployment(name, replicas, image):
    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": name},
        "spec": {
            "replicas": replicas,
            "selector": {"matchLabels": {"app": name}},
            "template": {
                "metadata": {"labels": {"app": name}},
                "spec": {
                    "containers": [{
                        "name": name,
                        "image": image
                    }]
                }
            }
        }
    }
    return yaml.dump(deployment, default_flow_style=False)

print(generate_deployment("myapp", 3, "nginx:latest"))
```

Remember to always:
1. **Validate** YAML syntax before applying
2. Use **--dry-run** flag for testing
3. **Version control** all manifests
4. Follow **security best practices** (non-root, read-only filesystems, etc.)
5. Implement **proper resource management**
6. Use **namespaces** for isolation
7. Add **labels and annotations** for better observability