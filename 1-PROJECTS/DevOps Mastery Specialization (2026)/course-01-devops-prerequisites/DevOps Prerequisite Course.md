# DevOps Prerequisite Course — Course 1

### A Comprehensive Tutorial with Hands-On Labs

---

## Table of Contents

- [Module 1 – DevOps Tools and Linux](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-1--devops-tools-and-linux)
    - [Understanding DevOps](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#understanding-devops)
    - [Working Your Way Through the CLI](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#working-your-way-through-the-cli)
    - [Mastering the VI Editor](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#mastering-the-vi-editor)
    - [More Linux Commands](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#more-linux-commands)
    - [Understanding Package Management](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#understanding-package-management)
    - [Managing System Services](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#managing-system-services)
    - [Module 1 Assessment](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-1-assessment)
- [Module 2 – Networking](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-2--networking)
    - [Essential Networking Principles](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#essential-networking-principles)
    - [Exploring the Domain Name System](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#exploring-the-domain-name-system)
    - [Module 2 Assessment](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-2-assessment)
- [Module 3 – Applications Basics](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-3--applications-basics)
    - [Java – Introduction and Build & Packaging](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#java--introduction-and-build--packaging)
    - [Node.js – Introduction and NPM](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#nodejs--introduction-and-npm)
    - [Python – Introduction and PIP](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#python--introduction-and-pip)
    - [Module 3 Assessment](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#module-3-assessment)
- [Quick Reference Card](https://claude.ai/local_sessions/local_c16524e5-1c07-464f-ba05-5cd93beac4e2#quick-reference-card)

---

# Module 1 – DevOps Tools and Linux

## Learning Objectives

By the end of this module you will be able to:

- Understand the purpose and scope of the DevOps Prerequisite course
- Master essential Linux commands and their applications in the CLI
- Develop proficiency in using the VI Editor
- Understand package management principles on Linux
- Manage system services with `systemctl`

---

## Understanding DevOps

### From Manual Tasks to DevOps Workflows

Before DevOps existed, software teams operated in silos. Developers wrote code, threw it "over the wall" to Operations, and waited days or weeks for it to appear in production. Operations manually configured servers, ran deployment scripts by hand, and treated infrastructure as precious, unrepeatable snowflakes.

DevOps is a cultural and technical movement that bridges that gap. It is built on three foundational ideas:

```
  ┌───────────────────────────────────────────-──────────┐
  │                  The DevOps Loop                     │
  │                                                      │
  │   Plan → Code → Build → Test → Release → Deploy      │
  │     ↑                                       │        │
  │     └─────────── Monitor & Operate ◄────────┘        │
  └──────────────────────────────────────────────────-───┘
```

**Key DevOps Principles:**

|Principle|Description|
|---|---|
|**Collaboration**|Dev and Ops share ownership of the full delivery pipeline|
|**Automation**|Eliminate manual, repetitive tasks wherever possible|
|**Continuous Integration**|Merge and test code frequently (multiple times per day)|
|**Continuous Delivery**|Always have a deployable artifact ready|
|**Infrastructure as Code**|Define servers and environments in version-controlled files|
|**Monitoring & Feedback**|Observe production continuously; feed learnings back into dev|

### The DevOps Toolchain

A typical DevOps toolchain spans the entire software lifecycle:

```
  SOURCE CONTROL     CI/CD            CONFIG MGMT       CONTAINERS
  ──────────────     ────────         ───────────        ──────────
  Git / GitHub       Jenkins          Ansible            Docker
  GitLab             GitLab CI        Puppet             Kubernetes
  Bitbucket          GitHub Actions   Chef               Helm

  MONITORING         CLOUD            INFRASTRUCTURE     ARTIFACT
  ──────────         ─────            ──────────────     ────────
  Prometheus         AWS              Terraform          Nexus
  Grafana            Azure            Pulumi             JFrog
  ELK Stack          GCP              CloudFormation     Docker Hub
```

All of these tools share one thing: they run on **Linux**. Mastering Linux is the essential prerequisite for every tool in this list.

### Why Linux?

- Over **96%** of the world's top web servers run Linux
- All major cloud providers (AWS, Azure, GCP) default to Linux VMs
- Docker, Kubernetes, and most CI/CD tools run natively on Linux
- Shell scripting (Bash) is the universal automation glue of DevOps

---

## Working Your Way Through the CLI

### The Shell

The **shell** is a program that reads your commands and passes them to the operating system kernel. The most common shell in Linux is **Bash** (Bourne Again SHell).

```
  You → Terminal → Shell (Bash) → Kernel → Hardware
```

When you open a terminal, you see a **prompt**:

```bash
username@hostname:~$
# username  = who you are
# hostname  = machine name
# ~         = current directory (~ means your home directory)
# $         = regular user  (# means root/superuser)
```

### Navigating the Filesystem

Linux uses a single tree rooted at `/` (the root directory):

```
/
├── bin/       → Essential user binaries (ls, cp, mv…)
├── boot/      → Bootloader and kernel files
├── dev/       → Device files
├── etc/       → System configuration files
├── home/      → User home directories (/home/alice, /home/bob)
├── lib/       → Shared libraries
├── opt/       → Optional/third-party software
├── proc/      → Virtual filesystem for process info
├── root/      → Root user's home directory
├── srv/       → Service data (web, FTP)
├── sys/       → Virtual filesystem for kernel/hardware info
├── tmp/       → Temporary files (cleared on reboot)
├── usr/       → User programs and data
│   ├── bin/   → Non-essential user binaries
│   ├── lib/   → Libraries for /usr/bin
│   └── local/ → Locally compiled software
└── var/       → Variable data (logs, databases, spool)
    └── log/   → System and application logs
```

**Navigation Commands:**

```bash
# Print working directory (where am I?)
pwd
# /home/alice

# List directory contents
ls                    # basic list
ls -l                 # long format (permissions, owner, size, date)
ls -la                # include hidden files (starting with .)
ls -lh                # human-readable file sizes (KB, MB, GB)
ls -lt                # sort by modification time (newest first)
ls /etc               # list a specific directory

# Change directory
cd /etc               # absolute path (from root)
cd Documents          # relative path (from current location)
cd ..                 # go up one level
cd ../..              # go up two levels
cd ~                  # go to your home directory
cd -                  # go to the previous directory

# Create directories
mkdir projects
mkdir -p projects/devops/ansible   # create nested dirs at once

# Remove directories
rmdir empty-dir                    # remove empty directory
rm -rf old-project/                # remove directory and all contents (CAREFUL!)
```

### Working with Files

```bash
# Create an empty file
touch notes.txt
touch file1.txt file2.txt file3.txt   # create multiple at once

# View file contents
cat file.txt                    # print entire file
cat -n file.txt                 # print with line numbers
less file.txt                   # paginated view (q to quit, / to search)
more file.txt                   # older paginator
head file.txt                   # first 10 lines
head -n 20 file.txt             # first 20 lines
tail file.txt                   # last 10 lines
tail -n 50 file.txt             # last 50 lines
tail -f /var/log/syslog         # follow a log in real time (Ctrl+C to stop)

# Copy files
cp source.txt destination.txt
cp -r source-dir/ destination-dir/   # recursive copy (for directories)
cp -p file.txt backup.txt            # preserve timestamps and permissions

# Move and rename
mv old-name.txt new-name.txt    # rename
mv file.txt /tmp/               # move to /tmp
mv dir1/ /opt/newdir            # move and rename directory

# Delete files
rm file.txt
rm -i file.txt                  # interactive (asks for confirmation)
rm -f file.txt                  # force (no confirmation)
rm *.log                        # delete all .log files

# Create a symbolic link (shortcut)
ln -s /opt/myapp/bin/myapp /usr/local/bin/myapp

# Find files
find /home -name "*.txt"                   # find by name
find /var/log -name "*.log" -mtime -7      # logs modified in last 7 days
find / -size +100M                         # files larger than 100 MB
find /etc -type f -name "*.conf"           # config files only

# Search inside files
grep "error" /var/log/syslog               # find lines containing "error"
grep -i "error" /var/log/syslog            # case-insensitive
grep -r "DATABASE_URL" /opt/myapp/         # search recursively
grep -n "def main" src/app.py              # show line numbers
grep -v "DEBUG" app.log                    # exclude lines matching pattern
grep -c "ERROR" app.log                    # count matching lines
```

### File Permissions

Linux uses a permission model with three categories and three permission types:

```
-rwxr-xr--  1  alice  developers  4096  Apr 01 10:00  script.sh
│└──┘└──┘└─┘   │      │           │     │             │
│ │    │  │    │      │           │     │             └── filename
│ │    │  │    │      │           │     └── date modified
│ │    │  │    │      │           └── file size (bytes)
│ │    │  │    │      └── group owner
│ │    │  │    └── user owner
│ │    │  └── other permissions (r--)
│ │    └── group permissions (r-x)
│ └── owner permissions (rwx)
└── file type (- = file, d = directory, l = symlink)

r = read    (4)
w = write   (2)
x = execute (1)
```

```bash
# Change permissions (symbolic)
chmod u+x script.sh         # add execute for owner
chmod g-w file.txt          # remove write for group
chmod o=r file.txt          # set other to read-only
chmod a+x script.sh         # add execute for all (a = all)
chmod ug+rw file.txt        # add read+write for owner and group

# Change permissions (numeric/octal)
chmod 755 script.sh         # rwxr-xr-x (common for executables)
chmod 644 config.txt        # rw-r--r-- (common for config files)
chmod 600 private-key.pem   # rw------- (private key, owner only)
chmod 777 shared/           # rwxrwxrwx (everyone can do everything — avoid!)

# Change owner
chown alice file.txt
chown alice:developers file.txt   # change owner and group
chown -R alice:developers /opt/myapp/  # recursive

# Change group
chgrp developers file.txt
```

### Users and Superuser

```bash
# Show current user
whoami

# Show all logged-in users
who
w

# Switch to another user
su - bob                    # switch to bob (- loads their environment)
su -                        # switch to root

# Run a single command as root
sudo apt update
sudo systemctl restart nginx

# Add a user to the sudoers group
sudo usermod -aG sudo alice        # Debian/Ubuntu
sudo usermod -aG wheel alice       # RHEL/CentOS

# View who can sudo
sudo cat /etc/sudoers

# User management
sudo useradd -m -s /bin/bash alice    # create user with home dir
sudo passwd alice                      # set password
sudo usermod -aG docker alice          # add to docker group
sudo userdel -r alice                  # delete user and home dir

# Group management
sudo groupadd devops
sudo groupdel devops
groups alice                           # show groups for alice
id alice                               # UID, GID, all groups
```

### I/O Redirection and Pipes

```bash
# Redirect stdout to a file (overwrite)
ls -la > listing.txt

# Redirect stdout to a file (append)
echo "new entry" >> log.txt

# Redirect stderr
command 2> errors.txt

# Redirect both stdout and stderr
command > output.txt 2>&1
command &> output.txt          # shorthand

# Discard output
command > /dev/null
command &> /dev/null

# Pipe: send stdout of one command as stdin to another
cat /etc/passwd | grep "alice"
ps aux | grep nginx
ls -la | sort -k5 -n           # sort by file size (column 5)
cat app.log | grep ERROR | wc -l   # count error lines

# Pipe to less for pagination
git log | less

# tee: write to file AND stdout simultaneously
command | tee output.txt
command | tee -a output.txt    # append mode
```

### Useful Utility Commands

```bash
# Display text
echo "Hello, World!"
echo -e "Line1\nLine2"         # interpret escape sequences

# Word/line/character count
wc -l file.txt                 # count lines
wc -w file.txt                 # count words
wc -c file.txt                 # count bytes

# Sort
sort names.txt
sort -r names.txt              # reverse
sort -n numbers.txt            # numeric sort
sort -u names.txt              # unique (remove duplicates)

# Unique (remove consecutive duplicates — use after sort)
sort names.txt | uniq
sort names.txt | uniq -c       # count occurrences

# Cut fields from text
cut -d: -f1 /etc/passwd        # first field, colon-delimited
cut -d, -f2,4 data.csv         # fields 2 and 4 from CSV

# Replace text in a stream
echo "Hello World" | sed 's/World/DevOps/'

# In-place file substitution
sed -i 's/localhost/db.internal/g' config.yaml

# AWK: process text by fields
awk '{print $1, $3}' file.txt             # print columns 1 and 3
awk -F: '{print $1}' /etc/passwd          # usernames from passwd
awk '/ERROR/ {print NR, $0}' app.log      # print error lines with numbers

# Environment variables
env                            # list all environment variables
echo $HOME                     # print value of HOME
echo $PATH                     # print executable search path
export MY_VAR="hello"          # set an environment variable
unset MY_VAR                   # remove it

# Process management
ps aux                         # all running processes
ps aux | grep nginx
top                            # interactive process viewer
htop                           # better interactive process viewer (if installed)
kill 1234                      # send SIGTERM to PID 1234
kill -9 1234                   # send SIGKILL (force kill)
killall nginx                  # kill all processes named nginx
pkill -f "python app.py"       # kill by command pattern

# Disk usage
df -h                          # filesystem disk usage (human readable)
du -sh /var/log                # size of a directory
du -sh /*  2>/dev/null | sort -h   # find largest top-level directories

# System information
uname -a                       # kernel and system info
hostname                       # machine hostname
uptime                         # how long system has been running
free -h                        # RAM usage
lscpu                          # CPU info
lsblk                          # block devices (disks)
```

### Archiving and Compression

```bash
# Create a tar archive (no compression)
tar -cvf archive.tar directory/

# Create a compressed archive (gzip)
tar -czvf archive.tar.gz directory/

# Create a compressed archive (bzip2 — smaller but slower)
tar -cjvf archive.tar.bz2 directory/

# List contents without extracting
tar -tzvf archive.tar.gz

# Extract an archive
tar -xzvf archive.tar.gz                    # extract to current dir
tar -xzvf archive.tar.gz -C /opt/           # extract to /opt/

# Compress a single file
gzip file.txt                               # creates file.txt.gz, removes original
gzip -k file.txt                            # keep original
gunzip file.txt.gz                          # decompress

# zip/unzip
zip -r archive.zip directory/
unzip archive.zip
unzip archive.zip -d /opt/destination/

# Flags reference for tar:
# c = create   x = extract   t = list
# v = verbose  f = filename  z = gzip   j = bzip2
```

### Hands-on Lab: Working Your Way Through the CLI

**Objective**: Navigate the Linux filesystem, create and manipulate files, and practice I/O redirection and pipes.

**Estimated time**: 25 minutes

---

**Step 1 – Orientation**

```bash
# Where are you?
pwd

# What's in your home directory?
ls -la ~

# What Linux distribution is this?
cat /etc/os-release
uname -r
```

**Step 2 – Build a project structure**

```bash
mkdir -p ~/devops-lab/{scripts,configs,logs,backups}
cd ~/devops-lab
ls -R
```

**Step 3 – Create and view files**

```bash
# Create a configuration file
cat > configs/app.conf << 'EOF'
[database]
host=localhost
port=5432
name=myapp
user=appuser
password=secret123

[server]
host=0.0.0.0
port=8080
debug=false
workers=4
EOF

cat configs/app.conf
```

**Step 4 – Search and filter**

```bash
# Find all keys in the config
grep -v "^#" configs/app.conf | grep "="

# Extract only the keys (before =)
grep "=" configs/app.conf | cut -d= -f1

# Count configuration items
grep -c "=" configs/app.conf
```

**Step 5 – Create a log file and analyze it**

```bash
cat > logs/app.log << 'EOF'
2026-04-01 08:00:01 INFO  Application started
2026-04-01 08:00:02 INFO  Connected to database
2026-04-01 08:01:15 DEBUG Request received: GET /api/health
2026-04-01 08:01:16 INFO  Response: 200 OK
2026-04-01 08:05:33 ERROR Failed to connect to cache server
2026-04-01 08:05:34 WARN  Falling back to in-memory cache
2026-04-01 08:10:11 ERROR Database query timeout after 30s
2026-04-01 08:10:12 ERROR Retrying query (attempt 1/3)
2026-04-01 08:10:43 ERROR Retrying query (attempt 2/3)
2026-04-01 08:11:14 ERROR Max retries exceeded
2026-04-01 08:11:15 INFO  Graceful shutdown initiated
EOF

# Count errors
grep -c "ERROR" logs/app.log

# Show only errors
grep "ERROR" logs/app.log

# Show errors with line numbers
grep -n "ERROR" logs/app.log

# Show unique log levels and their counts
awk '{print $3}' logs/app.log | sort | uniq -c | sort -rn
```

**Step 6 – File permissions**

```bash
# Create a shell script
cat > scripts/deploy.sh << 'EOF'
#!/bin/bash
echo "Deploying application..."
echo "Build: $(date)"
echo "Done!"
EOF

# Try to run it (will fail — not executable yet)
./scripts/deploy.sh

# Add execute permission
chmod +x scripts/deploy.sh

# Run it
./scripts/deploy.sh

# Verify permissions
ls -l scripts/deploy.sh
```

**Step 7 – Archiving**

```bash
cd ~

# Archive the entire lab directory
tar -czvf devops-lab-backup.tar.gz devops-lab/

# Verify
ls -lh devops-lab-backup.tar.gz
tar -tzvf devops-lab-backup.tar.gz | head -20
```

---

### Hands-on Lab: Linux Commands

**Objective**: Practice advanced Linux commands including `find`, `grep`, `sed`, `awk`, and process management.

**Estimated time**: 20 minutes

---

**Step 1 – Advanced find**

```bash
# Find all .conf files in /etc
find /etc -name "*.conf" -type f 2>/dev/null | head -20

# Find files modified in the last 24 hours in /var/log
find /var/log -mtime -1 -type f 2>/dev/null

# Find large files (>10MB) in /var
find /var -size +10M -type f 2>/dev/null

# Find world-writable files (security audit)
find /tmp -perm -o+w -type f
```

**Step 2 – Text processing with sed**

```bash
cd ~/devops-lab

# Replace a value in the config file (view only, don't save)
sed 's/localhost/db.prod.internal/' configs/app.conf

# Replace and save in-place
sed -i 's/debug=false/debug=true/' configs/app.conf
grep "debug" configs/app.conf

# Delete lines containing "password"
sed '/password/d' configs/app.conf

# Print only lines 3-6
sed -n '3,6p' configs/app.conf
```

**Step 3 – Text processing with awk**

```bash
# Print only the log level and message (columns 3 onwards)
awk '{$1=$2=""; print $0}' logs/app.log

# Print lines where log level is ERROR
awk '$3 == "ERROR" {print NR": "$0}' logs/app.log

# Count events per log level
awk '{levels[$3]++} END {for (l in levels) print l, levels[l]}' logs/app.log
```

**Step 4 – Process management**

```bash
# View running processes
ps aux | head -20

# Find a specific process
ps aux | grep bash

# Check what's listening on a port
ss -tlnp | grep :80
# or
netstat -tlnp 2>/dev/null | grep :80

# Run a job in the background
sleep 300 &
echo "Sleep PID: $!"

# View background jobs
jobs

# Bring to foreground
fg %1

# Send Ctrl+C equivalent programmatically
kill %1   # or kill <PID>
```

---

## Mastering the VI Editor

### Why VI/Vim?

VI (and its improved version, Vim) is installed on virtually every Unix/Linux system. When you SSH into a minimal server with no graphical interface and no other editors, VI will be there. Knowing VI is a survival skill for any DevOps engineer.

### VI Modes

VI is a **modal editor**: the same keys perform different actions depending on the current mode.

```
  ┌──────────────────────────────────────────────────-────────┐
  │                     VI MODES                              │
  │                                                           │
  │  NORMAL MODE        INSERT MODE       COMMAND MODE        │
  │  (default)          (editing text)    (: commands)        │
  │                                                           │
  │  Navigation,        Type to insert    Save, quit,         │
  │  deletion,          text              search, replace     │
  │  copy/paste                                               │
  │                                                           │
  │  Press i,a,o   →   Insert Mode                            │
  │  Press Esc     ←   Back to Normal                         │
  │  Press :       →   Command Mode                           │
  └──────────────────────────────────────────────────-────────┘
```

### Essential VI Commands

**Opening and closing:**

```bash
vi filename          # open or create a file
vim filename         # open with Vim (improved)
view filename        # open read-only
```

**Normal Mode – Navigation:**

```
h  j  k  l          ← ↓ ↑ → (arrow keys also work)
w                   jump forward one word
b                   jump backward one word
e                   jump to end of current word
0                   beginning of line
^                   first non-whitespace character of line
$                   end of line
gg                  first line of file
G                   last line of file
:42                 go to line 42
Ctrl+f              page down
Ctrl+b              page up
%                   jump to matching bracket/paren/brace
```

**Normal Mode – Editing:**

```
i                   insert before cursor
I                   insert at beginning of line
a                   append after cursor
A                   append at end of line
o                   open new line below cursor
O                   open new line above cursor

x                   delete character under cursor
X                   delete character before cursor
dw                  delete word
dd                  delete (cut) entire line
D                   delete from cursor to end of line
3dd                 delete 3 lines
d$                  delete to end of line
d0                  delete to beginning of line

yy                  yank (copy) line
yw                  yank word
3yy                 yank 3 lines
p                   paste after cursor/line
P                   paste before cursor/line

u                   undo
Ctrl+r              redo
.                   repeat last command

r<char>             replace single character
cw                  change word (delete + enter insert mode)
cc                  change entire line
C                   change from cursor to end of line

>>                  indent line right
<<                  indent line left
```

**Normal Mode – Searching:**

```
/pattern            search forward
?pattern            search backward
n                   next match (same direction)
N                   previous match (reverse direction)
*                   search for word under cursor (forward)
#                   search for word under cursor (backward)
```

**Command Mode (press `:` from Normal mode):**

```
:w                  save (write)
:q                  quit
:wq                 save and quit
:x                  save and quit (only writes if changes made)
:q!                 quit without saving (discard changes)
:wq!                force save and quit

:set number         show line numbers
:set nonumber       hide line numbers
:set hlsearch       highlight search matches
:set nohlsearch     turn off highlight
:set paste          paste mode (prevents auto-indent issues)
:set nopaste        turn off paste mode

:%s/old/new/g       replace all occurrences in file
:%s/old/new/gc      replace all with confirmation
:10,20s/old/new/g   replace in lines 10-20

:!command           run a shell command (e.g., :!ls)
:r filename         insert contents of another file
:syntax on          enable syntax highlighting (Vim)
```

**Visual Mode:**

```
v                   enter visual (character) mode
V                   enter visual line mode
Ctrl+v              enter visual block mode

(after selecting text)
d                   delete selection
y                   yank selection
>                   indent selection
<                   dedent selection
```

### Lab: VI Editor

**Objective**: Create, edit, and save files using VI/Vim.

**Estimated time**: 20 minutes

---

**Step 1 – Create a file with VI**

```bash
vi ~/devops-lab/configs/nginx.conf
```

1. Press `i` to enter Insert mode
2. Type the following content:

```nginx
server {
    listen 80;
    server_name myapp.example.com;

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    access_log /var/log/nginx/myapp_access.log;
    error_log  /var/log/nginx/myapp_error.log;
}
```

3. Press `Esc` to return to Normal mode
4. Type `:wq` and press Enter to save and quit

**Step 2 – Navigate and edit**

```bash
vi ~/devops-lab/configs/nginx.conf
```

Practice these operations:

```
gg              → go to first line
G               → go to last line
/proxy_pass     → search for "proxy_pass"
n               → find next occurrence
:set number     → enable line numbers
:5              → jump to line 5
dd              → delete a line
u               → undo the deletion
yy              → copy the current line
p               → paste it below
:wq             → save and quit
```

**Step 3 – Global search and replace**

```bash
vi ~/devops-lab/configs/nginx.conf
```

```
:%s/localhost/backend.internal/g    → replace all occurrences
:w                                   → save
:q                                   → quit
```

Verify:

```bash
cat ~/devops-lab/configs/nginx.conf | grep "backend"
```

**Step 4 – Create a `.vimrc` for a better experience**

```bash
vi ~/.vimrc
```

Press `i` and add:

```vim
set number
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set hlsearch
set incsearch
set ignorecase
set smartcase
syntax on
set background=dark
```

Press `Esc`, then `:wq`.

---

## More Linux Commands

### Networking Commands

```bash
# Show IP addresses for all interfaces
ip addr show
ip a                             # shorthand

# Show routing table
ip route show

# Test connectivity
ping google.com
ping -c 4 google.com             # send 4 packets only

# Trace network path
traceroute google.com
tracepath google.com             # no root required

# DNS lookup
nslookup google.com
dig google.com
dig google.com +short            # just the IP
dig MX google.com                # query MX records

# HTTP requests
curl https://example.com                      # GET request
curl -I https://example.com                   # headers only
curl -X POST -d '{"key":"val"}' \
  -H "Content-Type: application/json" \
  https://api.example.com/data
wget https://example.com/file.tar.gz          # download file

# Check open ports and connections
ss -tlnp                         # TCP listening ports
ss -an                           # all connections
netstat -tlnp                    # older equivalent

# Show network interfaces
ifconfig                         # older tool
ip link show

# Firewall management (Ubuntu/Debian)
sudo ufw status
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw enable

# Firewall management (RHEL/CentOS)
sudo firewall-cmd --list-all
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```

### File Viewing and Comparison

```bash
# View files side by side
diff file1.txt file2.txt
diff -u file1.txt file2.txt      # unified diff format (used in patches)
diff -r dir1/ dir2/              # compare directories recursively

# Show file type
file script.sh
file image.png
file archive.tar.gz

# View binary files in hex
xxd file.bin | head -20
od -c file.bin | head            # octal dump

# Checksums (verify file integrity)
md5sum file.tar.gz
sha256sum file.tar.gz
sha256sum -c checksums.txt       # verify against a checksum file
```

### SSH and Remote Access

```bash
# Connect to a remote server
ssh user@192.168.1.100
ssh -p 2222 user@server.example.com    # custom port
ssh -i ~/.ssh/my-key.pem user@host     # use specific key

# Copy files securely
scp file.txt user@remote:/opt/
scp -r directory/ user@remote:/opt/
scp user@remote:/var/log/app.log ./    # remote to local

# Sync directories
rsync -avz local-dir/ user@remote:/opt/app/
rsync -avz --delete local/ remote:/backup/   # mirror (delete extras)

# SSH config file (~/.ssh/config)
cat >> ~/.ssh/config << 'EOF'
Host devserver
    HostName 192.168.1.100
    User alice
    IdentityFile ~/.ssh/alice-key.pem
    Port 22
EOF

# Now connect with just:
ssh devserver
```

---

## Understanding Package Management

### What Is a Package Manager?

A **package manager** automates the process of installing, upgrading, configuring, and removing software. It resolves dependencies (ensuring that all libraries a program needs are also installed), verifies package integrity with checksums, and keeps track of everything installed on the system.

### APT — Debian/Ubuntu

APT (Advanced Package Tool) manages `.deb` packages.

```bash
# Update the package index (always run before installing)
sudo apt update

# Upgrade all installed packages
sudo apt upgrade
sudo apt full-upgrade              # also handles changing dependencies

# Install a package
sudo apt install nginx
sudo apt install -y nginx          # skip confirmation prompt
sudo apt install vim git curl wget

# Remove a package
sudo apt remove nginx              # remove but keep config files
sudo apt purge nginx               # remove including config files
sudo apt autoremove                # remove unneeded dependencies

# Search for packages
apt search nginx
apt-cache search python3

# Show package information
apt show nginx
apt-cache show nginx

# List installed packages
dpkg -l
dpkg -l | grep nginx
apt list --installed

# Check which package owns a file
dpkg -S /usr/bin/git
```

**APT Sources:**

```bash
# View configured repositories
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# Add a repository (example: Docker)
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install docker-ce
```

### YUM / DNF — RHEL/CentOS/Fedora

YUM (Yellowdog Updater, Modified) and its successor DNF manage `.rpm` packages.

```bash
# Update package index and upgrade
sudo yum update
sudo dnf update                    # DNF (Fedora, RHEL 8+)

# Install
sudo yum install nginx -y
sudo dnf install nginx -y

# Remove
sudo yum remove nginx
sudo dnf remove nginx

# Search
yum search nginx
dnf search nginx

# Show package info
yum info nginx

# List installed
yum list installed
rpm -qa                            # low-level RPM query

# Check which package owns a file
rpm -qf /usr/bin/git

# Enable a repository (EPEL — Extra Packages for Enterprise Linux)
sudo yum install epel-release -y
sudo dnf install epel-release -y
```

### Hands-on Lab: Package Management

**Objective**: Install, verify, and remove packages using APT (Ubuntu) or YUM/DNF (RHEL/CentOS).

**Estimated time**: 20 minutes

---

**On Ubuntu/Debian:**

```bash
# Step 1: Update the package index
sudo apt update

# Step 2: Install several tools
sudo apt install -y vim git curl wget tree htop

# Step 3: Verify installations
git --version
vim --version | head -1
tree --version

# Step 4: Explore package info
apt show git

# Step 5: Use tree to view a directory
tree ~/devops-lab

# Step 6: Install a more complex package (nginx)
sudo apt install -y nginx

# Verify nginx installed and its files
dpkg -L nginx | head -20

# Step 7: Remove it
sudo apt remove -y nginx
sudo apt autoremove -y
```

**On RHEL/CentOS/Rocky Linux:**

```bash
# Step 1: Update
sudo dnf update -y

# Step 2: Install EPEL and tools
sudo dnf install -y epel-release
sudo dnf install -y vim git curl wget tree htop

# Step 3: Verify
git --version
tree --version

# Step 4: Install nginx
sudo dnf install -y nginx
rpm -ql nginx | head -20

# Step 5: Remove
sudo dnf remove -y nginx
```

---

## Managing System Services

### What Is systemd?

**systemd** is the init system used by most modern Linux distributions (Ubuntu 16.04+, RHEL 7+, Debian 8+). It manages services (called **units**) and their dependencies, handles parallel startup for faster boot times, and provides logging via `journald`.

### systemctl Commands

```bash
# ─── Service Lifecycle ────────────────────────────────────────
sudo systemctl start nginx         # start a service
sudo systemctl stop nginx          # stop a service
sudo systemctl restart nginx       # stop, then start
sudo systemctl reload nginx        # reload config without restart
sudo systemctl status nginx        # show current status

# ─── Enable/Disable at Boot ───────────────────────────────────
sudo systemctl enable nginx        # start automatically at boot
sudo systemctl disable nginx       # do not start at boot
sudo systemctl enable --now nginx  # enable AND start immediately
sudo systemctl is-enabled nginx    # check if enabled

# ─── Checking Status ──────────────────────────────────────────
systemctl status nginx             # detailed status with recent logs
systemctl is-active nginx          # active/inactive
systemctl is-failed nginx          # failed/not-failed

# ─── Listing Units ────────────────────────────────────────────
systemctl list-units               # all active units
systemctl list-units --type=service   # only services
systemctl list-units --state=failed   # only failed units
systemctl list-unit-files          # all unit files with enabled state

# ─── System Control ───────────────────────────────────────────
sudo systemctl daemon-reload       # reload unit files after editing
sudo systemctl reboot              # reboot
sudo systemctl poweroff            # shut down
sudo systemctl suspend             # suspend
```

### Reading Service Status

```bash
sudo systemctl status nginx

# Output:
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2026-04-01 08:00:01 UTC; 2h 30min ago
       Docs: man:nginx(8)
   Main PID: 1234 (nginx)
      Tasks: 3 (limit: 1137)
     Memory: 5.6M
        CPU: 81ms
     CGroup: /system.slice/nginx.service
             ├─1234 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
             ├─1235 nginx: worker process
             └─1236 nginx: worker process

Apr 01 08:00:01 server systemd[1]: Starting A high performance web...
Apr 01 08:00:01 server nginx[1234]: nginx: configuration file /etc/nginx/nginx.conf test is successful
Apr 01 08:00:01 server systemd[1]: Started A high performance web server and a reverse proxy server.
```

Key fields:

|Field|Meaning|
|---|---|
|`Loaded`|Unit file path and whether it's enabled|
|`Active`|Current state (active/inactive/failed) and uptime|
|`Main PID`|Primary process ID|
|`CGroup`|Process hierarchy|
|Bottom lines|Recent log entries|

### Journald — Viewing Logs

```bash
# View all logs for a service
journalctl -u nginx

# Follow logs in real time
journalctl -u nginx -f

# Show logs since a point in time
journalctl -u nginx --since "1 hour ago"
journalctl -u nginx --since "2026-04-01" --until "2026-04-02"

# Show only error-level and above
journalctl -u nginx -p err

# Show kernel messages
journalctl -k

# Show boot messages
journalctl -b

# Disk usage of journals
journalctl --disk-usage

# Rotate/vacuum logs
sudo journalctl --vacuum-size=500M
sudo journalctl --vacuum-time=7d
```

### Writing a Custom Unit File

You can define your own services with unit files in `/etc/systemd/system/`:

```bash
sudo vi /etc/systemd/system/myapp.service
```

```ini
[Unit]
Description=My DevOps Application
After=network.target
Requires=postgresql.service

[Service]
Type=simple
User=appuser
Group=appuser
WorkingDirectory=/opt/myapp
EnvironmentFile=/opt/myapp/.env
ExecStart=/usr/bin/python3 /opt/myapp/src/app.py
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5s
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

```bash
# Reload unit files after creating/editing
sudo systemctl daemon-reload

# Enable and start
sudo systemctl enable --now myapp

# Check status
sudo systemctl status myapp
```

**Unit file sections:**

|Section|Purpose|
|---|---|
|`[Unit]`|Description, ordering (After/Before/Requires/Wants)|
|`[Service]`|How to start/stop/reload, user, environment, restart policy|
|`[Install]`|What target enables this unit (`WantedBy`)|

### Hands-on Lab: Services

**Objective**: Install, start, enable, and monitor a system service.

**Estimated time**: 20 minutes

---

**Step 1 – Install and start nginx**

```bash
# Ubuntu
sudo apt install -y nginx

# RHEL/CentOS
sudo dnf install -y nginx

# Start the service
sudo systemctl start nginx
sudo systemctl status nginx
```

**Step 2 – Verify nginx is serving traffic**

```bash
curl http://localhost
# Should return the nginx welcome HTML page
```

**Step 3 – Enable nginx to start on boot**

```bash
sudo systemctl enable nginx
sudo systemctl is-enabled nginx
# enabled
```

**Step 4 – Modify and reload**

```bash
# Check nginx config is valid before reloading
sudo nginx -t

# Reload without downtime
sudo systemctl reload nginx
sudo systemctl status nginx
```

**Step 5 – Stop and disable**

```bash
sudo systemctl stop nginx
sudo systemctl disable nginx
sudo systemctl status nginx
# Active: inactive (dead)
```

**Step 6 – View service logs**

```bash
# View all nginx logs
journalctl -u nginx --since "10 minutes ago"

# Follow live
sudo systemctl start nginx
journalctl -u nginx -f &

# Generate a request
curl http://localhost

# Stop following
kill %1
```

**Step 7 – Create a custom service**

```bash
# Create the application script
sudo mkdir -p /opt/helloapp
sudo tee /opt/helloapp/hello.sh << 'EOF'
#!/bin/bash
while true; do
    echo "$(date): Hello from DevOps service!"
    sleep 5
done
EOF
sudo chmod +x /opt/helloapp/hello.sh

# Create the unit file
sudo tee /etc/systemd/system/helloapp.service << 'EOF'
[Unit]
Description=Hello DevOps Application
After=network.target

[Service]
Type=simple
ExecStart=/opt/helloapp/hello.sh
Restart=on-failure
StandardOutput=journal

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now helloapp
sudo systemctl status helloapp
journalctl -u helloapp -f &
sleep 12
kill %1
sudo systemctl stop helloapp
```

---

## Module 1 Assessment

### Linux Basics Graded Assessment

**Question 1**: You need to find all files in `/var/log` that are larger than 50MB and were modified in the last 3 days. Write the `find` command.

**Question 2**: Explain the numeric permission `644`. What can the owner, group, and others do with a file that has this permission?

**Question 3**: A service called `myapp` is running but occasionally crashes. Write the `[Service]` section of a unit file that automatically restarts it 10 seconds after a crash, running as user `appuser`.

**Question 4**: You have a 10,000-line log file. Write a pipeline of commands that: (a) filters lines containing "ERROR", (b) extracts the timestamp (first two fields), (c) sorts by timestamp, and (d) counts the result.

**Question 5**: What is the difference between `apt remove` and `apt purge`? When would you use each?

**Question 6**: Describe the three VI modes and how to transition between them.

**Question 7**: Write the command to check if port 8080 is open and listening, then identify which process is using it.

---

# Module 2 – Networking

## Learning Objectives

By the end of this module you will be able to:

- Understand fundamental networking concepts (IP, MAC, subnets, routing, switching)
- Configure and troubleshoot network switches and routers
- Understand DNS and how it resolves domain names to IP addresses

---

## Essential Networking Principles

### How Computers Communicate

Every device on a network has two addresses:

```
  MAC Address (Layer 2 — Data Link)
  ─────────────────────────────────
  Hardware address burned into the NIC
  Format: 6 bytes in hex (e.g., 00:1A:2B:3C:4D:5E)
  Unique worldwide (in theory)
  Used for communication within a local network segment

  IP Address (Layer 3 — Network)
  ─────────────────────────────────
  Logical address assigned to an interface
  IPv4: 32 bits, dotted decimal (e.g., 192.168.1.50)
  IPv6: 128 bits, colon-hex (e.g., 2001:db8::1)
  Used for routing across networks
```

### The OSI Model

```
  Layer 7 — Application   HTTP, DNS, SMTP, SSH, FTP
  Layer 6 — Presentation  TLS/SSL, encoding, compression
  Layer 5 — Session       Session establishment/teardown
  Layer 4 — Transport     TCP (reliable), UDP (fast)
  Layer 3 — Network       IP routing, ICMP
  Layer 2 — Data Link     Ethernet, MAC addresses, switches
  Layer 1 — Physical      Cables, fiber, Wi-Fi signals
```

DevOps engineers most frequently work with Layers 3–7.

### IP Addressing and Subnets

An **IP address** combined with a **subnet mask** defines both the device's address and which network it belongs to.

```
IP Address:   192.168.1.50
Subnet Mask:  255.255.255.0   (or /24 in CIDR notation)

Network:      192.168.1.0/24
Usable hosts: 192.168.1.1 – 192.168.1.254  (254 hosts)
Broadcast:    192.168.1.255
```

**CIDR notation** (Classless Inter-Domain Routing) expresses the subnet mask as a prefix length:

|CIDR|Subnet Mask|Hosts|
|---|---|---|
|/8|255.0.0.0|16,777,214|
|/16|255.255.0.0|65,534|
|/24|255.255.255.0|254|
|/25|255.255.255.128|126|
|/28|255.255.255.240|14|
|/30|255.255.255.252|2|
|/32|255.255.255.255|1 (host route)|

**Private IP ranges** (RFC 1918 — not routable on the public internet):

```
10.0.0.0/8          10.0.0.0 – 10.255.255.255
172.16.0.0/12       172.16.0.0 – 172.31.255.255
192.168.0.0/16      192.168.0.0 – 192.168.255.255
```

### Switches

A **switch** operates at Layer 2. It forwards frames between devices on the same network using MAC addresses.

```
  ┌─────────┐
  │ SWITCH  │
  │         │
  ├─────────┤
  │ Port 1  │──── PC-A  (MAC: AA:BB:CC:11:22:33)
  │ Port 2  │──── PC-B  (MAC: AA:BB:CC:44:55:66)
  │ Port 3  │──── Server(MAC: AA:BB:CC:77:88:99)
  │ Port 4  │──── Router
  └─────────┘
```

The switch maintains a **MAC address table** (CAM table) that maps MAC addresses to ports. When PC-A sends a frame to PC-B:

1. Switch receives the frame on Port 1, learns PC-A's MAC → Port 1
2. Switch looks up PC-B's MAC in its table
3. If found: forwards only to Port 2
4. If not found: **floods** to all ports except Port 1

**VLANs (Virtual LANs)** logically segment a physical switch into multiple isolated networks:

```bash
# Example: configure a VLAN on a Cisco-style switch
# (syntax varies by vendor)
Switch> enable
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name PRODUCTION
Switch(config-vlan)# exit
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

### Routers

A **router** operates at Layer 3. It forwards packets between different networks using IP addresses and a routing table.

```
  INTERNET
      │
   [Router]──── 192.168.1.0/24 (LAN 1)
      │
      └───────── 10.0.0.0/8    (LAN 2)
```

The router makes forwarding decisions based on the **routing table**:

```bash
# View routing table on Linux
ip route show
# or
route -n

# Output:
# Kernel IP routing table
# Destination     Gateway         Genmask         Flags Metric Ref Use Iface
# 0.0.0.0         192.168.1.1     0.0.0.0         UG    100    0   0   eth0
# 192.168.1.0     0.0.0.0         255.255.255.0   U     100    0   0   eth0

# Add a static route
sudo ip route add 10.0.0.0/8 via 192.168.1.1 dev eth0

# Add a default gateway
sudo ip route add default via 192.168.1.1

# Delete a route
sudo ip route del 10.0.0.0/8
```

**Routing types:**

- **Static routing**: Routes manually configured by an administrator
- **Dynamic routing**: Routers exchange route information automatically using protocols like OSPF, BGP, EIGRP
- **Default route** (0.0.0.0/0): The "gateway of last resort" — where to send packets when no more specific route matches

### NAT (Network Address Translation)

NAT allows multiple devices with private IPs to share a single public IP address.

```
  Private Network              Internet
  ─────────────                ─────────
  192.168.1.10 ─┐
  192.168.1.11 ─┤── [NAT Router] ── 203.0.113.1 ──► Web Server
  192.168.1.12 ─┘   (replaces
                    private IP
                    with public IP)
```

### Common Ports to Know

|Port|Protocol|Service|
|---|---|---|
|22|TCP|SSH|
|25|TCP|SMTP (email)|
|53|TCP/UDP|DNS|
|80|TCP|HTTP|
|443|TCP|HTTPS|
|3306|TCP|MySQL|
|5432|TCP|PostgreSQL|
|6379|TCP|Redis|
|8080|TCP|HTTP alternate|
|27017|TCP|MongoDB|

### Network Troubleshooting Toolkit

```bash
# ─── Connectivity ────────────────────────────────────────────
ping -c 4 8.8.8.8                  # ICMP echo (is host reachable?)
traceroute 8.8.8.8                 # trace the path
mtr 8.8.8.8                        # continuous traceroute (better)

# ─── DNS ─────────────────────────────────────────────────────
dig google.com                     # full DNS query
dig google.com +short              # just the IP
dig @8.8.8.8 google.com           # query specific DNS server
nslookup google.com

# ─── Port Testing ────────────────────────────────────────────
telnet 192.168.1.10 80             # check if port is open
nc -zv 192.168.1.10 80             # netcat port check
nc -zv 192.168.1.10 80-100         # scan a port range
curl -v http://192.168.1.10        # HTTP-level check

# ─── Interface and Routes ────────────────────────────────────
ip addr show                       # all interfaces + IPs
ip route show                      # routing table
ip neigh show                      # ARP table (MAC to IP mappings)
arp -a                             # older ARP command

# ─── Active Connections ──────────────────────────────────────
ss -tlnp                           # TCP listening + process info
ss -anp | grep :8080               # who is using port 8080?
lsof -i :80                        # what process is on port 80?

# ─── Packet Capture ──────────────────────────────────────────
sudo tcpdump -i eth0               # capture all traffic on eth0
sudo tcpdump -i eth0 port 80       # only HTTP traffic
sudo tcpdump -i eth0 host 8.8.8.8  # traffic to/from specific host
sudo tcpdump -i eth0 -w capture.pcap  # save to file (open with Wireshark)
```

---

## Exploring the Domain Name System

### What Is DNS?

The **Domain Name System** is the internet's phone book. It translates human-readable names (like `google.com`) into machine-readable IP addresses (like `142.250.80.46`).

Without DNS, you would need to remember the IP address of every service you want to connect to.

### The DNS Hierarchy

```
  Root (.)
     │
  ┌──┴──────────────────────┐
 .com      .org     .io    .net    .uk ...
  │
  ├── google.com
  ├── amazon.com
  └── github.com
           │
           ├── api.github.com
           ├── docs.github.com
           └── *.github.com
```

### DNS Resolution: Step by Step

When you type `www.example.com` in a browser:

```
  1. Browser checks its local cache → not found
  2. OS checks /etc/hosts → not found
  3. OS asks the configured Resolver (e.g., 8.8.8.8)
  4. Resolver checks its cache → not found
  5. Resolver asks a Root Nameserver: "Who handles .com?"
     Root says: "Ask the .com TLD nameserver"
  6. Resolver asks .com TLD: "Who handles example.com?"
     TLD says: "Ask ns1.example.com"
  7. Resolver asks ns1.example.com: "What is www.example.com?"
     ns1.example.com says: "93.184.216.34"
  8. Resolver returns the answer to your OS → cached for TTL seconds
  9. Your browser connects to 93.184.216.34
```

This entire process typically takes **< 50ms**. Subsequent lookups are served from cache in microseconds.

### DNS Record Types

|Type|Purpose|Example|
|---|---|---|
|**A**|Maps hostname → IPv4 address|`www.example.com → 93.184.216.34`|
|**AAAA**|Maps hostname → IPv6 address|`www.example.com → 2606:2800::1`|
|**CNAME**|Canonical name (alias)|`blog.example.com → example.com`|
|**MX**|Mail exchanger|`example.com → mail.example.com (priority 10)`|
|**TXT**|Text records (SPF, DKIM, verification)|`"v=spf1 include:..."`|
|**NS**|Nameserver for the zone|`example.com → ns1.example.com`|
|**PTR**|Reverse lookup (IP → hostname)|`34.216.184.93 → www.example.com`|
|**SRV**|Service location|`_http._tcp.example.com`|
|**SOA**|Start of Authority (zone metadata)|Serial, refresh, retry, expiry|

### Configuring DNS on Linux

**System resolver configuration:**

```bash
# View current DNS servers
cat /etc/resolv.conf

# Example content:
# nameserver 8.8.8.8
# nameserver 8.8.4.4
# search example.com internal.company.com
# options ndots:5

# On Ubuntu with systemd-resolved:
resolvectl status
resolvectl query google.com

# Manually set DNS (temporary)
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf

# On Ubuntu 18.04+ (persistent — via netplan)
sudo vi /etc/netplan/01-netcfg.yaml
```

```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
        search: [example.com]
```

```bash
sudo netplan apply
```

**The `/etc/hosts` file:**

`/etc/hosts` is checked before DNS. You can override any DNS record here:

```bash
cat /etc/hosts
# 127.0.0.1   localhost
# 127.0.1.1   myserver
# 192.168.1.10  db.internal postgres.internal
# 192.168.1.20  redis.internal cache.internal

# Add entries
echo "192.168.1.50  myapp.local" | sudo tee -a /etc/hosts

# Test resolution
ping myapp.local
curl http://myapp.local
```

**NSSwitch — Resolution Order:**

```bash
cat /etc/nsswitch.conf | grep hosts
# hosts: files dns myhostname
# Order: /etc/hosts first, then DNS, then hostname
```

### Hands-on Lab: Exploring the Domain Name System

**Objective**: Use DNS tools to query records, trace resolution, and configure local name resolution.

**Estimated time**: 20 minutes

---

**Step 1 – Basic DNS queries**

```bash
# Install dig if not present
sudo apt install -y dnsutils        # Ubuntu
sudo dnf install -y bind-utils      # RHEL/CentOS

# Query A record
dig google.com

# Query just the answer section
dig google.com +short

# Query AAAA (IPv6)
dig AAAA google.com +short

# Query MX records (mail servers)
dig MX gmail.com +short

# Query NS records (nameservers)
dig NS google.com +short

# Query TXT records (SPF/DKIM)
dig TXT google.com

# Reverse lookup (PTR)
dig -x 8.8.8.8 +short
```

**Step 2 – Query specific DNS servers**

```bash
# Query Google's public DNS
dig @8.8.8.8 github.com

# Query Cloudflare's DNS
dig @1.1.1.1 github.com

# Compare response times
dig @8.8.8.8 google.com | grep "Query time"
dig @1.1.1.1 google.com | grep "Query time"
```

**Step 3 – Trace the full DNS resolution chain**

```bash
# Trace from root servers to final answer
dig +trace google.com

# This shows every step:
# . → .com → google.com → final answer
```

**Step 4 – Configure /etc/hosts for local development**

```bash
# Add a fake local hostname
echo "127.0.0.1  myapp.dev" | sudo tee -a /etc/hosts
echo "127.0.0.1  api.myapp.dev" | sudo tee -a /etc/hosts

# Test it
ping -c 1 myapp.dev
curl http://myapp.dev   # will fail with connection refused unless something is listening
nslookup myapp.dev

# Verify the entry
grep "myapp.dev" /etc/hosts
```

**Step 5 – View DNS cache and resolver status**

```bash
# On Ubuntu with systemd-resolved:
resolvectl status
resolvectl statistics

# Check what DNS servers are being used
systemd-resolve --status | head -30
```

**Step 6 – Troubleshoot a "DNS not working" scenario**

```bash
# Simulate DNS failure by pointing to a non-existent server
# (restore afterwards!)
sudo cp /etc/resolv.conf /etc/resolv.conf.backup
echo "nameserver 192.0.2.1" | sudo tee /etc/resolv.conf

# Try to resolve
dig google.com    # should time out
ping google.com   # should fail

# Restore
sudo cp /etc/resolv.conf.backup /etc/resolv.conf
dig google.com    # should work again
```

---

## Module 2 Assessment

### Networking Graded Assessment

**Question 1**: A server with IP `10.0.2.15/24` wants to communicate with `10.0.3.20`. Will this traffic stay on the local network or be routed? Explain why.

**Question 2**: What is the difference between a switch and a router? At which OSI layers do they operate?

**Question 3**: Explain the DNS resolution process for `api.github.com` from scratch, assuming all caches are empty.

**Question 4**: A developer reports that `db.internal` is not resolving. List at least 4 commands you would run to diagnose the problem.

**Question 5**: What is the purpose of TTL (Time to Live) in a DNS record? What are the trade-offs of setting TTL very low vs. very high?

**Question 6**: Your application can reach `8.8.8.8` by IP but cannot resolve `google.com`. What does this tell you, and how do you fix it?

---

# Module 3 – Applications Basics

## Learning Objectives

By the end of this module you will be able to:

- Understand basic concepts of Java, Node.js, and Python
- Build, package, and manage dependencies for each language
- Use language-specific package managers: Maven/Gradle JARs, NPM, and PIP

---

## Java – Introduction and Build & Packaging

### What Is Java?

Java is a statically typed, object-oriented, compiled-then-interpreted language released by Sun Microsystems in 1995. It runs on the **Java Virtual Machine (JVM)**, which means Java code compiles once and runs anywhere a JVM exists.

```
  Java Source (.java)
         │
         ▼  javac (Java Compiler)
  Bytecode (.class)
         │
         ▼  JVM (Java Virtual Machine)
  Machine execution
  (Windows / Linux / macOS)
```

Key Java concepts:

|Concept|Description|
|---|---|
|**JDK**|Java Development Kit — includes compiler (`javac`), JVM, and libraries|
|**JRE**|Java Runtime Environment — JVM + standard libraries (no compiler)|
|**JVM**|Java Virtual Machine — executes bytecode|
|**JAR**|Java ARchive — packages `.class` files + resources into a single `.jar`|
|**Maven/Gradle**|Build tools that manage dependencies, compile, test, and package|

### Installing Java

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y openjdk-17-jdk    # JDK (for development)
sudo apt install -y openjdk-17-jre    # JRE only (for running apps)

# RHEL/CentOS
sudo dnf install -y java-17-openjdk-devel   # JDK
sudo dnf install -y java-17-openjdk         # JRE

# Verify
java -version
javac -version

# Manage multiple Java versions (Ubuntu)
sudo update-alternatives --config java
sudo update-alternatives --config javac

# Set JAVA_HOME
echo 'export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))' >> ~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc
source ~/.bashrc
echo $JAVA_HOME
```

### Hands-on Lab: Java Introduction

**Objective**: Write, compile, and run your first Java program.

**Estimated time**: 15 minutes

---

**Step 1 – Write a Java program**

```bash
mkdir ~/java-lab && cd ~/java-lab

cat > HelloDevOps.java << 'EOF'
public class HelloDevOps {

    public static void main(String[] args) {
        System.out.println("Hello, DevOps!");
        System.out.println("Java version: " + System.getProperty("java.version"));
        System.out.println("OS: " + System.getProperty("os.name"));

        // Demonstrate variables and control flow
        int buildNumber = 42;
        String environment = args.length > 0 ? args[0] : "development";

        System.out.printf("Build #%d deploying to: %s%n", buildNumber, environment);

        if (environment.equals("production")) {
            System.out.println("WARNING: Deploying to PRODUCTION!");
        } else {
            System.out.println("Deploying to non-production environment.");
        }
    }
}
EOF
```

**Step 2 – Compile and run**

```bash
# Compile source to bytecode
javac HelloDevOps.java

# List generated files
ls -la
# HelloDevOps.class  HelloDevOps.java

# Run the program
java HelloDevOps

# Run with an argument
java HelloDevOps production
```

**Step 3 – Explore the compiled class**

```bash
# View bytecode (disassembled)
javap -c HelloDevOps.class | head -30

# View just the method signatures
javap HelloDevOps.class
```

### Java – Build and Packaging

#### Maven

**Apache Maven** is the most widely used Java build tool. It uses a `pom.xml` (Project Object Model) file to describe the project, dependencies, build configuration, and plugins.

**Maven Project Structure (Standard Layout):**

```
my-app/
├── pom.xml                        ← Project descriptor
└── src/
    ├── main/
    │   ├── java/
    │   │   └── com/example/App.java  ← Main source code
    │   └── resources/
    │       └── application.properties
    └── test/
        └── java/
            └── com/example/AppTest.java  ← Test code
```

**Sample `pom.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <!-- Project coordinates (GAV: GroupId, ArtifactId, Version) -->
    <groupId>com.example</groupId>
    <artifactId>my-devops-app</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <name>My DevOps Application</name>
    <description>A sample Java application for the DevOps course</description>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- HTTP client -->
        <dependency>
            <groupId>com.squareup.okhttp3</groupId>
            <artifactId>okhttp</artifactId>
            <version>4.12.0</version>
        </dependency>

        <!-- JSON processing -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.16.1</version>
        </dependency>

        <!-- Testing (scope=test means not included in final JAR) -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Create an executable "fat JAR" with all dependencies -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <version>3.6.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.example.App</mainClass>
                        </manifest>
                    </archive>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals><goal>single</goal></goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

**Maven Lifecycle and Commands:**

```bash
# Install Maven
sudo apt install -y maven           # Ubuntu
sudo dnf install -y maven           # RHEL

mvn --version

# Maven build lifecycle phases (in order):
# validate → compile → test → package → verify → install → deploy

mvn validate                   # validate pom.xml
mvn compile                    # compile src/main/java
mvn test                       # compile + run tests
mvn package                    # compile + test + create JAR/WAR
mvn verify                     # run integration tests
mvn install                    # package + install to local ~/.m2/repository
mvn deploy                     # install + upload to remote repository

# Common flags
mvn package -DskipTests        # skip tests (faster)
mvn package -T 4               # use 4 threads
mvn clean package              # clean build directory first
mvn dependency:tree            # show dependency tree
mvn dependency:resolve         # download all dependencies

# Run the app
java -jar target/my-devops-app-1.0.0-jar-with-dependencies.jar
```

#### Gradle

**Gradle** is a modern alternative to Maven that uses Groovy or Kotlin DSL instead of XML:

```groovy
// build.gradle (Groovy DSL)
plugins {
    id 'java'
    id 'application'
}

group = 'com.example'
version = '1.0.0'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'com.squareup.okhttp3:okhttp:4.12.0'
    implementation 'com.fasterxml.jackson.core:jackson-databind:2.16.1'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.1'
}

application {
    mainClass = 'com.example.App'
}

test {
    useJUnitPlatform()
}
```

```bash
# Gradle commands
./gradlew build               # compile + test + package
./gradlew test                # run tests
./gradlew jar                 # create JAR
./gradlew dependencies        # show dependency tree
./gradlew run                 # run the application
./gradlew clean build         # clean + build
```

#### Understanding JARs and WARs

```bash
# A JAR is just a ZIP file with a specific structure
jar tf myapp.jar                      # list contents
jar xf myapp.jar                      # extract
unzip -l myapp.jar | head -20         # same result (it's a ZIP!)

# JAR contents:
# META-INF/MANIFEST.MF   ← metadata including Main-Class
# com/example/App.class  ← compiled classes
# application.properties ← resources

# View the manifest
unzip -p myapp.jar META-INF/MANIFEST.MF

# Run an executable JAR
java -jar myapp.jar

# Run with custom heap size
java -Xmx512m -Xms256m -jar myapp.jar

# Pass system properties
java -Dspring.profiles.active=production -jar myapp.jar

# WAR (Web Application Archive) — for deploying to servlet containers
# Contains:
# WEB-INF/web.xml          ← deployment descriptor
# WEB-INF/lib/             ← dependency JARs
# WEB-INF/classes/         ← compiled classes
# index.html, static files
```

### Hands-on Lab: Java – JARs and Build & Packaging

**Objective**: Create a Maven project, add a dependency, build a JAR, and run it.

**Estimated time**: 25 minutes

---

**Step 1 – Install Maven**

```bash
sudo apt install -y maven     # Ubuntu
mvn --version
```

**Step 2 – Generate a project using the Maven archetype**

```bash
cd ~
mvn archetype:generate \
  -DgroupId=com.devops \
  -DartifactId=devops-app \
  -DarchetypeArtifactId=maven-archetype-quickstart \
  -DarchetypeVersion=1.4 \
  -DinteractiveMode=false

cd devops-app
```

**Step 3 – Explore the generated structure**

```bash
find . -type f | sort
cat pom.xml
cat src/main/java/com/devops/App.java
```

**Step 4 – Modify the application**

```bash
cat > src/main/java/com/devops/App.java << 'EOF'
package com.devops;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class App {
    public static void main(String[] args) {
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String timestamp = LocalDateTime.now().format(fmt);

        System.out.println("=================================");
        System.out.println("  DevOps Application v1.0.0");
        System.out.println("=================================");
        System.out.println("Started at: " + timestamp);
        System.out.println("Java:       " + System.getProperty("java.version"));
        System.out.println("OS:         " + System.getProperty("os.name"));
        System.out.println("User:       " + System.getProperty("user.name"));
        System.out.println("=================================");
    }
}
EOF
```

**Step 5 – Build and run**

```bash
# Compile
mvn compile

# Run tests
mvn test

# Package into a JAR
mvn package -DskipTests

# Check what was created
ls -lh target/
ls -lh target/*.jar

# Run the JAR
java -cp target/devops-app-1.0-SNAPSHOT.jar com.devops.App
```

**Step 6 – Add a dependency and build a fat JAR**

```bash
# Update pom.xml to add the assembly plugin and a version property
# (edit to add the properties, dependency, and plugin sections shown in the pom.xml example above)
# Then:
mvn clean package -DskipTests
ls -lh target/
java -jar target/devops-app-1.0-SNAPSHOT-jar-with-dependencies.jar
```

---

## Node.js – Introduction and NPM

### What Is Node.js?

**Node.js** is a JavaScript runtime built on Chrome's V8 engine. It allows JavaScript — traditionally a browser-only language — to run on the server. Node.js uses an **event-driven, non-blocking I/O model**, making it highly efficient for I/O-heavy workloads like web servers and APIs.

```
  Browser JavaScript            Node.js
  ────────────────              ──────────────────────────
  Runs in browser               Runs on server
  DOM APIs available            File system, network, OS APIs
  Sandboxed                     Full system access
  V8 engine                     V8 engine + libuv (async I/O)
```

### Installing Node.js

```bash
# Option 1: Install via NVM (Node Version Manager) — RECOMMENDED
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Reload shell
source ~/.bashrc

# Install latest LTS version
nvm install --lts
nvm use --lts

# Install a specific version
nvm install 20.11.0
nvm use 20.11.0

# List installed versions
nvm ls

# Option 2: Install via package manager (Ubuntu)
sudo apt install -y nodejs npm

# Option 3: Install from NodeSource (latest versions)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Verify
node --version
npm --version
```

### Hands-on Lab: Node.js Introduction

**Objective**: Write and run Node.js scripts, including a simple HTTP server.

**Estimated time**: 15 minutes

---

**Step 1 – Hello World**

```bash
mkdir ~/nodejs-lab && cd ~/nodejs-lab

cat > hello.js << 'EOF'
// Basic output
console.log("Hello, DevOps!");

// Variables
const appName = "DevOps App";
const version = "1.0.0";
const port = process.env.PORT || 3000;

console.log(`${appName} v${version} will listen on port ${port}`);

// Arrays and loops
const environments = ["development", "staging", "production"];
environments.forEach((env, index) => {
    console.log(`Environment ${index + 1}: ${env}`);
});

// System info
console.log("\nSystem Info:");
console.log(`Node.js version: ${process.version}`);
console.log(`Platform: ${process.platform}`);
console.log(`PID: ${process.pid}`);
EOF

node hello.js

# With environment variable
PORT=8080 node hello.js
```

**Step 2 – Create a simple HTTP server**

```bash
cat > server.js << 'EOF'
const http = require('http');
const os = require('os');

const PORT = process.env.PORT || 3000;
const HOST = process.env.HOST || '0.0.0.0';

const server = http.createServer((req, res) => {
    const timestamp = new Date().toISOString();

    if (req.url === '/health') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
            status: 'healthy',
            timestamp,
            uptime: process.uptime(),
            hostname: os.hostname()
        }));
    } else if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(`
            <h1>DevOps Node.js App</h1>
            <p>Timestamp: ${timestamp}</p>
            <p>Node.js: ${process.version}</p>
            <p>Hostname: ${os.hostname()}</p>
            <p><a href="/health">Health Check</a></p>
        `);
    } else {
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Not found' }));
    }

    console.log(`[${timestamp}] ${req.method} ${req.url} → ${res.statusCode}`);
});

server.listen(PORT, HOST, () => {
    console.log(`Server running at http://${HOST}:${PORT}`);
    console.log('Press Ctrl+C to stop');
});
EOF

# Run in background
node server.js &
SERVER_PID=$!

# Test it
sleep 1
curl http://localhost:3000
curl http://localhost:3000/health
curl http://localhost:3000/notfound

# Stop the server
kill $SERVER_PID
```

### Node.js – NPM

**NPM (Node Package Manager)** is the default package manager for Node.js and the world's largest software registry (over 2 million packages).

### `package.json` — The Project Manifest

Every Node.js project has a `package.json` that describes the project, its dependencies, scripts, and metadata:

```json
{
  "name": "devops-api",
  "version": "1.0.0",
  "description": "A DevOps API built with Express.js",
  "main": "src/index.js",
  "scripts": {
    "start":     "node src/index.js",
    "dev":       "nodemon src/index.js",
    "test":      "jest --coverage",
    "lint":      "eslint src/",
    "build":     "echo 'No build step needed'",
    "clean":     "rm -rf node_modules"
  },
  "dependencies": {
    "express":  "^4.18.2",
    "dotenv":   "^16.3.1",
    "axios":    "^1.6.5"
  },
  "devDependencies": {
    "jest":     "^29.7.0",
    "nodemon":  "^3.0.2",
    "eslint":   "^8.56.0"
  },
  "engines": {
    "node": ">=18.0.0",
    "npm":  ">=9.0.0"
  },
  "keywords": ["devops", "api", "nodejs"],
  "author": "Alice <alice@example.com>",
  "license": "MIT"
}
```

**Dependency types:**

|Type|Key|Purpose|
|---|---|---|
|**dependencies**|`"dependencies"`|Required in production|
|**devDependencies**|`"devDependencies"`|Testing, linting, build tools — not in production|
|**peerDependencies**|`"peerDependencies"`|Required by consumers of this package|
|**optionalDependencies**|`"optionalDependencies"`|Nice to have; build succeeds if absent|

**Version specifiers:**

|Specifier|Meaning|
|---|---|
|`"4.18.2"`|Exact version|
|`"^4.18.2"`|Compatible (same major: ≥4.18.2 <5.0.0)|
|`"~4.18.2"`|Patch updates only (≥4.18.2 <4.19.0)|
|`"*"`|Latest (avoid in production!)|
|`">=4.0.0 <5.0.0"`|Range|

### NPM Commands

```bash
# Initialize a new project
npm init                          # interactive wizard
npm init -y                       # accept all defaults

# Install dependencies
npm install                       # install all from package.json
npm install express               # add to dependencies
npm install jest --save-dev       # add to devDependencies
npm install -g nodemon            # install globally

# Remove a package
npm uninstall express
npm uninstall jest --save-dev

# Update packages
npm update                        # update within semver range
npm outdated                      # show outdated packages

# Run scripts from package.json
npm start                         # run "start" script
npm test                          # run "test" script
npm run dev                       # run custom scripts with "run"
npm run lint

# View installed packages
npm list                          # local tree
npm list --depth=0                # top-level only
npm list -g --depth=0             # globally installed

# Package information
npm info express
npm search jwt                    # search the registry

# Audit for security vulnerabilities
npm audit
npm audit fix                     # auto-fix where possible

# Publish a package (requires npm account)
npm publish
npm publish --access public       # for scoped packages
```

**`package-lock.json`** is automatically generated and should be committed to version control. It locks the exact version of every package in the dependency tree, ensuring reproducible installs across environments.

```bash
# Install using lock file (for CI/CD — faster, reproducible)
npm ci                            # clean install from lock file

# Never run npm install in CI — use npm ci instead
```

### Hands-on Lab: Node.js – NPM

**Objective**: Initialize a Node.js project, add dependencies, and build an Express API.

**Estimated time**: 25 minutes

---

**Step 1 – Initialize the project**

```bash
mkdir ~/nodejs-lab/express-api && cd ~/nodejs-lab/express-api
npm init -y

# View the generated package.json
cat package.json
```

**Step 2 – Install Express and dotenv**

```bash
npm install express dotenv
npm install nodemon --save-dev

# View the lock file
ls -la
cat package.json
```

**Step 3 – Create the application**

```bash
mkdir src

cat > .env << 'EOF'
PORT=3000
APP_NAME=DevOps API
VERSION=1.0.0
ENVIRONMENT=development
EOF

cat > src/index.js << 'EOF'
require('dotenv').config();
const express = require('express');
const os = require('os');

const app = express();
const PORT = process.env.PORT || 3000;
const APP_NAME = process.env.APP_NAME || 'API';

app.use(express.json());

// Request logging middleware
app.use((req, res, next) => {
    console.log(`${new Date().toISOString()} ${req.method} ${req.url}`);
    next();
});

// Routes
app.get('/', (req, res) => {
    res.json({
        name: APP_NAME,
        version: process.env.VERSION,
        environment: process.env.ENVIRONMENT,
        nodeVersion: process.version
    });
});

app.get('/health', (req, res) => {
    res.json({
        status: 'healthy',
        uptime: process.uptime(),
        memory: process.memoryUsage(),
        hostname: os.hostname(),
        timestamp: new Date().toISOString()
    });
});

app.get('/info', (req, res) => {
    res.json({
        platform: os.platform(),
        cpus: os.cpus().length,
        totalMemory: `${Math.round(os.totalmem() / 1024 / 1024)} MB`,
        freeMemory: `${Math.round(os.freemem() / 1024 / 1024)} MB`,
        loadAvg: os.loadavg()
    });
});

// 404 handler
app.use((req, res) => {
    res.status(404).json({ error: `Route ${req.url} not found` });
});

app.listen(PORT, () => {
    console.log(`${APP_NAME} listening on http://0.0.0.0:${PORT}`);
});

module.exports = app;
EOF
```

**Step 4 – Add scripts to package.json**

```bash
# Update package.json scripts section
node -e "
const pkg = require('./package.json');
pkg.scripts = {
  start: 'node src/index.js',
  dev: 'nodemon src/index.js',
  test: 'echo \"No tests yet\" && exit 0'
};
require('fs').writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

cat package.json
```

**Step 5 – Run and test**

```bash
# Start the server
node src/index.js &
SERVER_PID=$!
sleep 1

# Test endpoints
curl -s http://localhost:3000 | python3 -m json.tool
curl -s http://localhost:3000/health | python3 -m json.tool
curl -s http://localhost:3000/info | python3 -m json.tool
curl -s http://localhost:3000/missing | python3 -m json.tool

# Stop
kill $SERVER_PID
```

**Step 6 – Check for outdated packages and security issues**

```bash
npm outdated
npm audit
```

---

## Python – Introduction and PIP

### What Is Python?

Python is a dynamically typed, interpreted, high-level language known for its readability and versatility. It is the dominant language for DevOps scripting, automation, data science, and machine learning.

```
  Python source (.py)
         │
         ▼  CPython interpreter
  Bytecode (.pyc) ← cached in __pycache__/
         │
         ▼
  Machine execution
```

Key Python concepts:

|Concept|Description|
|---|---|
|**CPython**|The reference Python interpreter (written in C)|
|**pip**|Package Installer for Python|
|**venv**|Built-in virtual environment tool|
|**PyPI**|Python Package Index — the official package repository|
|**`__init__.py`**|Marks a directory as a Python package|
|**WSGI/ASGI**|Web server interfaces for deploying Python web apps|

### Installing Python

```bash
# Python 3 is the current standard (Python 2 is EOL)
# Most Linux systems include Python 3 by default

# Ubuntu
sudo apt install -y python3 python3-pip python3-venv

# RHEL/CentOS
sudo dnf install -y python3 python3-pip

# Verify
python3 --version
pip3 --version

# Set python3 as the default 'python' command
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Install pyenv for managing multiple Python versions
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

pyenv install 3.12.0
pyenv global 3.12.0
python --version
```

### Hands-on Lab: Python Introduction

**Objective**: Write and run Python scripts demonstrating key language features.

**Estimated time**: 15 minutes

---

**Step 1 – Write a Python script**

```bash
mkdir ~/python-lab && cd ~/python-lab

cat > devops_info.py << 'EOF'
#!/usr/bin/env python3
"""DevOps system information script."""

import os
import platform
import sys
import subprocess
from datetime import datetime


def get_system_info() -> dict:
    """Collect system information."""
    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "python_version": sys.version.split()[0],
        "timestamp": datetime.now().isoformat(),
        "user": os.getenv("USER", "unknown"),
    }


def check_tool(tool: str) -> str:
    """Check if a CLI tool is installed and return its version."""
    try:
        result = subprocess.run(
            [tool, "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = (result.stdout or result.stderr).strip().split("\n")[0]
        return output
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "not installed"


def main():
    print("=" * 50)
    print("  DevOps Environment Check")
    print("=" * 50)

    info = get_system_info()
    for key, value in info.items():
        print(f"  {key:<20}: {value}")

    print("\n  Tool Versions:")
    tools = ["git", "docker", "kubectl", "ansible", "terraform"]
    for tool in tools:
        version = check_tool(tool)
        status = "✓" if "not installed" not in version else "✗"
        print(f"  {status} {tool:<15}: {version[:50]}")

    print("=" * 50)


if __name__ == "__main__":
    main()
EOF

python3 devops_info.py
```

**Step 2 – Python data types and control flow**

```bash
cat > basics.py << 'EOF'
#!/usr/bin/env python3

# Strings
app_name = "DevOps App"
version = "2.1.0"
print(f"App: {app_name}, Version: {version}")

# Lists
environments = ["dev", "staging", "prod"]
print(f"Environments: {environments}")
print(f"Production: {environments[-1]}")
environments.append("dr")
print(f"After append: {environments}")

# Dictionaries
config = {
    "host": "0.0.0.0",
    "port": 8080,
    "debug": False,
    "workers": 4,
}
print(f"\nConfig: {config}")
print(f"Port: {config['port']}")

# Update config from environment
for key in config:
    env_val = __import__('os').getenv(key.upper())
    if env_val:
        config[key] = env_val
        print(f"Overrode {key} from environment")

# List comprehension (very Pythonic)
dev_envs = [env for env in environments if env != "prod"]
print(f"\nNon-prod environments: {dev_envs}")

# Functions
def deploy(app: str, env: str, dry_run: bool = False) -> bool:
    if dry_run:
        print(f"[DRY RUN] Would deploy {app} to {env}")
        return True
    print(f"Deploying {app} to {env}...")
    # Real deployment logic would go here
    return True

deploy("myapp", "staging")
deploy("myapp", "prod", dry_run=True)
EOF

python3 basics.py
```

**Step 3 – File I/O and JSON**

```bash
cat > config_manager.py << 'EOF'
#!/usr/bin/env python3
import json
import os

CONFIG_FILE = "app_config.json"

DEFAULT_CONFIG = {
    "database": {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "5432")),
        "name": os.getenv("DB_NAME", "myapp"),
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8080,
        "workers": 4,
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/myapp/app.log",
    }
}

def save_config(config: dict, path: str = CONFIG_FILE):
    with open(path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved to {path}")

def load_config(path: str = CONFIG_FILE) -> dict:
    if not os.path.exists(path):
        print(f"Config file not found: {path}. Using defaults.")
        return DEFAULT_CONFIG
    with open(path) as f:
        return json.load(f)

# Save
save_config(DEFAULT_CONFIG)

# Load and display
config = load_config()
print(json.dumps(config, indent=2))

# Access nested values safely
db_host = config.get("database", {}).get("host", "unknown")
print(f"\nDatabase host: {db_host}")
EOF

python3 config_manager.py
```

### Python – PIP

**pip** is Python's package installer. It downloads packages from **PyPI** (the Python Package Index at https://pypi.org).

### Virtual Environments

A **virtual environment** is an isolated Python installation for a specific project. It prevents dependency conflicts between projects.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate          # Linux/macOS
# venv\Scripts\activate           # Windows

# Your prompt changes to show the active venv:
# (venv) user@host:~/project$

# Deactivate when done
deactivate

# Remove the virtual environment
rm -rf venv/
```

**Always use a virtual environment.** Never install project dependencies globally with `sudo pip install`.

### pip Commands

```bash
# (With virtual environment activated)

# Install a package
pip install flask
pip install flask==3.0.0            # specific version
pip install "flask>=2.0,<4.0"       # version range
pip install flask requests gunicorn # multiple at once

# Install from a requirements file
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade flask

# Uninstall
pip uninstall flask
pip uninstall flask requests -y     # no confirmation

# List installed packages
pip list
pip list --outdated

# Show package info
pip show flask

# Freeze current environment to a requirements file
pip freeze > requirements.txt
cat requirements.txt

# Search PyPI (deprecated in newer pip; use web search or pip index)
pip index versions flask

# Audit for vulnerabilities
pip install pip-audit
pip-audit
```

### `requirements.txt` Best Practices

```bash
# requirements.txt — pinned versions for reproducibility
flask==3.0.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
redis==5.0.1
python-dotenv==1.0.0
requests==2.31.0

# For development dependencies, use a separate file:
# requirements-dev.txt
-r requirements.txt
pytest==7.4.4
pytest-cov==4.1.0
black==23.12.1
flake8==7.0.0
mypy==1.8.0
```

### Hands-on Lab: Python – PIP

**Objective**: Create a virtual environment, install packages, and build a Flask web application.

**Estimated time**: 25 minutes

---

**Step 1 – Create a virtual environment**

```bash
cd ~/python-lab
python3 -m venv venv
source venv/bin/activate

# Verify we're using the venv's Python
which python
which pip
python --version
```

**Step 2 – Install dependencies**

```bash
pip install flask requests python-dotenv
pip list

# Freeze to requirements.txt
pip freeze > requirements.txt
cat requirements.txt
```

**Step 3 – Create a Flask application**

```bash
cat > .env << 'EOF'
FLASK_ENV=development
SECRET_KEY=dev-secret-change-in-prod
PORT=5000
EOF

cat > app.py << 'EOF'
#!/usr/bin/env python3
"""A simple DevOps Flask API."""

import os
import platform
from datetime import datetime
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")

START_TIME = datetime.now()


@app.route("/")
def index():
    return jsonify({
        "name": "DevOps Flask API",
        "version": "1.0.0",
        "python": platform.python_version(),
        "flask": __import__("flask").__version__,
    })


@app.route("/health")
def health():
    uptime = (datetime.now() - START_TIME).total_seconds()
    return jsonify({
        "status": "healthy",
        "uptime_seconds": round(uptime, 2),
        "timestamp": datetime.now().isoformat(),
        "hostname": platform.node(),
    })


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    return jsonify({
        "received": data,
        "timestamp": datetime.now().isoformat(),
    })


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found", "path": request.path}), 404


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
EOF
```

**Step 4 – Run and test**

```bash
# Run in background
python app.py &
APP_PID=$!
sleep 2

# Test
curl -s http://localhost:5000/ | python3 -m json.tool
curl -s http://localhost:5000/health | python3 -m json.tool
curl -s -X POST http://localhost:5000/echo \
     -H "Content-Type: application/json" \
     -d '{"message": "hello", "env": "lab"}' | python3 -m json.tool

# Stop
kill $APP_PID
```

**Step 5 – Test reproducible install from requirements.txt**

```bash
# Deactivate and remove current venv
deactivate
rm -rf venv/

# Create a fresh venv and install from requirements.txt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip list

# Verify the app still works
python app.py &
APP_PID=$!
sleep 1
curl -s http://localhost:5000/ | python3 -m json.tool
kill $APP_PID
```

**Step 6 – Explore pip audit**

```bash
pip install pip-audit
pip-audit

deactivate
```

---

## Module 3 Assessment

### Applications Basics Graded Assessment

**Question 1**: Explain the difference between the JDK and the JRE. In a production deployment scenario (running, not developing), which do you install and why?

**Question 2**: What is the difference between `npm install` and `npm ci`? Which should you use in a CI/CD pipeline and why?

**Question 3**: A Python developer tells you they installed all their project's packages with `sudo pip3 install`. Why is this a problem, and what should they do instead?

**Question 4**: What is a "fat JAR" (or "uber JAR")? What problem does it solve for deployment?

**Question 5**: In `package.json`, what is the difference between `dependencies` and `devDependencies`? Give an example of a package that belongs in each.

**Question 6**: What is `pip freeze > requirements.txt` and why is committing this file to Git important for a DevOps team?

**Question 7**: A Maven build fails with a `Could not resolve dependencies` error. List three possible causes and how you would diagnose each.

---

# Quick Reference Card

## Linux Essentials

```bash
# Navigation
pwd / ls -la / cd / mkdir -p / rm -rf

# Files
cat / less / head / tail -f / cp / mv / find / grep

# Permissions
chmod 755 file / chown user:group file / ls -l

# Users
whoami / id / sudo / su - / useradd / usermod -aG

# Pipes & Redirection
cmd > file / cmd >> file / cmd1 | cmd2 / cmd 2>&1

# Archive
tar -czvf out.tar.gz dir/ / tar -xzvf archive.tar.gz

# Process
ps aux / kill PID / jobs / bg / fg

# System
df -h / free -h / uname -a / uptime
```

## Package Management

```bash
# APT (Debian/Ubuntu)
sudo apt update && sudo apt install -y PKG
sudo apt remove PKG / sudo apt purge PKG

# DNF/YUM (RHEL/CentOS)
sudo dnf install -y PKG / sudo dnf remove PKG

# NPM
npm install PKG / npm uninstall PKG
npm install --save-dev PKG / npm ci / npm audit

# PIP (always in a venv!)
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt / pip-audit
```

## systemctl

```bash
sudo systemctl start|stop|restart|reload|status SERVICE
sudo systemctl enable|disable SERVICE
sudo systemctl daemon-reload        # after editing unit files
journalctl -u SERVICE -f            # follow logs
```

## Networking

```bash
ip addr show / ip route show
ping -c 4 HOST / traceroute HOST
ss -tlnp / lsof -i :PORT
dig DOMAIN +short / dig @8.8.8.8 DOMAIN
curl -I http://HOST / curl -sv https://HOST
```

## Java / Maven

```bash
javac App.java && java App
mvn clean package -DskipTests
java -jar target/app.jar
mvn dependency:tree
```

## Node.js / NPM

```bash
node app.js
npm init -y
npm install express
npm run start / npm test / npm ci
```

## Python / PIP

```bash
python3 -m venv venv && source venv/bin/activate
pip install flask && pip freeze > requirements.txt
python3 app.py
deactivate
```

---

_End of DevOps Prerequisite Course — Course 1_

> **Next in the series**: Course 2 – Git Basics for DevOps builds on these Linux and application fundamentals to introduce version control for your code and infrastructure.