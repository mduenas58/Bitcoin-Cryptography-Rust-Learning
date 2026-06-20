# Module 1 – Python Basics

## Hands-On Exercises

> **About this module**
>
> This module introduces the core building blocks of Python programming. Each topic is accompanied
> by three progressive exercises: the first builds familiarity, the second adds complexity, and
> the third challenges you to apply the concept in a realistic scenario.
>
> Work through the starter code, predict the expected output before running, then check your
> solution against the provided answer.


### Topics Covered

| # | Topic | Key Concept |
|---|-------|-------------|
| 1 | Print Function | `print()`, `sep`, `end`, f-strings, escape sequences |
| 2 | Literals | Numeric (`int`, `float`, `complex`), string, boolean, `None` |
| 3 | Operators | Arithmetic, comparison, logical, augmented assignment |
| 4 | Variables | Assignment, dynamic typing, multiple assignment, type conversion |
| 5 | Comments | Single-line (`#`), docstrings, commenting best practices |
| 6 | Input | `input()`, type conversion, interactive programs |
| 7 | String Methods | Case, strip, find, replace, split, join, `isdigit`, `count` |


### How to Use These Exercises

1. **Read the Explanation** carefully — understand the concept before writing code.
2. **Fill in the blanks** (`_____`) in the Starter Code without looking at the Solution.
3. **Predict the Expected Output** — write your guess on paper first.
4. **Run your code** in Python (IDLE, VS Code, or [python.org/shell](https://www.python.org/shell/)).
5. **Compare with the Solution** only after attempting the exercise yourself.


---


## Topic 1: Print Function

The `print()` function is the primary way to display output in Python. It can accept multiple values, format data, and control line endings — making it an essential tool for debugging and communicating results to the user.

### Exercise 1.1 — Hello World & Print Arguments


**🎯 Objective**

Use the `print()` function with multiple arguments and the `sep` parameter.

**📖 Explanation**

The `print()` function outputs text to the screen. You can pass multiple values separated by commas. The `sep` parameter controls what goes between them (default is a space) and `end` controls what is printed at the end (default is a newline `\n`).

**📝 Task**

Complete the starter code to produce the expected output:

- Print your full name using two separate string arguments.
- Print the same name but separated by a hyphen using `sep`.
- Print three numbers on the same line separated by `" | "` using `sep`.

**💻 Starter Code**

```python
# Exercise 1.1 – Print Arguments

# 1. Print first and last name (two arguments)
print(_____, _____)

# 2. Print first and last name separated by " - "
print(_____, _____, sep=_____)

# 3. Print 10, 20, 30 separated by " | " on one line
print(_____, _____, _____, sep=_____)
```

**✅ Expected Output**

```text
John Doe
John - Doe
10 | 20 | 30
```

**💡 Hint**

Each comma-separated value inside `print()` becomes an argument. Combine `sep="..."` with multiple arguments to control spacing.

**🔑 Solution**

```python
print("John", "Doe")
print("John", "Doe", sep=" - ")
print(10, 20, 30, sep=" | ")
```


### Exercise 1.2 — F-Strings & Formatted Output


**🎯 Objective**

Use f-strings (formatted string literals) inside `print()` to embed variables.

**📖 Explanation**

An f-string is a string prefixed with `f"..."` that lets you embed Python expressions inside curly braces `{}`. This makes `print()` output dynamic without manual concatenation.

**📝 Task**

Fill in the blanks to produce the expected output:

- Declare variables for a product name, price, and quantity.
- Use an f-string to print a formatted receipt line.
- Print the total (`price * quantity`) also using an f-string.

**💻 Starter Code**

```python
# Exercise 1.2 – F-Strings

product  = _____
price    = _____
quantity = _____

print(f"Product : {_____}")
print(f"Price   : ${_____:.2f}")
print(f"Qty     : {_____}")
print(f"Total   : ${_____:.2f}")
```

**✅ Expected Output**

```text
Product : Widget
Price   : $4.99
Qty     : 3
Total   : $14.97
```

**💡 Hint**

Use `:.2f` inside curly braces to format a float to 2 decimal places. Example: `{price:.2f}`.

**🔑 Solution**

```python
product  = "Widget"
price    = 4.99
quantity = 3

print(f"Product : {product}")
print(f"Price   : ${price:.2f}")
print(f"Qty     : {quantity}")
print(f"Total   : ${price * quantity:.2f}")
```


### Exercise 1.3 — Escape Sequences & the `end` Parameter


**🎯 Objective**

Use escape sequences (`\n`, `\t`) and the `end` parameter to control `print()` output formatting.

**📖 Explanation**

Escape sequences are special characters in strings: `\n` inserts a newline, `\t` inserts a tab. The `end` parameter replaces the default newline at the end of `print()`, allowing you to keep the cursor on the same line.

**📝 Task**

Write `print()` statements to produce the exact output shown:

- Print a 2-column table header with a tab between columns.
- Print two rows of data using `\t` for alignment.
- Print `"Loading"` followed by three dots on the same line using `end`.

**💻 Starter Code**

```python
# Exercise 1.3 – Escape Sequences

# 1. Print header with tab separation
print(___________)

# 2. Print two data rows
print(___________)
print(___________)

# 3. Print "Loading..." staying on one line
print("Loading", end=_____)
print(".", end=_____)
print(".", end=_____)
print(".")
```

**✅ Expected Output**

```text
Name\t\tScore
Alice\t\t95
Bob\t\t\t87
Loading...
```

**💡 Hint**

`\t` moves to the next tab stop (usually 8 spaces). Use extra `\t` for shorter names to keep columns aligned.

**🔑 Solution**

```python
print("Name\t\tScore")
print("Alice\t\t95")
print("Bob\t\t\t87")
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".")
```



---


## Topic 2: Literals

A literal is a value written directly in the code. Python supports numeric literals (`int`, `float`, `complex`), string literals (single, double, or triple-quoted), boolean literals (`True`/`False`), and the `None` literal. Understanding literals is the foundation of working with data in Python.

### Exercise 2.1 — Numeric Literals


**🎯 Objective**

Identify and use integer, float, and complex number literals in Python.

**📖 Explanation**

A **literal** is a fixed value written directly in the code. Python supports several numeric literal types: `int` (whole numbers), `float` (decimal numbers), and `complex` (real + imaginary part, e.g. `3+2j`). The `type()` function returns the data type of any value.

**📝 Task**

Complete each line to create the specified literal and verify its type:

- Create an integer literal representing the year 2024.
- Create a float literal representing pi (3.14159).
- Create a complex literal `4+3j` and print both its real and imaginary parts.

**💻 Starter Code**

```python
# Exercise 2.1 – Numeric Literals

year = _____
print(year, type(year))

pi = _____
print(pi, type(pi))

z = _____
print(z.real, z.imag, type(z))
```

**✅ Expected Output**

```text
2024 <class 'int'>
3.14159 <class 'float'>
4.0 3.0 <class 'complex'>
```

**💡 Hint**

Python automatically determines the type based on how you write the literal. A decimal point makes it a `float`; the `j` suffix makes it `complex`.

**🔑 Solution**

```python
year = 2024
print(year, type(year))

pi = 3.14159
print(pi, type(pi))

z = 4+3j
print(z.real, z.imag, type(z))
```


### Exercise 2.2 — String Literals & Escape Sequences


**🎯 Objective**

Work with single-quoted, double-quoted, and triple-quoted string literals.

**📖 Explanation**

String literals can be enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`""" """` or `''' '''`). Triple-quoted strings span multiple lines. They support escape sequences such as `\'` (apostrophe), `\n` (newline), and `\\` (backslash).

**📝 Task**

Fill in the correct string literal for each situation:

- Create a string containing an apostrophe: `It's Python!`
- Create a string containing double quotes: `He said "Hello".`
- Create a multi-line string (haiku) using triple quotes.

**💻 Starter Code**

```python
# Exercise 2.2 – String Literals

# 1. Contains an apostrophe
msg1 = _____
print(msg1)

# 2. Contains double quotes
msg2 = _____
print(msg2)

# 3. Multi-line haiku
haiku = _____
print(haiku)
```

**✅ Expected Output**

```text
It's Python!
He said "Hello".
An old silent pond
A frog jumps into the pond
Splash! Silence again.
```

**💡 Hint**

For apostrophes, wrap in double quotes: `"It's Python!"`. For double quotes inside, wrap in single quotes: `'He said "Hello".'`. Triple quotes start and end with three quote characters.

**🔑 Solution**

```python
msg1 = "It's Python!"
print(msg1)

msg2 = 'He said "Hello".'
print(msg2)

haiku = """An old silent pond
A frog jumps into the pond
Splash! Silence again."""
print(haiku)
```


### Exercise 2.3 — Boolean & None Literals


**🎯 Objective**

Understand and use boolean (`True`/`False`) and `None` literals in Python.

**📖 Explanation**

Python has exactly two boolean literals: `True` and `False` (capitalisation matters). `None` is a special literal representing the absence of a value — similar to `null` in other languages. Boolean values are the result of comparisons and logical expressions.

**📝 Task**

Complete the code and predict the output before running it:

- Assign `True` to `is_raining` and `False` to `is_sunny`.
- Print the result of: `is_raining and is_sunny`, `is_raining or is_sunny`, `not is_raining`.
- Assign `None` to `result` and print both its value and type.

**💻 Starter Code**

```python
# Exercise 2.3 – Boolean & None

is_raining = _____
is_sunny   = _____

print(is_raining and is_sunny)
print(is_raining or  is_sunny)
print(not is_raining)

result = _____
print(result, type(result))
```

**✅ Expected Output**

```text
False
True
False
None <class 'NoneType'>
```

**💡 Hint**

`and` returns `True` only if **both** sides are True. `or` returns `True` if **at least one** side is True. `not` flips the boolean value.

**🔑 Solution**

```python
is_raining = True
is_sunny   = False

print(is_raining and is_sunny)   # False
print(is_raining or  is_sunny)   # True
print(not is_raining)            # False

result = None
print(result, type(result))      # None <class 'NoneType'>
```



---


## Topic 3: Operators

Operators are symbols that perform operations on values and variables. Python includes arithmetic operators for maths, comparison operators that produce `True`/`False`, logical operators to combine conditions, and augmented assignment operators as a shorthand for updating variables.

### Exercise 3.1 — Arithmetic Operators


**🎯 Objective**

Apply all seven arithmetic operators in Python to solve a real-world problem.

**📖 Explanation**

Python arithmetic operators: `+` (add), `-` (subtract), `*` (multiply), `/` (true division → float), `//` (floor division → int), `%` (modulo/remainder), `**` (exponentiation). Operator precedence follows PEMDAS/BODMAS.

**📝 Task**

A baker made 100 cupcakes. Use arithmetic operators to answer:

- How many full boxes of 12 can be packed? (use `//`)
- How many cupcakes are left over? (use `%`)
- If each cupcake sells for $2.50, what is the total revenue? (use `*`)
- What is 2 to the power of 8? (use `**`)

**💻 Starter Code**

```python
# Exercise 3.1 – Arithmetic Operators

total_cupcakes = 100
box_size       = 12
price_each     = 2.50

full_boxes  = _____
leftover    = _____
revenue     = _____
power_of_2  = _____

print(f"Full boxes : {full_boxes}")
print(f"Leftover   : {leftover}")
print(f"Revenue    : ${revenue:.2f}")
print(f"2^8        : {power_of_2}")
```

**✅ Expected Output**

```text
Full boxes : 8
Leftover   : 4
Revenue    : $250.00
2^8        : 256
```

**💡 Hint**

`//` performs integer (floor) division — no remainder. `%` gives only the remainder. `**` is right-associative: `2**8` means 2 multiplied by itself 8 times.

**🔑 Solution**

```python
total_cupcakes = 100
box_size       = 12
price_each     = 2.50

full_boxes  = total_cupcakes // box_size
leftover    = total_cupcakes % box_size
revenue     = total_cupcakes * price_each
power_of_2  = 2 ** 8

print(f"Full boxes : {full_boxes}")
print(f"Leftover   : {leftover}")
print(f"Revenue    : ${revenue:.2f}")
print(f"2^8        : {power_of_2}")
```


### Exercise 3.2 — Comparison & Logical Operators


**🎯 Objective**

Use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) and logical operators (`and`, `or`, `not`) to evaluate conditions.

