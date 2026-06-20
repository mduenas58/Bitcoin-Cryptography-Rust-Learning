# VIM 60-Hour Learning Plan: 80/20 Mastery Path

## 20 Sessions × 3 Hours | Pareto Principle Applied

**Total Time:** 60 hours instruction \+ 5 hours review  
**Objective:** Master 20% of VIM that drives 80% of daily productivity  
**Focus Areas:** Navigation, editing, search/replace, buffers, basic config

---
## 📊 Learning Structure

Sessions 1-3:    Fundamentals & Mode Mastery (9 hours)

Sessions 4-8:    Core Navigation & Movement (15 hours)

Sessions 9-12:   Text Editing & Manipulation (12 hours)

Sessions 13-15:  Buffers, Windows, Tabs (9 hours)

Sessions 16-17:  Search, Replace, Regex (6 hours)

Sessions 18-19:  Configuration & Customization (6 hours)

Session 20:      Integration & Workflow Mastery (3 hours)

---

# 🎯 THE CORE 20% (What Drives 80% of Results)

**Navigation:** hjkl, word jumps, line movements, percentage navigation  
**Editing:** insert/append, delete, change, yank, paste, undo/redo  
**Text Objects:** word, sentence, paragraph, brackets, quotes  
**Operators:** d, c, y, \>, \<, \~ (delete, change, yank, indent, swap case)  
**Search:** /, ?, \*, \#, search & replace (s/old/new/g)  
**Buffers & Windows:** split windows, navigate between buffers  
**Practical Workflows:** coding, editing config files, working with multiple files

---

# SESSION BREAKDOWN

## **SESSION 1: VIM Foundations & The Three Modes** (3 hours)

### Objectives

- Understand VIM philosophy and modal editing  
- Master mode transitions  
- Navigate basic file editing  
- Develop muscle memory for essential keys

### Content (2h 45min)

1. **Why VIM exists** (10 min)  
     
   - Modal editing paradigm  
   - Keyboard-centric design  
   - Why it's everywhere (Linux, servers, embedded systems)

2. **Installing VIM** (10 min)  
     
   - macOS: `brew install vim`  
   - Linux: `apt install vim` / `yum install vim`  
   - Windows: Vim binary or WSL  
   - Verify: `vim --version`

3. **The Three Modes** (45 min) — **PRACTICE HEAVY**  
     
   - **Normal Mode** (command mode): Default; press `Esc` to return  
   - **Insert Mode**: Press `i`, `a`, `I`, `A`, `o`, `O`  
   - **Command Mode**: Press `:` for commands like `:w`, `:q`, `:wq`  
   - Exercise: Open a file, cycle through all modes 50 times  
   - Goal: Automatic muscle memory for mode switching

4. **Basic Navigation in Normal Mode** (40 min) — **PRACTICE HEAVY**  
     
   - `h` (left), `j` (down), `k` (up), `l` (right)  
   - Why not arrow keys? Better for touch typing position  
   - Navigate a 50-line document using only hjkl  
   - Speed drill: Move cursor 200 times in 10 minutes  
   - Goal: hjkl feels as natural as arrow keys

5. **Essential Editing in Insert Mode** (30 min) — **PRACTICE HEAVY**  
     
   - Start insert: `i` (before), `a` (after), `I` (line start), `A` (line end)  
   - Start new line: `o` (below), `O` (above)  
   - Type text, press Esc  
   - Exercise: Create 5 paragraphs of dummy text using different insert modes

6. **Save, Quit, and Basic Commands** (20 min)  
     
   - `:w` (save), `:q` (quit), `:wq` (save & quit), `:q!` (force quit)  
   - `:set number` (show line numbers)  
   - `shift+g` to go to end of file, `gg` to go to beginning

### Resources

