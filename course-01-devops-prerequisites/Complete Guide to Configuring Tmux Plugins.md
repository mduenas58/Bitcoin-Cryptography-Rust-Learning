
## **1. Overview of Tmux Plugin Ecosystem**

Tmux plugins extend tmux functionality in several key areas:
- **Status line enhancements** (powerline, themes)
- **Session management** (session saving/restoring)
- **Copy/paste integration** (system clipboard)
- **Navigation improvements** (vim-like movement)
- **Utility tools** (CPU, battery, weather, etc.)

## **2. Plugin Manager Options**

### **A. TPM (Tmux Plugin Manager) - Most Popular**
**GitHub**: https://github.com/tmux-plugins/tpm

**Advantages**:
- Simple installation and usage
- Large plugin ecosystem
- Automatic updates
- No external dependencies

**Installation**:
```bash
# 1. Install TPM
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# 2. Add to ~/.tmux.conf
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Other plugins go here...

# Initialize TPM (keep this line at the very bottom of .tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
```

### **B. Manual Installation (without plugin manager)**
```bash
# Example: Install tmux-resurrect manually
mkdir -p ~/.tmux/plugins
git clone https://github.com/tmux-plugins/tmux-resurrect ~/.tmux/plugins/tmux-resurrect

# Add to .tmux.conf:
run-shell ~/.tmux/plugins/tmux-resurrect/resurrect.tmux
```

### **C. Using zpm-tmux (Zsh Plugin Manager style)**
```bash
# Install zpm-tmux
git clone https://github.com/zpm-zsh/zpm-tmux ~/.tmux/plugins/zpm-tmux

# In .tmux.conf:
set -g @tpm_plugins '          \
  tmux-plugins/tpm             \
  tmux-plugins/tmux-sensible   \
  tmux-plugins/tmux-resurrect  \
'
run-shell ~/.tmux/plugins/zpm-tmux/zpm.tmux
```

## **3. Essential Plugin Setup with TPM**

### **Step-by-Step Complete Setup**

**1. Create/Update `~/.tmux.conf`:**
```tmux
# ========== TPM CONFIGURATION ==========
# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'      # Sensible defaults

# Theme/Status Bar plugins
set -g @plugin 'dracula/tmux'                   # Dracula theme
# OR
set -g @plugin 'catppuccin/tmux'                # Catppuccin theme

# Session Management
set -g @plugin 'tmux-plugins/tmux-resurrect'    # Save/restore sessions
set -g @plugin 'tmux-plugins/tmux-continuum'    # Auto-save/restore

# Navigation/Productivity
set -g @plugin 'christoomey/vim-tmux-navigator' # Seamless vim/tmux nav
set -g @plugin 'tmux-plugins/tmux-yank'         # Copy to system clipboard
set -g @plugin 'tmux-plugins/tmux-pain-control' # Enhanced pane operations

# Utilities
set -g @plugin 'sainnhe/tmux-fzf'               # Fuzzy finder
set -g @plugin 'thewtex/tmux-mem-cpu-load'      # CPU/Memory status
set -g @plugin 'tmux-plugins/tmux-battery'      # Battery status
set -g @plugin 'tmux-plugins/tmux-online-status' # Internet connection

# Initialize TPM (keep at the bottom!)
run '~/.tmux/plugins/tpm/tpm'
```

**2. Install Plugins** (after saving config):
```bash
# Start tmux or reload config
tmux source-file ~/.tmux.conf

# Then press prefix + I (capital i) to install plugins
# Or from terminal:
~/.tmux/plugins/tpm/bin/install_plugins
```

**3. Update Plugins:**
```bash
# Inside tmux: prefix + U
# Or from terminal:
~/.tmux/plugins/tpm/bin/update_plugins all
```

**4. Uninstall Plugins:**
```bash
# 1. Remove from plugin list in .tmux.conf
# 2. Press prefix + alt + u
# 3. Or manually:
~/.tmux/plugins/tpm/bin/clean_plugins
```

## **4. Popular Plugin Configurations**

