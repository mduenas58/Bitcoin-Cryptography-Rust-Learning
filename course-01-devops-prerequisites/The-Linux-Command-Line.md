---
tags: [linux, shell, cli, reference, bash, scripting]
source: "The Linux Command Line, 3rd Edition — William Shotts"
created: 2026-03-08
type: reference
---

# 🐧 The Linux Command Line — Reference Note

> **Source:** *The Linux Command Line, 3rd Edition* by William Shotts
> **Scope:** Bash shell — navigation, file ops, scripting, and beyond

---

## Part I — Learning the Shell

### Ch 1 · The Shell

The **shell** is a program that takes keyboard commands and passes them to the OS. `bash` is the most common shell on Linux.

```bash
date        # Show current date/time
uptime      # Show how long system has been running
df          # Show disk space usage
free        # Show free memory
exit        # End terminal session
```

**Keyboard shortcuts:**

| Shortcut | Action |
|----------|--------|
| `↑` / `↓` | Browse command history |
| `←` / `→` | Move cursor within line |
| `Ctrl+A` | Move to beginning of line |
| `Ctrl+E` | Move to end of line |
| `Ctrl+C` | Interrupt current command |
| `Ctrl+D` | Send EOF / exit shell |

> **Tip:** Middle-click pastes selected text in most terminal emulators.

---

### Ch 2 · Navigation

```bash
pwd             # Print working directory
ls              # List directory contents
ls /path        # List contents of specific path
cd /usr/bin     # Change to absolute path
cd ..           # Go up one level (parent directory)
cd ~            # Go to home directory
cd -            # Go to previous directory
```

**Path types:**
- **Absolute path** — starts from `/` (root): `/home/user/documents`
- **Relative path** — relative to current dir: `../docs` or `./file.txt`

---

### Ch 3 · Exploring the System

```bash
ls -l           # Long format listing
ls -a           # Show hidden (dot) files
ls -lt          # Long format, sorted by modification time
ls -lt --reverse  # Oldest first
ls -lh          # Human-readable file sizes

file filename   # Determine file type
less filename   # View file contents (scrollable)
```

**Long listing fields:** `permissions · links · owner · group · size · date · name`

**`less` navigation:**

| Key | Action |
|-----|--------|
| `Space` | Next page |
| `b` | Previous page |
| `/pattern` | Search forward |
| `n` | Next search match |
| `q` | Quit |

**Important Linux directories:**

| Dir | Purpose |
|-----|---------|
| `/` | Root of filesystem |
| `/bin` | Essential system binaries |
| `/etc` | System configuration files |
| `/home` | User home directories |
| `/usr/bin` | User programs/binaries |
| `/var` | Variable data (logs, mail, etc.) |
| `/tmp` | Temporary files |
| `/dev` | Device files |

---

### Ch 4 · Manipulating Files and Directories

#### Wildcards

| Pattern | Matches |
|---------|---------|
| `*` | Any characters |
| `?` | Any single character |
| `[abc]` | Any character in set |
| `[!abc]` | Any character NOT in set |
| `[a-z]` | Any character in range |

#### Core Commands

```bash
mkdir dir               # Create directory
mkdir -p a/b/c          # Create nested directories

cp file1 file2          # Copy file
cp -r dir1 dir2         # Copy directory recursively
cp -u *.html dest/      # Copy only if source is newer

mv file1 file2          # Rename or move file
mv file dir/            # Move file into directory

rm file                 # Delete file
rm -r dir               # Delete directory recursively
rm -i file              # Prompt before deleting (safe)
rm -f file              # Force delete (no prompt)

ln file hardlink        # Create hard link
ln -s file symlink      # Create symbolic (soft) link
```

> ⚠️ **Caution:** `rm` has no recycle bin. Always use `-i` when unsure, especially with wildcards.

---

### Ch 5 · Working with Commands

**Four types of commands:**
1. **Executable programs** — compiled binaries (`/usr/bin`)
2. **Shell builtins** — built into the shell (`cd`, `echo`)
3. **Shell functions** — scripts defined in environment
4. **Aliases** — user-defined shortcuts