- **Interactive:** `vimtutor` (built-in, 30 min tutorial)  
- **Video:** [VIM Basics in 8 Minutes](https://www.youtube.com/watch?v=ER5JYFKkYDg) (8 min)  
- **Cheat Sheet:** [Vim Cheatsheet](https://vim.rtorr.com/)

### Practice Exercises (45 min)

1. Open VIM, practice 100 mode transitions (5 min)  
2. Navigate a 100-line file with hjkl only (10 min)  
3. Create 10 new lines using `o` and `O` alternately (5 min)  
4. Edit 5 different lines using `i`, `a`, `I`, `A` (10 min)  
5. Create, save, and quit 3 files (5 min)  
6. Speed drill: hjkl navigation (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Can switch between all three modes without thinking  
- [ ] hjkl navigation feels natural  
- [ ] Can open, edit, save, and quit a file  
- [ ] Know the difference between `i`, `a`, `I`, `A`, `o`, `O`  
- [ ] Completed vimtutor 50% of the way  
- [ ] No longer reaching for arrow keys  
- **Speed Test:** Navigate a file and make 5 edits in under 2 minutes

---

## **SESSION 2: The Grammar of VIM (Operators \+ Motions)** (3 hours)

### Objectives

- Understand VIM's language: Operator \+ Motion  
- Master the 5 essential operators  
- Build predictability into editing  
- Reach 50% faster editing than normal editors

### Content (2h 45min)

1. **VIM's Language Structure** (15 min)  
     
   - VIM is a language: `<Operator><Motion>`  
   - Example: `dw` \= delete word, `d5j` \= delete 5 lines down  
   - Why: Composable, predictable, fewer keystrokes  
   - Benefit: 1 operator \+ 20 motions \= 20 commands you already know

1. **Essential Operators** (60 min) — **PRACTICE HEAVY**  
     
   - `d` (delete): `dw`, `dd`, `d$`, `d^`, `d5d`  
   - `c` (change/delete+insert): `cw`, `cc`, `c$`, same as `d` but enters Insert mode  
   - `y` (yank/copy): `yw`, `yy`, `y$`, copies without deleting  
   - `>` (indent): `>>`, `>5j`, `>G` (indent to end of file)  
   - `<` (outdent): `<<`, `<5j`, `<G`  
   - Motion: `j` (line down), `k` (line up), `w` (word), `$` (end), `^` (start)

1. **Motions (The Direction Part)** (50 min) — **PRACTICE HEAVY**  
     
   - **Character:** `h`, `l`, `space`, `backspace`  
   - **Word:** `w` (start of next), `b` (start of previous), `e` (end of word)  
   - **Line:** `j`, `k`, `^` (first non-blank), `$` (end), `0` (absolute start)  
   - **Sentence:** `)` (next), `(` (previous)  
   - **Paragraph:** `}` (next), `{` (previous)  
   - **Number-modified:** `5j`, `10w`, `3}` (repeat motion N times)  
   - **Special:** `G` (end of file), `gg` (start of file), `10G` (line 10\)

1. **Combining Operators \+ Motions** (50 min) — **PRACTICE HEAVY**  
     
   - Examples: `d5w` (delete 5 words), `y2}` (copy 2 paragraphs), `c$` (change to end of line)  
   - Common patterns: `dd` (delete line), `yy` (copy line), `cc` (change line)  
   - Exercise: Edit a document using ONLY operator+motion (no visual mode yet)  
   - Speed drill: Make 20 edits using operator+motion in 5 minutes
   
5. **Undo & Redo** (15 min)  
     
   - `u` (undo), `ctrl+r` (redo), `.` (repeat last command)  
   - Undo entire line: `U`  
   - Why `u` is different from other editors (undo per keystroke)

1. **Numbers with Everything** (15 min)  
     
   - `5dd` (delete 5 lines)  
   - `3cw` (change 3 words)  
   - `10j` (move 10 lines down)  
   - Why: Multiplicative power of the language
### Resources

- **Video:** [Learn VIM Progressively](https://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/) (read version, 20 min)  
- **Interactive:** [VIM Trainer \- Operator/Motion](https://www.vim-adventures.com/) (gamified learning)  
- **Video:** [VIM Grammar \- Operator+Motion](https://www.youtube.com/watch?v=wlR5gYd6xQM) (15 min)

### Practice Exercises (45 min)

1. Create a document with 20 lines of text  
2. Delete 5 different words using `dw` (5 min)  
3. Change 3 lines to different text using `cc` (5 min)  
4. Copy 2 paragraphs using `y}` and paste elsewhere (5 min)  
5. Indent 10 lines using `>5j` (5 min)  
6. Make 15 random edits using only operator+motion (15 min)  
7. Speed drill: 20 edits in 5 minutes (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Can explain VIM grammar: Operator \+ Motion  
- [ ] Know all 5 essential operators (`d`, `c`, `y`, `>`, `<`)  
- [ ] Know 10 motions and can combine them  
- [ ] Can edit without thinking about keystrokes  
- [ ] Using `.` to repeat commands naturally  
- [ ] Completed at least 50 operator+motion combinations  
- **Speed Test:** Edit a 30-line file making 10 changes in under 3 minutes

---

## **SESSION 3: Text Objects & Smart Selection** (3 hours)

### Objectives

- Learn text objects (the 80/20 of smart editing)  
- Master selection without visual mode  
- Edit at semantic level (word, sentence, paragraph, brackets)  
- Reach 70% faster editing than visual mode users

### Content (2h 45min)

1. **What Are Text Objects?** (15 min)  
     
   - Text object \= semantic unit: word, sentence, paragraph, brackets  
   - Format: `<operator><inner|around><text-object>`  
   - `i` \= inner (contents only), `a` \= around (with delimiters)  
   - Example: `ci"` \= change inside quotes, `ca(` \= change around parentheses  
   - Power: One mental model, infinite applications
   
2. **Inner vs Around** (30 min) — **PRACTICE HEAVY**  
     
   - `iw` (inner word) vs `aw` (around word \+ space)  
   - `is` (inner sentence) vs `as` (around sentence \+ space)  
   - `ip` (inner paragraph) vs `ap` (around paragraph \+ blank line)  
   - Brackets: `i(`, `a(`, `i[`, `a[`, `i{`, `a}`, `i<`, `a>`  
   - Quotes: `i"`, `a"`, `i'`, `a'`, ``` i`` ``` , ``` a`` ```   
   - Tags: `it` (inner tag), `at` (around tag) for HTML/XML

3. **Operators \+ Text Objects** (60 min) — **PRACTICE HEAVY**  
     
   - Delete: `diw` (delete word), `da(` (delete around parens), `di"` (delete inside quotes)  
   - Change: `cis` (change sentence), `ci[` (change inside brackets)  
   - Yank: `yip` (copy paragraph), `ya"` (copy with quotes)  
   - Most powerful combo: `ci"`, `ca{`, `di(`, `yi[`  
   - Real-world examples: Edit function arguments, change string contents, modify config values

4. **Practical Application: Code Editing** (45 min) — **PRACTICE HEAVY**  
     
   - Edit function arguments: `ci(` inside `function(arg1, arg2)`  
   - Change array elements: `ci[` inside `[1, 2, 3]`  
   - Modify dictionary values: `ci"` or `ci'`  
   - Fix indentation: `=i{` (indent inside braces)  
   - Exercise: Edit a small Python/JavaScript file using only text objects

4. **Text Objects \+ Numbers** (15 min)  
     
   - `d2w` (delete 2 words), `y3is` (copy 3 sentences)  
   - Why fewer use this: Less common but powerful
   
6. **Text Objects in Different Languages** (10 min)  
     
   - HTML: `dit` (delete inside tag), `ca>` (change around tag)  
   - Programming: `di(`, `ci{`, `yi[`  
   - Markdown: Less applicable but understanding helps

### Resources

- **Cheat Sheet:** [VIM Text Objects](https://blog.carbonfive.com/vim-text-objects-the-definitive-guide/)  
- **Interactive:** Practice file with brackets, quotes, sentences (provided below)  
- **Video:** [VIM Text Objects Explained](https://www.youtube.com/watch?v=X3I1ggHMBhQ) (12 min)

### Practice Exercises (45 min)

1. Create file with nested brackets and quotes  
     
   function foo(arg1, "string", \[1, 2, 3\]) { return (x \+ y); }  
     
2. Change word inside quotes using `ci"` (5 min)  
3. Delete arguments inside parens using `di(` (5 min)  
4. Modify array contents using `ca[` (5 min)  
5. Indent function body using `=i{` (5 min)  
6. Edit 10 text objects in real code file (15 min)  
7. Speed drill: 15 text object edits in 3 minutes (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Understand `i` (inner) vs `a` (around)  
- [ ] Know 8+ text object types  
- [ ] Can combine operators with text objects  
- [ ] Comfortable editing without visual mode  
- [ ] Text objects feel more efficient than selection  
- [ ] Can edit at semantic level (not just character-based)  
- **Speed Test:** Edit 10 text objects (mixed types) in 2 minutes

---

## **SESSION 4: Essential Motions & Jumping** (3 hours)

### Objectives

- Master all essential movement commands  
- Navigate large files efficiently (1000+ lines)  
- Jump to specific locations instantly  
- Reach 80% navigation proficiency

### Content (2h 45min)

1. **Character & Line Navigation Review** (15 min)  
     
   - Recap: `hjkl`, `^`, `$`, `0`  
   - New: `+` (next line first char), `-` (prev line first char)  
   - `Home`/`End` vs VIM keys (stick with `^`/`$`)  
   - Why: Hands stay on home row

   

2. **Word-Level Movement** (40 min) — **PRACTICE HEAVY**  
     
   - `w` (word forward, start), `b` (word back, start), `e` (word forward, end)  
   - `W` (WORD forward, by whitespace), `B`, `E` (same but ignore punctuation)  
   - When to use `w` vs `W`: Most code uses `w`, configuration uses `W`  
   - Exercise: Navigate 20-word sentence using only `w`, `b`, `e`  
   - Speed: Move 100 words in 2 minutes

   

3. **Line-Level Jumps** (45 min) — **PRACTICE HEAVY**  
     
   - `j`, `k` (line-by-line), `ctrl+d` (down half-page), `ctrl+u` (up half-page)  
   - `ctrl+f` (forward full page), `ctrl+b` (back full page)  
   - `G` (end of file), `gg` (start of file), `10G` (line 10\)  
   - `{`, `}` (paragraph jumps)  
   - `)`, `(` (sentence jumps)  
   - Exercise: Jump from line 1 to line 500 in 3 jumps

   

4. **Search-Based Navigation** (40 min) — **PRACTICE HEAVY**  
     
   - `/pattern` (search forward), `?pattern` (search backward)  
   - `n` (next match), `N` (previous match)  
   - `*` (search word under cursor forward), `#` (backward)  
   - Speed-up: Hit `/` and immediately start typing (no Enter needed for preview)  
   - Exercise: Find and jump to 10 different words in a document

   

5. **Percentage Navigation** (15 min)  
     
   - `10%G` (go to 10% through file)  
   - `50G` (go to 50%, middle)  
   - Useful for large files: Estimate position as percentage

   

6. **Advanced Jumps** (10 min)  
     
   - `ctrl+]` (jump to tag, if set up)  
   - `ctrl+^` (toggle between two files)  
   - `:10` (go to line 10\)  
   - Know but don't overuse

### Resources

- **Cheat Sheet:** Motion section of [Vim Cheatsheet](https://vim.rtorr.com/)  
- **Practice:** Large file (1000+ lines) for navigation drills  
- **Video:** [VIM Navigation \- Beginners](https://www.youtube.com/watch?v=nxPF4eWXHKQ) (15 min)

### Practice Exercises (45 min)

1. Create a 500-line file (or use real code)  
2. Navigate using `hjkl` and `w`/`b` only (10 min)  
3. Jump from start to end using fewest motions (5 min)  
4. Search for 10 words and navigate to each (10 min)  
5. Jump to line 250, 100, 450, 50 using `nG` (5 min)  
6. Speed drill: Navigate to 20 random locations in 5 minutes (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know all character/word/line motions  
- [ ] Can navigate 500-line file in under 10 jumps  
- [ ] Search and jump feel natural  
- [ ] Using `*`/`#` instead of manual `/` often  
- [ ] Understand `{`/`}` for paragraph jumps  
- [ ] Can reach any line in 2-3 keystrokes  
- **Speed Test:** Navigate to 10 random lines in 1 minute

---

## **SESSION 5: The Dot (.) Command & Macros Intro** (3 hours)

### Objectives

- Master the most powerful VIM command: `.`  
- Record and replay macros for repetitive tasks  
- Save 50+ keystrokes per common task  
- Understand automation philosophy

### Content (2h 45min)

1. **The Dot Command: Repeat Last Edit** (45 min) — **PRACTICE HEAVY**  
     
   - `.` repeats the last editing action (not movement)  
   - Example: `dw` deletes word, `.` deletes next word  
   - Can combine with motion: `dw` then `2.` deletes 3 words total  
   - Why powerful: Edit once, repeat infinitely  
   - Use cases: Fix repeated typos, apply same edit to multiple lines  
   - Exercise: Delete 50 words using 1 `dw` \+ 49 `.` keystrokes

   

2. **Dot \+ Motion Patterns** (45 min) — **PRACTICE HEAVY**  
     
   - Common pattern: `dw` then `j.` (delete word on each line)  
   - Alternative: `dw` then `3j.` (skip 2 lines, delete word)  
   - Edit once, move, repeat: Most efficient approach  
   - Exercise: Edit a 50-line file using dot command pattern  
   - Real example: Change all `foo` to `bar` manually using dot (before learning substitute)

   

3. **Introduction to Macros (Recording)** (50 min) — **PRACTICE HEAVY**  
     
   - What is a macro: Recorded sequence of commands  
   - Record: `q<letter>` (start), commands, `q` (end)  
   - Example: `qaciw<new_word><esc>q` records changing a word  
   - Playback: `@a` (run macro a), `3@a` (run 3 times)  
   - Why macros: More powerful than dot, can record movement  
   - Exercise: Record 3 different macros (change word, add comment, indent line)

   

4. **Practical Macro Examples** (25 min)  
     
   - Add line numbers: Record `I[#]<esc>j` (add \# to each line)  
   - Convert variable name: Record `ciwbetter_name<esc>j`  
   - Bulk edits: Record any multi-step operation, repeat 100 times  
   - When to use: Complex, repetitive tasks

### Resources

- **Video:** [VIM Dot Command](https://www.youtube.com/watch?v=GJsULFMNwPA) (12 min)  
- **Video:** [VIM Macros Explained](https://www.youtube.com/watch?v=C3EwJjWJ0Oo) (18 min)  
- **Practice:** Repetitive editing tasks (provided examples)

### Practice Exercises (45 min)

1. Edit file using dot command only (no arrow keys, no macros) (15 min)  
   - Delete 20 words using `dw` \+ `.`  
   - Change 10 lines using `cw` \+ `j` \+ `.`  
2. Record 3 macros (15 min)  
   - Macro 1: Add prefix to line  
   - Macro 2: Change variable name and move down  
   - Macro 3: Format specific data  
3. Run macros on 50 lines and verify (10 min)  
4. Combine dot and macros: Create a complex edit (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Use dot command naturally for repeated edits  
- [ ] Understand dot vs macro use cases  
- [ ] Can record a macro in under 10 keystrokes  
- [ ] Can run macro multiple times and see results  
- [ ] Avoid using manual repetition (always use `.` or macro)  
- [ ] Know `qa`, `q`, `@a` flow  
- **Speed Test:** Record a 5-step macro and run it 10 times

---

## **SESSION 6: Insert Mode Mastery & Speed Editing** (3 hours)

### Objectives

- Edit faster in Insert mode  
- Master insert shortcuts  
- Reduce mode-switching overhead  
- Reach 90% faster than non-VIM users in insert-heavy tasks

### Content (2h 45min)

1. **Insert Mode Variations** (30 min) — **PRACTICE HEAVY**  
     
   - `i` (before cursor), `a` (after cursor)  
   - `I` (start of line, before indent), `A` (end of line)  
   - `o` (new line below), `O` (new line above)  
   - `s` (delete char and insert), `S` (delete line and insert)  
   - `gi` (insert at last insert point, useful after navigation)  
   - Exercise: Create 10 new lines using different insert commands  
   - Speed: Decide right insert mode in under 1 second

   

2. **Insert Mode Shortcuts** (45 min) — **PRACTICE HEAVY**  
     
   - `ctrl+h` (backspace), `ctrl+w` (delete word), `ctrl+u` (delete line)  
   - `ctrl+n` (next autocomplete), `ctrl+p` (prev autocomplete)  
   - `ctrl+y` (copy line above), `ctrl+e` (copy line below)  
   - `ctrl+r"` (paste from register), `ctrl+r/` (paste last search)  
   - `ctrl+t` (indent), `ctrl+d` (outdent)  
   - `ctrl+v` (insert special char, e.g., `ctrl+v<tab>` for literal tab)  
   - Exercise: Use each shortcut 10 times

   

3. **Abbreviations & Auto-Correction** (30 min)  
     
   - `:iabbrev <buffer> teh the` (auto-correct in file)  
   - `:iabbrev <buffer> =>` (expand abbreviation)  
   - Useful for: Common typos, code snippets, boilerplate  
   - Exercise: Create 5 abbreviations for your workflow  
   - Note: Abbreviations expand on non-keyword char (space, enter, punctuation)

   

4. **Exiting Insert Mode Efficiently** (15 min)  
     
   - Standard: `Esc`, `ctrl+[` (same as Esc, easier on some keyboards)  
   - `Esc` is far, consider remapping to `jk` or `kj` in `.vimrc`  
   - Or keep Esc but practice frequently  
   - Why: Reduces finger strain and mode-switching delay

   

5. **Insert Mode Workflow Patterns** (25 min) — **PRACTICE HEAVY**  
     
   - Pattern 1: `i` \+ type \+ `Esc`  
   - Pattern 2: `A` \+ type \+ `Esc` (common for adding to line)  
   - Pattern 3: `o` \+ type \+ `Esc` \+ `^` (new line at indent)  
   - Pattern 4: `s` \+ type \+ `Esc` (replace single char)  
   - Most editing: 20% insert mode, 80% normal mode  
   - Never stay in insert mode unnecessarily

### Resources

- **Cheat Sheet:** Insert Mode section of [Vim Cheatsheet](https://vim.rtorr.com/)  
- **Video:** [Insert Mode Tips](https://www.youtube.com/watch?v=GJsULFMNwPA) (10 min)  
- **Config tip:** Consider mapping `inoremap jk <Esc>` in `.vimrc` for easier exit

### Practice Exercises (45 min)

1. Create 20 lines of text alternating between `i`, `a`, `I`, `A`, `o` (10 min)  
2. Use each shortcut (`ctrl+h`, `ctrl+w`, `ctrl+u`, etc.) 5 times (10 min)  
3. Type a paragraph with auto-correct abbreviations active (5 min)  
4. Speed test: Create 10 new lines with varying content in 3 minutes (10 min)  
5. Practice insert→escape flow 30 times (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know all insert mode variations  
- [ ] Can choose right insert mode automatically  
- [ ] Use `ctrl+w` and `ctrl+u` for error correction  
- [ ] Know and use 5+ insert shortcuts  
- [ ] Comfortable with abbreviations  
- [ ] Exit insert mode quickly  
- [ ] Spend 20% time in insert, 80% in normal  
- **Speed Test:** Create a 30-line formatted text block in 3 minutes

---

## **SESSION 7: Copy, Paste, Registers** (3 hours)

### Objectives

- Master paste buffers (registers)  
- Understand 11 different register types  
- Use copy/paste for productivity (not just basic operations)  
- Handle multiple clipboards efficiently

### Content (2h 45min)

1. **Basic Copy & Paste** (25 min) — **PRACTICE HEAVY**  
     
   - `y` (yank/copy), `p` (paste after), `P` (paste before)  
   - `yy` (copy line), `p` (paste line below)  
   - `yw` (copy word), `p` (paste)  
   - Most used: `yy` and `p`  
   - Exercise: Copy and paste 20 different lines and words

   

2. **Understanding Registers** (50 min) — **PRACTICE HEAVY**  
     
   - VIM has 26 letter registers \+ special registers  
   - Unnamed register `"` (default for y and d)  
   - Numbered registers `0`\-`9` (previous yanks and deletes)  
   - Special registers: `"_` (black hole), `"*` (system clipboard), `"+` (system clipboard macOS)  
   - Show registers: `:reg`  
   - Access: `"ayw` (yank word into register a), `"ap` (paste from register a)

   

3. **Practical Register Usage** (50 min) — **PRACTICE HEAVY**  
     
   - Copy without overwriting: `"ayy` (copy to register a, doesn't change default)  
   - Use 3 registers: Copy 3 things, paste each separately  
   - System clipboard: `"*p` (paste system), `"*yy` (copy system)  
   - Black hole: `"_dd` (delete without saving)  
   - Exercise: Copy text to 5 different registers and paste each in right order

   

4. **Paste with Auto-Indent** (15 min)  
     
   - `:paste` command (toggles paste mode for terminal pastes)  
   - Why: VIM auto-indent interferes with pasted text sometimes  
   - In normal mode: Use `p` and `=` (indent) automatically handles it  
   - Example: Paste then `=p` to fix indentation

   

5. **Advanced: Macros \+ Registers** (10 min)  
     
   - Macros are stored in registers: `@a` is register a  
   - Combine: Record in one register, paste commands into another

### Resources

- **Cheat Sheet:** Registers section of [Vim Cheatsheet](https://vim.rtorr.com/)  
- **Video:** [VIM Registers and Marks](https://www.youtube.com/watch?v=Gy8Ew1WfPgc) (15 min)  
- **Command:** `:reg` to see all current registers

### Practice Exercises (45 min)

1. Copy and paste 30 different text blocks using default register (10 min)  
2. Copy to 5 different registers and paste each in order (10 min)  
3. Copy from system clipboard and paste into VIM (5 min)  
4. Use black hole register to delete without saving (5 min)  
5. Macro in register: Record in `a`, examine with `"ap`, modify, run as `@a` (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know `y`, `p`, `P` automatically  
- [ ] Understand 5+ register types  
- [ ] Can copy to specific register using `"ayw`  
- [ ] Access system clipboard efficiently  
- [ ] Use black hole for clean deletes  
- [ ] Examine and edit register contents  
- **Speed Test:** Copy 5 things to different registers, paste in reverse order

---

## **SESSION 8: Marks & Navigation Between Positions** (3 hours)

### Objectives

- Create bookmarks within files  
- Jump between marked positions instantly  
- Navigate large files efficiently  
- Track editing history

### Content (2h 45min)

1. **What Are Marks?** (15 min)  
     
   - Mark \= bookmark at specific line and column  
   - Local marks `a-z` (file-specific), Global marks `A-Z` (project-wide)  
   - Automatic marks: `'` (last position), `"` (last edit)  
   - View marks: `:marks`

   

2. **Creating & Using Marks** (60 min) — **PRACTICE HEAVY**  
     
   - Create: `ma` (mark position in register a)  
   - Jump to mark: `` `a `` (exact column), `'a` (first non-blank)  
   - Example: Mark function start `mf`, edit elsewhere, return `` `f ``  
   - Most used: `ma` (temp marker), `mm` (middle), `ms` (start), `me` (end)  
   - Exercise: Mark 10 positions and jump between them

   

3. **Automatic Marks** (30 min) — **PRACTICE HEAVY**  
     
   - `'0` (position before last exit)  
   - `'1`\-`'9` (previous positions in undo history)  
   - `'[` (start of last change), `']` (end of last change)  
   - `'.` (last edit position)  
   - Very useful for: Finding where you last edited, returning to previous position  
   - Exercise: Make changes and return using automatic marks

   

4. **Practical Mark Patterns** (30 min) — **PRACTICE HEAVY**  
     
   - Working on multiple functions: Mark each with `m[first letter]`  
   - Review cycle: `ma` at start, `mb` at key section, cycle with `'a`/`'b`  
   - Pair marks: `mm` at middle (halfway), helps navigation  
   - Delete marks: None needed (they auto-expire), but can `:delmark a`

   

5. **Combining Marks with Other Commands** (10 min)  
     
   - Delete to mark: `d'a` (delete from here to mark a)  
   - Copy to mark: `y'a` (yank from here to mark a)  
   - Indent to mark: `>'a` (indent to mark a)  
   - Why: Powerful for multi-step edits

### Resources

- **Cheat Sheet:** Marks section of [Vim Cheatsheet](https://vim.rtorr.com/)  
- **Video:** [VIM Marks](https://www.youtube.com/watch?v=d-l3N0zVVBo) (12 min)

### Practice Exercises (45 min)

1. Mark 10 positions in a large file (500+ lines) (10 min)  
2. Jump between marks using `` `a `` and `'a` (10 min)  
3. Delete and yank to marks (5 min)  
4. Use automatic marks to return to last edits (10 min)  
5. Create a workflow: Mark function boundaries, navigate to edit, return (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know difference between `` ` `` (exact) and `'` (first non-blank)  
- [ ] Can create marks instantly with `m[letter]`  
- [ ] Jump to marks as naturally as navigation  
- [ ] Use 3+ automatic marks in workflow  
- [ ] Combine marks with operators (`d'a`, `y'a`)  
- [ ] Navigate large file using mark patterns  
- **Speed Test:** Mark 5 positions and navigate between them in 30 seconds

---

## **SESSION 9: Search & Replace Basics** (3 hours)

### Objectives

- Master search fundamentals  
- Use regex for powerful replacements  
- Replace across files efficiently  
- Automate text transformations

### Content (2h 45min)

1. **Basic Search** (30 min) — **PRACTICE HEAVY**  
     
   - `/pattern` (search forward), `?pattern` (search backward)  
   - `n` (next match), `N` (prev match)  
   - `*` (search word under cursor), `#` (search word backward)  
   - Case sensitivity: `/\Cpattern` (ignore case), `/\cpattern` (force case-sensitive)  
   - `:set ignorecase` (permanent toggle)  
   - Exercise: Search for 30 different patterns in a document

   

2. **Search with Regular Expressions** (60 min) — **PRACTICE HEAVY**  
     
   - Basic regex: `.` (any char), `*` (0+ repetitions), `+` (1+), `?` (0 or 1\)  
   - Character class: `[abc]` (a or b or c), `[^abc]` (not a, b, c)  
   - Anchors: `^` (start line), `$` (end line)  
   - Examples: `/^def` (lines starting with def), `/class$` (lines ending with class)  
   - Word boundary: `/\<word\>` (exact word match)  
   - Shorthand: `\d` (digit), `\w` (word char), `\s` (whitespace)  
   - Exercise: Write 10 regex patterns that match specific text

   

3. **Basic Replace (Substitute)** (40 min) — **PRACTICE HEAVY**  
     
   - `:s/old/new/` (replace first on line)  
   - `:s/old/new/g` (replace all on line)  
   - `:10,20s/old/new/` (replace in lines 10-20)  
   - `:%s/old/new/g` (replace all in file)  
   - `:%s/old/new/gc` (interactive: confirm each)  
   - Case preservation: `:s/old/NEW/I` (ignore case in search)  
   - Exercise: Replace 20 different patterns

   

4. **Replace with Regex** (45 min) — **PRACTICE HEAVY**  
     
   - `:%s/\(.*\)/[\1]/g` (wrap each line in brackets, `\1` \= capture group)  
   - `:%s/foo\(.*\)bar/\1/g` (extract middle between foo and bar)  
   - `:%s/^  //g` (remove leading 2 spaces)  
   - `:%s/$/;/g` (add semicolon to end of each line)  
   - Exercise: Transform text using regex replace (5 patterns)

   

5. **Advanced Replace** (15 min)  
     
   - `:&` (repeat last substitution)  
   - `:%s/old/new/ge` (no error if no matches)  
   - `:'<,'>s/old/new/` (replace in selection)  
   - Ranges: `1,5` (lines 1-5), `.,$` (current to end), `.,.+5` (current \+ 5 lines)

### Resources

- **Cheat Sheet:** [Vim Regex](https://vimregex.com/)  
- **Interactive:** [Regex 101](https://regex101.com/) (test patterns before VIM)  
- **Video:** [VIM Search and Replace](https://www.youtube.com/watch?v=GJsULFMNwPA) (25 min)

### Practice Exercises (45 min)

1. Search for 20 different patterns (5 min)  
2. Write 5 regex patterns and test with `/` (10 min)  
3. Replace simple patterns on multiple lines (10 min)  
4. Replace with regex and capture groups (10 min)  
5. Transform a data file using replace (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know `/pattern`, `?pattern`, `*`, `#` for search  
- [ ] Use `n` and `N` naturally  
- [ ] Understand basic regex (`.`, `*`, `+`, `[abc]`, `^`, `$`)  
- [ ] Can write simple regex patterns  
- [ ] Know `:s/old/new/g`, `:%s/old/new/g`, `:%s/old/new/gc`  
- [ ] Understand capture groups in replace (`\1`, `\2`)  
- **Speed Test:** Replace 10 patterns in a file in 5 minutes

---

## **SESSION 10: Advanced Search & Multi-File Replace** (3 hours)

### Objectives

- Search across multiple files  
- Use quickfix list for navigation  
- Perform batch replacements  
- Combine search with editing

### Content (2h 45min)

1. **Search Across Files (Grep)** (45 min) — **PRACTICE HEAVY**  
     
   - `:grep pattern file` (search in file)  
   - `:grep pattern .` (search in current directory)  
   - `:grep pattern **/*.py` (search all Python files)  
   - `:vimgrep pattern file` (VIM's internal grep, slower but doesn't need grep installed)  
   - Opens quickfix list: `:copen` (view all matches)  
   - Exercise: Search for 5 patterns across multiple files

   

2. **Quickfix List & Navigation** (45 min) — **PRACTICE HEAVY**  
     
   - `:copen` (open quickfix window), `:cclose` (close)  
   - `:cnext` (next match), `:cprev` (previous match)  
   - `Enter` on match to jump to it  
   - `:cdo %s/old/new/` (execute command on all matches in quickfix)  
   - Jump directly: `:cc 5` (go to 5th match)  
   - Exercise: Search, view in quickfix, navigate to each match

   

3. **Replace Across Multiple Files** (50 min) — **PRACTICE HEAVY**  
     
   - Pattern: `:grep pattern` → `:cdo %s/old/new/`  
   - Save all: `:cfdo update` (update all files in quickfix)  
   - Example: Find all `TODO` comments and replace with `FIXME`  
   - Alternative: Use quickfix, open all in buffers with `:cdo execute "tabnew %"`  
   - Exercise: Replace across 5 files using quickfix

   

4. **Improving Search Efficiency** (20 min)  
     
   - `:set grepprg=rg` (use ripgrep for faster searching)  
   - `:set grepprg=ag` (use ag for fast searching)  
   - Better performance on large codebases  
   - Requires installing `rg` or `ag` separately

### Resources

- **Video:** [VIM Grep and Quickfix](https://www.youtube.com/watch?v=JOYZY5lZqZs) (18 min)  
- **Install:** `ripgrep` for faster grep: `brew install ripgrep`

### Practice Exercises (45 min)

1. Create 5 small files with repeated patterns (5 min)  
2. Search for pattern across all files using grep (5 min)  
3. View results in quickfix window (5 min)  
4. Navigate through matches (5 min)  
5. Replace using `:cdo %s/old/new/` (10 min)  
6. Replace across 3 files and verify (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know `:grep` and `:vimgrep` differences  
- [ ] Can open quickfix list and view matches  
- [ ] Navigate through matches with `:cnext`, `:cprev`  
- [ ] Use `:cdo` for batch operations  
- [ ] Understand `:cfdo update` for saving changes  
- [ ] Replace across multiple files reliably  
- **Speed Test:** Replace a pattern across 3 files in 3 minutes

---

## **SESSION 11: Split Windows & Buffer Management** (3 hours)

### Objectives

- Create split windows (vertical and horizontal)  
- Switch between windows and buffers efficiently  
- Maximize screen real estate  
- Work on multiple files simultaneously

### Content (2h 45min)

1. **Understanding Buffers vs Windows** (20 min)  
     
   - Buffer \= file loaded in memory  
   - Window \= viewport into a buffer  
   - Multiple windows can show same buffer  
   - One window per split pane  
   - `:buffers` (list all buffers), `:buffer N` (switch to buffer N)

   

2. **Creating Split Windows** (40 min) — **PRACTICE HEAVY**  
     
   - `:split` (horizontal split), `:vsplit` (vertical split)  
   - `:split file.txt` (open file in new split)  
   - `:split .` (open file browser in split)  
   - `:new` (new empty buffer split), `:vnew` (vertical new)  
   - Shortcuts: `:split` \= `:sp`, `:vsplit` \= `:vsp`  
   - Exercise: Create 4 splits (2 horizontal, 2 vertical)

   

3. **Navigating Between Windows** (45 min) — **PRACTICE HEAVY**  
     
   - `ctrl+w` then `w` (next window), `p` (prev), `n` (next), `P` (prev)  
   - `ctrl+w` then `h/j/k/l` (move to window in direction)  
   - `ctrl+w` then `t` (top-left), `b` (bottom-right)  
   - `ctrl+w` then `c` (close current), `o` (close others, keep current)  
   - `ctrl+w` then `=` (equalize window sizes)  
   - Exercise: Create 3 windows, jump between each using different methods

   

4. **Resizing Windows** (30 min) — **PRACTICE HEAVY**  
     
   - `ctrl+w` then `+/-` (increase/decrease height by 1 line)  
   - `ctrl+w` then `5+` (increase by 5 lines)  
   - `ctrl+w` then `>/<` (increase/decrease width)  
   - `:resize 20` (set height to 20 lines)  
   - `:vertical resize 40` (set width to 40 columns)  
   - Exercise: Resize 3 windows to different sizes

   

5. **Buffer Navigation** (30 min) — **PRACTICE HEAVY**  
     
   - `:bnext` (next buffer), `:bprev` (previous buffer)  
   - `:buffer 2` (go to buffer 2\)  
   - `:b filename` (go to buffer by partial name)  
   - `:ba` (open all buffers in windows)  
   - `:bdelete` (delete buffer)  
   - Exercise: Open 5 files, navigate between buffers

   

6. **Tabs vs Splits (When to Use Which)** (15 min)  
     
   - Tabs: Multiple projects or unrelated files  
   - Splits: Related files (e.g., test and source code)  
   - Workflow: Usually 1-3 tabs, multiple splits per tab

### Resources

- **Cheat Sheet:** Windows section of [Vim Cheatsheet](https://vim.rtorr.com/)  
- **Video:** [VIM Windows and Buffers](https://www.youtube.com/watch?v=2nBzL5GDXz8) (20 min)

### Practice Exercises (45 min)

1. Create 4-split window layout (2x2) (5 min)  
2. Navigate between all splits (5 min)  
3. Open 3 files in different splits (5 min)  
4. Resize splits to different sizes (5 min)  
5. Switch between buffers (5 min)  
6. Create workflow: Edit file A, switch to B, back to A (5 min)  
7. Maximize and minimize splits (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Understand buffer vs window vs tab  
- [ ] Can create horizontal and vertical splits  
- [ ] Navigate between windows with `ctrl+w` \+ hjkl  
- [ ] Close and equalize windows  
- [ ] Resize windows to specific sizes  
- [ ] Switch buffers efficiently  
- [ ] Choose splits for related files, tabs for projects  
- **Speed Test:** Create 3-window layout, open 3 files, navigate between all in 2 minutes

---

## **SESSION 12: Tabs & Advanced Buffer Workflows** (3 hours)

### Objectives

- Organize work with tabs  
- Create efficient multi-window/tab layouts  
- Work on multiple projects simultaneously  
- Build productive workflows

### Content (2h 45min)

1. **Creating & Navigating Tabs** (35 min) — **PRACTICE HEAVY**  
     
   - `:tabnew` (new tab), `:tabedit file` (open file in new tab)  
   - `:tabnext` (next tab), `:tabprevious` (prev tab)  
   - `gt` (next tab), `gT` (previous tab), `2gt` (go to tab 2\)  
   - `:tabfirst`, `:tablast` (go to first/last tab)  
   - `:tab split` (open current buffer in new tab)  
   - Exercise: Create 5 tabs, navigate between them

   

2. **Closing & Moving Tabs** (25 min) — **PRACTICE HEAVY**  
     
   - `:tabclose` (close tab), `:tabonly` (close other tabs)  
   - `:tabmove 2` (move tab to position 2\)  
   - Why tab over split: Independent window layouts per tab  
   - Exercise: Close and move tabs

   

3. **Tab Configuration & Display** (20 min)  
     
   - `:set showtabline=2` (always show tab bar)  
   - Tab labels: Show filename by default  
   - Customize: `:set tabline=%!...` (advanced, skip for now)

   

4. **Advanced Buffer Workflows** (50 min) — **PRACTICE HEAVY**  
     
   - Workflow 1: Argument list (load specific files)  
     - `:args file1 file2 file3` (load multiple files)  
     - `:argdo %s/old/new/` (edit across arg list)  
   - Workflow 2: Multiple projects  
     - Project A: Tab 1 with splits  
     - Project B: Tab 2 with splits  
     - Quick switch with `gt`  
   - Workflow 3: Scratch buffer  
     - `:tabnew` (new scratch space)  
     - Keep for notes or temporary edits  
   - Exercise: Create 2-project layout with tabs and splits

   

5. **Sessions (Save/Restore Workspace)** (15 min)  
     
   - `:mksession session.vim` (save current layout)  
   - `:source session.vim` (restore layout)  
   - Why: Restore complex layouts automatically  
   - Note: Advanced, focus on manual organization first

### Resources

- **Cheat Sheet:** Tabs section of [Vim Cheatsheet](https://vim.rtorr.com/)  
- **Video:** [VIM Tabs](https://www.youtube.com/watch?v=y4Z3KWJgnIg) (12 min)

### Practice Exercises (45 min)

1. Create 3 tabs for different projects (10 min)  
2. Create splits within each tab (10 min)  
3. Navigate between tabs and windows (10 min)  
4. Use argument list to edit across files (10 min)  
5. Create and restore a session (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know difference between tabs and splits  
- [ ] Create tabs with `:tabnew` and `:tabedit`  
- [ ] Navigate between tabs with `gt` and `gT`  
- [ ] Understand tab per project, splits for related files  
- [ ] Use argument list for batch edits  
- [ ] Can organize complex multi-window layouts  
- **Speed Test:** Create a 2-project layout (tabs \+ splits) in 3 minutes

---

## **SESSION 13: Text Objects Deep Dive** (3 hours)

### Objectives

- Master advanced text object combinations  
- Learn custom text object patterns  
- Edit at highest semantic level  
- Reach 95% editing efficiency

### Content (2h 45min)

1. **Review Core Text Objects** (20 min)  
     
   - Recap: `iw`, `aw`, `is`, `as`, `ip`, `ap`, `i/a[({<"'` \`\`\`, etc.  
   - Mental model: Inner \= contents, Around \= with delimiters  
   - Why text objects are superior to visual mode

   

2. **Text Objects with Operators** (50 min) — **PRACTICE HEAVY**  
     
   - Delete inside paragraph: `dip`  
   - Change a sentence: `cas`  
   - Yank a word: `yaw`  
   - Indent block: `=i{`  
   - Shift case: `g~iw` (toggle case of word), `gUaw` (uppercase word)  
   - Exercise: 20 different operator+text object combinations

   

3. **Nesting & Complex Edits** (50 min) — **PRACTICE HEAVY**  
     
   - Function arguments in brackets: `ci(` inside function definition  
   - Nested: String inside bracket: `ci"` inside `[...]`  
   - HTML: `cit` (change inner tag), `cat` (change around tag)  
   - Example: Edit `<div class="item">text</div>` → change content with `cit`  
   - Exercise: Edit nested structures

   

4. **Extending Text Objects with Motions** (30 min) — **PRACTICE HEAVY**  
     
   - Text object replaces motion but can mix  
   - Example: `di(` is `di` \+ `(` motion  
   - Why: Text objects are semantic motions  
   - `ciw` \= change inner word \= `cE` (different path, same result)

   

5. **Pseudo Text Objects (Patterns)** (10 min)  
     
   - Entire file: `:%` (not technically text object but similar)  
   - Buffer: `gg` then `G` with `d`, `y`, `c` (delete/copy/change whole file)  
   - Advanced: Custom text objects via plugins (skip for now)

### Resources

- **Cheat Sheet:** [VIM Text Objects Complete](https://blog.carbonfive.com/vim-text-objects-the-definitive-guide/)  
- **Practice:** Code files with various structures

### Practice Exercises (45 min)

1. Create a file with nested structures (30 lines) (5 min)  
2. Use 15 different text objects (15 min)  
3. Edit nested structures accurately (10 min)  
4. Complex edits: Change multiple text object types in one file (10 min)  
5. Speed test: Edit 20 different text objects in 5 minutes (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Master inner vs around distinction  
- [ ] Combine operators with 10+ text objects  
- [ ] Edit nested structures confidently  
- [ ] Understand text objects as semantic units  
- [ ] Know when to use text objects vs motions  
- [ ] Can change any semantic unit in code or text  
- **Speed Test:** Edit 10 text objects in 2 minutes

---

## **SESSION 14: Indentation & Formatting** (3 hours)

### Objectives

- Master automatic indentation  
- Format code efficiently  
- Handle different indentation styles  
- Apply formatting to large blocks

### Content (2h 45min)

1. **Indentation Basics** (30 min) — **PRACTICE HEAVY**  
     
   - `>>` (indent line), `<<` (outdent line)  
   - `>motion` (indent to motion), `<motion` (outdent to motion)  
   - `5>>` (indent 5 lines), `>G` (indent to end of file)  
   - Visual mode: Select, then `>` or `<`  
   - Exercise: Indent 50 lines various ways

   

2. **Auto-Indentation** (30 min) — **PRACTICE HEAVY**  
     
   - `=motion` (auto-indent using file's indentation rules)  
   - `==` (auto-indent current line), `=G` (auto-indent to end)  
   - `gg=G` (auto-indent entire file)  
   - Requires proper filetype detection (VIM guesses based on extension)  
   - Exercise: Auto-indent a messy code file

   

3. **Configuring Indentation** (30 min)  
     
   - `:set tabstop=4` (tab width in display)  
   - `:set shiftwidth=4` (indent amount)  
   - `:set expandtab` (use spaces instead of tabs)  
   - `:set noexpandtab` (use tabs)  
   - `:set smartindent` (smart auto-indentation)  
   - Config: Add to `.vimrc` for persistence  
   - Exercise: Change indentation style and reindent

   

4. **Visual Block Indentation** (20 min) — **PRACTICE HEAVY**  
     
   - `ctrl+v` (visual block mode)  
   - Select block, press `>` or `<` to indent  
   - Useful for: Indenting comments, code snippets  
   - Exercise: Visual block indent 3 columns of text

### Resources

- **Cheat Sheet:** Indentation section of [Vim Cheatsheet](https://vim.rtorr.com/)  
- **Video:** [VIM Indentation](https://www.youtube.com/watch?v=X3I1ggHMBhQ) (12 min)

### Practice Exercises (45 min)

1. Create messy code file with inconsistent indentation (5 min)  
2. Fix indentation using `>>`, `<<`, `=` (10 min)  
3. Auto-indent entire file (5 min)  
4. Visual block indent a section (10 min)  
5. Change indentation style (expand/tabs) and reformat (10 min)  
6. Indent using text objects: `>i{`, `<ip` (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know `>>`, `<<`, `=` commands  
- [ ] Auto-indent code correctly  
- [ ] Use visual block for indentation  
- [ ] Configure tab size and indent width  
- [ ] Differentiate `tabstop` and `shiftwidth`  
- [ ] Auto-indent entire file reliably  
- **Speed Test:** Fix indentation in a 50-line file in 3 minutes

---

## **SESSION 15: Visual Mode & Block Editing** (3 hours)

### Objectives

- Master three visual modes  
- Edit blocks of text efficiently  
- Use visual mode for complex selections  
- Know when visual mode is better than text objects

### Content (2h 45min)

1. **Three Visual Modes** (40 min) — **PRACTICE HEAVY**  
     
   - `v` (character visual mode): Select char by char  
   - `V` (line visual mode): Select whole lines  
   - `ctrl+v` (block visual mode): Select rectangular block  
   - Why three modes: Different selection types  
   - Exercise: Use all three modes to select same content

   

2. **Selecting in Visual Mode** (40 min) — **PRACTICE HEAVY**  
     
   - Extend selection: `hjkl`, `w`, `b`, `$`, `^`, etc.  
   - Extend to motion: `v/pattern<enter>` (select to next match)  
   - `o` (toggle cursor end in visual mode)  
   - Select line: `V` then `j` selects multiple lines  
   - Block select: `ctrl+v` then `5j` then `10l` selects rectangular block  
   - Exercise: Select 20 different types of content

   

3. **Editing in Visual Mode** (40 min) — **PRACTICE HEAVY**  
     
   - Delete: `d` or `x`  
   - Change: `c` (replace selected with new text)  
   - Indent: `>` or `<`  
   - Yank: `y`  
   - Format: `gq` (reformat selected text)  
   - Uppercase: `U`, Lowercase: `u`, Toggle: `~`  
   - Exercise: Edit selection in 10 different ways

   

4. **Block Visual Editing** (25 min) — **PRACTICE HEAVY**  
     
   - Rectangle selection: `ctrl+v` then select  
   - Indent block: Select, press `>`  
   - Delete column: `ctrl+v`, select, press `d`  
   - Add to multiple lines: `ctrl+v`, select, `$`, then edit (complicated)  
   - Simpler alternative: Use macros  
   - Exercise: Edit columns and blocks

### Resources

- **Video:** [VIM Visual Mode](https://www.youtube.com/watch?v=nxPF4eWXHKQ) (15 min)  
- **Cheat Sheet:** Visual Mode section

### Practice Exercises (45 min)

1. Select content using all three visual modes (10 min)  
2. Delete, change, yank selections (10 min)  
3. Indent and format selections (10 min)  
4. Block edit: Select column and delete (10 min)  
5. Complex selection: Select across lines and paragraphs (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Know all three visual modes (`v`, `V`, `ctrl+v`)  
- [ ] Select efficiently using motions  
- [ ] Edit selections with `d`, `c`, `y`, `>`, `<`  
- [ ] Use block mode for rectangular selections  
- [ ] Know when visual mode beats text objects  
- [ ] Can edit columns of text  
- **Speed Test:** Select, edit, format content in 3 minutes

---

## **SESSION 16: Efficient Searching with Highlights & Settings** (3 hours)

### Objectives

- Optimize search workflow  
- Use search highlighting productively  
- Configure search preferences  
- Navigate search results efficiently

### Content (2h 45min)

1. **Search Highlighting & Clearing** (35 min) — **PRACTICE HEAVY**  
     
   - `:set hlsearch` (highlight all matches)  
   - `/ <enter>` without pattern repeats last search  
   - `:nohlsearch` (clear highlights temporarily)  
   - `<leader>` \+ mapping to clear highlights (advanced, skip for now)  
   - Why highlight: Visual feedback, error detection  
   - Exercise: Search 20 patterns with highlighting

   

2. **Search History & Recall** (25 min) — **PRACTICE HEAVY**  
     
   - `/` then `up arrow` (previous searches)  
   - `?` then `up arrow` (previous backward searches)  
   - `:history /` (view search history)  
   - Grep search: `/pattern` shows matches in real-time  
   - Exercise: Recall and reuse previous searches

   

3. **Search Settings** (30 min)  
     
   - `:set ignorecase` (case-insensitive search)  
   - `:set smartcase` (case-sensitive if uppercase in pattern)  
   - `:set incsearch` (incremental search \- show matches while typing)  
   - `:set wrapscan` (wrap search at end of file)  
   - `:set wildmenu` (command mode autocomplete)  
   - Why smartcase: Usually ignore case, but allow override  
   - Add to `.vimrc` for persistence

   

4. **Advanced Search Patterns** (35 min) — **PRACTICE HEAVY**  
     
   - Magic mode: `:set magic` (default, regex on)  
   - Very magic: `/\v(pattern)` (Perl-like regex)  
   - No magic: `/\Mpattern` (literal pattern)  
   - Escape: `\*` to search literal `*`  
   - Word boundary: `/\<word\>` or `/\bword\b`  
   - Exercise: Search 10 complex patterns

   

5. **Combining Search with Editing** (20 min)  
     
   - Search then modify all matches: `/pattern` then `:%s///g` (replace all matches)  
   - Search, navigate, edit: `/pattern` \+ `n` to next \+ `ce` to change word  
   - Find error, fix across file

### Resources

- **Cheat Sheet:** Search section of [Vim Cheatsheet](https://vim.rtorr.com/)  
- **Advanced:** [VIM Regex Detailed](https://vimregex.com/)

### Practice Exercises (45 min)

1. Search with highlighting enabled (10 min)  
2. Recall previous searches using history (5 min)  
3. Configure search settings (5 min)  
4. Write 10 complex regex patterns (10 min)  
5. Search and replace all matches (10 min)  
6. Combine search navigation with editing (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Use highlighting productively  
- [ ] Recall search history  
- [ ] Know `ignorecase`, `smartcase`, `incsearch`  
- [ ] Write regex patterns for common scenarios  
- [ ] Search and navigate efficiently  
- [ ] Combine search with replace  
- **Speed Test:** Find and replace 10 patterns in a file in 4 minutes

---

## **SESSION 17: Advanced Replace & Text Transformations** (3 hours)

### Objectives

- Use advanced replace features  
- Transform text with regex and capture groups  
- Batch edit complex patterns  
- Master multi-step transformations

### Content (2h 45min)

1. **Capture Groups & Backreferences** (50 min) — **PRACTICE HEAVY**  
     
   - Capture: `\(pattern\)` creates group 1, `\(pattern1\)\(pattern2\)` groups 1 and 2  
   - Backreference: `\1`, `\2` refer to groups in replacement  
   - Example: `:%s/\(foo\)\(bar\)/\2\1/g` (swap foo and bar)  
   - Complex example: `:%s/\([0-9]\+\)-\([0-9]\+\)/$\1 - $\2/g` (format number ranges)  
   - Exercise: Write 10 capture group replacements

   

2. **Advanced Replace Flags** (30 min) — **PRACTICE HEAVY**  
     
   - `/g` (global all matches on line)  
   - `/I` (ignore case), `/i` (force case-sensitive)  
   - `/c` (confirm each replacement)  
   - `/e` (execute as command, advanced)  
   - Example: `:%s/\(.*\)/echo \1/e` (very advanced, skip)  
   - Exercise: Replace using different flags

   

3. **Multi-Step Transformations** (45 min) — **PRACTICE HEAVY**  
     
   - Use multiple `:s` commands sequentially  
   - Example: Convert format:  
     1. `:%s/,/ | /g` (replace commas with pipes)  
     2. `:%s/^\(.*\)$/Table: \1/` (add prefix)  
   - Real-world: Convert CSV to HTML table (3-4 steps)  
   - Exercise: Multi-step transformation of data

   

4. **Special Replacement Sequences** (20 min)  
     
   - `&` in replacement \= entire match  
   - Example: `:%s/foo/[&]/g` (wrap matches in brackets)  
   - `\L` (lowercase), `\U` (uppercase) in replacement  
   - Example: `:%s/\(.*\)/\U\1/g` (uppercase everything)  
   - Function names: Advanced, skip

### Resources

- **Guide:** [VIM Regex & Replace Advanced](https://vim.fandom.com/wiki/Search_and_replace)  
- **Test Tool:** [Regex 101](https://regex101.com/) for testing patterns

### Practice Exercises (45 min)

1. Write 5 capture group replacements (10 min)  
2. Use replace with confirmation flag (5 min)  
3. Multi-step transformation (10 min)  
4. Use special sequences (`&`, `\L`, `\U`) (10 min)  
5. Complex real-world transformation (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Understand capture groups (`\1`, `\2`)  
- [ ] Write complex replacements with backreferences  
- [ ] Know replace flags (`g`, `i`, `c`)  
- [ ] Use `&` and case-changing sequences  
- [ ] Perform multi-step transformations  
- [ ] Test patterns before applying widely  
- **Speed Test:** Multi-step transformation of data in 3 minutes

---

## **SESSION 18: Configuration (.vimrc) & Essential Settings** (3 hours)

### Objectives

- Create effective `.vimrc` configuration  
- Customize VIM to match workflow  
- Set up key bindings  
- Understand plugin system basics

### Content (2h 45min)

1. **Understanding .vimrc** (15 min)  
     
   - Location: `~/.vimrc` (Unix/Linux/macOS), `%USERPROFILE%\_vimrc` (Windows)  
   - When loaded: On startup  
   - Syntax: VIM command language  
   - Backup: Edit incrementally, keep working copy

   

2. **Essential Settings** (60 min)  
     
   - **Appearance:**  
     - `:set number` (show line numbers)  
     - `:set relativenumber` (relative line numbers)  
     - `:set ruler` (show cursor position)  
     - `:set cursorline` (highlight cursor line)  
   - **Indentation:**  
     - `:set tabstop=4`, `:set shiftwidth=4`, `:set expandtab`  
   - **Search:**  
     - `:set ignorecase smartcase incsearch`  
   - **Behavior:**  
     - `:set backspace=indent,eol,start` (backspace behavior)  
     - `:set mouse=a` (enable mouse)  
     - `:set clipboard=unnamed` (use system clipboard)  
   - Exercise: Build a `.vimrc` with 15 settings

   

3. **Key Mappings** (45 min) — **PRACTICE HEAVY**  
     
   - `nnoremap <key> <command>` (normal mode mapping)  
   - `inoremap <key> <command>` (insert mode)  
   - `vnoremap <key> <command>` (visual mode)  
   - Example: `nnoremap <leader>w :w<enter>` (map leader+w to save)  
   - Leaderkey: `:let mapleader = ","` (use comma as leader)  
   - Common mappings:  
     - `nnoremap <leader>w :w<enter>` (save)  
     - `inoremap jk <Esc>` (exit insert mode)  
     - `nnoremap ; :` (semicolon for command mode)  
   - Exercise: Create 5 mappings

   

4. **Color Scheme & Themes** (15 min)  
     
   - `:colorscheme default` (built-in)  
   - Install custom: Drop `.vim` file in `~/.vim/colors/`  
   - Popular: `monokai`, `dracula`, `gruvbox`  
   - Set: `:colorscheme monokai` in `.vimrc`  
   - Try: `:colorscheme <tab>` to browse installed

   

5. **Plugin Management (Brief Overview)** (10 min)  
     
   - Plugin manager: `vim-plug` (simple)  
   - Basic plugins: Syntax highlighting, themes, fuzzy finder  
   - Skip for now: Plugins not in 80/20 core

### Resources

- **Guide:** [A Good VIM .vimrc](https://dougblack.io/words/a-good-vimrc.html)  
- **Starter:** [Vim Bootstrap](http://vim-bootstrap.com/) (generate .vimrc)  
- **Plugin Manager:** [Vim-plug](https://github.com/junegunn/vim-plug)

### Practice Exercises (45 min)

1. Create `.vimrc` with 20 settings (15 min)  
2. Test each setting in VIM (10 min)  
3. Create 5 key mappings (10 min)  
4. Choose and install color scheme (10 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Locate and edit `.vimrc`  
- [ ] Know 15+ essential settings  
- [ ] Configure indentation style  
- [ ] Set up search preferences  
- [ ] Create helpful key mappings  
- [ ] Choose comfortable color scheme  
- [ ] Understand syntax: `:set`, `nnoremap`, `let`  
- **Completion Test:** Create functional `.vimrc` with 20 settings

---

## **SESSION 19: Speed & Workflow Optimization** (3 hours)

### Objectives

- Develop muscle memory for common tasks  
- Build efficient workflows  
- Eliminate inefficiencies  
- Reach expert-level speed (\>2x normal editor speed)

### Content (2h 45min)

1. **Speed Drills** (45 min) — **PRACTICE HEAVY**  
     
   - Navigation drill: Jump to 20 random lines in 2 minutes  
   - Text object drill: Edit 20 text objects in 2 minutes  
   - Operator+motion drill: 30 edits in 3 minutes  
   - Macro drill: Record and run 5 different macros  
   - Focus: Accuracy \> speed initially, then speed increases naturally  
   - Track: Time yourself weekly, goal is 20% improvement each week

   

2. **Workflow Patterns** (50 min) — **PRACTICE HEAVY**  
     
   - Pattern 1: Search → Edit → Repeat  
     - `/pattern`, `n`, `cw`, `Esc`, `n` (repeat)  
   - Pattern 2: Mark → Navigate → Edit  
     - `mm` (mark middle), `gg`, edit, `` `m `` (return)  
   - Pattern 3: Macro → Repeat  
     - `qaciw<newword><esc>j0q` (record), `@a` (run), `10@a` (repeat 10x)  
   - Pattern 4: Split windows  
     - `:vsp filename` (open related file), `ctrl+w` to switch  
   - Pattern 5: Multiple files  
     - `:args file1 file2 file3`, `:argdo %s/old/new/`  
   - Exercise: Practice each pattern 10 times

   

3. **Error Recovery & Undo** (30 min) — **PRACTICE HEAVY**  
     
   - `u` (undo), `ctrl+r` (redo)  
   - `.` (repeat last edit)  
   - Undo tree visualization: `:undolist`  
   - Persistent undo: `:set undodir=~/.vim/undo` (advanced)  
   - Why important: Mistakes happen, quick recovery is key  
   - Exercise: Deliberately make 20 mistakes, undo all

   

4. **Common Tasks Speed Challenge** (30 min) — **PRACTICE HEAVY**  
     
   - Task 1: Find and replace 20 patterns in a file (time: \<2 min)  
   - Task 2: Edit 10 text objects in a file (time: \<2 min)  
   - Task 3: Format messy code (indent, spacing) (time: \<3 min)  
   - Task 4: Extract data from file using regex (time: \<3 min)  
   - Task 5: Multi-file editing workflow (time: \<5 min)  
   - Goal: Sub-5-minute completion per task

### Resources

- **Challenge:** Create speed-test files for practice  
- **Video:** [VIM Expert Level](https://www.youtube.com/watch?v=MquaityA1SM) (15 min)

### Practice Exercises (45 min)

1. Speed navigation drill (5 min)  
2. Text object speed drill (5 min)  
3. Operator+motion speed drill (5 min)  
4. Practice each workflow pattern (10 min)  
5. 5-task challenge (20 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Complete navigation drill in 2 minutes  
- [ ] Complete text object drill in 2 minutes  
- [ ] Execute 30 edits in 3 minutes  
- [ ] Know 5+ workflow patterns  
- [ ] Recover from mistakes quickly  
- [ ] Complete common tasks \< 5 minutes each  
- **Speed Test:** Complete all 5 common tasks in under 20 minutes

---

## **SESSION 20: Integration & Mastery Consolidation** (3 hours)

### Objectives

- Integrate all skills into cohesive practice  
- Build real-world editing workflows  
- Solve complex problems efficiently  
- Achieve true VIM mastery

### Content (2h 45min)

1. **Real-World Project Editing** (60 min) — **PRACTICE HEAVY**  
     
   - Scenario 1: Debug code file  
     - Find function, navigate to error, fix using text objects  
     - Search for similar errors, replace all  
   - Scenario 2: Refactor variable name  
     - Search across multiple files using grep  
     - Replace using quickfix list  
   - Scenario 3: Format configuration file  
     - Navigate sections, indent, align values  
     - Search and replace patterns  
   - Scenario 4: Extract data from log file  
     - Search pattern, copy relevant lines, format in new file  
   - Exercise: Complete each scenario

   

2. **Advanced Workflow Integration** (40 min) — **PRACTICE HEAVY**  
     
   - Combine: Splits \+ Buffers \+ Search \+ Replace  
   - Example: Open function in split, search for calls, replace in quickfix  
   - Workflow: Open test and source files in splits, sync edits  
   - Multi-file: Load 10 files, use argument list to refactor  
   - Exercise: Complete integrated workflow

   

3. **Mastery Checklist** (15 min)  
     
   - Can achieve 2x speed of normal editors for text editing  
   - Rarely use mouse  
   - Keyboard-only workflows feel natural  
   - Can edit code, configuration, prose efficiently  
   - Problem-solving is faster: Think in VIM motions  
   - Confident with any file type (code, config, text, logs)

   

4. **Continuous Improvement** (20 min)  
     
   - Identify weak areas: Use `:verbose` to log commands  
   - Learn one new command per week: Don't stop improving  
   - Join community: Share tips, learn from others  
   - Practice areas: Speed drills 10 min/week  
   - Extend: Learn language-specific plugins after mastery  
   - Philosophy: VIM is a lifestyle, not a tool

### Resources

- **Community:** Reddit r/vim, VIM subreddit  
- **Advanced:** Once master basics, explore plugins (LuaSnip, LSP, nvim)  
- **Continued Learning:** [VIM Tips Wiki](https://vim.fandom.com/wiki/Vim_Tips_Wiki)

### Practice Exercises (45 min)

1. Real-world code debugging scenario (15 min)  
2. Multi-file refactoring scenario (15 min)  
3. Data extraction and formatting (10 min)  
4. Assess mastery checklist, identify improvements (5 min)

### ⏱️ 15-Minute Session Review Checklist

- [ ] Complete real-world scenarios confidently  
- [ ] Integrate multiple VIM skills seamlessly  
- [ ] Problem-solve faster than non-VIM users  
- [ ] Keyboard-only workflows are natural  
- [ ] Work with any file type comfortably  
- [ ] Achieve 2x+ speed on typical editing tasks  
- [ ] Know next steps for continued learning  
- **Final Test:** Complete 3 scenarios in under 20 minutes

---

# 🎓 MASTERY SUMMARY

## You Now Know:

✅ Modal editing philosophy and practice  
✅ The grammar of VIM: Operator \+ Motion  
✅ Semantic editing with text objects  
✅ Navigation and jumping efficiently  
✅ Repetition with `.` and macros  
✅ Search, replace, and regex  
✅ Buffers, windows, tabs, and workflows  
✅ Configuration and customization  
✅ Real-world problem-solving

## You Can Do:

✅ Edit 2-3x faster than non-VIM users  
✅ Navigate large files in seconds  
✅ Perform complex text transformations  
✅ Work on multiple files simultaneously  
✅ Automate repetitive tasks with macros  
✅ Search and replace across projects  
✅ Configure VIM for any workflow

## Next Steps After 60 Hours:

- Learn plugins: NeoVim, LSP, fuzzy finder (fzf)  
- Master one language's ecosystem plugin  
- Explore advanced regex and scripting  
- Contribute to VIM community  
- Teach others (accelerates your learning)

---

# 📊 PROGRESS TRACKING

Create a spreadsheet to track:

- Session completion date  
- Time spent (actual vs 3 hours)  
- Topics mastered (0-100%)  
- Speed improvements  
- Weak areas to revisit

**Weekly Goal:** 3 sessions (9 hours)  
**Milestone 1:** Sessions 1-5 (15 hours) \= Confident with fundamentals  
**Milestone 2:** Sessions 6-10 (15 hours) \= Productive for daily work  
**Milestone 3:** Sessions 11-15 (15 hours) \= Advanced workflows mastered  
**Milestone 4:** Sessions 16-20 (15 hours) \= Expert-level mastery

---

# ⚡ THE 80/20 ESSENTIALS (Cheatsheet)

| Category | 20% That Drives 80% |
| :---- | :---- |
| **Navigation** | hjkl, w/b/e, j/k, \*, / |
| **Editing** | d, c, y, i, a, o |
| **Text Objects** | iw, aw, i(, i{, i", is, ip |
| **Operators** | d, c, y, \>, \<, \= |
| **Search** | /pattern, ?, n, N, \* |
| **Replace** | :%s/old/new/g, capture groups |
| **Buffers** | :split, :vsplit, ctrl+w, :buffer |
| **Config** | `:set` essentials, key mappings |
| **Workflow** | Marks, macros, quickfix, arglist |

---

**You have everything needed. Start with Session 1, practice daily, and master VIM in 20 weeks (3 sessions/week).**