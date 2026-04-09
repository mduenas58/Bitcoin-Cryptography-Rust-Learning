## **Cursor Movement**
```
Ctrl + A  → Move to beginning of line
Ctrl + E  → Move to end of line
Alt + B   → Move back one word
Alt + F   → Move forward one word
Ctrl + B  → Move back one character
Ctrl + F  → Move forward one character
```

## **Editing Commands**
```
Ctrl + D  → Delete character under cursor (or exit shell if line empty)
Ctrl + H  → Delete character before cursor (Backspace)
Ctrl + W  → Delete word before cursor
Alt + D   → Delete word after cursor
Ctrl + K  → Delete from cursor to end of line
Ctrl + U  → Delete from cursor to beginning of line
Ctrl + Y  → Paste (yank) last deleted text
Ctrl + _  → Undo last edit
```

## **History Navigation**
```
Ctrl + P  → Previous command (Up arrow)
Ctrl + N  → Next command (Down arrow)
Ctrl + R  → Reverse search history (press again to cycle)
Ctrl + G  → Exit history search mode
Ctrl + J  → Execute command from search
!!        → Execute previous command
!$        → Last argument of previous command
!*        → All arguments of previous command
!abc      → Execute most recent command starting with "abc"
```

## **Process Control**
```
Ctrl + C  → Kill/terminate current process
Ctrl + Z  → Suspend current process (fg to resume)
Ctrl + S  → Stop output to screen (XOFF)
Ctrl + Q  → Resume output to screen (XON)
```

## **Screen Operations**
```
Ctrl + L  → Clear screen (same as `clear`)
Ctrl + S  → Stop screen output (freeze)
Ctrl + Q  → Resume screen output
```

## **Word Operations (Alt/Meta key)**
```
Alt + T   → Swap current word with previous word
Alt + U   → Uppercase current word
Alt + L   → Lowercase current word
Alt + C   → Capitalize current word
Alt + .   → Insert last argument of previous command
Alt + _   → Same as Alt + .
```

## **Tab Completion**
```
Tab       → Auto-complete file/command
Tab Tab   → Show all completion options
Alt + ?   → Show possible completions (list)
Alt + *   → Insert all possible completions
```

## **Bang (!) Commands (History Substitution)**
```
!!        → Last command
!-2       → Second to last command
!5        → Command #5 from history
!ssh      → Last command starting with "ssh"
!?ftp?    → Last command containing "ftp"
^wrong^correct → Replace "wrong" with "correct" in last command
```

## **Argument Selection**
```
Alt + .   → Cycle through last arguments of previous commands
!$        → Last argument of previous command
!^        → First argument of previous command
!:2       → Second argument of previous command
!:2-4     → Arguments 2 through 4
!:*       → All arguments
!:2*      → Arguments from 2 to end
```

## **Cut and Paste (Kill Ring)**
```
Ctrl + K  → Cut from cursor to end (kill)
Ctrl + U  → Cut from cursor to beginning
Ctrl + W  → Cut previous word
Ctrl + Y  → Paste (yank) last cut text
Alt + Y   → After Ctrl+Y, cycle through kill ring
```

## **Miscellaneous**
```
Ctrl + T  → Swap two characters
Ctrl + V  → Insert next character literally (e.g., for escape codes)
Alt + T   → Swap current word with previous
Ctrl + ]  → Jump to character (follow with character)
Alt + Ctrl + Y → Insert first argument of previous command
```

## **Useful Combinations**
```bash
# Fix a typo in previous command
^typo^correct
# Example: ^ls^ls -la

# Reuse parts of previous commands
sudo !!               # Rerun last command with sudo
vim !$                # Edit the last argument of previous command
cd !:1                # cd into first argument of previous command

# Quick editing
Ctrl+A → type "sudo " → Ctrl+E  # Prepend sudo to current line
```

## **Customizing (in ~/.inputrc)**
```bash
# Enable case-insensitive tab completion
set completion-ignore-case on

# Show all matches immediately with double tab
set show-all-if-ambiguous on

# Cycle through completions with tab
TAB: menu-complete

# Make Alt key work in terminal
set meta-flag on
set input-meta on
```

## **Pro Tips**
1. **Use Ctrl+R frequently** - Search through history instead of scrolling
2. **Ctrl+_** is your friend - Undo any editing mistake immediately
3. **Alt+.** saves time - Cycle through previous arguments
4. **Tab completion works for variables too** - `echo $HO` + Tab → `$HOME`
5. **Combine shortcuts**: `Ctrl+A → Ctrl+K` clears the entire line

These shortcuts work in most Unix-like shells (bash is default on most Linux/macOS). Some may require enabling in terminal settings or via `stty` commands.