### **A. Dracula Theme**
```tmux
set -g @plugin 'dracula/tmux'

# Dracula configuration options
set -g @dracula-show-powerline true
set -g @dracula-fixed-location "New York"
set -g @dracula-plugins "weather"
set -g @dracula-show-flags true
set -g @dracula-show-left-icon session
set -g @dracula-border-contrast true
set -g @dracula-day-month true
set -g @dracula-military-time true
set -g @dracula-show-timezone false
set -g @dracula-show-fahrenheit false

# Position customization
set -g @dracula-show-left-sep 
set -g @dracula-show-right-sep 

# Colors (optional)
set -g @dracula-cyan "#8be9fd"
set -g @dracula-green "#50fa7b"
set -g @dracula-orange "#ffb86c"
set -g @dracula-pink "#ff79c6"
set -g @dracula-purple "#bd93f9"
set -g @dracula-red "#ff5555"
set -g @dracula-yellow "#f1fa8c"

# Window status
set -g @dracula-show-empty-plugins false
```

### **B. Catppuccin Theme**
```tmux
set -g @plugin 'catppuccin/tmux'

# Choose flavor: mocha, macchiato, frappe, latte
set -g @catppuccin_flavour 'mocha'

# Status bar customization
set -g @catppuccin_window_left_separator ""
set -g @catppuccin_window_right_separator " "
set -g @catppuccin_window_middle_separator " █"
set -g @catppuccin_window_number_position "right"
set -g @catppuccin_window_default_fill "number"
set -g @catppuccin_window_default_text "#W"
set -g @catppuccin_window_current_fill "number"
set -g @catppuccin_window_current_text "#W"

# Status modules
set -g @catppuccin_status_modules_right "directory session date_time"
set -g @catppuccin_status_modules_left "host"
set -g @catppuccin_status_left_separator  ""
set -g @catppuccin_status_right_separator ""
set -g @catppuccin_status_right_separator_inverse "no"
set -g @catppuccin_status_fill "icon"
set -g @catppuccin_status_connect_separator "no"

# Individual modules
set -g @catppuccin_directory_text "#{pane_current_path}"
set -g @catppuccin_date_time_text "%H:%M"
```

### **C. Tmux Resurrect & Continuum**
```tmux
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

# Resurrect configuration
set -g @resurrect-strategy-nvim 'session'
set -g @resurrect-capture-pane-contents 'on'
set -g @resurrect-processes 'ssh mysqld sqlite3 psql pgcli mysql'
set -g @resurrect-processes ':all:'  # Restore all programs

# Save additional programs
set -g @resurrect-processes '
  "~ssh"
  "~psql"
  "~mysql"
  "~sqlite3"
  "~vtop"
  "~htop"
  "~btm"
'

# Continuum configuration
set -g @continuum-restore 'on'
set -g @continuum-save-interval '15'  # minutes
set -g @continuum-boot 'on'           # restore at system boot
set -g @continuum-boot-options 'full' # or 'quiet'

# Save/restore hooks
set -g @resurrect-hook-pre-save-all 'tmux list-windows -F "#{window_name}" > /tmp/tmux-windows.txt'
set -g @resurrect-hook-post-save-all 'echo "Session saved at $(date)" >> ~/.tmux-resurrect.log'
set -g @resurrect-hook-pre-restore-all 'echo "Restoring session..." >> ~/.tmux-resurrect.log'
set -g @resurrect-hook-post-restore-all 'tmux display-message "Session restored!"'

# Save extra data
set -g @resurrect-save-bash-history 'on'
set -g @resurrect-save-shell-history 'on'

# Key bindings (optional - defaults are prefix + Ctrl-s / Ctrl-r)
set -g @resurrect-save 'S'
set -g @resurrect-restore 'R'
```

**Usage:**
```bash
# Save session manually
prefix + Ctrl-s

# Restore session manually  
prefix + Ctrl-r

# View saved sessions
ls -la ~/.tmux/resurrect/

# Force save
~/.tmux/plugins/tmux-resurrect/scripts/save.sh

# Force restore
~/.tmux/plugins/tmux-resurrect/scripts/restore.sh
```

