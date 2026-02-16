Below is a **hands-on, step-by-step lab walkthrough** you can run on any modern Linux distro that uses **systemd** (Ubuntu, Fedora, Debian, RHEL, etc.).

This lab will teach you:

- How boot targets work
    
- How services are created and managed
    
- How logging works with `journalctl`
    
- How resource limits are applied
    
- How dependencies affect startup
    
- How to inspect the boot process
    

---

# 🧪 LAB: Exploring systemd in Practice

> ⚠️ You’ll need sudo privileges.

---

# 🔹 Part 1 — Inspect the Running System

### 1️⃣ Confirm systemd is PID 1

```bash
ps -p 1 -o comm=
```

Expected output:

```
systemd
```

---

### 2️⃣ Check Default Boot Target

```bash
systemctl get-default
```

Common outputs:

- `multi-user.target`
    
- `graphical.target`
    

List all targets:

```bash
systemctl list-units --type=target
```

---

### 3️⃣ Analyze Boot Performance

```bash
systemd-analyze
```

More detail:

```bash
systemd-analyze blame
systemd-analyze critical-chain
```

---

# 🔹 Part 2 — Create Your Own Service

We’ll create a simple custom service.

---

### 1️⃣ Create a Test Script

```bash
sudo nano /usr/local/bin/lab-service.sh
```

Paste:

```bash
#!/bin/bash
while true; do
    echo "Lab service running at $(date)"
    sleep 10
done
```

Make executable:

```bash
sudo chmod +x /usr/local/bin/lab-service.sh
```

---

### 2️⃣ Create a systemd Unit File

```bash
sudo nano /etc/systemd/system/lab.service
```

Paste:

```ini
[Unit]
Description=My Lab Test Service
After=network.target

[Service]
ExecStart=/usr/local/bin/lab-service.sh
Restart=always
User=nobody

[Install]
WantedBy=multi-user.target
```

---

### 3️⃣ Reload systemd

```bash
sudo systemctl daemon-reload
```

---

### 4️⃣ Start the Service

```bash
sudo systemctl start lab.service
```

Check status:

```bash
systemctl status lab.service
```

---

### 5️⃣ Enable at Boot

```bash
sudo systemctl enable lab.service
```

This creates a symlink under:

```
/etc/systemd/system/multi-user.target.wants/
```

---

# 🔹 Part 3 — Explore Logging (journalctl)

View logs for your service:

```bash
journalctl -u lab.service
```

Follow live logs:

```bash
journalctl -u lab.service -f
```

View logs from current boot:

```bash
journalctl -b
```

---

# 🔹 Part 4 — Experiment with Resource Control

Edit the unit file:

```bash
sudo nano /etc/systemd/system/lab.service
```

Add under `[Service]`:

```ini
MemoryMax=50M
CPUQuota=20%
```

Reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl restart lab.service
```

Check applied limits:

```bash
systemctl show lab.service | grep -E 'Memory|CPU'
```

---

# 🔹 Part 5 — Work With Targets

Switch temporarily to CLI mode:

```bash
sudo systemctl isolate multi-user.target
```

Return to GUI:

```bash
sudo systemctl isolate graphical.target
```

⚠️ This will close graphical session when isolating multi-user.

---

# 🔹 Part 6 — Explore User Sessions

List sessions:

```bash
loginctl list-sessions
```

Inspect current user:

```bash
loginctl show-user $USER
```

---

# 🔹 Part 7 — Create a Timer (Cron Replacement)

Instead of cron, use systemd timer.

---

### 1️⃣ Create Service

```bash
sudo nano /etc/systemd/system/lab-timer.service
```

```ini
[Unit]
Description=Lab Timer Service

[Service]
Type=oneshot
ExecStart=/usr/bin/date >> /tmp/lab-timer.log
```

---

### 2️⃣ Create Timer

```bash
sudo nano /etc/systemd/system/lab-timer.timer
```

```ini
[Unit]
Description=Run Lab Timer Every Minute

[Timer]
OnCalendar=*-*-* *:*:00
Persistent=true

[Install]
WantedBy=timers.target
```

---

### 3️⃣ Enable Timer

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now lab-timer.timer
```

Check timers:

```bash
systemctl list-timers
```

Check output:

```bash
cat /tmp/lab-timer.log
```

---

# 🔹 Part 8 — Dependency Experiment

Modify lab.service:

```ini
After=network.target
Requires=network.target
```

Restart and observe ordering:

```bash
systemctl list-dependencies lab.service
```

---

# 🔹 Part 9 — Inspect cgroup Hierarchy

```bash
systemd-cgls
```

or:

```bash
systemd-cgtop
```

You’ll see your lab service under:

```
system.slice
```

---

# 🔹 Part 10 — Simulate Failure & Restart

Kill service process:

```bash
sudo pkill -f lab-service.sh
```

Check:

```bash
systemctl status lab.service
```

Because of:

```
Restart=always
```

systemd automatically restarts it.

---

# 🔹 Part 11 — Cleanup

```bash
sudo systemctl disable --now lab.service
sudo rm /etc/systemd/system/lab.service
sudo rm /usr/local/bin/lab-service.sh

sudo systemctl disable --now lab-timer.timer
sudo rm /etc/systemd/system/lab-timer.*
sudo systemctl daemon-reload
```

---

# 🎓 What You Learned

You now understand:

✔ How systemd manages services  
✔ How unit files work  
✔ How logging works  
✔ How targets control boot modes  
✔ How timers replace cron  
✔ How resource control works  
✔ How dependencies shape startup  
✔ How cgroups organize processes

---

# 🚀 Advanced Optional Challenges

If you want to go deeper:

- Create a socket-activated service
    
- Create a path-triggered service
    
- Modify default target permanently
    
- Write a custom generator
    
- Boot into rescue.target and analyze differences
    
- Use `systemd-analyze plot > boot.svg`
    

---

If you'd like, I can create:

- 🔬 An advanced production-style lab
    
- 🧩 A troubleshooting challenge scenario
    
- 🐳 A systemd + container lab
    
- 🔥 A deep-dive into dependency debugging
    
- 🧠 A mental model cheat sheet for interviews