```bash
type ls             # Show what kind of command 'ls' is
which ls            # Show executable location
help cd             # Help for shell builtins
man ls              # Manual page for command
apropos search      # Search man pages by keyword
whatis ls           # One-line description of command
info coreutils      # Info page (more detailed than man)
--help              # Most commands support this flag

# Creating aliases
alias ll='ls -la'
alias rm='rm -i'    # Safer rm with confirmation prompt
```

---

### Ch 6 · Redirection

```bash
# Standard streams
# stdin  (0) — keyboard input
# stdout (1) — screen output
# stderr (2) — error messages

# Redirecting stdout
ls /usr/bin > output.txt        # Overwrite file
ls /usr/bin >> output.txt       # Append to file

# Redirecting stderr
ls /bad/path 2> errors.txt
ls /bad/path 2>> errors.txt     # Append errors

# Redirect both stdout and stderr
ls /usr/bin /bad/path > all.txt 2>&1
ls /usr/bin /bad/path &> all.txt    # Shorthand (bash 4+)

# Discard output
ls > /dev/null

# stdin from file
sort < unsorted.txt

# Pipelines
ls | sort | less
ls /usr/bin | grep zip          # Filter output
ls /usr/bin | wc -l             # Count lines
```

**Useful pipeline commands:**

| Command | Purpose |
|---------|---------|
| `cat` | Concatenate and display files |
| `sort` | Sort lines of text |
| `uniq` | Report or omit repeated lines |
| `wc` | Count lines, words, bytes |
| `grep pattern` | Print lines matching pattern |
| `head -n 5` | Show first N lines |
| `tail -n 5` | Show last N lines |
| `tee file` | Read stdin, write to stdout AND file |

---

### Ch 7 · Shell Expansion

```bash
echo *              # Pathname expansion (globbing)
echo D*             # Files starting with D
echo ~              # Tilde expansion → home dir
echo ~username      # Another user's home dir

echo $((2 + 2))     # Arithmetic expansion
echo $((5 ** 2))    # Exponentiation

echo {a,b,c}        # Brace expansion → a b c
echo {1..5}         # Range → 1 2 3 4 5
echo file{A,B}.txt  # → fileA.txt fileB.txt

ls $(which cp)      # Command substitution
echo $(date)
```

**Quoting rules:**
- `"double quotes"` — suppress word splitting and pathname expansion; allow `$`, `\`, backtick
- `'single quotes'` — suppress ALL special characters
- `\` — escape a single character

---

### Ch 8 · Advanced Keyboard Tricks

**Cursor movement:**

| Key | Action |
|-----|--------|
| `Ctrl+A` | Beginning of line |
| `Ctrl+E` | End of line |
| `Ctrl+F` / `Ctrl+B` | Forward / back one char |
| `Alt+F` / `Alt+B` | Forward / back one word |
| `Ctrl+K` | Delete to end of line |
| `Ctrl+U` | Delete to beginning of line |
| `Ctrl+D` | Delete char at cursor |
| `Ctrl+Y` | Paste (yank) deleted text |

**History:**

```bash
history             # Show command history
history | grep ssh  # Search history
!88                 # Execute history item 88
!!                  # Repeat last command
!string             # Repeat last command starting with string
Ctrl+R              # Reverse search through history
```

---

### Ch 9 · Permissions

```bash
# Permission notation: rwxrwxrwx (owner|group|other)
# r=read(4), w=write(2), x=execute(1)

chmod 755 file      # rwxr-xr-x (octal)
chmod u+x file      # Add execute for owner (symbolic)
chmod go-w file     # Remove write from group and other
chmod a=rw file     # Set all to read-write

chown user file         # Change file owner
chown user:group file   # Change owner and group
chgrp group file        # Change group only

# Viewing permissions
ls -l file          # -rwxr-xr-x 1 user group size date name

# Changing identities
su                  # Switch to root
su -l username      # Login as user
sudo command        # Run single command as root
sudo -l             # List sudo privileges
```

**Special permissions:**

| Permission | Octal | Effect |
|------------|-------|--------|
| `setuid` | `4xxx` | Run as file owner |
| `setgid` | `2xxx` | Run as file group |
| `sticky bit` | `1xxx` | Only owner can delete in shared dir |

---

### Ch 10 · Processes

```bash
ps              # Snapshot of current processes
ps aux          # All processes, detailed
top             # Dynamic real-time process view
htop            # Enhanced interactive process viewer