### **D. Vim Tmux Navigator**
```tmux
set -g @plugin 'christoomey/vim-tmux-navigator'

# Disable tmux navigator when zoomed (optional)
set -g @tmux-navigator-disable-on-zoom '1'

# Disable wrapping around at edges (optional)
set -g @tmux-navigator-no-wrap '1'

# Custom key bindings (optional - defaults are Ctrl+h/j/k/l)
set -g @tmux-navigator-left 'C-h'
set -g @tmux-navigator-down 'C-j'
set -g @tmux-navigator-up 'C-k'
set -g @tmux-navigator-right 'C-l'
set -g @tmux-navigator-next 'C-\'

# Also configure in ~/.vimrc:
let g:tmux_navigator_no_mappings = 1

nnoremap <silent> <C-h> :TmuxNavigateLeft<cr>
nnoremap <silent> <C-j> :TmuxNavigateDown<cr>
nnoremap <silent> <C-k> :TmuxNavigateUp<cr>
nnoremap <silent> <C-l> :TmuxNavigateRight<cr>
nnoremap <silent> <C-\> :TmuxNavigatePrevious<cr>
```

### **E. Tmux Yank (System Clipboard Integration)**
```tmux
set -g @plugin 'tmux-plugins/tmux-yank'

# Configuration
set -g @yank_selection 'primary'  # or 'secondary' or 'clipboard'
set -g @yank_selection_mouse 'clipboard'  # mouse drag copies to clipboard
set -g @yank_with_mouse on        # copy with mouse without entering copy mode
set -g @yank_action 'copy-pipe'   # or 'copy-pipe-and-cancel'

# Platform-specific settings
if-shell '[[ "$(uname)" == "Darwin" ]]' 'set -g @yank_selection "clipboard"'
if-shell '[[ "$(uname)" == "Linux" ]]' 'set -g @yank_selection "primary"'

# Custom key bindings
set -g @yank_with_mouse off  # if you want only keyboard yank
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "pbcopy"
bind -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "xclip"

# Yank to clipboard and system selection
bind -T copy-mode-vi Y send-keys -X copy-pipe-and-cancel "xclip -selection clipboard && xclip -selection primary"
```

**Usage:**
```bash
# Copy in copy mode: y
# Copy line: prefix + Y
# Copy pane contents: prefix + Alt + y
# Paste: prefix + p  (if using system clipboard)
```

### **F. Tmux FZF (Fuzzy Finder)**
```tmux
set -g @plugin 'sainnhe/tmux-fzf'

# Configuration options
set -g @tmux-fzf-command "fzf-tmux"
set -g @tmux-fzf-prompt "  "
set -g @tmux-fzf-preview true
set -g @tmux-fzf-position "C"
set -g @tmux-fzf-size "80%"

# Key bindings (defaults shown)
bind-key "f" run-shell -b "~/.tmux/plugins/tmux-fzf/scripts/session.sh switch"
bind-key "F" run-shell -b "~/.tmux/plugins/tmux-fzf/scripts/window.sh switch"
bind-key "s" run-shell -b "~/.tmux/plugins/tmux-fzf/scripts/pane.sh switch"
bind-key "S" run-shell -b "~/.tmux/plugins/tmux-fzf/scripts/session.sh attach"

# Custom bindings example:
bind -r C-f display-popup -E "\
  ~/.tmux/plugins/tmux-fzf/scripts/session.sh switch"

# Use ripgrep for searching if available
if-shell 'command -v rg' \
  'set -g @tmux-fzf-search-program "rg"' \
  'set -g @tmux-fzf-search-program "grep"'

# Preview window configuration
set -g @tmux-fzf-preview-size "70%"
```

