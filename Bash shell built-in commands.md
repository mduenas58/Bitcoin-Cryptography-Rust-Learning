Here is a comprehensive list of Bash shell built-in commands. These are commands that are executed directly by the shell itself, without needing to call an external program .

You can get a complete list on your own system at any time by running the command `help` in your terminal .

| Command | Description |
| :--- | :--- |
| `:` | Null command, does nothing and returns a success (0) exit status . |
| `.` (period) | Reads and executes commands from a file in the current shell environment (synonym for `source`) . |
| `[` | Evaluate a conditional expression; synonym for the `test` builtin . |
| `[[ ... ]]` | Execute a conditional command (more advanced than `[` or `test`) . |
| `alias` | Create or display command aliases . |
| `bg` | Resume a suspended job and run it in the background . |
| `bind` | Display and manage Readline (command-line editing) key bindings . |
| `break` | Exit from a `for`, `while`, `until`, or `select` loop . |
| `builtin` | Execute a shell built-in command, useful when you have a function with the same name . |
| `caller` | Display the context of any active subroutine call (function or sourced script) for debugging . |
| `case` | Execute commands based on pattern matching (a reserved word) . |
| `cd` | Change the current working directory . |
| `command` | Execute a command, bypassing any shell function of the same name . |
| `compgen` | Generate possible completion matches for a word, used by programmable completion . |
| `complete` | Specify how arguments to a command should be auto-completed . |
| `compopt` | Modify or display completion options for a command . |
| `continue` | Resume the next iteration of a `for`, `while`, `until`, or `select` loop . |
| `coproc` | Create a coprocess (a background process with a two-way pipe to the shell) . |
| `declare` | Declare variables and set their attributes (e.g., integer, readonly, array) . |
| `dirs` | Display the list of currently remembered directories (directory stack) . |
| `disown` | Remove a job from the shell's job table, so it is not terminated when the shell exits . |
| `echo` | Write arguments to the standard output . |
| `enable` | Enable or disable shell built-in commands . |
| `eval` | Concatenate arguments into a single command and execute it . |
| `exec` | Replace the shell process with a given command . |
| `exit` | Exit the shell with an optional exit status . |
| `export` | Create or modify environment variables, making them available to child processes . |
| `false` | Do nothing, but return a non-zero (failure) exit status . |
| `fc` | Display, edit, or re-execute commands from the history list . |
| `fg` | Bring a background or suspended job to the foreground . |
| `for` | Execute commands for each item in a list (a reserved word) . |
| `function` | Define a shell function (a reserved word) . |
| `getopts` | Parse positional parameters (command-line options) for a script . |
| `hash` | Remember or display the full pathnames of commands to avoid repeated PATH lookups . |
| `help` | Display help information about shell built-in commands . |
| `history` | Display or manipulate the command history list . |
| `if` | Execute commands based on a conditional result (a reserved word) . |
| `jobs` | Display the status of jobs running in the current shell session . |
| `kill` | Send a signal to a process or job . |
| `let` | Perform arithmetic evaluation . |
| `local` | Define a variable that is local to a function . |
| `logout` | Exit a login shell . |
| `mapfile` | Read lines from standard input into an indexed array variable . |
| `popd` | Remove an entry from the directory stack and change to that directory . |
| `printf` | Format and print data (similar to C's `printf`) . |
| `pushd` | Add a directory to the directory stack and change to it . |
| `pwd` | Print the current working directory's full pathname . |
| `read` | Read a line from standard input and split it into fields for assignment to variables . |
| `readarray` | Read lines from standard input into an array variable; synonym for `mapfile` . |
| `readonly` | Mark specified variables as read-only, preventing their value from being changed . |
| `return` | Exit a shell function, optionally providing an exit status . |
| `select` | Generate a simple menu system from a list of words (a reserved word) . |
| `set` | Set or unset shell options and positional parameters . |
| `shift` | Shift positional parameters down by a specified number (default is 1) . |
| `shopt` | Set and unset shell options that control the behavior of the shell . |
| `source` | Read and execute commands from a file in the current shell environment . |
| `suspend` | Suspend the current shell (send a SIGSTOP signal) . |
| `test` | Evaluate a conditional expression; synonym for `[` . |
| `time` | Report the time consumed by a command's execution (a reserved word) . |
| `times` | Display the accumulated user and system CPU times for the shell and its children . |
| `trap` | Set a command to be executed when a signal or other event is received . |
| `true` | Do nothing, but return a zero (success) exit status . |
| `type` | Indicate how a command name would be interpreted if used (e.g., builtin, alias, function, file) . |
| `typeset` | Set variable values and attributes; synonym for `declare` . |
| `ulimit` | Get or set the resource limits of the shell and processes it creates . |
| `umask` | Set or display the file mode creation mask (permissions for new files/directories) . |
| `unalias` | Remove an alias definition . |
| `unset` | Remove a variable or function, deleting its value and attributes . |
| `until` | Execute commands as long as a test condition is false (a reserved word) . |
| `variables` | Display common shell variable names and their usage . |
| `wait` | Wait for a background process to finish and report its exit status . |
| `while` | Execute commands as long as a test condition is true (a reserved word) . |
| `{ ... }` | Group commands together as a unit (a reserved word) . |

I hope this comprehensive list is helpful for your work with Bash. Are you interested in learning more about a specific command or how to use them effectively in a script?