## **1. What is Systemd?**

**Systemd** is a system and service manager for Linux operating systems that has become the de facto standard for most modern distributions (since 2015+). It's PID 1 - the first process that starts when Linux boots.

### **Why Systemd Replaced SysVinit:**
```bash
# Old SysVinit approach
/etc/init.d/apache2 start
service apache2 start
update-rc.d apache2 defaults

# New Systemd approach
systemctl start apache2
systemctl enable apache2
```

**Key Advantages:**
- **Parallel startup** of services (faster boot)
- **On-demand activation** of services
- **Socket activation** (services start when connections arrive)
- **Dependency-based service control**
- **Integrated logging** with journald
- **Cgroups integration** for resource management
- **Snapshot/restore** capabilities

## **2. Systemd Architecture Overview**

```
┌─────────────────────────────────────────────────────────────┐
│                      Systemd Ecosystem                      │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│  systemctl  │ journalctl  │  loginctl   │   hostnamectl     │
│   (control) │   (logs)    │ (sessions)  │   (host info)     │
├─────────────┼─────────────┼─────────────┼───────────────────┤
│             │             │             │                   │
│  Units      │  Targets    │  Sockets    │   Timers          │
│  (Services, │  (Runlevels)│  (IPC)      │   (Cron jobs)     │
│   Mounts,   │             │             │                   │
│   Devices)  │             │             │                   │
├─────────────┴─────────────┴─────────────┴───────────────────┤
│                    Core Systemd Daemon                      │
│                    (PID 1 - /usr/lib/systemd/systemd)       │
└─────────────────────────────────────────────────────────────┘
```

## **3. Systemd Unit Types**

Systemd manages different types of **units** (12 types total):

| Type | Extension | Description |
|------|-----------|-------------|
| Service | `.service` | System services (daemons) |
| Socket | `.socket` | IPC sockets for activation |
| Device | `.device` | Kernel device files |
| Mount | `.mount` | Filesystem mount points |
| Automount | `.automount` | Auto-mounting filesystems |
| Swap | `.swap` | Swap space |
| Target | `.target` | Group of units (like runlevels) |
| Path | `.path` | Files/directories for activation |
| Timer | `.timer` | Scheduled tasks (cron replacement) |
| Slice | `.slice` | Cgroup resource management |
| Scope | `.scope` | External processes |
| Slice | `.slice` | Resource management |

## **4. Systemctl Command Deep Dive**

### **A. Basic Service Management**

```bash
# Starting/Stopping/Restarting
systemctl start service_name          # Start service
systemctl stop service_name           # Stop service
systemctl restart service_name        # Restart service
systemctl reload service_name         # Reload config (if supported)
systemctl reload-or-restart service_name  # Smart restart

# Enable/Disable (start at boot)
systemctl enable service_name         # Enable auto-start
systemctl disable service_name        # Disable auto-start
systemctl reenable service_name       # Re-enable (reset symlinks)
systemctl preset service_name         # Reset to vendor defaults

# Status Checking
systemctl status service_name         # Detailed status
systemctl is-active service_name      # Check if running (returns active/inactive)
systemctl is-enabled service_name     # Check if enabled
systemctl is-failed service_name      # Check if failed
systemctl show service_name           # Show all properties

# Listing Services
systemctl list-units --type=service   # Show all services
systemctl list-units --type=service --state=running  # Only running
systemctl list-units --type=service --all            # Include inactive
systemctl list-unit-files --type=service            # Show all unit files
```

### **B. Advanced Service Management**

```bash
# Masking/Unmasking (prevent manual start)
systemctl mask service_name           # Prevent ALL startups (creates symlink to /dev/null)
systemctl unmask service_name         # Remove mask

# Emergency/Rescue Actions
systemctl rescue                     # Enter rescue mode (single-user)
systemctl emergency                  # Enter emergency mode (minimal)
systemctl halt                       # Halt the system
systemctl poweroff                   # Power off
systemctl reboot                     # Reboot

# System State Management
systemctl default                    # Return to default target
systemctl isolate graphical.target   # Switch to graphical mode
systemctl set-default multi-user.target  # Set default boot target

# Daemon Control
systemctl daemon-reload              # Reload systemd config (after unit file changes)
systemctl daemon-reexec              # Re-execute systemd (reloads manager config)

# Resource Management
systemctl set-property service_name CPUQuota=50%  # Limit CPU
systemctl set-property service_name MemoryLimit=1G  # Limit memory
```

