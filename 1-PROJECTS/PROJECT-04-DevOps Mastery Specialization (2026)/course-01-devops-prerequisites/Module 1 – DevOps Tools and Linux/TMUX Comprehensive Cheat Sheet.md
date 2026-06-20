
## **🚀 QUICK START**
```bash
tmux                     # Start new session
tmux new -s mysession    # Start named session
tmux a                   # Attach to last session
tmux a -t mysession      # Attach to named session
tmux kill-session -t name # Kill session
tmux ls                  # List sessions
exit or Ctrl+d           # Kill pane/window/session
```

## **🎛️ PREFIX KEY**
Default prefix is **`Ctrl+b`**
- `Prefix ?` - Show all key bindings
- `Prefix :` - Enter command mode
- `Prefix r` - Reload config
- `Prefix d` - Detach session

## **🪟 PANES (SPLITS)**

### **Creating Panes**
```
Prefix %          # Split vertically (left/right)
Prefix "          # Split horizontally (top/bottom)
Prefix {          # Swap current pane with previous
Prefix }          # Swap current pane with next
Prefix x          # Kill current pane
Prefix !          # Convert pane to window
Prefix z          # Zoom/Unzoom pane (toggle)
Prefix q          # Show pane numbers briefly
```

### **Navigating Panes**
```
Prefix arrow      # Move to pane in direction
Prefix o          # Next pane (cycle)
Prefix ;          # Toggle last active pane
Prefix q [0-9]    # Jump to pane by number
Prefix Space      # Toggle between layouts
Prefix Ctrl+o     # Rotate panes
Prefix Alt+1-5    # Switch layouts
```

### **Resizing Panes**
```
Prefix Ctrl+arrow     # Resize pane by 1 cell
Prefix Alt+arrow      # Resize pane by 5 cells
Prefix M-1 to M-5     # Switch preset layouts
:resize-pane -L 10    # Resize left by 10 cells
:resize-pane -U 5     # Resize up by 5 cells
```

## **📑 WINDOWS**

### **Window Management**
```
Prefix c          # Create new window
Prefix ,          # Rename current window
Prefix .          # Move window (prompt for index)
Prefix &          # Kill current window
Prefix p          # Previous window
Prefix n          # Next window
Prefix 0-9        # Switch to window by number
Prefix l          # Last active window
Prefix w          # Choose window from list
Prefix f          # Find window by name
Prefix '          # Prompt for window index
Prefix M-n        # Next window with alert
Prefix M-p        # Previous window with alert
```

### **Window Layouts**
- **even-horizontal** - Panes spread horizontally
- **even-vertical** - Panes spread vertically
- **main-horizontal** - Large top pane, others horizontal
- **main-vertical** - Large left pane, others vertical
- **tiled** - Equal size panes

## **🎭 SESSIONS**

### **Session Commands**
```bash
# Command line
tmux new -s session_name
tmux attach -t session_name
tmux rename-session -t old new
tmux switch -t session_name
tmux kill-session -t name
tmux list-sessions

# Inside tmux
Prefix $          # Rename current session
Prefix s          # Switch session (interactive)
Prefix (          # Previous session
Prefix )          # Next session
Prefix L          # Last session
:new -s name      # Create new session
:kill-session -t name # Kill session
```

## **📋 COPY MODE (SCROLL/BUFFER)**

### **Entering Copy Mode**
```
Prefix [          # Enter copy mode
Prefix PgUp       # Enter copy mode and scroll up
```

### **Navigation in Copy Mode**
```
h/j/k/l   # Vim-style movement
arrow     # Arrow key movement
Ctrl+b/u  # Page up/down
g/G       # Top/bottom of buffer
/         # Search forward
?         # Search backward
n/N       # Next/previous match
q         # Exit copy mode
```

### **Selection & Copy**
```
Space     # Start selection
Enter     # Copy selection and exit
Ctrl+g    # Clear selection
v         # Begin selection (vim mode)
y         # Copy selection (vim mode)
```

### **Paste**
```
Prefix ]          # Paste from buffer
:show-buffer      # Display buffer content
:choose-buffer    # Choose from multiple buffers
```

## **🐭 MOUSE SUPPORT**

### **Configuration** (add to `~/.tmux.conf`):
```bash
set -g mouse on              # Enable mouse
# Optional refinements:
set -g mouse-resize-pane on
set -g mouse-select-pane on
set -g mouse-select-window on
```

### **Mouse Actions** (when enabled):
- **Click** - Select pane/window
- **Drag** - Select text in copy mode
- **Scroll** - Scroll through history
- **Drag divider** - Resize panes