**📖 Explanation**

Comparison operators compare two values and return a boolean (`True` or `False`). Logical operators combine boolean expressions: `and` (both must be True), `or` (at least one True), `not` (inverts). These are the building blocks of decision-making in code.

**📝 Task**

A website requires users to be aged 13–120 and to have accepted the terms. Write conditions to validate:

- Check if `age` is within the valid range (13 to 120 inclusive).
- Check if the user accepted terms **AND** is old enough.
- Check if the user is **NOT** eligible (either underage OR did not accept terms).

**💻 Starter Code**

```python
# Exercise 3.2 – Comparison & Logical

age            = 17
accepted_terms = True

# 1. Is age valid?
valid_age = (age >= _____) and (age <= _____)

# 2. Can register?
can_register = valid_age _____ accepted_terms

# 3. Not eligible?
not_eligible = _____ valid_age _____ _____ accepted_terms

print(f"Valid age    : {valid_age}")
print(f"Can register : {can_register}")
print(f"Not eligible : {not_eligible}")
```

**✅ Expected Output**

```text
Valid age    : True
Can register : True
Not eligible : False
```

**💡 Hint**

De Morgan's law: `not (A and B) == (not A) or (not B)`. "Not eligible" means: invalid age OR did not accept terms.

**🔑 Solution**