### **C. System Analysis & Debugging**

```bash
# Dependency Analysis
systemctl list-dependencies service_name          # Show what service depends on
systemctl list-dependencies --reverse service_name # Show what depends on service
systemctl list-dependencies --before service_name  # Show ordering before
systemctl list-dependencies --after service_name   # Show ordering after

# Performance Analysis
systemd-analyze                      # Show boot time statistics
systemd-analyze blame                # Show services sorted by boot time
systemd-analyze critical-chain       # Show critical chain of units
systemd-analyze plot > boot.svg      # Generate boot timeline SVG
systemd-analyze dot | dot -Tsvg > deps.svg  # Generate dependency graph

# System State Analysis
systemctl --state=failed             # Show all failed units
systemctl --failed --type=service    # Show failed services
systemctl show --property=LoadState,ActiveState,SubState service_name

# Cgroup Inspection
systemd-cgls                         # Show cgroup hierarchy
systemd-cgtop                        # Show cgroup resource usage (like top)
```

## **5. Comprehensive Unit File Examples**

### **A. Simple Service Unit File**

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Custom Application
Documentation=https://example.com/docs
After=network.target nss-lookup.target mysql.service
Requires=mysql.service
Wants=network.target
Before=some-other.service
Conflicts=old-app.service
ConditionPathExists=/opt/myapp/config.conf
AssertPathExists=/opt/myapp/
AssertFileNotEmpty=/opt/myapp/config.conf

[Service]
Type=simple
User=appuser
Group=appgroup
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
ExecStartPre=/opt/myapp/scripts/prepare.sh
ExecStartPost=/opt/myapp/scripts/post-start.sh
ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/opt/myapp/scripts/cleanup.sh
ExecStopPost=/bin/rm -f /tmp/myapp.pid

# Security & Sandboxing
ProtectSystem=strict
ReadWritePaths=/var/lib/myapp /tmp/myapp
PrivateTmp=true
NoNewPrivileges=true
ProtectHome=true
ProtectKernelTunables=true
ProtectKernelModules=true
ProtectControlGroups=true
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6
RestrictNamespaces=true
SystemCallFilter=@system-service
SystemCallErrorNumber=EPERM
MemoryDenyWriteExecute=true
LockPersonality=true

# Resource Management
LimitNOFILE=65536
LimitNPROC=4096
CPUQuota=75%
MemoryLimit=1G
IOWeight=100
CPUShares=1024

# Environment & Runtime
Environment="NODE_ENV=production"
EnvironmentFile=/etc/myapp/env.conf
StandardOutput=journal
StandardError=journal
SyslogIdentifier=myapp
Restart=always
RestartSec=10
StartLimitInterval=100
StartLimitBurst=5
TimeoutStartSec=300
TimeoutStopSec=30
RuntimeMaxSec=86400  # Auto-restart after 24h
SuccessExitStatus=0 1 SIGTERM

# PID File Management
PIDFile=/run/myapp.pid
RemainAfterExit=no

# Notify Support
NotifyAccess=main
WatchdogSec=30

[Install]
WantedBy=multi-user.target
Alias=myappd.service
Also=myapp-socket.service
```

### **B. Socket Activation Unit File**

```ini
# /etc/systemd/system/myapp.socket
[Unit]
Description=MyApp Socket
Documentation=man:myapp(8)

[Socket]
ListenStream=0.0.0.0:8080
ListenDatagram=0.0.0.0:8081
ListenStream=/run/myapp.sock
SocketUser=appuser
SocketGroup=appgroup
SocketMode=0660
Accept=yes  # For multi-instance services (like Apache)
MaxConnections=1024
Backlog=128
ReceiveBuffer=8M
SendBuffer=8M
KeepAlive=yes
KeepAliveTimeSec=300
KeepAliveInterval=30
KeepAliveProbes=3
DeferAcceptSec=1
TimeoutSec=30