## **🎨 CUSTOMIZATION**

### **Common `.tmux.conf` Settings**
```bash
# Change prefix
set -g prefix C-a
unbind C-b
bind C-a send-prefix

# Start windows/panes at 1 not 0
set -g base-index 1
setw -g pane-base-index 1

# Enable true color
set -g default-terminal "tmux-256color"
set -ag terminal-overrides ",xterm*:Tc"

# Longer history
set -g history-limit 50000

# Faster escape time
set -sg escape-time 0

# Vim keys for copy mode
setw -g mode-keys vi

# Rebind split keys
bind | split-window -h
bind - split-window -v
unbind '"'
unbind %

# Reload config
bind r source-file ~/.tmux.conf \; display "Reloaded!"
```

### **Status Bar Customization**
```bash
# Position
set -g status-position top

# Colors
set -g status-style bg=black,fg=white

# Left section (session info)
set -g status-left "#[fg=green]#S #[fg=yellow]|"

# Right section (time, date, host)
set -g status-right "#[fg=cyan]%H:%M | %d-%b-%y | #{host_short}"

# Window list
setw -g window-status-current-style fg=black,bg=yellow
setw -g window-status-format "#I:#W#F"
setw -g window-status-current-format "#I:#W#F"

# Refresh interval
set -g status-interval 1
```

## **🔧 ADVANCED FEATURES**

### **Synchronized Panes**
```
:setw synchronize-panes on  # Type in all panes
:setw synchronize-panes off # Disable sync
Prefix :                    # Type commands
```

### **Run Commands**
```bash
# Send commands to tmux
tmux send-keys -t session:window "ls" C-m

# Run command in new window
tmux new-window -n "logs" "tail -f app.log"
```

### **Session Groups**
```bash
# Link windows between sessions
:link-window -s session:window -t target_session
```

### **Buffer Management**
```
:list-buffers              # Show all buffers
:save-buffer filename      # Save buffer to file
:delete-buffer -b 1       # Delete buffer 1
```

## **🎯 PRACTICAL WORKFLOWS**

### **Pair Programming**
```bash
# Create shared session
tmux new -s pairing

# Other person attaches
tmux -S /tmp/pairing.sock attach

# OR with specific socket
tmux -S /tmp/shared new -s pair
```

### **Session Templates**
```bash
# Save layout
tmux list-windows -F "#{window_index} #{window_layout}" > layout.txt

# Restore session
#!/bin/bash
tmux new-session -d -s dev
tmux send-keys -t dev:1 "cd ~/project" C-m
tmux send-keys -t dev:1 "vim" C-m
tmux split-window -h -t dev:1
tmux send-keys -t dev:1.2 "cd ~/project && git status" C-m
tmux attach -t dev
```

### **Nested tmux Sessions**
```
# Send prefix to inner tmux
Prefix Prefix     # Send prefix to nested session
Prefix :send-prefix

# Escape sequences
Prefix 2          # Send to second level
```

## **⚡ PERFORMANCE TIPS**

```bash
# Faster refresh
set -g status-interval 2

# Disable unused features
set -g visual-activity off
set -g visual-bell off
set -g visual-silence off
setw -g monitor-activity off
set -g bell-action none

# Optimize for remote sessions
set -g assume-paste-time 1
set -s focus-events on
```

## **🔍 DEBUGGING**

```bash
# Check tmux info
tmux info                    # Show server info
tmux show-options -g         # Show all global options
tmux show-window-options -g  # Show window options

# Logging
tmux -vv new-session         # Verbose logging
:capture-pane -S -1000       # Capture last 1000 lines
:save-buffer ~/tmux.log      # Save buffer to file

# Version info
tmux -V                      # Show version
```

## **🔄 MIGRATION & BACKUP**

```bash
# Save sessions (with tmux-resurrect plugin)
Prefix Ctrl+s    # Save
Prefix Ctrl+r    # Restore

# Manual backup
tmux list-sessions > sessions.txt
tmux list-windows -a > windows.txt
```

## **📚 USEFUL PLUGINS**
- **tpm** - Tmux Plugin Manager
- **tmux-resurrect** - Restore tmux sessions
- **tmux-continuum** - Auto-save/restore
- **tmux-yank** - Copy to system clipboard
- **tmux-battery** - Battery status
- **tmux-prefix-highlight** - Show prefix status

---

## **💡 PRO TIPS**

1. **Quick pane navigation**: Add to `.tmux.conf`:
   ```bash
   bind -r h select-pane -L
   bind -r j select-pane -D
   bind -r k select-pane -U
   bind -r l select-pane -R
   ```

