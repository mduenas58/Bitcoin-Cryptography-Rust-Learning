**Goal:** By the end of this lab, you will stop seeing tmux as "that complicated terminal thing" and start seeing it as **a window into parallel universes**.

**Time:** 20 minutes
**Difficulty:** Beginner
**Outcome:** You will create, navigate, and manage multiple terminal sessions without opening a single new tab.

---

## Prerequisites

```bash
# Check if tmux is installed
tmux -V

# If not installed:
# Ubuntu/Debian
sudo apt install tmux -y

# MacOS
brew install tmux

# Fedora/RHEL
sudo dnf install tmux -y
```

---

## Lab 1: Your First Session (The Container)

### Step 1: Create a Session
```bash
tmux new -s lab1
```

**Notice what happened:**
- Your terminal changed. There's a **green bar** at the bottom.
- This is not a new window. This is a **session container**.
- You are still in the same terminal window, but you've entered a different dimension.

**Visualization:** Think of your regular terminal as your desk. Tmux just gave you a **warehouse** connected to your desk. You can walk into the warehouse, work, and walk back out.

---

### Step 2: Name Your Window
Look at the bottom bar. You'll see:
```
[0] 0:bash*                 "yourhost" Date Time
```

Currently, your window is named "bash". Let's name it meaningfully:

```
Ctrl-b ,                   # (that's Ctrl-b + comma)
```

The status bar will highlight. Type:
```
server-setup
```

Press Enter.

**You just named your workspace.** This seems trivial, but when you have 6 windows open, "bash" vs "server-setup" is the difference between chaos and control.

---

### Step 3: Detach Without Closing
This is the superpower. **Do not exit**. Do not `Ctrl-d`. Do not close the terminal.

```
Ctrl-b d                  # d = detach
```

You're back in your regular terminal. But your session is **still running**.

**Prove it:**
```bash
tmux list-sessions
# or
tmux ls
```

You should see:
```
lab1: 1 windows (created ...) (attached)
```

Wait. It says `(attached)`? But you're looking at your regular terminal. This is tmux's elegant lie. You detached, but tmux still thinks you *might* come back.

---

### Step 4: Reattach
```bash
tmux attach -t lab1
```

You're back. Everything is exactly as you left it. That Python script still running? Still running. That Vim session? Still open. That error message you didn't want to lose? Still there.

**This is the core loop:**
```
Create → Work → Detach → Live Life → Attach → Continue
```

**Achievement Unlocked:** You can now put terminal sessions in your pocket and take them out later.

---

## Lab 2: Windows (Tabs on Steroids)

You have one window now. Let's get more.

### Step 1: Create a New Window
Inside your tmux session:

```
Ctrl-b c                  # c = create
```

**Observe:**
- Bottom bar now shows: `0:server-setup* 1:bash-`
- The `*` is on window 1 (bash)
- The `-` is on window 0

**Visualization:** You just opened a second tab. But it's not a browser tab. It's a **parallel universe**. Window 0 is compiling a server. Window 1 is editing config files. They don't interfere. They don't compete for your prompt.

---

### Step 2: Name Your Second Window
```
Ctrl-b ,                  # while in window 1
```

Name it: `config-editing`

Now your bar shows:
```
0:server-setup- 1:config-editing*
```

---

### Step 3: Navigate Windows

| Command | Action | Mnemonic |
|--------|--------|----------|
| `Ctrl-b 0` | Go to window 0 | Numbered! |
| `Ctrl-b 1` | Go to window 1 | |
| `Ctrl-b n` | Next window | n = next |
| `Ctrl-b p` | Previous window | p = previous |
| `Ctrl-b w` | Show all windows | w = windows |

**Try this flow:**
1. `Ctrl-b 0` - Go to server-setup
2. Run `ping google.com` (let it run)
3. `Ctrl-b 1` - Go to config-editing
4. Run `vim dummy.txt` (create a file)
5. `Ctrl-b 0` - Ping still running
6. `Ctrl-b 1` - Vim still open

**Achievement Unlocked:** Parallel processing without parallel terminals.

---

## Lab 3: Panes (Split Screening)

Windows are separate tabs. Panes are **splits within a window**.

### Step 1: Split Vertically
In any window:

```
Ctrl-b %                  # % looks like two halves
```

Your window splits vertically. Two terminals, side by side.

---

### Step 2: Split Horizontally
In either pane:

```
Ctrl-b "                  # " looks like two lines
```

Now you have three panes. It's getting crowded.

**Visualization:** Your terminal is now a dashboard. Top pane: logs. Bottom-left: editor. Bottom-right: git commands.

---

### Step 3: Navigate Panes

| Command | Action |
|--------|--------|
| `Ctrl-b left-arrow` | Go to pane on left |
| `Ctrl-b right-arrow` | Go to pane on right |
| `Ctrl-b up-arrow` | Go to pane above |
| `Ctrl-b down-arrow` | Go to pane below |
| `Ctrl-b o` | Cycle through panes |

**Critical Habit:** These arrows are not for moving between characters. They are for moving between **worlds**.

---

### Step 4: Resize Panes

Hold `Ctrl-b`, then:
- Hold `Alt` (Mac: `Option`) + arrow keys
- Or: `Ctrl-b : resize-pane -L 10` (left by 10 cells)

**Too tedious?** There's a better way. For now, just know it exists. You'll memorize the resize commands when you actually need them.

---

### Step 5: Close Panes

| Method | Command |
|--------|--------|
| Exit the shell | `exit` or `Ctrl-d` |
| Kill pane directly | `Ctrl-b x` (confirm with y) |