[Install]
WantedBy=sockets.target
```

### **C. Timer Unit File (Cron Replacement)**

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Daily Backup Timer
Requires=backup.service

[Timer]
OnCalendar=daily
Persistent=true  # Run missed timers on boot
RandomizedDelaySec=1h  # Add random delay
AccuracySec=1h
Unit=backup.service

# Multiple schedules possible:
# OnCalendar=Mon..Fri 02:00:00
# OnCalendar=*-*-* 00,12:00:00
# OnCalendar=hourly
# OnCalendar=weekly

[Install]
WantedBy=timers.target
```

### **D. Mount Unit File**

```ini
# /etc/systemd/system/mnt-data.mount
[Unit]
Description=Mount Data Partition

[Mount]
What=/dev/sdb1
Where=/mnt/data
Type=ext4
Options=defaults,noatime,nofail
TimeoutSec=30
LazyUnmount=yes

[Install]
WantedBy=multi-user.target
```

### **E. Path Unit File (File/Directory Monitoring)**

```ini
# /etc/systemd/system/upload-processor.path
[Unit]
Description=Monitor Upload Directory

[Path]
PathExists=/var/uploads/
PathChanged=/var/uploads/
PathModified=/var/uploads/
DirectoryNotEmpty=/var/uploads/
MakeDirectory=yes
Unit=upload-processor.service

[Install]
WantedBy=multi-user.target
```

## **6. Service Types Explained**

```ini
[Service]
Type=simple      # Default - ExecStart is main process
Type=forking     # ExecStart forks, parent exits (traditional daemons)
Type=oneshot     # Run once and exit (scripts)
Type=dbus        # D-Bus activated (requires BusName=)
Type=notify      # Uses sd_notify() to signal readiness
Type=idle        # Wait until all jobs finished before starting
```

## **7. Journalctl - Systemd Logging System**

### **Basic Journalctl Commands:**

```bash
# Viewing logs
journalctl                         # View all logs (since boot)
journalctl -f                      # Follow logs (like tail -f)
journalctl -u service_name         # View logs for specific service
journalctl -u nginx -u mysql       # View multiple services
journalctl -p err                  # View only errors
journalctl --since "2024-01-15 10:00:00"
journalctl --until "2024-01-15 11:00:00"
journalctl --since yesterday
journalctl --since "1 hour ago"

# Filtering and output
journalctl -k                      # Kernel messages only
journalctl -b                      # Current boot only
journalctl -b -1                   # Previous boot
journalctl -b -2                   # Boot before previous
journalctl --list-boots           # List all boots
journalctl -o json                 # JSON output
journalctl -o json-pretty         # Pretty JSON
journalctl -o verbose             # Verbose output (all fields)
journalctl -o cat                  # Simple output (no metadata)
journalctl --no-pager             # Disable pager
journalctl -n 100                 # Show last 100 entries
journalctl --disk-usage           # Show journal disk usage

# Advanced filtering
journalctl _PID=1234              # Filter by PID
journalctl _UID=1000              # Filter by UID
journalctl _SYSTEMD_UNIT=ssh.service
journalctl _COMM=sshd             # Filter by command
journalctl _EXE=/usr/bin/bash     # Filter by executable
journalctl SYSLOG_IDENTIFIER=myapp
journalctl TAG=important
journalctl MESSAGE_ID=1234567890abcdef
journalctl +/usr/bin/nginx        # Filter by executable path

# Journal management
journalctl --vacuum-size=100M     # Reduce journal to 100MB
journalctl --vacuum-time=1weeks   # Keep only last week
journalctl --rotate               # Rotate journal files
journalctl --flush                # Flush to disk
journalctl --sync                 # Sync unwritten to journal
journalctl --header               # Show journal header info
```

### **Permanent Journal Configuration:**
```ini
# /etc/systemd/journald.conf
[Journal]
Storage=persistent          # auto, persistent, volatile, none
Compress=yes               # Compress old logs
Seal=yes                   # Use Forward Secure Sealing (FSS)
SplitMode=uid              # uid, none, login
SyncIntervalSec=5m
RateLimitInterval=30s
RateLimitBurst=1000
SystemMaxUse=1G
SystemKeepFree=2G
SystemMaxFileSize=100M
RuntimeMaxUse=100M
MaxRetentionSec=1month
MaxFileSec=1month
```