### **G. Tmux CPU/Memory Load**
```tmux
set -g @plugin 'thewtex/tmux-mem-cpu-load'

# Configuration
set -g @tmux-mem-cpu-load-interval 2  # update interval in seconds
set -g @tmux-mem-cpu-load-args "--colors --powerline-right --interval 2"

# Display format options
# --colors: color output
# --powerline-right: powerline style with right arrow
# --graph-lines 0: disable graphs
# --mem-mode 1: show used/total memory

# Add to status line
set -g status-right "#{tmux-mem-cpu-load} %H:%M %d-%b-%y"

# Custom colors
set -g @tmux-mem-cpu-load-colors-low "#[fg=green]"
set -g @tmux-mem-cpu-load-colors-medium "#[fg=yellow]"
set -g @tmux-mem-cpu-load-colors-high "#[fg=red]"

# Thresholds (percentage)
set -g @tmux-mem-cpu-load-threshold-low 30
set -g @tmux-mem-cpu-load-threshold-medium 60
```

### **H. Tmux Pain Control (Enhanced Pane Operations)**
```tmux
set -g @plugin 'tmux-plugins/tmux-pain-control'

# Default key bindings:
# prefix + h/j/k/l: resize panes
# prefix + H/J/K/L: move panes
# prefix + =: maximize current pane
# prefix + -: restore from maximized
# prefix + _: horizontal split
# prefix + |: vertical split
# prefix + r: rotate panes
# prefix + R: reverse rotate panes
# prefix + b: break pane into window
# prefix + z: zoom pane

# Customize bindings (optional):
set -g @pain-control-resize-step-x 5   # horizontal resize step
set -g @pain-control-resize-step-y 2   # vertical resize step
set -g @pain-control-no-default-keybindings 0  # keep defaults

# If you want to disable specific bindings:
unbind-key h
unbind-key j
unbind-key k
unbind-key l
# Then define your own...
```

## **5. Advanced Plugin Configuration**

### **A. Creating a Complete Tmux Configuration File**

```tmux
# ~/.tmux.conf - Complete Example

# ========== BASIC SETTINGS ==========
set -g default-terminal "tmux-256color"
set -ag terminal-overrides ",xterm-256color:RGB"
set -g mouse on
set -g history-limit 10000
set -g base-index 1
set -g pane-base-index 1
set -g renumber-windows on
set -g escape-time 10
set -g focus-events on
set -g default-shell /bin/zsh

# ========== KEY BINDINGS ==========
# Set prefix to Ctrl-a (instead of Ctrl-b)
unbind C-b
set -g prefix C-a
bind C-a send-prefix

# Reload config
bind r source-file ~/.tmux.conf \; display "Config reloaded!"

# Split panes
bind | split-window -h -c "#{pane_current_path}"
bind - split-window -v -c "#{pane_current_path}"
bind c new-window -c "#{pane_current_path}"

# Vim keys for copy mode
set-window-option -g mode-keys vi
bind -T copy-mode-vi v send-keys -X begin-selection
bind -T copy-mode-vi y send-keys -X copy-selection

# ========== PLUGINS ==========
# TPM must be at the beginning
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Theme
set -g @plugin 'catppuccin/tmux'
set -g @catppuccin_flavour 'mocha'
set -g @catppuccin_status_modules_right "directory date_time"
set -g @catppuccin_date_time_text "%H:%M"

# Session Management
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @resurrect-capture-pane-contents 'on'
set -g @continuum-restore 'on'

# Navigation
set -g @plugin 'christoomey/vim-tmux-navigator'

# Productivity
set -g @plugin 'tmux-plugins/tmux-yank'
set -g @plugin 'tmux-plugins/tmux-pain-control'

# Utilities
set -g @plugin 'sainnhe/tmux-fzf'
set -g @plugin 'thewtex/tmux-mem-cpu-load'
set -g @tmux-mem-cpu-load-interval 3

# ========== STATUS BAR ==========
set -g status on
set -g status-interval 2
set -g status-justify left
set -g status-left-length 200
set -g status-right-length 200

# Add CPU load to status
set -g status-right "#{tmux-mem-cpu-load} #[fg=white]#(date '+%H:%M')"

# ========== TPM INITIALIZATION ==========
run '~/.tmux/plugins/tpm/tpm'
```

### **B. Plugin-Specific Environment Variables**

