
## **1. Foundation & Philosophy**

### What is Bash?
Bash (Bourne Again SHell) is the default shell on most Linux distributions and macOS (pre-Catalina). It's a command processor that runs in a text window where users type commands to perform tasks.

### Shell Philosophy
- **Everything is a file** (devices, directories, sockets)
- **Small, sharp tools** that do one thing well
- **Composition over monoliths** (chain commands together)
- **Text as universal interface**

## **2. Essential Concepts & Environment**

### Startup Files
```bash
# Execution order for login shells:
/etc/profile → ~/.bash_profile → ~/.bash_login → ~/.profile

# For interactive non-login shells:
~/.bashrc

# For all shells:
/etc/bash.bashrc
```

### Environment Variables
```bash
# Key variables
echo $HOME      # Home directory
echo $PATH      # Command search path
echo $USER      # Current user
echo $SHELL     # Current shell
echo $PS1       # Primary prompt string

# Set variables
export EDITOR=vim           # Available to child processes
MY_VAR="value"              # Local to current shell
readonly CONSTANT="fixed"   # Immutable variable

# Add to PATH
export PATH="$PATH:/usr/local/bin"
```

## **3. Essential Commands & Navigation**

### Filesystem Navigation
```bash
pwd                     # Print working directory
cd /path/to/dir         # Change directory
cd ~                    # Go to home directory
cd -                    # Go to previous directory
ls -la                  # List all files with details
tree -L 2               # Visual directory structure (2 levels)
```

### File Operations
```bash
# Create/remove
touch file.txt          # Create empty file or update timestamp
mkdir -p dir1/dir2      # Create nested directories
rm -rf directory/       # Remove recursively (CAUTION!)

# Copy/move
cp -r source/ dest/     # Copy recursively
mv oldname newname      # Rename or move
rsync -av source/ dest/ # Advanced sync with progress

# View files
cat file.txt            # Concatenate files
less file.txt           # Page through file (search with /)
head -n 20 file.log     # First 20 lines
tail -f logfile         # Follow file as it grows
```

## **4. Powerful Text Processing**

### The UNIX Text Processing Trinity
```bash
# grep - pattern searching
grep "error" logfile           # Basic search
grep -r "TODO" src/            # Recursive search
grep -i "warning" file         # Case-insensitive
grep -v "debug" file           # Invert match (lines NOT containing)
grep -E "^[A-Z]" file          # Extended regex
egrep "error|warning" file     # Multiple patterns

# sed - stream editor
sed 's/old/new/g' file         # Replace all occurrences
sed '/pattern/d' file          # Delete lines matching pattern
sed -n '5,10p' file            # Print lines 5-10
sed -i.bak 's/foo/bar/' file   # In-place edit with backup

# awk - pattern scanning and processing
awk '{print $1}' file          # Print first column
awk -F: '{print $1}' /etc/passwd # Use colon as delimiter
awk '$3 > 1000' file           # Filter rows where column 3 > 1000
awk '{sum+=$1} END{print sum}' file # Sum first column
awk '!seen[$0]++' file         # Remove duplicate lines
```

### Advanced Text Manipulation
```bash
# Sort and unique
sort file.txt                  # Alphabetical sort
sort -n file.txt               # Numerical sort
sort -u file.txt               # Unique sort
uniq -c file.txt               # Count occurrences

# Cut and paste
cut -d: -f1,3 /etc/passwd      # Extract specific fields
paste file1 file2              # Merge files line by line
join file1 file2               # Join on common field

# Character translation
tr 'a-z' 'A-Z' < file          # Convert to uppercase
tr -d '\r' < file              # Remove carriage returns
tr -s ' ' < file               # Squeeze multiple spaces
```

## **5. Shell Scripting Fundamentals**

### Shebang and Basic Script
```bash
#!/bin/bash
# script.sh - A sample script
# Comments start with #

echo "Hello, $(whoami)!"       # Command substitution
```