**Note:** Killing the last pane kills the window. Killing the last window kills the session.

---

## Lab 4: The Copy Mode (Terminal Time Travel)

This is the hidden superpower that terminal natives use but never explain.

### Step 1: Enter Copy Mode

```
Ctrl-b [                  # [ = backwards in time
```

Your terminal freezes. You can now:
- Move up with arrow keys
- Move down with arrow keys
- Scroll through **all output** since this pane started

**Why this matters:** That error message from 400 lines up? Not lost. It's in the buffer.

---

### Step 2: Search

In copy mode:

```
Ctrl-r                   # Reverse search
```

Type "error" or "exception". Tmux jumps to the first match.

**Spacebar** to start selection. **Enter** to copy.

---

### Step 3: Paste

```
Ctrl-b ]                  # ] = push out
```

Whatever you copied appears at your prompt.

**Achievement Unlocked:** You can now copy error messages without touching your mouse.

---

## Lab 5: Multiple Sessions (The Advanced Container)

You've been in one session (`lab1`). Let's create another.

### Step 1: Detach First
```
Ctrl-b d
```

### Step 2: Create Second Session
```bash
tmux new -s lab2 -d     # -d = create but don't attach
```

### Step 3: List All Sessions
```bash
tmux ls
```
```
lab1: 2 windows (created ...)
lab2: 1 windows (created ...)
```

### Step 4: Switch Between Sessions

| Command | Action |
|--------|--------|
| `tmux attach -t lab1` | Attach to lab1 |
| `tmux attach -t lab2` | Attach to lab2 |
| `Ctrl-b s` | Interactive session switcher |

**Try `Ctrl-b s`:**
- You see all sessions
- Arrow keys to select
- Enter to switch

**Visualization:** Sessions are **entirely separate workspaces**. Lab1 is your web dev environment. Lab2 is your sysadmin environment. They never touch. They never conflict.

---

## Lab 6: Customization (Making It Yours)

Tmux's defaults are... austere. Here's a 30-second customization to make it feel like home.

### Step 1: Create Config File
```bash
vim ~/.tmux.conf
```

### Step 2: Add These Lines
```bash
# remap prefix from Ctrl-b to Ctrl-a (easier)
set -g prefix C-a
unbind C-b
bind C-a send-prefix

# split panes using | and - (intuitive)
bind | split-window -h
bind - split-window -v

# reload config without restarting
bind r source-file ~/.tmux.conf \; display "Config Reloaded!"

# enable mouse support (game-changer)
set -g mouse on

# start window numbering at 1 (0 is weird)
set -g base-index 1
```

### Step 3: Reload Config
```bash
tmux source-file ~/.tmux.conf
```

Or, if inside tmux: `Ctrl-b r`

**Now:**
- `Ctrl-a %` → split vertically? No. `Ctrl-a |` (pipe)
- `Ctrl-a "` → split horizontally? No. `Ctrl-a -` (dash)
- You can click panes to switch

**Achievement Unlocked:** You are no longer using default tmux. You are using **your** tmux.

---

## Lab 7: The Killer Workflow

Here is the exact sequence that makes tmux irreplaceable:

### The Server Admin Flow

1. **SSH into your server**
   ```bash
   ssh user@production-server
   tmux new -s deploy
   ```

2. **Split into dashboard**
   ```
   Ctrl-a |     # vertical split
   Ctrl-a -     # split right pane horizontally
   ```

3. **Arrange:**
   - Left pane: `htop` (system monitor)
   - Top-right: `tail -f logs/app.log`
   - Bottom-right: ready for commands

4. **Detach:**
   ```
   Ctrl-a d
   ```

5. **Disconnect SSH** (close terminal, go home, get coffee)

6. **Later, from anywhere:**
   ```bash
   ssh user@production-server
   tmux attach -t deploy
   ```

Everything is still running. Every log, every process, every cursor position.

---

## Troubleshooting Cheat Sheet

| Symptom | Likely Cause | Fix |
|--------|--------------|-----|
| `Ctrl-b` does nothing | Not in tmux | Check status bar; run `tmux new` |
| Lost session after SSH disconnect | Forgot to detach | Use `tmux attach` to recover |
| Can't type in pane | In copy mode | Press `q` or `Enter` |
| Panes unequally sized | Need to resize | `Ctrl-b : resize-pane -D 10` |
| Tmux feels slow | Need mouse support off? | Toggle `set -g mouse on/off` |
| Forgot session name | `tmux ls` | Lists everything |

---

## The One-Week Challenge

Tmux mastery doesn't come from reading. It comes from **forced repetition**.

**Day 1-2:** Every time you open a terminal, start with `tmux new -s [name]`. Force yourself.

**Day 3-4:** When you need a second terminal, use `Ctrl-b c` or `Ctrl-b %`. Not a new tab. Not a new window.

**Day 5-6:** Detach and reattach intentionally. Leave sessions running overnight.

**Day 7:** Delete your mouse-based terminal workflow. Use copy mode for everything.

---

## Summary: What You Just Learned

| Concept | Command | Visualization |
|--------|---------|---------------|
| Session | `tmux new -s name` | A warehouse |
| Detach | `Ctrl-b d` | Leaving the warehouse |
| Attach | `tmux attach -t name` | Re-entering |
| Window | `Ctrl-b c` | A room in the warehouse |
| Pane | `Ctrl-b %` or `"` | Dividing a room |
| Copy mode | `Ctrl-b [` | Rewinding time |
| Paste | `Ctrl-b ]` | Playing back |

**You now speak tmux.** The rest is just vocabulary building.