```bash
# Add to ~/.bashrc, ~/.zshrc, or shell profile:
export TMUX_PLUGIN_MANAGER_PATH="$HOME/.tmux/plugins"

# For better clipboard integration on Linux:
if [[ "$(uname)" == "Linux" ]]; then
    export TMUX_YANK_WITH_XCLIP=1
    export TMUX_YANK_WITH_WL_CLIPBOARD=1  # Wayland
fi

# For macOS:
if [[ "$(uname)" == "Darwin" ]]; then
    export TMUX_YANK_WITH_PBCOPY=1
fi

# For tmux-fzf:
export FZF_DEFAULT_OPTS="--height 40% --layout=reverse --border"
```

### **C. Conditional Plugin Loading**

```tmux
# Load plugins based on conditions
if-shell '[[ -f ~/.tmux/plugins/tpm/tpm ]]' \
    'set -g @plugin "tmux-plugins/tpm"' \
    'display "TPM not installed. Run: git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm"'

# Load theme only if terminal supports 256 colors
if-shell '[[ "$TERM" =~ "256color" ]]' \
    'set -g @plugin "dracula/tmux"' \
    'set -g @plugin "tmux-plugins/tmux-sensible"'

# Platform-specific plugins
if-shell '[[ "$(uname)" == "Darwin" ]]' \
    'set -g @plugin "tmux-plugins/tmux-battery"' \
    'set -g @plugin "thewtex/tmux-mem-cpu-load"'

# Load local/custom plugins
if-shell '[[ -f ~/.tmux/plugins/my-custom-plugin/my-plugin.tmux ]]' \
    'run-shell ~/.tmux/plugins/my-custom-plugin/my-plugin.tmux'
```

### **D. Custom Plugin Development**

**1. Create a simple tmux plugin:**
```bash
mkdir -p ~/.tmux/plugins/my-tmux-plugin
cd ~/.tmux/plugins/my-tmux-plugin

# Create plugin structure
touch my_plugin.tmux
mkdir scripts
```

**2. Plugin file example:**
```bash
#!/usr/bin/env bash
# ~/.tmux/plugins/my-tmux-plugin/my_plugin.tmux

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define default key bindings
DEFAULT_KEY="M-c"  # Alt+c

# Get user configuration
get_tmux_option() {
    local option="$1"
    local default_value="$2"
    local option_value=$(tmux show-option -gqv "$option")
    if [ -z "$option_value" ]; then
        echo "$default_value"
    else
        echo "$option_value"
    fi
}

# Main plugin logic
main() {
    local key_binding=$(get_tmux_option "@my-plugin-key" "$DEFAULT_KEY")
    
    # Bind key to custom command
    tmux bind-key "$key_binding" run-shell "$CURRENT_DIR/scripts/my_script.sh"
    
    # Add to status bar (optional)
    tmux set-option -g status-right "#{my_plugin_status}"
}

# Run main function
main
```

**3. Script file:**
```bash
#!/usr/bin/env bash
# ~/.tmux/plugins/my-tmux-plugin/scripts/my_script.sh

# Get current window/pane info
window_name=$(tmux display-message -p '#W')
pane_id=$(tmux display-message -p '#P')

# Do something useful
tmux display-message "Hello from plugin! Window: $window_name, Pane: $pane_id"

# Or display in status bar
echo "Plugin Active"
```

**4. Add to TPM:**
```tmux
set -g @plugin 'your-username/my-tmux-plugin'
set -g @my-plugin-key 'C-c'  # Custom configuration
```

## **6. Troubleshooting Plugin Issues**

### **Common Problems and Solutions**

**1. Plugins not loading:**
```bash
# Check if TPM is installed
ls ~/.tmux/plugins/tpm/tpm

# Check .tmux.conf syntax
tmux source-file ~/.tmux.conf 2>&1 | head -20

# Check plugin installation
ls ~/.tmux/plugins/ | grep -E "(tpm|resurrect|yank)"

# Manually install missing plugins
~/.tmux/plugins/tpm/bin/install_plugins
```

**2. Theme not appearing correctly:**
```tmux
# Check terminal compatibility
echo $TERM  # Should be tmux-256color or similar

# Force 256 colors
set -g default-terminal "tmux-256color"
set -ag terminal-overrides ",xterm-256color:RGB"

# Reload config
tmux source-file ~/.tmux.conf
```