# Background / foreground
command &       # Run in background
jobs            # List background jobs
fg %1           # Bring job 1 to foreground
bg %1           # Resume job 1 in background
Ctrl+Z          # Pause / suspend current process
Ctrl+C          # Kill current foreground process

# Sending signals
kill PID            # Send SIGTERM (graceful stop)
kill -9 PID         # Send SIGKILL (force kill)
kill -l             # List all signals
killall program     # Kill all processes by name

# Shutdown / reboot
shutdown -h now     # Halt system immediately
shutdown -r now     # Reboot immediately
```

---

## Part II — Configuration & Environment

### Ch 11 · The Environment

```bash
printenv            # Print all environment variables
printenv HOME       # Print specific variable
set                 # Print all shell variables + functions
echo $PATH          # Show executable search path
echo $HOME          # Home directory
echo $USER          # Current username
echo $SHELL         # Current shell

export VAR=value    # Set and export variable to environment
unset VAR           # Remove variable
```

**Shell startup files:**

| File | Read when |
|------|-----------|
| `~/.bash_profile` | Login shell |
| `~/.bashrc` | Interactive non-login shell |
| `~/.bash_logout` | On logout |
| `/etc/profile` | System-wide login settings |

```bash
source ~/.bashrc    # Reload config without restarting
. ~/.bashrc         # Shorthand
```

---

### Ch 12 · vi/vim Basics

```
vim filename        # Open file in vim

# Modes
i                   # Insert mode (type text)
Esc                 # Return to command mode
:                   # Enter command-line mode

# Navigation (command mode)
h j k l             # Left / Down / Up / Right
0 / ^               # Start of line
$                   # End of line
gg / G              # First / last line
:n                  # Go to line n

# Editing
dd                  # Delete (cut) line
yy                  # Yank (copy) line
p                   # Paste after cursor
u                   # Undo
Ctrl+R              # Redo
x                   # Delete character

# Search & Replace
/pattern            # Search forward
?pattern            # Search backward
n / N               # Next / previous match
:%s/old/new/g       # Replace all in file
:s/old/new/g        # Replace in current line

# Save & Quit
:w                  # Save
:q                  # Quit
:wq or ZZ           # Save and quit
:q!                 # Quit without saving
```

---

## Part III — Common Tasks & Essential Tools

### Ch 14 · Package Management

**Debian/Ubuntu (apt):**
```bash
apt update                  # Update package index
apt upgrade                 # Upgrade installed packages
apt install package         # Install package
apt remove package          # Remove package
apt search keyword          # Search packages
apt show package            # Show package info
dpkg -l                     # List installed packages
```

**Red Hat/Fedora (dnf/rpm):**
```bash
dnf install package
dnf remove package
dnf update
dnf search keyword
rpm -qa                     # List installed packages
```

---

### Ch 16 · Networking

```bash
ip a                        # Show network interfaces (modern)
ifconfig                    # Show interfaces (legacy)
ping host                   # Test connectivity
ping -c 3 google.com        # Send 3 pings
traceroute host             # Show network path

netstat -tulpn              # Show open ports
ss -tulpn                   # Modern alternative to netstat

# File transfer
wget URL                    # Download file
curl -O URL                 # Download file
scp file user@host:/path    # Secure copy to remote
rsync -av src/ dest/        # Sync files (local or remote)

# SSH
ssh user@hostname           # Connect to remote host
ssh -p 2222 user@host       # Custom port
ssh-keygen                  # Generate SSH key pair
ssh-copy-id user@host       # Copy public key to remote
```

---

### Ch 17 · Searching for Files

```bash
locate filename         # Fast filename search (uses database)
updatedb                # Update locate database

# find — powerful, searches live filesystem
find / -name "*.txt"            # Find by name (case-sensitive)
find / -iname "*.txt"           # Case-insensitive
find /home -type f              # Files only
find /home -type d              # Directories only
find / -size +1M                # Files larger than 1MB
find / -mtime -7                # Modified in last 7 days
find / -user username           # Owned by user
find / -perm 777                # By permission

