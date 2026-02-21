Below is a **comprehensive deep dive on systemd** — what it is, how it works, core concepts, common use cases, troubleshooting, and advanced topics. The goal is to help you understand _not just how to use it_ but _why it’s designed the way it is_.

---

## 🚀 What Is systemd?

**systemd** is a system and service manager for Linux — _the first process started by the kernel during boot (`PID 1`)_ — responsible for:

- Starting and stopping services (daemons)
    
- Mounting file systems
    
- Managing sockets, timers, and devices
    
- Logging (via `journald`)
    
- Controlling the boot process
    
- Handling sessions and user services
    

systemd replaced older init systems such as **SysV init** and **Upstart**, providing **parallel startup, dependency tracking, dynamic control, and more consistent configuration**.

---

## 🧠 Why systemd Matters

Traditional init systems were serial and script-based, leading to:

- Slow boot times
    
- Hard-to-maintain dependency graphs
    
- Custom scripts with inconsistent behavior
    

systemd modernizes this with:

- **Parallel service startup**
    
- **Declarative unit files**
    
- **Event-based activation**
    
- **Granular control & introspection tools**
    
- Centralized logging
    

---

## 📦 Key Concepts

### 🔹 Units

A _unit_ is any object systemd manages. Units are represented by files under:

```
/etc/systemd/system
/run/systemd/system
/usr/lib/systemd/system
```

Each unit type serves a purpose:

|Unit Type|Suffix|Purpose|
|---|---|---|
|Service|`.service`|Manages daemons|
|Socket|`.socket`|Socket activation|
|Target|`.target`|Boot milestones (like SysV runlevels)|
|Timer|`.timer`|Scheduled activation|
|Mount|`.mount`|Mount points|
|Device|`.device`|Kernel devices|
|Path|`.path`|Path change triggers|
|Slice|`.slice`|Resource control|
|Scope|`.scope`|Externally created processes|

---

## 🧩 Unit Files — Anatomy

Unit files declare how a service should behave. Example:

```
[Unit]
Description=My App
After=network.target

[Service]
ExecStart=/usr/bin/myapp --serve
Restart=on-failure
User=myuser

[Install]
WantedBy=multi-user.target
```

Key sections:

- **[Unit]**: metadata, dependencies
    
- **[Service]**: how to start the process
    
- **[Install]**: how it’s linked into boot targets
    

---

## 🔁 Targets — Modern Runlevels

Targets group units. Analogous to old runlevels:

|Target|Description|
|---|---|
|`default.target`|System default|
|`multi-user.target`|CLI mode|
|`graphical.target`|GUI|
|`network.target`|Networking ready|
|`rescue.target`|Single user mode|

Use:

```
systemctl get-default
systemctl set-default multi-user.target
```

---

## ▶️ Controlling Services

### Start/Stop/Restart

```
sudo systemctl start foo.service
sudo systemctl stop foo.service
sudo systemctl restart foo.service
```

### Enable/Disable at Boot

```
sudo systemctl enable foo.service
sudo systemctl disable foo.service
```

### Status & Logs

```
systemctl status foo.service
journalctl -u foo.service
```

---

## 🧠 Dependencies & Ordering

systemd builds a **dependency graph**. Common dependency options:

- **Requires=** – must start; failure propagates
    
- **Wants=** – soft dependency
    
- **After=** – ordering (not a hard requirement)
    
- **Before=** – reverse ordering
    

Example:

```
After=network.target mysqld.service
```

---

## 📈 Parallel Booting

systemd starts units in parallel where possible, speeding boot time.

Use:

```
systemd-analyze
systemd-analyze blame
systemd-analyze critical-chain
```

These show boot time breakdowns and dependency paths.

---

## 🔥 Socket & Path Activation

### Socket Activation

Listen on sockets and start services on demand:

```
foo.socket
[Socket]
ListenStream=8080

[Install]
WantedBy=sockets.target
```

Benefits:

- Fast boot
    
- Services start only on demand
    

### Path Activation

Watch files/dirs:

```
foo.path
[Path]
PathModified=/etc/foo/config
```

Triggers a service when something changes.

---

## 📆 Timer Units

Timers replace cron for system services:

```
foo.timer
[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

Start with:

```
sudo systemctl enable --now foo.timer
```

---

## 📜 Logging — journalctl

systemd’s logging is centralized:

```
journalctl
journalctl -u foo.service
journalctl -b             # since boot
journalctl --since today
```

Logs are binary and can be persisted to disk.

---

## 👤 User Services

Users can define per-user services:

Start the user manager:

```
systemctl --user start foo.service
```

List user units:

```
systemctl --user list-units
```

---

## 🛠 Advanced Features

### cgroups & Resource Control

Units can be placed in slices and controlled:

```
CPUQuota=50%
MemoryLimit=1G
```

### SELinux & Security

systemd can integrate with SELinux/AppArmor for sandboxing.

### Dynamic Devices

Units for devices appear automatically under `.device` when the kernel notifies systemd.

---

## 🧪 Debugging

Useful tools:

```
systemctl list-dependencies foo.service
systemctl show foo.service
strace systemd
journalctl -xe
```

Check for:

- Missing dependencies
    
- Misconfigured unit files
    
- Permission or environment issues
    

---

## 🧱 Best Practices

- **Use Wants/After**, not hard Requires unless necessary
    
- **Keep unit files simple and declarative**
    
- Don’t reinvent cron — use `.timer` units
    
- Log to journal, use structured logs
    
- Version-control custom units
    

---

## 🧰 Example Real-World Unit

```
[Unit]
Description=Web App
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/webapp
ExecStart=/opt/webapp/bin/start
Restart=on-failure
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```

---

## 📚 Further Learning

- `man systemd` / `man systemctl`
    
- `man systemd.unit`, `man systemd.service`
    
- systemd source docs / tutorials
    

---