**3. Resurrect not saving sessions:**
```bash
# Check if plugin is loaded
tmux list-keys | grep resurrect

# Check save directory
ls -la ~/.tmux/resurrect/

# Manually trigger save
prefix + Ctrl-s

# Check logs
tail -f ~/.tmux/resurrect/last

# Check process exclusions
cat ~/.tmux/plugins/tmux-resurrect/resurrect.tmux | grep "ignore"
```

**4. Yank not working with system clipboard:**
```bash
# Check dependencies
command -v xclip    # Linux
command -v pbcopy   # macOS
command -v wl-copy  # Wayland

# Test manually
echo "test" | xclip -selection clipboard
echo "test" | pbcopy

# Check tmux-yank configuration
grep -A5 -B5 "yank" ~/.tmux.conf

# Try alternative clipboard tools
set -g @yank_selection_mouse 'clipboard'
set -g @yank_with_mouse on
```

**5. Performance issues with many plugins:**
```tmux
# Disable heavy plugins temporarily
# Comment out in .tmux.conf:
# set -g @plugin 'thewtex/tmux-mem-cpu-load'
# set -g @plugin 'tmux-plugins/tmux-battery'

# Increase update intervals
set -g status-interval 5
set -g @tmux-mem-cpu-load-interval 10

# Use lazy loading for heavy plugins
if-shell '[ -f ~/.tmux/plugins/tmux-fzf/tmux-fzf.tmux ]' \
    'run-shell ~/.tmux/plugins/tmux-fzf/tmux-fzf.tmux'
```

**6. Debug plugin loading:**
```bash
# Start tmux with verbose logging
tmux -vv -f ~/.tmux.conf 2> ~/tmux-debug.log

# Check what's being loaded
grep -i "plugin\|run-shell" ~/tmux-debug.log

# Test plugin manually
~/.tmux/plugins/tmux-resurrect/resurrect.tmux
```

## **7. Plugin Management Script**

Create a script for easier plugin management:

```bash
#!/usr/bin/env bash
# ~/bin/tmux-plugin-manager

TMUX_PLUGINS_DIR="$HOME/.tmux/plugins"
TPM_DIR="$TMUX_PLUGINS_DIR/tpm"

case "$1" in
    install)
        echo "Installing TPM..."
        git clone https://github.com/tmux-plugins/tpm "$TPM_DIR"
        ;;
    
    update)
        echo "Updating TPM..."
        cd "$TPM_DIR" && git pull
        
        echo "Updating all plugins..."
        "$TPM_DIR/bin/update_plugins" all
        ;;
    
    clean)
        echo "Cleaning unused plugins..."
        "$TPM_DIR/bin/clean_plugins"
        ;;
    
    list)
        echo "Installed plugins:"
        ls -la "$TMUX_PLUGINS_DIR" | grep -v "^total" | awk '{print $9}'
        ;;
    
    add)
        if [ -z "$2" ]; then
            echo "Usage: $0 add <github-user/repo>"
            exit 1
        fi
        
        # Add to .tmux.conf
        echo "set -g @plugin '$2'" >> ~/.tmux.conf
        echo "Added $2 to .tmux.conf"
        
        # Install
        tmux source-file ~/.tmux.conf
        echo "Press prefix + I in tmux to install"
        ;;
    
    *)
        echo "Usage: $0 {install|update|clean|list|add}"
        exit 1
        ;;
esac
```

Make executable: `chmod +x ~/bin/tmux-plugin-manager`

## **8. Recommended Plugin Combinations**

### **For Developers:**
```tmux
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'catppuccin/tmux'                    # Clean theme
set -g @plugin 'christoomey/vim-tmux-navigator'    # Vim navigation
set -g @plugin 'tmux-plugins/tmux-yank'            # Clipboard
set -g @plugin 'tmux-plugins/tmux-resurrect'       # Session save
set -g @plugin 'tmux-plugins/tmux-open'            # Open files/URLs
set -g @plugin 'joshmedeski/tmux-nerd-font-window-name' # Pretty window names
```