# Combine with actions
find . -name "*.log" -delete            # Delete found files
find . -name "*.sh" -exec chmod +x {} \;  # Execute on each result
```

---

### Ch 18 · Archiving and Backup

```bash
# gzip / gunzip
gzip file               # Compress file (replaces original)
gunzip file.gz          # Decompress
gzip -d file.gz         # Same as gunzip

# bzip2 (better compression, slower)
bzip2 file
bunzip2 file.bz2

# tar — tape archive
tar -czf archive.tar.gz dir/    # Create compressed archive
tar -xzf archive.tar.gz        # Extract
tar -xzf archive.tar.gz -C /target  # Extract to specific dir
tar -tzf archive.tar.gz        # List contents

# zip
zip -r archive.zip dir/
unzip archive.zip

# rsync — efficient file sync
rsync -av source/ dest/
rsync -avz -e ssh user@host:/src/ /local/dest/   # Over SSH
rsync -av --delete src/ dest/  # Mirror (delete extra files)
```

---

### Ch 19 · Regular Expressions

```bash
grep 'pattern' file         # Search for pattern
grep -i 'pattern' file      # Case-insensitive
grep -r 'pattern' dir/      # Recursive search
grep -v 'pattern' file      # Invert (lines NOT matching)
grep -n 'pattern' file      # Show line numbers
grep -l 'pattern' dir/*     # Show only filenames
grep -c 'pattern' file      # Count matching lines
grep -E 'pattern' file      # Extended regex
```

**Regex quick reference:**

| Pattern | Meaning |
|---------|---------|
| `.` | Any single character |
| `^` | Start of line |
| `$` | End of line |
| `*` | Zero or more of preceding |
| `+` | One or more of preceding (ERE) |
| `?` | Zero or one of preceding (ERE) |
| `{n,m}` | Between n and m occurrences |
| `[abc]` | Character class |
| `[^abc]` | Negated character class |
| `\b` | Word boundary |
| `(a\|b)` | Alternation — a or b |

---

### Ch 20 · Text Processing

```bash
cat -A file         # Show non-printing characters
sort file           # Sort lines alphabetically
sort -n file        # Sort numerically
sort -r file        # Reverse sort
sort -k 2 file      # Sort by field 2
sort -u file        # Sort and remove duplicates

uniq file           # Remove adjacent duplicate lines
uniq -c file        # Count occurrences
uniq -d file        # Show only duplicates

cut -d: -f1 /etc/passwd     # Cut field 1, delimiter ':'
cut -c1-10 file             # Cut first 10 characters

paste file1 file2           # Merge files side by side
join file1 file2            # SQL-style join on first field

diff file1 file2            # Compare files
wc -l file                  # Count lines
wc -w file                  # Count words

# sed — stream editor
sed 's/old/new/' file       # Replace first occurrence per line
sed 's/old/new/g' file      # Replace all occurrences
sed -i 's/old/new/g' file   # Edit in-place
sed -n '1,5p' file          # Print lines 1-5
sed '/pattern/d' file       # Delete lines matching pattern

# awk — text processing language
awk '{print $1}' file           # Print first field
awk -F: '{print $1}' /etc/passwd  # Custom delimiter
awk 'NR==5' file                # Print line 5
awk '$3 > 100' file             # Print lines where field 3 > 100
```

---

### Ch 23 · Compiling Programs

```bash
./configure         # Check dependencies, generate Makefile
make                # Compile the program
sudo make install   # Install compiled program
make clean          # Clean up build files
```

---

## Part IV — Shell Scripting

### Ch 24 · Writing Your First Script

```bash
#!/bin/bash
# This is a comment

echo "Hello, World!"
```

```bash
chmod +x script.sh      # Make executable
./script.sh             # Run script
bash script.sh          # Run without execute permission
```

**Script locations:**
- Place scripts in `~/bin/` or `~/.local/bin/` for personal use
- These are added to `$PATH` automatically on many distros

---

### Ch 25 · Variables and Constants

```bash
#!/bin/bash

# Variables (no spaces around =)
NAME="Manuel"
echo "Hello, $NAME"
echo "Hello, ${NAME}!"      # Braces for clarity

# Constants (convention: UPPERCASE)
TITLE="Linux Reference"
readonly PI=3.14159

# Command substitution
DATE=$(date +%Y-%m-%d)
FILES=$(ls | wc -l)

# Here document
cat << EOF
Line 1
Line 2
EOF
```

---

### Ch 26 · Functions

```bash
#!/bin/bash

# Define function
greet() {
    local name="$1"     # Local variable
    echo "Hello, $name!"
}

# Call function
greet "Manuel"

# Function with return value (via exit status)
is_root() {
    [[ "$(id -u)" -eq 0 ]]
}

if is_root; then
    echo "Running as root"
fi
```

---

### Ch 27 · Flow Control — if / test

```bash
#!/bin/bash

# Basic if
if [ "$x" -eq 5 ]; then
    echo "x is 5"
elif [ "$x" -gt 5 ]; then
    echo "x is greater than 5"
else
    echo "x is less than 5"
fi

# Modern syntax with [[ ]]
if [[ "$string" == "hello" ]]; then
    echo "matched"
fi

if [[ -f "$file" ]]; then       # File exists and is regular file
    echo "file exists"
fi
```

**Test expressions:**

| Expression | True if |
|------------|---------|
| `-e file` | File exists |
| `-f file` | File exists and is regular |
| `-d file` | File exists and is directory |
| `-r file` | File is readable |
| `-w file` | File is writable |
| `-x file` | File is executable |
| `-z string` | String is empty |
| `-n string` | String is not empty |
| `str1 == str2` | Strings are equal |
| `str1 != str2` | Strings are not equal |
| `n1 -eq n2` | Numbers are equal |
| `n1 -ne n2` | Numbers are not equal |
| `n1 -lt n2` | n1 less than n2 |
| `n1 -gt n2` | n1 greater than n2 |
| `n1 -le n2` | n1 ≤ n2 |
| `n1 -ge n2` | n1 ≥ n2 |

```bash
# Arithmetic with (( ))
if (( x > 5 )); then
    echo "greater"
fi

# Logical operators
if [[ -f "$file" && -r "$file" ]]; then   # AND
if [[ -z "$a" || -z "$b" ]]; then         # OR

# Short-circuit operators
mkdir dir && cd dir          # Run second only if first succeeds
cd dir || echo "Failed"      # Run second only if first fails
```

---

### Ch 28 · Reading Input

```bash
#!/bin/bash

# Basic read
read -p "Enter your name: " name
echo "Hello, $name"

# Read with timeout
read -t 5 -p "Answer within 5s: " answer

# Silent input (passwords)
read -s -p "Password: " pass

# Read multiple variables
read -p "First Last: " first last
echo "First=$first, Last=$last"
```

---

### Ch 29 · Loops — while / until

```bash
#!/bin/bash

# while loop
count=1
while [[ "$count" -le 5 ]]; do
    echo "Count: $count"
    count=$((count + 1))
done

# until loop (opposite of while)
until [[ "$count" -gt 5 ]]; do
    echo "Count: $count"
    count=$((count + 1))
done

# Read file line by line
while read line; do
    echo "$line"
done < file.txt

# break and continue
while true; do
    read -p "Input: " val
    [[ -z "$val" ]] && break
    [[ "$val" == "skip" ]] && continue
    echo "Got: $val"
done
```

---

### Ch 31 · Branching — case

```bash
#!/bin/bash

read -p "Enter choice: " choice

case "$choice" in
    1|one)
        echo "You chose one"
        ;;
    2|two)
        echo "You chose two"
        ;;
    q|quit)
        echo "Quitting"
        exit 0
        ;;
    *)
        echo "Unknown choice"
        ;;
esac
```

---

### Ch 32 · Positional Parameters

```bash
#!/bin/bash
# Usage: ./script.sh arg1 arg2 arg3

echo "Script name:  $0"
echo "First arg:    $1"
echo "Second arg:   $2"
echo "All args:     $@"
echo "Arg count:    $#"
echo "Exit status:  $?"     # Of last command
echo "Script PID:   $$"

# Shift positional parameters
while [[ $# -gt 0 ]]; do
    echo "Arg: $1"
    shift
done
```

---

### Ch 33 · Loops — for

```bash
#!/bin/bash

# Traditional for
for i in 1 2 3 4 5; do
    echo "Item: $i"
done

# Range expansion
for i in {1..10}; do
    echo "$i"
done

# Iterate over files
for file in *.txt; do
    echo "Processing: $file"
done

# Iterate over array
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# C-style for loop
for (( i=0; i<5; i++ )); do
    echo "$i"
done
```

---

### Ch 34 · Strings and Numbers

```bash
# Arithmetic expansion
echo $((5 + 3))
echo $((10 % 3))        # Modulo
echo $((2 ** 8))        # Exponentiation

# Parameter expansion
var="Hello, World"
echo ${#var}            # Length: 12
echo ${var:0:5}         # Substring: Hello
echo ${var/World/Linux} # Replace: Hello, Linux
echo ${var,,}           # Lowercase
echo ${var^^}           # Uppercase
echo ${var:-"default"}  # Use default if unset
echo ${var:="default"}  # Assign default if unset
echo ${var:+"set"}      # Use "set" if var is set

# Removing prefixes/suffixes
file="archive.tar.gz"
echo ${file%.gz}        # Remove shortest suffix match: archive.tar
echo ${file%%.*}        # Remove longest suffix match: archive
echo ${file#*.}         # Remove shortest prefix match: tar.gz
echo ${file##*.}        # Remove longest prefix match: gz
```

---

### Ch 35 · Arrays

```bash
#!/bin/bash

# Create indexed array
fruits=("apple" "banana" "cherry")
a[0]="first"
a[1]="second"

# Access elements
echo "${fruits[0]}"         # apple
echo "${fruits[@]}"         # All elements
echo "${#fruits[@]}"        # Count: 3
echo "${!fruits[@]}"        # Indices: 0 1 2

# Append element
fruits+=("date")

# Slice
echo "${fruits[@]:1:2}"     # Elements starting at index 1, length 2

# Remove element
unset fruits[1]

# Loop over array
for item in "${fruits[@]}"; do
    echo "$item"
done

# Associative array (bash 4+)
declare -A colors
colors["red"]="#ff0000"
colors["green"]="#00ff00"
echo "${colors[red]}"
echo "${!colors[@]}"        # All keys
```

---

### Ch 30 · Troubleshooting Scripts

```bash
# Debug modes
bash -n script.sh       # Check syntax without running
bash -x script.sh       # Trace execution (show each command)
bash -v script.sh       # Verbose — print lines as read

# Enable in script
set -x                  # Enable tracing
set +x                  # Disable tracing
set -e                  # Exit on any error
set -u                  # Treat unset variables as error
set -o pipefail         # Pipe fails if any command fails

# Common defensive patterns
cd "$dir" || exit 1
[[ -f "$file" ]] || { echo "File not found"; exit 1; }

# Check exit status
if ! mkdir "$dir"; then
    echo "Failed to create $dir"
    exit 1
fi
```

---

### Ch 36 · Advanced Topics

```bash
# Group commands (run in current shell)
{ command1; command2; command3; } > output.txt

# Subshell (run in child shell, no effect on parent)
( cd /tmp; ls )

# Process substitution
diff <(ls dir1) <(ls dir2)          # Diff output of two commands

# Traps — handle signals
trap "echo 'Interrupted'; exit" INT TERM
trap "rm -f /tmp/tmpfile" EXIT      # Cleanup on exit

# eval — construct and run commands dynamically
cmd="ls -la"
eval "$cmd"

# Named pipes (FIFO)
mkfifo mypipe
ls > mypipe &
cat mypipe

# Asynchronous execution
long_task &
PID=$!
# ... do other work ...
wait $PID       # Wait for background task to finish
echo "Task done, exit: $?"
```

---

## Quick Reference — Most Used Commands

```bash
# Navigation
pwd · ls · cd · ls -la

# Files
cp · mv · rm · mkdir · ln · touch · find · locate

# Viewing
cat · less · more · head · tail · file

# Search
grep · find · locate · which · whereis

# Text processing
sort · uniq · wc · cut · sed · awk · diff · tr

# Archives
tar · gzip · bzip2 · zip · rsync

# Permissions
chmod · chown · chgrp · sudo · su

# Processes
ps · top · kill · jobs · fg · bg

# Network
ping · ssh · scp · wget · curl · netstat · ip

# System info
df · du · free · uname · hostname · uptime · env
```

---

*Generated from: The Linux Command Line, 3rd Edition (William Shotts)*
*Note template for Obsidian — last updated: 2026-03-08*
