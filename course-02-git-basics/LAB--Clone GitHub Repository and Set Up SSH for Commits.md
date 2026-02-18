## **Part 1: Understanding SSH vs HTTPS**

### **Why Use SSH?**
- **Security**: Encrypted connection, no password needed after setup
- **Convenience**: No password prompts after initial setup
- **Access Control**: SSH keys tied to your machine
- **Required for**: Some corporate networks, automated scripts, CI/CD pipelines

### **SSH vs HTTPS Comparison**
```
SSH: git@github.com:username/repo.git
HTTPS: https://github.com/username/repo.git
```

## **Part 2: Generate SSH Keys (One-Time Setup)**

### **Step 1: Check Existing SSH Keys**
```bash
# Check for existing keys
ls -al ~/.ssh
# Look for: id_rsa, id_rsa.pub, id_ed25519, id_ed25519.pub
```

### **Step 2: Generate New SSH Key Pair**
```bash
# Modern approach (recommended)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Or if your system doesn't support Ed25519
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

**Interactive prompts:**
```
Enter file in which to save the key (/home/username/.ssh/id_ed25519): [Press Enter]
Enter passphrase (empty for no passphrase): [Create a secure passphrase]
Enter same passphrase again: [Repeat]
```

### **Step 3: Start SSH Agent and Add Key**
```bash
# Start the SSH agent in background
eval "$(ssh-agent -s)"

# Add your SSH private key to the agent
ssh-add ~/.ssh/id_ed25519
```

**For macOS Keychain integration:**
```bash
# Create ~/.ssh/config file
cat > ~/.ssh/config << EOF
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
EOF

# Add with keychain
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

### **Step 4: Add SSH Key to GitHub**
```bash
# Copy public key to clipboard
# Linux
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard

# macOS
cat ~/.ssh/id_ed25519.pub | pbcopy

# Windows (Git Bash)
cat ~/.ssh/id_ed25519.pub | clip
```

**On GitHub:**
1. Go to **Settings** → **SSH and GPG keys**
2. Click **"New SSH key"**
3. **Title**: e.g., "Personal Laptop - Ed25519"
4. **Key type**: Authentication Key
5. **Key**: Paste your public key
6. Click **"Add SSH key"**

### **Step 5: Test SSH Connection**
```bash
ssh -T git@github.com
```
**Expected response:**
```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

## **Part 3: Clone Repository Using SSH**

### **Step 1: Get SSH URL**
On GitHub repository page:
1. Click **"Code"** button
2. Select **"SSH"** tab
3. Copy URL: `git@github.com:username/repository.git`

### **Step 2: Clone Repository**
```bash
# Navigate to where you want to store the repo
cd ~/Documents  # or your preferred location

# Clone using SSH URL
git clone git@github.com:username/obsidian-notes.git

# If you want specific folder name
git clone git@github.com:username/obsidian-notes.git my-obsidian-vault
```

### **Step 3: Verify Remote URL**
```bash
cd obsidian-notes
git remote -v
```
**Should show:**
```
origin  git@github.com:username/obsidian-notes.git (fetch)
origin  git@github.com:username/obsidian-notes.git (push)
```

### **Step 4: Configure Git Identity**
```bash
# Set your name and email (crucial for commits)
git config user.name "Your Name"
git config user.email "your_email@example.com"

# Set globally (for all repos)
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

# Check configuration
git config --list
```

## **Part 4: Configure Git for SSH Operations**

### **Git Configuration File (~/.gitconfig)**
```bash
# Edit global config
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "nano"         # Nano
git config --global core.editor "vim"          # Vim

# Set default branch name
git config --global init.defaultBranch main

# Set pull behavior
git config --global pull.rebase false

# Color output
git config --global color.ui auto

# Set credential helper (not needed for SSH but good for HTTPS)
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'
```

### **Custom SSH Configuration**
Create/edit `~/.ssh/config`:
```bash
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    AddKeysToAgent yes
    UseKeychain yes  # macOS only
    
# For multiple GitHub accounts
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal

Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
```

**Then clone with custom host:**
```bash
git clone git@github-personal:username/repo.git
```

## **Part 5: Making Commits with SSH**

### **Basic Git Workflow**
```bash
# Navigate to your repository
cd ~/Documents/obsidian-notes

# Check repository status
git status

# Add changes
git add .                         # Add all changes
git add filename.md               # Add specific file
git add folder/                   # Add folder

# Commit changes
git commit -m "Your commit message"
git commit -m "Add daily notes for Feb 2024"
git commit -m "Update project structure" -m "Detailed description here"

# Push to GitHub
git push origin main
git push                          # If tracking is set

# Pull updates from GitHub
git pull origin main
git pull                          # If tracking is set
```

### **Advanced Commit Workflow**
```bash
# View changes before adding
git diff
git diff --staged

# Add with patch (interactive)
git add -p

# Commit with detailed message
git commit
# Opens editor with:
# First line: Subject (50 chars max)
# Blank line
# Body (72 chars per line)
# Blank line
# Footer (references, breaking changes)

# Amend last commit
git commit --amend -m "New message"
git commit --amend --no-edit     # Keep same message