### **For Sysadmins:**
```tmux
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'dracula/tmux'                      # Information-rich
set -g @plugin 'thewtex/tmux-mem-cpu-load'         # System stats
set -g @plugin 'tmux-plugins/tmux-battery'         # Battery status
set -g @plugin 'tmux-plugins/tmux-online-status'   # Network status
set -g @plugin 'sainnhe/tmux-fzf'                  # Quick switching
set -g @plugin 'tmux-plugins/tmux-logging'         # Session logging
```

### **For Minimalists:**
```tmux
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-yank'
set -g @plugin 'christoomey/vim-tmux-navigator'
# That's it!
```

### **For Power Users:**
```tmux
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'dracula/tmux'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @plugin 'christoomey/vim-tmux-navigator'
set -g @plugin 'tmux-plugins/tmux-yank'
set -g @plugin 'tmux-plugins/tmux-pain-control'
set -g @plugin 'sainnhe/tmux-fzf'
set -g @plugin 'tmux-plugins/tmux-copycat'         # Enhanced searching
set -g @plugin 'tmux-plugins/tmux-open'
set -g @plugin 'tmux-plugins/tmux-logging'
set -g @plugin 'nhdaly/tmux-better-mouse-mode'     # Better mouse
```

## **9. Migration from Old Configuration**

If migrating from old tmux config or other plugin managers:

```bash
# 1. Backup old config
cp ~/.tmux.conf ~/.tmux.conf.backup

# 2. Clean old plugins
rm -rf ~/.tmux/plugins/*

# 3. Install TPM
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# 4. Create new .tmux.conf with TPM structure
cat > ~/.tmux.conf << 'EOF'
# TPM plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Add your old custom settings here...
set -g mouse on
set -g history-limit 10000

# Add more plugins...
# set -g @plugin 'dracula/tmux'

# Initialize TPM
run '~/.tmux/plugins/tpm/tpm'
EOF

# 5. Start tmux and install plugins
tmux
# Then press: prefix + I
```

## **10. Performance Considerations**

```tmux
# Optimize plugin performance

# 1. Increase intervals for status updates
set -g status-interval 3
set -g @tmux-mem-cpu-load-interval 5

# 2. Disable heavy plugins on slow systems
# set -g @plugin 'thewtex/tmux-mem-cpu-load'  # Comment out if slow

# 3. Use lazy loading
bind-key C-l run-shell "~/.tmux/plugins/tmux-fzf/scripts/session.sh switch"

# 4. Limit history for performance
set -g history-limit 5000

# 5. Disable unused features
set -g monitor-activity off
set -g visual-activity off
set -g visual-bell off
set -g bell-action none
```

## **Conclusion**

### **Quick Start Summary:**

1. **Install TPM:**
   ```bash
   git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
   ```

2. **Configure `~/.tmux.conf`:**
   ```tmux
   set -g @plugin 'tmux-plugins/tpm'
   set -g @plugin 'tmux-plugins/tmux-sensible'
   # Add more plugins...
   run '~/.tmux/plugins/tpm/tpm'
   ```

3. **Install plugins:**
   ```bash
   tmux source-file ~/.tmux.conf
   # Then press: prefix + I
   ```

4. **Essential plugins to start with:**
   - `tmux-plugins/tmux-sensible` (sane defaults)
   - `tmux-plugins/tmux-yank` (clipboard integration)
   - `christoomey/vim-tmux-navigator` (vim-style navigation)
   - Choose one theme: `dracula/tmux` or `catppuccin/tmux`

### **Key Commands:**
- **Install plugins**: `prefix + I` (capital i)
- **Update plugins**: `prefix + U` (capital u)
- **Uninstall plugins**: `prefix + alt + u`
- **Reload config**: `prefix + r`

### **Best Practices:**
1. Keep TPM initialization line at the **bottom** of `.tmux.conf`
2. Use **drop-in configuration** files for complex plugin settings
3. **Regularly update** plugins with `prefix + U`
4. **Backup** your configuration and resurrect sessions
5. Test new plugins in a **separate tmux session** first

Tmux plugins significantly enhance productivity and aesthetics. Start with a minimal set and gradually add plugins based on your workflow needs.