## **8. Real-World Examples & Use Cases**

### **A. Docker Container as Systemd Service**

```ini
# /etc/systemd/system/docker-postgres.service
[Unit]
Description=PostgreSQL Docker Container
Requires=docker.service
After=docker.service network.target

[Service]
Type=simple
Restart=always
RestartSec=10
TimeoutStartSec=300

ExecStartPre=-/usr/bin/docker stop postgres
ExecStartPre=-/usr/bin/docker rm postgres
ExecStartPre=/usr/bin/docker pull postgres:15

ExecStart=/usr/bin/docker run \
  --name postgres \
  --hostname postgres \
  --network my-network \
  --restart unless-stopped \
  --memory 2g \
  --memory-swap 2g \
  --cpus 1.5 \
  --cpu-shares 1024 \
  --pids-limit 200 \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  -e POSTGRES_PASSWORD_FILE=/run/secrets/postgres_password \
  -e POSTGRES_DB=appdb \
  -v /var/lib/postgresql/data:/var/lib/postgresql/data \
  -v /etc/postgresql/config:/etc/postgresql \
  --mount type=bind,source=/opt/backups,destination=/backups \
  --mount type=tmpfs,destination=/tmp \
  postgres:15 \
  -c 'max_connections=100' \
  -c 'shared_buffers=256MB'

ExecStop=/usr/bin/docker stop -t 30 postgres
ExecStopPost=/usr/bin/docker rm -f postgres

[Install]
WantedBy=multi-user.target
```

### **B. Python Application with Virtual Environment**

```ini
# /etc/systemd/system/flask-app.service
[Unit]
Description=Flask Web Application
After=network.target postgresql.service redis.service
Requires=postgresql.service
Wants=redis.service

[Service]
Type=simple
User=flaskuser
Group=flaskgroup
WorkingDirectory=/opt/flask-app

# Virtual environment activation
Environment="PATH=/opt/flask-app/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Environment="PYTHONPATH=/opt/flask-app"
Environment="FLASK_APP=app.py"
Environment="FLASK_ENV=production"

# Read environment variables from file
EnvironmentFile=/etc/flask-app/environment

# Security hardening
PrivateTmp=true
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/var/log/flask-app /var/lib/flask-app
PrivateDevices=true
ProtectKernelTunables=true
ProtectKernelModules=true
ProtectControlGroups=true
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6
RestrictRealtime=true
SystemCallFilter=@system-service
SystemCallArchitectures=native
MemoryDenyWriteExecute=true
LockPersonality=true

# Process management
ExecStart=/opt/flask-app/venv/bin/gunicorn \
  --workers 4 \
  --worker-class gevent \
  --bind unix:/run/flask-app.sock \
  --access-logfile /var/log/flask-app/access.log \
  --error-logfile /var/log/flapp-app/error.log \
  --user flaskuser \
  --group flaskgroup \
  --max-requests 1000 \
  --max-requests-jitter 50 \
  --timeout 30 \
  --graceful-timeout 30 \
  --keep-alive 5 \
  app:app

ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/bin/kill -TERM $MAINPID

# Auto-restart on failure
Restart=always
RestartSec=10
StartLimitIntervalSec=600
StartLimitBurst=5

# Resource limits
LimitNOFILE=65536
LimitNPROC=4096
LimitCORE=0
CPUQuota=80%
MemoryMax=2G
MemoryHigh=1.8G
IOWeight=100

# Standard output/error
StandardOutput=journal
StandardError=journal
SyslogIdentifier=flask-app

# PID file (optional)
PIDFile=/run/flask-app.pid

[Install]
WantedBy=multi-user.target
```

### **C. Nginx with Socket Activation**

```ini
# /etc/systemd/system/nginx.socket
[Unit]
Description=nginx socket
PartOf=nginx.service

[Socket]
ListenStream=0.0.0.0:80
ListenStream=0.0.0.0:443
ListenStream=[::]:80
ListenStream=[::]:443
SocketUser=root
SocketGroup=nginx
SocketMode=0660

[Install]
WantedBy=sockets.target
```