### Variables and Expansion
```bash
name="John"
echo "Hello $name"             # Variable expansion
echo "Hello ${name}son"        # Braces for clarity

# Special parameters
echo "Script: $0"              # Script name
echo "Args count: $#"          # Number of arguments
echo "All args: $@"            # All arguments as separate words
echo "All args: $*"            # All arguments as single string
echo "Exit code: $?"           # Last command's exit status
echo "PID: $$"                 # Current process ID

# Default values
${var:-default}                # Use default if var is unset or empty
${var:=default}                # Set to default if unset/empty
${var:?error message}          # Show error if unset/empty
${var:+alternate}              # Use alternate if var is set
```

### Conditionals
```bash
# File tests
if [[ -f "file.txt" ]]; then
    echo "File exists"
elif [[ -d "directory" ]]; then
    echo "Directory exists"
else
    echo "Neither"
fi

# String comparisons
if [[ "$str1" == "$str2" ]]; then
    echo "Equal"
fi

if [[ -z "$string" ]]; then
    echo "String is empty"
fi

# Numeric comparisons
if (( a > b )); then
    echo "a is greater"
fi

# Pattern matching
if [[ "$filename" == *.txt ]]; then
    echo "Text file"
fi

# Case statement
case "$1" in
    start)
        echo "Starting..."
        ;;
    stop|halt)
        echo "Stopping..."
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        ;;
esac
```

### Loops
```bash
# For loops
for i in {1..5}; do
    echo "Iteration $i"
done

for file in *.txt; do
    echo "Processing $file"
done

# C-style for loop
for ((i=0; i<10; i++)); do
    echo "$i"
done

# While loop
count=1
while [[ $count -le 5 ]]; do
    echo "Count: $count"
    ((count++))
done

# Reading lines from file
while IFS= read -r line; do
    echo "$line"
done < file.txt

# Until loop
until ping -c1 github.com &>/dev/null; do
    echo "Waiting for connection..."
    sleep 5
done
```

## **6. Functions & Modularization**

### Function Basics
```bash
# Define function
greet() {
    local name="$1"           # Local variable
    echo "Hello, $name!"
    return 0                  # Exit status
}

# Call function
greet "Alice"

# Function with return value
add() {
    local sum=$(( $1 + $2 ))
    echo $sum                 # Output result
}

result=$(add 5 3)            # Capture output
```

### Advanced Functions
```bash
# Function that modifies global variable
counter=0
increment() {
    ((counter++))
}

# Function with default arguments
create_file() {
    local filename=${1:-"default.txt"}
    local content=${2:-"Default content"}
    echo "$content" > "$filename"
}

# Trap errors in functions
error_handler() {
    echo "Error on line $1"
    exit 1
}
trap 'error_handler $LINENO' ERR
```

## **7. Input/Output Redirection & Pipes**

### Redirection Operators
```bash
cmd > file                 # Stdout to file (overwrite)
cmd >> file                # Stdout to file (append)
cmd < file                 # Stdin from file
cmd 2> error.log           # Stderr to file
cmd &> file                # Both stdout and stderr to file
cmd 2>&1                   # Stderr to stdout
cmd > file 2>&1            # Both to file (order matters!)
cmd > /dev/null            # Discard output

# Here documents
cat << EOF
This is a
multiline string
EOF

# Here strings
grep "pattern" <<< "$variable"
```

### Powerful Piping Patterns
```bash
# Basic pipeline
cat file.txt | grep "error" | sort | uniq -c

# Tee - split output
ls -la | tee listing.txt | wc -l

# Process substitution
diff <(sort file1) <(sort file2)

# Named pipes (FIFOs)
mkfifo mypipe
ls -la > mypipe &
cat < mypipe
```

## **8. Job Control & Process Management**

### Job Control Basics
```bash
sleep 100 &
jobs                        # List background jobs
fg %1                      # Bring job 1 to foreground
bg %1                      # Send to background
kill %1                    # Terminate job
disown -h %1               # Detach job from shell

# No hangup
nohup long_running_cmd &
```