```python
valid_age    = (age >= 13) and (age <= 120)
can_register = valid_age and accepted_terms
not_eligible = (not valid_age) or (not accepted_terms)

print(f"Valid age    : {valid_age}")
print(f"Can register : {can_register}")
print(f"Not eligible : {not_eligible}")
```


### Exercise 3.3 — Augmented Assignment Operators


**🎯 Objective**

Use augmented assignment operators (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`) to update variables in place.

**📖 Explanation**

Augmented assignment operators are a shorthand that combines an arithmetic operation with assignment. For example, `x += 5` is equivalent to `x = x + 5`. They make code shorter and more readable when updating a variable based on its current value.

**📝 Task**

A game tracks a player's score. Simulate 5 game events using only augmented assignment operators:

- Start with `score = 100`.
- Event 1: Collect a coin — add 25 points.
- Event 2: Hit an enemy — subtract 15 points.
- Event 3: Bonus multiplier — multiply by 2.
- Event 4: Share with partner — floor-divide by 2.
- Event 5: Bonus round — raise to the power of 1 (verify with `**`).

**💻 Starter Code**

```python
# Exercise 3.3 – Augmented Assignment

score = 100
print(f"Start  : {score}")

score _____   # +25
print(f"Coin   : {score}")

score _____   # -15
print(f"Hit    : {score}")

score _____   # x2
print(f"Bonus  : {score}")

score _____   # //2
print(f"Share  : {score}")

score _____   # **1
print(f"Final  : {score}")
```

**✅ Expected Output**

```text
Start  : 100
Coin   : 125
Hit    : 110
Bonus  : 220
Share  : 110
Final  : 110
```

**💡 Hint**

Each augmented operator modifies the variable and stores the result back. `score += 25` means `score = score + 25`.

**🔑 Solution**

```python
score = 100
print(f"Start  : {score}")
score += 25
print(f"Coin   : {score}")
score -= 15
print(f"Hit    : {score}")
score *= 2
print(f"Bonus  : {score}")
score //= 2
print(f"Share  : {score}")
score **= 1
print(f"Final  : {score}")
```



---


## Topic 4: Variables

Variables are named containers that store values in memory. Python is **dynamically typed**, meaning a variable can hold any type and its type can change. Mastering variable assignment, naming conventions, multiple assignment, and type conversion is essential for writing any Python program.

### Exercise 4.1 — Variable Assignment & Dynamic Typing


**🎯 Objective**

Assign values of different types to variables and observe Python's dynamic typing.

**📖 Explanation**

In Python, a variable is a named reference to a value in memory. Variables are **dynamically typed** — the same variable can hold different types at different times. Use `type()` to inspect the current type. Variable names must start with a letter or `_`, and are case-sensitive.

**📝 Task**

Create and reassign variables, checking `type()` at each step:

- Create a variable called `data` and assign the integer `42`.
- Reassign `data` to the float `3.14` and print its new type.
- Reassign `data` to the string `"Python"` and print its value and type.
- Reassign `data` to `True` and print its value and type.

**💻 Starter Code**

```python
# Exercise 4.1 – Dynamic Typing

data = _____
print(data, type(data))

data = _____
print(data, type(data))

data = _____
print(data, type(data))

data = _____
print(data, type(data))
```

**✅ Expected Output**

```text
42 <class 'int'>
3.14 <class 'float'>
Python <class 'str'>
True <class 'bool'>
```

**💡 Hint**

Python is dynamically typed: you never declare the type — it is inferred from the value assigned. The type can change freely as you reassign.

**🔑 Solution**

```python
data = 42
print(data, type(data))
data = 3.14
print(data, type(data))
data = "Python"
print(data, type(data))
data = True
print(data, type(data))
```


### Exercise 4.2 — Multiple Assignment & Variable Swap


**🎯 Objective**

Use multiple assignment (`a, b = 1, 2`) and swap two variables without a temporary variable.

**📖 Explanation**

Python allows you to assign multiple variables in a single line using tuple unpacking: `a, b = 1, 2`. This also makes swapping values elegant: `a, b = b, a` — no temp variable needed. This is a uniquely Pythonic feature.

**📝 Task**

Complete the code to perform multi-assignment and swap:

- Assign `x=10`, `y=20`, `z=30` in a single line.
- Swap `x` and `y` in a single line (no temp variable).
- Assign the same value (`0`) to `a`, `b`, and `c` simultaneously.

**💻 Starter Code**

```python
# Exercise 4.2 – Multiple Assignment

# 1. Single-line multi-assignment
_____ = 10, 20, 30
print(x, y, z)

# 2. Swap x and y
_____ = _____
print("After swap:", x, y)

# 3. Same value to a, b, c
a = b = c = _____
print(a, b, c)
```

**✅ Expected Output**

```text
10 20 30
After swap: 20 10
0 0 0
```

**💡 Hint**

Tuple unpacking: `x, y, z = 10, 20, 30` reads right to left. Python evaluates the right side first, then assigns. That's why swapping works without a temp variable.

**🔑 Solution**

```python
x, y, z = 10, 20, 30
print(x, y, z)
x, y = y, x
print("After swap:", x, y)
a = b = c = 0
print(a, b, c)
```


### Exercise 4.3 — Type Conversion (Casting)


**🎯 Objective**

Convert between variable types using `int()`, `float()`, `str()`, and `bool()`.

**📖 Explanation**

Explicit type conversion (also called **casting**) lets you convert a value from one type to another using built-in functions: `int()` truncates to integer, `float()` converts to decimal, `str()` converts to string, `bool()` evaluates truthiness (`0`, `""`, `None` → `False`; anything else → `True`).

**📝 Task**

Fix and complete the code to make all conversions work correctly:

- Convert the string `"42"` to an integer and add `8`.
- Convert the integer `7` to a float.
- Convert the float `9.99` to an integer (notice what happens to the decimal).
- Convert `0` and `100` to `bool` and observe the results.

**💻 Starter Code**

```python
# Exercise 4.3 – Type Conversion

# 1. String to int
age_str = "42"
age_int = _____(age_str)
print(age_int + 8)

# 2. Int to float
num = 7
num_f = _____(num)
print(num_f)

# 3. Float to int (truncates)
price = 9.99
print(_____(price))

# 4. Int to bool
print(_____(0), _____(100))
```

**✅ Expected Output**

```text
50
7.0
9
False True
```

**💡 Hint**

`int()` on a float **truncates** (does not round): `int(9.99)` → `9`. `bool(0)` is always `False`; any non-zero number is `True`.

**🔑 Solution**

```python
age_str = "42"
age_int = int(age_str)
print(age_int + 8)         # 50
num = 7
num_f = float(num)
print(num_f)               # 7.0
price = 9.99
print(int(price))          # 9
print(bool(0), bool(100))  # False True
```



---


## Topic 5: Comments

Comments are notes in the code intended for human readers — Python ignores them entirely. Single-line comments use `#` while multi-line documentation uses triple-quoted docstrings. Good commenting habits improve code readability, collaboration, and long-term maintainability.

### Exercise 5.1 — Single-Line Comments


**🎯 Objective**

Add meaningful single-line comments to explain what code does.

**📖 Explanation**

A single-line comment starts with `#` and extends to the end of the line. Python ignores everything after `#` on that line. Comments should explain **WHY**, not just WHAT — the code itself shows what; good comments add context, intent, and clarification.

**📝 Task**

The code below has no comments and uses poor variable names. Add at least 5 meaningful `#` comments to explain what each block does:

- What does each calculation represent?
- What are the units (km, hours, km/h)?
- What is the purpose of the final `print` statement?

**💻 Starter Code**

```python
# Exercise 5.1 – Add Comments
# (Add at least 5 meaningful comments to explain the code)

d = 150
t = 2.5
v = d / t
toll = d * 0.05
fuel = d / 12.5
cost = fuel * 1.45
print(f"Speed: {v:.1f} | Toll: ${toll:.2f} | Fuel cost: ${cost:.2f}")
```

**✅ Expected Output**

```text
# Output (unchanged):
Speed: 60.0 | Toll: $7.50 | Fuel cost: $17.40
```

**💡 Hint**

Good comment: `# Distance in kilometres` (not just `# d`). Avoid: `# Divide d by t` (that is obvious from the code).

**🔑 Solution**

```python
# Distance of the trip in kilometres
d = 150
# Travel time in hours
t = 2.5
# Average speed = distance / time (km/h)
v = d / t
# Toll charge at $0.05 per km
toll = d * 0.05
# Fuel consumed assuming 12.5 km per litre
fuel = d / 12.5
# Fuel cost at $1.45 per litre
cost = fuel * 1.45
# Print trip summary in a formatted line
print(f"Speed: {v:.1f} | Toll: ${toll:.2f} | Fuel cost: ${cost:.2f}")
```


### Exercise 5.2 — Docstrings (Multi-line Comments)


**🎯 Objective**

Write a proper docstring for a function using triple quotes.

**📖 Explanation**

A **docstring** is a string literal that appears as the first statement inside a function, class, or module. It documents purpose, parameters, and return value. Access it with `help(function_name)` or `function_name.__doc__`. Docstrings follow the **PEP 257** convention.

**📝 Task**

Add a complete docstring to the function below:

- One-line summary of what the function does.
- `Args` section listing each parameter, its type, and description.
- `Returns` section describing the return value and type.
- `Raises` section if any exceptions can be raised.

**💻 Starter Code**

```python
# Exercise 5.2 – Docstrings

def calculate_bmi(weight_kg, height_m):
    """
    _____

    Args:
        _____
        _____

    Returns:
        _____

    Raises:
        _____
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero")
    return weight_kg / (height_m ** 2)

help(calculate_bmi)
```

**✅ Expected Output**

```text
Help on function calculate_bmi:

calculate_bmi(weight_kg, height_m)
    Calculate Body Mass Index (BMI).
    ...
```

**💡 Hint**

PEP 257 tip: The one-line summary should fit on one line and end with a period. Use `Args:`, `Returns:`, and `Raises:` sections for clarity.

**🔑 Solution**

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight of the person in kilograms.
        height_m  (float): Height of the person in metres.

    Returns:
        float: BMI value rounded to two decimal places.

    Raises:
        ValueError: If height_m is zero or negative.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero")
    return round(weight_kg / (height_m ** 2), 2)
```


### Exercise 5.3 — Commenting Best Practices — Refactoring


**🎯 Objective**

Identify and fix bad comments while improving code readability.

**📖 Explanation**

Bad comments either state the obvious (`# add 1 to x` before `x += 1`) or are outdated/misleading. Good comments explain intent, edge cases, and business logic. This exercise trains you to distinguish between useful and redundant comments.

**📝 Task**

The code below has 4 bad comments. Identify each problem and either remove or replace with a better comment:

- Comment A: `# set x to 5` — is it useful?
- Comment B: `# multiply` — is it clear enough?
- Comment C: `# TODO: remove this later` (it has been there 2 years) — what to do?
- Comment D: `# This never runs` (but the condition CAN be True) — what is wrong?

**💻 Starter Code**

```python
# Exercise 5.3 – Fix Bad Comments

x = 5               # A: set x to 5
y = x * 2           # B: multiply

# C: TODO: remove this later
discount = 0.10

temp = 30
# D: This never runs
if temp > 25:
    print("Heat warning!")
```

**✅ Expected Output**

```text
# (Improved version — same output, better comments)
```

**💡 Hint**

Rule of thumb: if removing the comment makes the code harder to understand, keep it (but improve it). If the comment just repeats the code, delete it.

**🔑 Solution**

```python
x = 5               # Base price in dollars
y = x * 2           # Doubled for premium tier

discount = 0.10     # 10% loyalty discount applied to returning customers

temp = 30           # Current temperature in Celsius
if temp > 25:       # Warn user when temperature exceeds comfort threshold
    print("Heat warning!")
```



---


## Topic 6: Input

The `input()` function allows your program to receive data from the user at runtime. Because it **always returns a string**, you must convert the input to the appropriate type (`int`, `float`) before performing calculations. Input is what makes programs interactive and dynamic.

### Exercise 6.1 — Basic User Input


**🎯 Objective**

Use the `input()` function to collect and display user-provided data.

**📖 Explanation**

The `input()` function pauses the program and waits for the user to type something and press Enter. It **always returns a string**. The optional argument is the prompt shown to the user. Use `print()` or f-strings to display the result.

**📝 Task**

Build a simple greeting program:

- Ask for the user's first name.
- Ask for their favourite colour.
- Print a personalised greeting using both inputs.

**💻 Starter Code**

```python
# Exercise 6.1 – Basic Input

name   = input(_____)
colour = input(_____)

print(f"Hello, {_____}! I hear {_____} is your favourite colour.")
```

**✅ Expected Output**

```text
Enter your name: Alice
Your favourite colour: Blue
Hello, Alice! I hear Blue is your favourite colour.
```

**💡 Hint**

The string inside `input()` is the prompt — it is displayed to the user before they type. Include a trailing space if needed: `input("Name: ")`.

**🔑 Solution**

```python
name   = input("Enter your name: ")
colour = input("Your favourite colour: ")
print(f"Hello, {name}! I hear {colour} is your favourite colour.")
```


### Exercise 6.2 — Input with Type Conversion


**🎯 Objective**

Convert user input (always a string) to numeric types for calculations.

**📖 Explanation**

Because `input()` always returns a string, you must convert to `int` or `float` before doing arithmetic. Wrap `input()` with `int()` or `float()`: `age = int(input("Age: "))`. Failing to do so causes a `TypeError` when you try to add strings to numbers.

**📝 Task**

Build a simple age calculator:

- Ask the user for their birth year.
- Convert it to an integer.
- Calculate and print their age in 2024 and the year they will turn 100.

**💻 Starter Code**

```python
# Exercise 6.2 – Input with Conversion

birth_year   = _____(input("Enter your birth year: "))
current_year = 2024

age      = _____
year_100 = _____

print(f"You are {age} years old in {current_year}.")
print(f"You will turn 100 in {year_100}.")
```

**✅ Expected Output**

```text
Enter your birth year: 1995
You are 29 years old in 2024.
You will turn 100 in 2095.
```

**💡 Hint**

Remember: `input()` → `str`. You **MUST** wrap with `int()` before arithmetic. Try adding `1` to `input()` without conversion and observe the `TypeError`.

**🔑 Solution**

```python
birth_year   = int(input("Enter your birth year: "))
current_year = 2024
age          = current_year - birth_year
year_100     = birth_year + 100
print(f"You are {age} years old in {current_year}.")
print(f"You will turn 100 in {year_100}.")
```


### Exercise 6.3 — Interactive Calculator


**🎯 Objective**

Build a simple two-number calculator that takes all values from user input.

**📖 Explanation**

This exercise combines `input()`, type conversion, arithmetic operators, and f-string formatting into a mini-application. The program prompts for two numbers, then performs and displays all basic arithmetic operations on them.

**📝 Task**

Build a calculator that:

- Asks for two numbers (support decimals — use `float`).
- Prints the result of `+`, `-`, `*`, `/` between them.
- Prints the result of `//` and `%` (floor division and remainder).
- Prints the result of `a ** b` (a to the power of b).

**💻 Starter Code**

```python
# Exercise 6.3 – Interactive Calculator

a = _____(input("Enter first number : "))
b = _____(input("Enter second number: "))

print(f"{a} + {b} = {_____}")
print(f"{a} - {b} = {_____}")
print(f"{a} * {b} = {_____}")
print(f"{a} / {b} = {_____:.2f}")
print(f"{a} // {b} = {_____}")
print(f"{a} % {b}  = {_____}")
print(f"{a} ** {b} = {_____}")
```

**✅ Expected Output**

```text
Enter first number : 10
Enter second number: 3
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 * 3.0 = 30.0
10.0 / 3.0 = 3.33
10.0 // 3.0 = 3.0
10.0 % 3.0  = 1.0
10.0 ** 3.0 = 1000.0
```

**💡 Hint**

Use `float()` not `int()` so the calculator handles decimals. Division of floats still produces a float, so `//` and `%` on floats return floats too.

**🔑 Solution**

```python
a = float(input("Enter first number : "))
b = float(input("Enter second number: "))
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b}  = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```



---


## Topic 7: String Methods

Strings in Python come with a rich library of built-in methods for transforming, searching, and validating text. These methods — accessed via dot notation — do **not** modify the original string (strings are immutable) but return a new one with the change applied.

### Exercise 7.1 — Case & Strip Methods


**🎯 Objective**

Apply `upper()`, `lower()`, `title()`, `capitalize()`, `strip()`, `lstrip()`, and `rstrip()` to clean and format strings.

**📖 Explanation**

String methods are functions built into every string object, called with dot notation: `"hello".upper()`. Case methods change letter casing. Strip methods remove unwanted whitespace (or other characters) from the edges of a string — useful when processing user input or file data.

**📝 Task**

Clean and format the messy strings below using the appropriate methods:

- Remove leading/trailing whitespace from `raw_input`.
- Convert `name` to title case (first letter of each word capitalised).
- Convert `code` to all uppercase for a SKU label.
- Convert `shout` to all lowercase for normalisation.

**💻 Starter Code**

```python
# Exercise 7.1 – Case & Strip

raw_input = "   hello world   "
name      = "aLiCe sMiTh"
code      = "prod-abc-007"
shout     = "WHY IS THIS ALL CAPS"

print(raw_input._____())
print(name._____())
print(code._____())
print(shout._____())
```

**✅ Expected Output**

```text
hello world
Alice Smith
PROD-ABC-007
why is this all caps
```

**💡 Hint**

`strip()` removes **both** ends. `lstrip()` removes left only. `rstrip()` removes right only. `title()` capitalises every word; `capitalize()` only the very first letter.

**🔑 Solution**

```python
print(raw_input.strip())
print(name.title())
print(code.upper())
print(shout.lower())
```


### Exercise 7.2 — Find, Replace, Split & Join


**🎯 Objective**

Use `find()`, `replace()`, `split()`, and `join()` to search, modify, and restructure strings.

**📖 Explanation**

`find()` returns the index of the first occurrence of a substring (`-1` if not found). `replace()` returns a new string with all occurrences replaced. `split()` breaks a string into a list by a delimiter. `join()` is the inverse — it merges a list of strings with a separator.

**📝 Task**

Process the CSV-style data string using string methods:

- Find the position of the word `"Python"`.
- Replace all commas with `" | "` for display.
- Split the original string by comma to get a list of items.
- Join the list with `" - "` to create a formatted string.

**💻 Starter Code**

```python
# Exercise 7.2 – Find, Replace, Split, Join

data = "HTML,CSS,Python,JavaScript,TypeScript"

# 1. Find index of 'Python'
pos = data._____(_____)  
print(f"'Python' starts at index: {pos}")

# 2. Replace commas with " | "
display = data._____(_____, _____)
print(display)

# 3. Split into a list
items = data._____(_____)  
print(items)

# 4. Join with " - "
result = _____.join(items)
print(result)
```

**✅ Expected Output**

```text
'Python' starts at index: 9
HTML | CSS | Python | JavaScript | TypeScript
['HTML', 'CSS', 'Python', 'JavaScript', 'TypeScript']
HTML - CSS - Python - JavaScript - TypeScript
```

**💡 Hint**

`find()` returns the starting index as an integer. `split(",")` splits on every comma. `" - ".join(list)` joins list elements with `" - "` between each pair.

**🔑 Solution**

```python
data = "HTML,CSS,Python,JavaScript,TypeScript"
pos     = data.find("Python")
print(f"'Python' starts at index: {pos}")
display = data.replace(",", " | ")
print(display)
items   = data.split(",")
print(items)
result  = " - ".join(items)
print(result)
```


### Exercise 7.3 — String Checking & Counting Methods


**🎯 Objective**

Use `startswith()`, `endswith()`, `isdigit()`, `isalpha()`, `isspace()`, and `count()` to validate and analyse strings.

**📖 Explanation**

Python provides many is-checking methods that return `True` or `False`. These are valuable for input validation without writing complex logic. `count()` counts non-overlapping occurrences of a substring. These methods do **not** modify the string — they only inspect it.

**📝 Task**

Validate and analyse user-provided data using string checking methods:

- Check if `filename` ends with `".py"`.
- Check if a `pin` is all digits.
- Check if a `name` contains only alphabetic characters (no spaces/digits).
- Count how many times the letter `"a"` appears in a sentence.

**💻 Starter Code**

```python
# Exercise 7.3 – String Checking & Counting

filename  = "script.py"
pin       = "4829"
name      = "Alice123"
sentence  = "a banana a day keeps the doctor away"

# 1. Does filename end with .py?
print(filename._____(".py"))

# 2. Is pin all digits?
print(pin._____())

# 3. Is name alphabetic only?
print(name._____())

# 4. How many times does "a" appear?
print(sentence._____("a"))
```

**✅ Expected Output**

```text
True
True
False
6
```

**💡 Hint**

`isalpha()` returns `False` if the string contains digits, spaces, or punctuation. `count()` is case-sensitive: `"a"` ≠ `"A"`. Try `sentence.lower().count("a")` to count all regardless of case.

**🔑 Solution**

```python
print(filename.endswith(".py"))   # True
print(pin.isdigit())              # True
print(name.isalpha())             # False  (contains "123")
print(sentence.count("a"))        # 6
```



---


*End of Module 1 Exercises — Python for Beginners*