### **D. Backup Script with Timer**

```ini
# /etc/systemd/system/backup.service
[Unit]
Description=Database Backup Service
Requires=postgresql.service
After=postgresql.service

[Service]
Type=oneshot
User=backup
Group=backup

# Environment
Environment="BACKUP_DIR=/backups"
Environment="DB_NAME=mydb"
Environment="RETENTION_DAYS=30"

# Security
NoNewPrivileges=true
PrivateTmp=true
ReadWritePaths=/backups
ReadOnlyPaths=/etc/postgresql

ExecStart=/usr/local/bin/backup.sh

# Logging
StandardOutput=journal+console
StandardError=journal+console
SyslogIdentifier=backup

# Success/failure codes
SuccessExitStatus=0 1
```

```ini
# /etc/systemd/system/backup.timer
[Unit]
Description=Daily Database Backup Timer

[Timer]
OnCalendar=daily
AccuracySec=1h
RandomizedDelaySec=30m
Persistent=true

[Install]
WantedBy=timers.target
```

### **E. Systemd User Service (for user-specific daemons)**

```ini
# ~/.config/systemd/user/syncthing.service
[Unit]
Description=Syncthing - Personal File Sync
Documentation=https://docs.syncthing.net/

[Service]
Type=simple
ExecStart=/usr/bin/syncthing serve --no-browser --logfile=/home/%u/.config/syncthing/syncthing.log
Restart=on-failure
RestartSec=5
SuccessExitStatus=0 2
Environment=STNORESTART=1
Nice=10
IOSchedulingClass=idle

[Install]
WantedBy=default.target
```

Enable with:
```bash
systemctl --user enable syncthing
systemctl --user start syncthing
loginctl enable-linger username  # Keep running after logout
```

## **9. Advanced Systemctl Features**

### **A. Drop-in Configuration (Overrides)**

Instead of modifying unit files directly, use drop-ins:
```bash
# Create override directory
mkdir -p /etc/systemd/system/nginx.service.d/

# Create override file
cat > /etc/systemd/system/nginx.service.d/override.conf << EOF
[Service]
Environment="NGINX_WORKER_PROCESSES=8"
LimitNOFILE=65536
Restart=always
RestartSec=10
EOF

# Apply changes
systemctl daemon-reload
systemctl restart nginx

# View merged configuration
systemctl cat nginx
```

### **B. Transient Units (Temporary Services)**

```bash
# Create temporary service (disappears on stop/reboot)
systemd-run --unit=temp-job --description="Temporary job" \
  --property="Type=oneshot" \
  --property="User=nobody" \
  --property="Group=nogroup" \
  /path/to/script.sh

# With resource limits
systemd-run --unit=limited-task \
  --property="CPUQuota=50%" \
  --property="MemoryLimit=512M" \
  --property="IOWeight=50" \
  /usr/bin/stress --cpu 4 --io 2 --vm 2 --vm-bytes 256M --timeout 60s

# View status
systemctl status temp-job
```

### **C. Systemd Socket Activation Example**

Create socket and service:
```ini
# /etc/systemd/system/echo.socket
[Unit]
Description=Echo Server Socket

[Socket]
ListenStream=0.0.0.0:7777
Accept=yes

[Install]
WantedBy=sockets.target
```

```ini
# /etc/systemd/system/echo@.service
[Unit]
Description=Echo Server Instance

[Service]
Type=simple
ExecStart=-/usr/bin/nc -k -l 7777 -e /bin/cat
StandardInput=socket
```

Test with: `echo "Hello" | nc localhost 7777`

### **D. Instantiated Services (Template Units)**

```ini
# /etc/systemd/system/container@.service
[Unit]
Description=Container %i
After=network.target docker.service

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/docker start -a %i
ExecStop=/usr/bin/docker stop -t 30 %i

[Install]
WantedBy=multi-user.target
```

Usage:
```bash
systemctl start container@webapp
systemctl start container@database
```

## **10. Troubleshooting & Debugging**

### **A. Common Issues and Solutions**