### Process Management
```bash
ps aux                      # Show all processes
pstree                      # Show process tree
top                         # Interactive process viewer
htop                        # Enhanced top

# Kill signals
kill -9 PID                 # SIGKILL (forceful)
kill -15 PID                # SIGTERM (graceful)
kill -l                     # List all signals

# Wait for processes
wait                        # Wait for all background jobs
wait %1                     # Wait for specific job
```

## **9. Advanced Features & Techniques**

### Arrays
```bash
# Indexed arrays
fruits=("apple" "banana" "cherry")
echo ${fruits[0]}           # apple
echo ${fruits[@]}           # All elements
echo ${#fruits[@]}          # Length

# Append
fruits+=("date")

# Associative arrays (Bash 4+)
declare -A colors
colors["red"]="#FF0000"
colors["green"]="#00FF00"
echo ${colors["red"]}
```

### Brace Expansion & Globbing
```bash
# Brace expansion
echo file.{txt,log,conf}    # file.txt file.log file.conf
mkdir -p dir{1..3}/sub{1..2}
echo {a..z}{1..3}

# Extended globbing
shopt -s extglob
ls !(*.txt)                 # Everything except .txt files
ls +(file|dir)              # One or more occurrences
ls @(file|dir)              # Exactly one of
ls ?(file)                  # Zero or one occurrence
ls *(file)                  # Zero or more occurrences
```

### Parameter Expansion Tricks
```bash
# String manipulation
str="hello world"
echo ${str:0:5}             # hello (substring)
echo ${str/ /_}             # hello_world (replace)
echo ${str// /_}            # Replace all occurrences
echo ${str/#hello/goodbye}  # Replace at beginning
echo ${str/%world/universe} # Replace at end

# Array tricks
echo ${!colors[@]}          # All keys
echo ${!fruits[@]}          # All indices
```

## **10. Debugging & Optimization**

### Debugging Techniques
```bash
#!/bin/bash
# Debug options
set -x                      # Print commands before execution
set -e                      # Exit on error
set -u                      # Exit on undefined variable
set -o pipefail             # Exit if any command in pipe fails

# Combined
set -euxo pipefail

# Manual debugging
echo "DEBUG: value is $variable" >&2
read -p "Press enter to continue"

# Trap debugging
trap 'echo "Line $LINENO: $BASH_COMMAND"' DEBUG
```

### Performance Optimization
```bash
# Use builtins over external commands
# Slow
cat file.txt | grep "pattern"

# Fast
grep "pattern" file.txt

# Even faster (builtin)
while IFS= read -r line; do
    [[ "$line" =~ pattern ]] && echo "$line"
done < file.txt

# Avoid unnecessary subshells
# Slow
result=$(echo "$var" | tr 'a-z' 'A-Z')

# Fast
result="${var^^}"           # Bash 4+
```

## **11. Security Best Practices**

### Secure Scripting
```bash
# Always quote variables
echo "$filename"            # Good
echo $filename              # Bad (word splitting, globbing)

# Use printf for formatted output
printf "Name: %s\n" "$name"

# Validate input
if [[ ! "$input" =~ ^[a-zA-Z0-9_]+$ ]]; then
    echo "Invalid input" >&2
    exit 1
fi

# Limit privileges
if [[ $EUID -ne 0 ]]; then
    echo "Must be run as root" >&2
    exit 1
fi

# Clean environment
env -i PATH="$PATH" script.sh
```

## **12. Real-World Examples**

### System Monitoring Script
```bash
#!/bin/bash
# monitor.sh - System monitoring script

set -euo pipefail

check_disk() {
    local threshold=${1:-80}
    df -h | awk -v th="$threshold" '
    NR>1 && $5+0 > th {print "WARNING: "$1" at "$5}
    '
}

check_memory() {
    free -h | awk '/Mem:/ {
        printf "Memory: Used %s/%s (%.1f%%)\n", $3, $2, $3/$2*100
    }'
}

check_load() {
    uptime | awk -F'load average:' '{print $2}'
}

main() {
    echo "=== System Monitor ==="
    echo "Time: $(date)"
    echo "Host: $(hostname)"
    echo
    check_disk 90
    echo
    check_memory
    echo "Load averages: $(check_load)"
}

main "$@"
```