# Push to different branch
git push origin feature-branch
```

### **Branch Operations with SSH**
```bash
# Create and switch to new branch
git checkout -b feature/daily-notes

# List branches
git branch          # Local
git branch -r       # Remote
git branch -a       # All

# Switch branches
git checkout main
git switch main     # Newer command

# Merge branches
git checkout main
git merge feature/daily-notes

# Delete branch
git branch -d feature/daily-notes
git push origin --delete feature/daily-notes
```

## **Part 6: Troubleshooting SSH Issues**

### **Common SSH Problems & Solutions**

1. **Permission denied (publickey)**
```bash
# Verify key is loaded
ssh-add -l

# Test connection
ssh -vT git@github.com

# Check key permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 644 ~/.ssh/known_hosts
```

2. **SSH agent not running**
```bash
# Start agent
eval "$(ssh-agent -s)"

# Add key
ssh-add ~/.ssh/id_ed25519

# For persistent setup (add to ~/.bashrc or ~/.zshrc)
cat >> ~/.bashrc << 'EOF'
# Start SSH agent
if [ -z "$SSH_AUTH_SOCK" ]; then
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519 2>/dev/null
fi
EOF
```

3. **Wrong remote URL**
```bash
# Check current remote
git remote -v

# Change from HTTPS to SSH
git remote set-url origin git@github.com:username/repo.git

# Or add new remote
git remote add origin-ssh git@github.com:username/repo.git
```

4. **Multiple SSH keys**
```bash
# Create SSH config for different keys
cat > ~/.ssh/config << EOF
Host github.com-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    
Host github.com-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
EOF

# Clone with specific host
git clone git@github.com-personal:username/repo.git
```

## **Part 7: Automation & Aliases**

### **Git Aliases for Efficiency**
```bash
# Add to ~/.gitconfig or run these commands
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
git config --global alias.pushall 'push --all origin'
```

### **Shell Aliases**
Add to `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`:
```bash
# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git pull'
alias gco='git checkout'
alias gb='git branch'
alias gd='git diff'
alias glog='git log --oneline --graph --all'

# SSH shortcuts
alias ssh-list='ssh-add -l'
alias ssh-addkey='ssh-add ~/.ssh/id_ed25519'
alias ssh-test='ssh -T git@github.com'
```

### **Automated Sync Script for Obsidian**
Create `sync-notes.sh` in your vault:
```bash
#!/bin/bash
# Obsidian Git Sync Script

VAULT_PATH="$HOME/Documents/obsidian-notes"
LOG_FILE="$VAULT_PATH/.obsidian/sync.log"

cd "$VAULT_PATH" || exit 1

echo "=== Sync started at $(date) ===" >> "$LOG_FILE"

# Pull changes first
if git pull --rebase origin main 2>&1 | tee -a "$LOG_FILE"; then
    echo "✓ Pull successful" >> "$LOG_FILE"
else
    echo "✗ Pull failed" >> "$LOG_FILE"
    exit 1
fi

# Add all changes
git add . 2>&1 | tee -a "$LOG_FILE"

# Commit with timestamp
if git commit -m "Auto-sync: $(date '+%Y-%m-%d %H:%M:%S')" 2>&1 | tee -a "$LOG_FILE"; then
    echo "✓ Commit created" >> "$LOG_FILE"
else
    echo "ℹ No changes to commit" >> "$LOG_FILE"
fi

# Push changes
if git push origin main 2>&1 | tee -a "$LOG_FILE"; then
    echo "✓ Push successful" >> "$LOG_FILE"
else
    echo "✗ Push failed" >> "$LOG_FILE"
    exit 1
fi

echo "=== Sync completed at $(date) ===" >> "$LOG_FILE"
```

Make executable:
```bash
chmod +x sync-notes.sh
./sync-notes.sh
```

## **Part 8: Security Best Practices**

### **SSH Key Security**
1. **Use strong passphrases**
2. **Never share private keys**
3. **Use different keys for different services**
4. **Regularly rotate keys** (annually)
5. **Use hardware security keys** (Yubikey) for extra security

### **Git Security**
```bash
# Avoid committing sensitive data
# Add to .gitignore:
.secrets/
.env
*.key
*.pem
config.json

# If committed accidentally:
git filter-repo --invert-paths --path-sensitive-file.txt
git push origin --force --all
```

## **Part 9: Verification Checklist**

### **After Setup Verification**
```bash
# 1. SSH connection test
ssh -T git@github.com

# 2. Verify git configuration
git config --get user.name
git config --get user.email

# 3. Verify remote URL
git remote -v

# 4. Test clone/push
echo "# Test" >> README.md
git add README.md
git commit -m "Test commit"
git push

# 5. Verify on GitHub
# Check your repository on github.com
```

### **Quick Reference Commands**
```bash
# Clone with SSH
git clone git@github.com:username/repo.git

# Check SSH connection
ssh -T git@github.com

# List SSH keys
ssh-add -l

# Change remote to SSH
git remote set-url origin git@github.com:username/repo.git

# First time setup in existing folder
git init
git remote add origin git@github.com:username/repo.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

This setup provides a secure, authenticated connection to GitHub without password prompts, making your Obsidian note synchronization seamless and secure across all devices.