```bash
# Service won't start
systemctl status service_name            # Check status
journalctl -u service_name -f           # Follow logs
systemctl cat service_name              # View complete config
systemd-analyze verify service_name.service  # Check syntax

# Service starts but exits immediately
journalctl -u service_name --since "5 minutes ago" -o cat
systemctl show service_name -p Type     # Check service type
systemctl show service_name -p ExecStart

# Dependency issues
systemctl list-dependencies service_name --reverse
systemctl list-jobs                      # See pending jobs

# Boot problems
systemd-analyze critical-chain          # Find boot bottlenecks
systemd-analyze blame                    # See slowest services
systemctl --failed                      # See failed units

# Permission issues
systemd-analyze security service_name   # Check security context
id appuser                              # Verify user exists
ls -la /path/to/working/directory       # Check permissions

# Resource constraints
systemctl show service_name -p MemoryCurrent,MemoryMax
systemd-cgtop                           # Monitor cgroup usage
```

### **B. Debug Mode**

```bash
# Run service with debug output
systemctl run service_name --debug

# Enable debug logging for systemd itself
mkdir -p /etc/systemd/system/systemd-journald.service.d/
cat > /etc/systemd/system/systemd-journald.service.d/debug.conf << EOF
[Service]
Environment=SYSTEMD_LOG_LEVEL=debug
EOF

systemctl daemon-reload
systemctl restart systemd-journald
```

### **C. Emergency Recovery**

```bash
# Boot into emergency mode
# Edit kernel cmdline in GRUB: add "systemd.unit=emergency.target"

# From running system:
systemctl rescue                      # Single-user mode with networking
systemctl emergency                   # Minimal rescue shell

# Reset failed units
systemctl reset-failed               # Reset all failed units
systemctl reset-failed service_name  # Reset specific service
```

## **11. Performance Tuning**

### **A. Optimizing Boot Time**

```bash
# Analyze boot performance
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain
systemd-analyze plot > boot.svg

# Disable slow/unnecessary services
systemctl mask systemd-timesyncd    # If using NTP elsewhere
systemctl mask bluetooth            # If not using Bluetooth
systemctl disable NetworkManager-wait-online  # If not needed

# Parallelize startup
# Edit: /etc/systemd/system.conf
# DefaultStartLimitIntervalSec=10s -> 5s
# DefaultTimeoutStartSec=90s -> 30s
# DefaultTimeoutStopSec=90s -> 30s
```

### **B. Resource Optimization**

```ini
# In service files:
[Service]
# Memory management
MemoryMax=1G
MemoryHigh=900M
MemorySwapMax=2G

# CPU management
CPUQuota=75%
CPUWeight=100
CPUQuotaPeriodSec=100ms

# I/O management
IOWeight=100
IOReadBandwidthMax=/dev/sda 10M
IOWriteBandwidthMax=/dev/sda 10M
```

## **12. Security Hardening**

### **A. Service Sandboxing**

```ini
[Service]
# Filesystem isolation
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true
PrivateDevices=true
PrivateUsers=true  # User namespacing
ProtectHostname=true
ProtectKernelTunables=true
ProtectKernelModules=true
ProtectControlGroups=true

# Network restrictions
PrivateNetwork=false  # or true for complete network isolation
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6
IPAddressDeny=any
IPAddressAllow=localhost
IPAddressAllow=192.168.1.0/24

# Capabilities
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
AmbientCapabilities=CAP_NET_BIND_SERVICE
NoNewPrivileges=true

# System call filtering
SystemCallFilter=@system-service
SystemCallArchitectures=native
SystemCallErrorNumber=EPERM

# Process restrictions
RestrictSUIDSGID=true
RestrictRealtime=true
LockPersonality=true
MemoryDenyWriteExecute=true
ProtectProc=invisible
ProcSubset=pid
```

### **B. Security Analysis**

```bash
# Check service security
systemd-analyze security service_name
systemd-analyze security --pretty service_name
systemd-analyze security --no-pager service_name

# Generate security profile
systemd-analyze unit-paths
```

## **13. Systemd Timers vs Cron**