2. **Easy resize**:
   ```bash
   bind -r H resize-pane -L 5
   bind -r J resize-pane -D 5
   bind -r K resize-pane -U 5
   bind -r L resize-pane -R 5
   ```

3. **Quick session switcher**:
   ```bash
   bind S choose-session
   ```

4. **Never lose your session**:
   ```bash
   # Add to .bashrc/zshrc
   if command -v tmux &> /dev/null && [ -z "$TMUX" ]; then
       tmux attach -t default || tmux new -s default
   fi
   ```

5. **Useful aliases**:
   ```bash
   alias t='tmux'
   alias ta='tmux attach'
   alias tl='tmux ls'
   alias tn='tmux new -s'
   ```

**Remember**: All `Prefix` commands mean press your prefix key (default `Ctrl+b`) then the following key.

I need to see the specific line you're referring to! However, I can provide some common tmux configuration file examples and what they do:

## **Common tmux.conf lines and their functions:**

### **1. Key Bindings:**
```bash
# Change prefix from Ctrl+b to Ctrl+a
set -g prefix C-a
```

```bash
# Enable mouse support
set -g mouse on
```

```bash
# Split pane horizontally with | instead of %
bind | split-window -h
```

### **2. Visual Settings:**
```bash
# Enable 256 colors
set -g default-terminal "screen-256color"
```

```bash
# Set status bar position
set -g status-position top
```

### **3. Pane & Window Management:**
```bash
# Renumber windows when one is closed
set -g renumber-windows on
```

```bash
# Use vi keys for copy mode
setw -g mode-keys vi
```

### **4. Performance & Behavior:**
```bash
# Faster escape time
set -sg escape-time 0
```

```bash
# Increase scrollback buffer
set -g history-limit 50000
```

## **To explain your specific line:**
Please share the exact line from your tmux.conf file, and I'll explain:
- What command it executes
- What configuration it changes
- What the flags/options mean
- What practical effect it has on tmux behavior

**Tip:** You can usually find your tmux config at `~/.tmux.conf` or `~/.config/tmux/tmux.conf`.

This line in your tmux config enables **true color (24-bit color)** support for terminals that identify as `xterm`:

## **Breakdown:**

```bash
set-option -sa terminal-overrides ",xterm*:Tc"
```

### **Parts explained:**
- **`set-option`** (`set` for short) - Sets a tmux option
- **`-sa`** - Flags:
  - `s` = Server option (affects all sessions)
  - `a` = Append to existing value (don't replace)
- **`terminal-overrides`** - The option being set
- **`",xterm*:Tc"`** - The value:
  - `,xterm*` = Matches any terminal whose name starts with "xterm"
  - `:Tc` = Enables the `Tc` (True Color) terminal capability

## **What it does:**

1. **Enables 24-bit color** for terminals that report themselves as xterm variants
2. **Fixes color issues** in modern terminals (like iTerm2, Kitty, Alacritty, etc.) that often identify as xterm
3. **Allows tmux to pass through** RGB colors instead of being limited to 256 colors

## **Why it's needed:**

- Many modern terminals **lie about their capabilities** and report as "xterm"
- Without this override, tmux might limit colors to 256 colors (8-bit) even if your terminal supports millions of colors (24-bit)
- This ensures **color themes, syntax highlighting, and applications** display correctly with full color range

## **Related settings:**

You might also see or need these similar lines:
```bash
# Enable true color for more terminal types
set -g default-terminal "tmux-256color"
set -ag terminal-overrides ",xterm-256color:RGB"
```

## **Common terminal emulators this affects:**
- iTerm2 (when TERM=xterm-256color)
- GNOME Terminal
- macOS Terminal
- Kitty, Alacritty, etc.

## **To test if it's working:**
Run this command in tmux:
```bash
# Should show smooth gradient if true color is working
awk 'BEGIN{
    s="/\\/\\/\\/\\/\\"; s=s s s s s s s s;
    for (colnum = 0; colnum<77; colnum++) {
        r = 255-(colnum*255/76);
        g = (colnum*510/76);
        b = (colnum*255/76);
        if (g>255) g = 510-g;
        printf "\033[48;2;%d;%d;%dm", r,g,b;
        printf "\033[38;2;%d;%d;%dm", 255-r,255-g,255-b;
        printf "%s\033[0m", substr(s,colnum+1,1);
    }
    printf "\n";
}'
```

If you see **banding** (distinct color stripes), true color isn't working. If you see a **smooth gradient**, it's working correctly!