### Backup Script with Error Handling
```bash
#!/bin/bash
# backup.sh - Secure backup script

BACKUP_DIR="/backups"
SOURCE_DIRS=("/home" "/etc" "/var/www")
RETENTION_DAYS=7
LOG_FILE="/var/log/backup.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

create_backup() {
    local backup_name="backup_$(date '+%Y%m%d_%H%M%S').tar.gz"
    local temp_dir=$(mktemp -d)
    
    log "Starting backup: $backup_name"
    
    # Copy files to temp directory
    for dir in "${SOURCE_DIRS[@]}"; do
        if [[ -d "$dir" ]]; then
            cp -r "$dir" "$temp_dir/" || {
                log "ERROR: Failed to copy $dir"
                return 1
            }
        fi
    done
    
    # Create archive
    tar -czf "$BACKUP_DIR/$backup_name" -C "$temp_dir" . || {
        log "ERROR: Failed to create archive"
        return 1
    }
    
    # Cleanup
    rm -rf "$temp_dir"
    
    log "Backup completed: $backup_name ($(du -h "$BACKUP_DIR/$backup_name" | cut -f1))"
}

clean_old_backups() {
    log "Cleaning backups older than $RETENTION_DAYS days"
    find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +$RETENTION_DAYS -delete
}

main() {
    [[ -d "$BACKUP_DIR" ]] || mkdir -p "$BACKUP_DIR"
    
    trap 'log "Backup interrupted"; exit 1' INT TERM
    
    create_backup
    clean_old_backups
    
    log "Backup process completed successfully"
}

main "$@"
```

## **13. Learning Resources & Tools**

### Essential Tools to Master
- **tmux/screen** - Terminal multiplexers
- **vim/emacs** - Text editors
- **curl/wget** - HTTP clients
- **jq** - JSON processor
- **ssh/scp** - Remote access
- **cron** - Job scheduler
- **find/locate** - File searching
- **tar/gzip** - Archiving

### Practice Resources
```bash
# Test skills with these challenges:
# 1. Find top 10 largest files
find / -type f -exec du -h {} + 2>/dev/null | sort -hr | head -10

# 2. Monitor failed login attempts
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c

# 3. Create a directory with dated structure
mkdir -p backup/$(date '+%Y/%m/%d')

# 4. Kill zombie processes
ps aux | awk '$8=="Z" {print $2}' | xargs kill -9
```

## **14. Pro Tips**

### Efficiency Boosters
```bash
# Use Ctrl shortcuts
# Ctrl+R - Reverse search history
# Ctrl+A - Beginning of line
# Ctrl+E - End of line
# Ctrl+U - Cut to beginning
# Ctrl+K - Cut to end
# Ctrl+Y - Paste cut text
# Ctrl+W - Cut previous word
# Alt+. - Insert last argument

# Customize .bashrc
export HISTSIZE=10000
export HISTFILESIZE=20000
export HISTCONTROL=ignoreboth:erasedups
shopt -s histappend
PROMPT_COMMAND='history -a'

# Aliases for productivity
alias ll='ls -la'
alias grep='grep --color=auto'
alias df='df -h'
alias du='du -h'
alias mkdir='mkdir -p'
alias rm='rm -i'
alias h='history'
alias ..='cd ..'
alias ...='cd ../..'
```

### Mastery Path
1. **Beginner**: Learn basic commands, navigation, and simple scripting
2. **Intermediate**: Master pipes, redirection, grep/sed/awk, functions
3. **Advanced**: Understand process control, signal handling, performance
4. **Expert**: Write production scripts, handle edge cases, security considerations

**Remember**: Mastery comes from consistent practice. Start with small tasks, build reusable scripts, and gradually tackle more complex problems. The shell is not just a tool but a programming environment that, when mastered, becomes an extension of your thought process for system interaction.