**Advantages of systemd timers:**
- Integrated logging with journald
- Dependency management
- Monotonic timers (relative to boot)
- Calendar events with timezones
- Persistent timers (run missed jobs)
- Resource control (cgroups)
- Socket activation compatibility

**Conversion example:**
```crontab
# Cron: 0 2 * * * /usr/local/bin/backup.sh
```

```ini
# Timer equivalent
[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true
RandomizedDelaySec=1h
```

## **14. Integration Examples**

### **A. With Docker Compose**

```ini
# /etc/systemd/system/docker-compose-app.service
[Unit]
Description=Docker Compose Application
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/docker-compose-app
ExecStart=/usr/bin/docker-compose up -d
ExecStop=/usr/bin/docker-compose down
ExecReload=/usr/bin/docker-compose restart
TimeoutStartSec=300
TimeoutStopSec=30

[Install]
WantedBy=multi-user.target
```

### **B. With Kubernetes**

```ini
# /etc/systemd/system/k3s.service
[Unit]
Description=Lightweight Kubernetes
Documentation=https://k3s.io
After=network-online.target

[Service]
Type=notify
EnvironmentFile=/etc/systemd/system/k3s.service.env
KillMode=process
Delegate=yes
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
TasksMax=infinity
TimeoutStartSec=0
Restart=always
RestartSec=5s
ExecStartPre=-/sbin/modprobe br_netfilter
ExecStartPre=-/sbin/modprobe overlay
ExecStart=/usr/local/bin/k3s \
    server \
    --disable-cloud-controller \
    --disable=servicelb \
    --disable=traefik \
    --write-kubeconfig-mode=644

[Install]
WantedBy=multi-user.target
```

### **C. With Database Failover**

```ini
# /etc/systemd/system/postgresql-failover.service
[Unit]
Description=PostgreSQL Failover Monitor
After=network.target
ConditionPathExists=/usr/local/bin/pg_failover_monitor

[Service]
Type=simple
User=postgres
Group=postgres
Restart=always
RestartSec=10

# Monitor primary
ExecStart=/usr/local/bin/pg_failover_monitor \
    --primary-host=pg-primary.example.com \
    --standby-host=pg-standby.example.com \
    --promotion-script=/usr/local/bin/promote_standby.sh \
    --check-interval=30

# Watchdog for self-monitoring
WatchdogSec=60

[Install]
WantedBy=multi-user.target
```

## **15. Best Practices**

1. **Never edit** `/usr/lib/systemd/system/` files - use `/etc/systemd/system/` for overrides
2. Always run `systemctl daemon-reload` after changing unit files
3. Use `systemd-analyze verify` to check syntax before reloading
4. Include `[Install]` section in custom services
5. Use `Wants=` instead of `Requires=` for optional dependencies
6. Set appropriate `Restart=` policies
7. Implement proper security sandboxing
8. Use `journalctl` for logging instead of custom log files
9. Test with `--dry-run` for complex commands
10. Use templates for multiple similar services

## **16. Quick Reference Cheat Sheet**

```bash
# Service Management
systemctl start|stop|restart|reload|status SERVICE

# Enable/Disable
systemctl enable|disable SERVICE
systemctl is-enabled SERVICE

# System State
systemctl reboot|poweroff|halt|suspend|hibernate
systemctl rescue|emergency

# Logs
journalctl -fu SERVICE      # Follow logs
journalctl -b -1           # Previous boot
journalctl --since "1 hour ago"

# Analysis
systemd-analyze blame      # Boot time analysis
systemd-analyze security   # Security analysis

# Debugging
systemctl cat SERVICE      # Show full config
systemctl show SERVICE     # Show properties
systemctl list-dependencies SERVICE
```

## **Conclusion**

Systemd has revolutionized Linux service management by providing:

1. **Unified interface** for all system components
2. **Parallel startup** for faster boot times
3. **Sophisticated dependency management**
4. **Integrated logging** with structured metadata
5. **Resource control** through cgroups
6. **Socket activation** for on-demand services
7. **Template units** for mass deployment
8. **Security features** for service isolation

While systemd has been controversial in some circles, its comprehensive feature set and widespread adoption make it essential knowledge for any Linux system administrator or DevOps engineer.