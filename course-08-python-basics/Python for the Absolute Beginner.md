# Python for the Absolute Beginner

A comprehensive, hands-on tutorial covering Python fundamentals from your very first line of code through functions, data structures, error handling, and Python internals.

---

## Table of Contents

1. [Module 1 – Python Basics](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-1--python-basics)
2. [Module 2 – Decision Making in Python](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-2--decision-making-in-python)
3. [Module 3 – Iteration in Python](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-3--iteration-in-python)
4. [Module 4 – Exploring Logic and Bit Operations in Python](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-4--exploring-logic-and-bit-operations-in-python)
5. [Module 5 – Exploring Python Lists](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-5--exploring-python-lists)
6. [Module 6 – Python Functions](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-6--python-functions)
7. [Module 7 – Tuples and Dictionaries](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-7--tuples-and-dictionaries)
8. [Module 8 – Exceptions](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-8--exceptions)
9. [Module 9 – Python Internals and Conclusion](https://claude.ai/local_sessions/local_4e5327dd-b99f-4c21-b2ce-e233b861a37f#module-9--python-internals-and-conclusion)

---

## Course Overview

Welcome to **Python for the Absolute Beginner**! This course is designed for individuals with no prior programming experience. By the end of this course, you will be able to write Python programs that take input, make decisions, repeat tasks with loops, organize data in lists, dictionaries, and tuples, define reusable functions, and handle errors gracefully.

**Prerequisites:** None — just curiosity and a computer with Python 3.10+ installed.

**How to use this tutorial:** Each module contains explanations followed by hands-on labs. Type every example yourself — do not copy-paste. Muscle memory is a real part of learning to code.

---

# Module 1 – Python Basics

This module serves as an orientation and provides you with essential knowledge and skills to get started with Python programming. You will learn the syntax and basic concepts of Python, gain practical experience with the `print` function, work with different types of literals, understand operators, variables, comments, input functions, and string methods.

### Learning Objectives

- Understand the fundamentals of Python programming language.
- Learn how to use the `print` function to display output.
- Explore different types of literals in Python, including numeric, string, and boolean literals.
- Gain proficiency in using operators for arithmetic, comparison, and logical operations.
- Learn about variables and their usage for storing and manipulating data.
- Understand the importance of comments for code documentation and readability.
- Learn how to take user input using the `input` function.
- Explore various string methods for manipulating and working with string data.

---

## Why Python Works the Way It Does

Python was created by Guido van Rossum and first released in 1991. Its design philosophy emphasizes **readability** and **simplicity**. Where other languages use curly braces `{}` to define code blocks, Python uses indentation. Where other languages require semicolons at the end of every statement, Python uses newlines.

This matters because Python was built around one core idea: **code is read far more often than it is written.** Every design choice — from significant whitespace to duck typing — serves that principle.

Python is an **interpreted** language, meaning you don't need to compile your code before running it. You write a `.py` file, and the Python interpreter executes it line by line. This makes the feedback loop incredibly fast: write, run, see results, adjust.

Python is also **dynamically typed**, meaning you don't have to declare the type of a variable ahead of time. The interpreter figures out what type a value is at runtime.

---

## Python Introduction

To check that Python is installed, open a terminal or command prompt and type:

```bash
python --version
```

You should see something like `Python 3.12.0` (your version may differ). If you see `Python 2.x`, try `python3 --version` instead.

**Running Python interactively:** Type `python` (or `python3`) in your terminal to open the interactive interpreter (also called the REPL — Read, Eval, Print, Loop):

```
$ python
Python 3.12.0 (...)
>>> 2 + 2
4
>>> print("Hello!")
Hello!
>>> exit()
```

**Running Python scripts:** Create a file called `hello.py` with a text editor and add:

```python
print("Hello, World!")
```

Then run it from the terminal:

```bash
python hello.py
```

Output:

```
Hello, World!
```

---

## Print Function

The `print()` function is the most fundamental way to display output in Python. It sends text to the console (your terminal or output window).

**Basic syntax:**

```python
print("Hello, World!")
```

**Printing multiple values:**

The `print()` function can take multiple arguments, separated by commas. By default, they are joined with a space:

```python
print("Hello", "World")
# Output: Hello World
```

**The `sep` parameter:**

You can change the separator between values:

```python
print("Hello", "World", sep="-")
# Output: Hello-World

print("2026", "04", "01", sep="/")
# Output: 2026/04/01
```

**The `end` parameter:**

By default, `print()` adds a newline character at the end. You can change this:

```python
print("Hello", end=" ")
print("World")
# Output: Hello World  (on one line)
```

**Printing special characters:**

Use escape sequences to include special characters:

```python
print("Line one\nLine two")     # \n = newline
print("Column1\tColumn2")       # \t = tab
print("She said \"hello\"")     # \" = literal quote
print('She said "hello"')       # Or use single quotes outside
```

**Printing numbers and expressions:**

```python
print(42)
print(3.14)
print(2 + 3)          # Output: 5
print("Result:", 2+3)  # Output: Result: 5
```

---

### Hands-on Lab: Print Function

**Lab Goal:** Practice using the `print()` function with various arguments and parameters.

**Exercise 1:** Write a program that prints your full name on one line.

```python
# Exercise 1: Print your full name
print("Ada Lovelace")
```

**Exercise 2:** Print three lines using a single `print()` statement and the newline escape character.

```python
# Exercise 2: Three lines with one print
print("Line 1\nLine 2\nLine 3")
```

**Exercise 3:** Print the following using the `sep` parameter: `2026-04-01`

```python
# Exercise 3: Date formatting with sep
print("2026", "04", "01", sep="-")
```

**Exercise 4:** Print the words "Python", "is", "fun!" on the same line using three separate `print()` calls and the `end` parameter.

```python
# Exercise 4: Same line with end parameter
print("Python", end=" ")
print("is", end=" ")
print("fun!")
```

**Exercise 5:** Print a multiplication table row for the number 5 (5x1 through 5x5), using `\t` for alignment.

```python
# Exercise 5: Multiplication table row
print("5 x 1 =", 5*1)
print("5 x 2 =", 5*2)
print("5 x 3 =", 5*3)
print("5 x 4 =", 5*4)
print("5 x 5 =", 5*5)
```

Expected Output:

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
```

---

## Literals

A **literal** is a fixed value written directly in your code. Python supports several types of literals.

### Numeric Literals

**Integers** — whole numbers without a decimal point:

```python
print(42)
print(-17)
print(0)
print(1_000_000)   # Underscores for readability — same as 1000000
```

**Floats** — numbers with a decimal point:

```python
print(3.14)
print(-0.5)
print(1.0)
print(2.5e3)   # Scientific notation: 2500.0
print(1.2e-4)  # 0.00012
```

**Octal, Hexadecimal, and Binary literals:**

```python
print(0o17)    # Octal: 15 in decimal
print(0xFF)    # Hexadecimal: 255 in decimal
print(0b1010)  # Binary: 10 in decimal
```

### String Literals

Strings are sequences of characters enclosed in quotes:

```python
print("Hello, World!")          # Double quotes
print('Hello, World!')          # Single quotes
print("It's a beautiful day")   # Double quotes to include apostrophe
print('She said "hi"')          # Single quotes to include double quotes
```

**Multiline strings** use triple quotes:

```python
print("""This is
a multiline
string.""")

print('''This also
works with
single quotes.''')
```

**Empty string:**

```python
empty = ""
print(empty)     # Prints a blank line
print(len(empty))  # Output: 0
```

### Boolean Literals

Boolean values represent truth. There are exactly two:

```python
print(True)
print(False)
print(type(True))   # <class 'bool'>
```

Booleans are actually a subclass of integers: `True` equals `1` and `False` equals `0`:

```python
print(True + True)    # Output: 2
print(True * 10)      # Output: 10
print(False + 5)      # Output: 5
```

### The `None` Literal

`None` represents the absence of a value:

```python
print(None)
print(type(None))   # <class 'NoneType'>
```

---

### Hands-on Lab: Literals

**Lab Goal:** Explore and experiment with different types of literals in Python.

**Exercise 1:** Create and print examples of each numeric type.

```python
# Integer literals
print(100)
print(-50)
print(1_000_000)

# Float literals
print(3.14159)
print(-2.5)
print(1.5e2)       # 150.0

# Octal, Hex, Binary
print(0o77)         # 63
print(0xDEAD)       # 57005
print(0b11111111)   # 255
```

**Exercise 2:** Experiment with string literals and escape characters.

```python
# String literals
print("Double-quoted string")
print('Single-quoted string')
print("Tab\there")
print("Newline\nhere")
print("Backslash: \\")
print("Quote: \"Hello\"")

# Multiline
print("""
    Python
    is
    great!
""")
```

**Exercise 3:** Experiment with boolean arithmetic.

```python
# Boolean literals
print(True)
print(False)
print(True + True + True)      # 3
print(True * 100)              # 100
print(False * 100)             # 0
print(type(True))              # <class 'bool'>
```

**Exercise 4:** Verify the type of different literals using `type()`.

```python
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type(None))        # <class 'NoneType'>
```

---

## Operators

Operators are symbols that perform operations on values (called operands).

### Arithmetic Operators

|Operator|Name|Example|Result|
|---|---|---|---|
|`+`|Addition|`5 + 3`|`8`|
|`-`|Subtraction|`10 - 4`|`6`|
|`*`|Multiplication|`3 * 7`|`21`|
|`/`|Division|`15 / 4`|`3.75`|
|`//`|Floor Division|`15 // 4`|`3`|
|`%`|Modulus|`15 % 4`|`3`|
|`**`|Exponentiation|`2 ** 10`|`1024`|

```python
print(10 + 3)     # 13
print(10 - 3)     # 7
print(10 * 3)     # 30
print(10 / 3)     # 3.3333333333333335
print(10 // 3)    # 3 (rounds down to nearest integer)
print(10 % 3)     # 1 (remainder of 10 / 3)
print(2 ** 8)     # 256
```

### Operator Precedence

Python follows standard mathematical order of operations (PEMDAS):

1. `**` (exponentiation)
2. `*`, `/`, `//`, `%` (multiplication, division, modulus)
3. `+`, `-` (addition, subtraction)

Use parentheses to override precedence:

```python
print(2 + 3 * 4)       # 14  (multiplication first)
print((2 + 3) * 4)     # 20  (parentheses first)
print(2 ** 3 ** 2)      # 512 (right-to-left: 3**2=9, then 2**9=512)
```

### String Operators

The `+` operator concatenates strings, and `*` repeats them:

```python
print("Hello" + " " + "World")    # Hello World
print("Ha" * 3)                    # HaHaHa
print("-" * 40)                    # ----------------------------------------
```

---

### Hands-on Lab: Operators

**Lab Goal:** Practice using arithmetic operators and understand precedence.

**Exercise 1:** Calculate the area of a rectangle with width 15 and height 8.

```python
# Area of a rectangle
print("Area:", 15 * 8)
# Output: Area: 120
```

**Exercise 2:** A pizza costs $12.50 and you want to split it among 4 people. How much does each person pay? What if there are 3 people?

```python
# Splitting a pizza cost
print("Cost per person (4):", 12.50 / 4)
print("Cost per person (3):", 12.50 / 3)
```

**Exercise 3:** Use the modulus operator to determine if 247 is even or odd.

```python
# Even or odd
print("247 % 2 =", 247 % 2)   # 1 means odd, 0 means even
```

**Exercise 4:** Calculate 2 to the power of 16.

```python
# Exponentiation
print("2^16 =", 2 ** 16)   # 65536
```

**Exercise 5:** Demonstrate operator precedence with and without parentheses.

```python
# Precedence
print(10 + 5 * 2)         # 20 (not 30)
print((10 + 5) * 2)       # 30
print(100 / 5 / 2)        # 10.0
print(100 / (5 / 2))      # 40.0
print(2 + 3 ** 2)         # 11 (not 25)
print((2 + 3) ** 2)       # 25
```

**Exercise 6:** Use string operators to create a decorative banner.

```python
# String operators
border = "*" * 30
print(border)
print("*" + " Welcome to Python! ".center(28) + "*")
print(border)
```

Expected Output:

```
******************************
*    Welcome to Python!      *
******************************
```

---

## Variables

A **variable** is a named container for storing data. In Python, you create a variable by assigning a value to a name using the `=` operator.

```python
name = "Alice"
age = 30
height = 5.7
is_student = True

print(name)          # Alice
print(age)           # 30
print(height)        # 5.7
print(is_student)    # True
```

### Variable Naming Rules

1. Names can contain letters, digits, and underscores.
2. Names must begin with a letter or an underscore (not a digit).
3. Names are **case-sensitive**: `age`, `Age`, and `AGE` are three different variables.
4. Names cannot be Python keywords (like `if`, `for`, `while`, `class`, etc.).

```python
# Valid names
my_variable = 10
_private = 20
name2 = "Bob"
MAX_SIZE = 100

# Invalid names (would cause errors)
# 2nd_name = "error"    # Cannot start with a digit
# my-variable = 10      # Hyphens are not allowed
# class = "error"       # 'class' is a reserved keyword
```

### Naming Conventions

Python programmers conventionally use **snake_case** for variable and function names:

```python
first_name = "Alice"
last_name = "Smith"
total_price = 99.99
is_logged_in = False
```

### Reassigning Variables

Variables can be reassigned at any time, even to a different type:

```python
x = 10
print(x)       # 10

x = "hello"
print(x)       # hello

x = 3.14
print(x)       # 3.14
```

### Multiple Assignment

```python
# Assign same value to multiple variables
a = b = c = 0
print(a, b, c)    # 0 0 0

# Assign different values on one line
x, y, z = 1, 2, 3
print(x, y, z)    # 1 2 3

# Swap two variables
x, y = y, x
print(x, y)        # 2 1
```

### Augmented Assignment Operators

Shorthand for modifying a variable's value:

```python
count = 0
count += 1     # Same as: count = count + 1
count += 5     # count is now 6
count -= 2     # count is now 4
count *= 3     # count is now 12
count /= 4     # count is now 3.0
count //= 2    # count is now 1.0
count **= 3    # count is now 1.0

print(count)
```

---

### Hands-on Lab: Variables

**Lab Goal:** Practice creating, modifying, and using variables.

**Exercise 1:** Create variables for your personal info and print them.

```python
# Personal info
first_name = "Ada"
last_name = "Lovelace"
age = 36
favorite_language = "Python"

print("Name:", first_name, last_name)
print("Age:", age)
print("Favorite language:", favorite_language)
```

**Exercise 2:** Swap two variables without using a temporary variable.

```python
# Variable swapping
a = 100
b = 200
print("Before swap:", a, b)

a, b = b, a
print("After swap:", a, b)
```

**Exercise 3:** Use augmented assignment to track a bank balance.

```python
# Bank balance tracker
balance = 1000.00
print("Starting balance:", balance)

balance += 500.00     # Deposit
print("After deposit:", balance)

balance -= 200.00     # Withdrawal
print("After withdrawal:", balance)

balance *= 1.05       # 5% interest
print("After 5% interest:", balance)
```

**Exercise 4:** Demonstrate that variables are case-sensitive.

```python
# Case sensitivity
name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)    # Alice
print(Name)    # Bob
print(NAME)    # Charlie
```

---

## Comments

Comments are notes in your code that Python ignores during execution. They exist solely for humans reading the code.

### Single-Line Comments

Use the `#` symbol:

```python
# This is a comment
print("Hello")   # This is an inline comment

# Calculate the area of a circle
radius = 5
area = 3.14159 * radius ** 2
print("Area:", area)
```

### Multi-Line Comments

Python doesn't have a dedicated multi-line comment syntax, but you can use consecutive `#` lines or a multiline string (which is not assigned to anything):

```python
# This is a longer comment
# that spans multiple lines
# explaining something complex.

"""
This is sometimes used as a multi-line comment.
Technically it's a string literal that isn't assigned
to a variable, so Python evaluates it and discards it.
"""
```

### When to Use Comments

- Explain **why** something is done, not **what** is done (the code shows what).
- Document assumptions or edge cases.
- Mark sections of code for readability.

```python
# Good comment - explains WHY
# Using floor division because we need whole packages only
packages_needed = total_items // items_per_package

# Bad comment - just restates the code
# Add 1 to x
x = x + 1

# Better
# Adjust for zero-based indexing
x = x + 1
```

---

### Hands-on Lab: Comments

**Lab Goal:** Practice adding meaningful comments to code.

**Exercise 1:** Add appropriate comments to the following code.

```python
# Calculate the total cost of an order with tax

price = 49.99
quantity = 3
tax_rate = 0.08     # 8% sales tax

# Calculate subtotal before tax
subtotal = price * quantity

# Calculate tax amount
tax = subtotal * tax_rate

# Calculate final total
total = subtotal + tax

# Display the order summary
print("Subtotal: $", subtotal)
print("Tax: $", tax)
print("Total: $", total)
```

**Exercise 2:** Identify and fix the poorly commented code below. Rewrite the comments to be meaningful.

```python
# BEFORE (bad comments):
# set x to 100
x = 100
# set y to 12
y = 12
# divide x by y
z = x / y
# print z
print(z)

# AFTER (good comments):
# Monthly budget calculation
annual_budget = 100       # Total annual budget in thousands
months = 12

# Calculate average monthly allocation
monthly_budget = annual_budget / months

print("Monthly budget: $", monthly_budget, "thousand")
```

---

## Input

The `input()` function reads text typed by the user from the keyboard and returns it as a **string**.

```python
name = input("What is your name? ")
print("Hello,", name)
```

When this runs:

```
What is your name? Alice
Hello, Alice
```

### Important: `input()` Always Returns a String

Even if the user types a number, `input()` returns it as a string:

```python
age = input("Enter your age: ")
print(type(age))    # <class 'str'>
```

To use the value as a number, you must **convert** it:

```python
age = int(input("Enter your age: "))          # Convert to integer
price = float(input("Enter the price: "))     # Convert to float

print(type(age))      # <class 'int'>
print(type(price))    # <class 'float'>
```

### Reading Multiple Values

```python
# Read two numbers and add them
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
```

---

### Hands-on Lab: Input

**Lab Goal:** Practice reading user input and converting types.

**Exercise 1:** Write a greeting program that asks for the user's name and age.

```python
# Greeting program
name = input("What is your name? ")
age = input("How old are you? ")
print("Hello,", name + "! You are", age, "years old.")
```

**Exercise 2:** Build a simple calculator that reads two numbers and prints their sum, difference, product, and quotient.

```python
# Simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
```

**Exercise 3:** Write a program that calculates how many days old the user is (approximate).

```python
# Days old calculator
age = int(input("Enter your age in years: "))
days = age * 365
print("You are approximately", days, "days old!")
```

**Exercise 4:** Write a temperature converter (Fahrenheit to Celsius).

```python
# Temperature converter
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(fahrenheit, "°F is", round(celsius, 2), "°C")
```

---

## String Methods

Strings in Python come with many built-in methods for manipulation.

### Changing Case

```python
text = "Hello, World!"

print(text.upper())        # HELLO, WORLD!
print(text.lower())        # hello, world!
print(text.title())        # Hello, World!
print(text.capitalize())   # Hello, world!
print(text.swapcase())     # hELLO, wORLD!
```

### Searching and Checking

```python
text = "Hello, World!"

print(text.find("World"))       # 7 (index where "World" starts)
print(text.find("Python"))      # -1 (not found)
print(text.count("l"))          # 3
print(text.startswith("Hello")) # True
print(text.endswith("!"))       # True
print("World" in text)          # True
```

### Stripping Whitespace

```python
text = "   Hello, World!   "

print(text.strip())        # "Hello, World!"
print(text.lstrip())       # "Hello, World!   "
print(text.rstrip())       # "   Hello, World!"
```

### Replacing and Splitting

```python
text = "Hello, World!"

print(text.replace("World", "Python"))   # Hello, Python!
print(text.replace("l", "L"))            # HeLLo, WorLd!

csv_data = "apple,banana,cherry"
print(csv_data.split(","))               # ['apple', 'banana', 'cherry']

words = "Hello World Python"
print(words.split())                     # ['Hello', 'World', 'Python']
```

### Joining Strings

```python
fruits = ["apple", "banana", "cherry"]
result = ", ".join(fruits)
print(result)     # apple, banana, cherry

letters = ["P", "y", "t", "h", "o", "n"]
print("".join(letters))   # Python
```

### Type-Checking Methods

```python
print("hello".isalpha())     # True (only letters)
print("12345".isdigit())     # True (only digits)
print("hello5".isalnum())    # True (letters and/or digits)
print("   ".isspace())       # True (only whitespace)
print("Hello".isupper())     # False
print("HELLO".isupper())     # True
print("hello".islower())     # True
```

### String Formatting (f-strings)

F-strings (formatted string literals) are the modern way to embed expressions inside strings:

```python
name = "Alice"
age = 30

# f-string
print(f"My name is {name} and I am {age} years old.")

# Expressions inside f-strings
print(f"In 5 years, I'll be {age + 5}.")
print(f"Pi is approximately {3.14159:.2f}")   # 3.14 (2 decimal places)

# Alignment and padding
print(f"{'left':<20}")     # Left-aligned in 20 chars
print(f"{'center':^20}")   # Center-aligned in 20 chars
print(f"{'right':>20}")    # Right-aligned in 20 chars
```

---

### Hands-on Lab: String Methods

**Lab Goal:** Practice using string methods to process and transform text.

**Exercise 1:** Ask the user for their full name and print it in all caps, all lowercase, and title case.

```python
# Name case transformer
name = input("Enter your full name: ")
print("UPPER:", name.upper())
print("lower:", name.lower())
print("Title:", name.title())
```

**Exercise 2:** Write a program that counts the number of vowels in a user-provided string.

```python
# Vowel counter
text = input("Enter a string: ").lower()
vowel_count = 0
for char in "aeiou":
    vowel_count += text.count(char)
print("Number of vowels:", vowel_count)
```

**Exercise 3:** Write a program that takes a comma-separated list of items and prints each on a new line.

```python
# CSV splitter
items = input("Enter items separated by commas: ")
item_list = items.split(",")
for item in item_list:
    print(item.strip())
```

**Exercise 4:** Use an f-string to create a formatted receipt.

```python
# Formatted receipt
item = "Widget"
price = 19.99
quantity = 3
total = price * quantity

print(f"{'Item':<15}{'Qty':>5}{'Price':>10}{'Total':>10}")
print(f"{'-'*40}")
print(f"{item:<15}{quantity:>5}{price:>10.2f}{total:>10.2f}")
```

**Exercise 5:** Check if a user-entered string is a palindrome (reads the same forward and backward).

```python
# Palindrome checker
text = input("Enter a word: ").lower().strip()
reversed_text = text[::-1]

if text == reversed_text:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")
```

---

### Graded Assessment: Python Basics

Test your understanding with these challenges. Try to solve them without looking at earlier examples.

**Challenge 1:** Write a program that asks for the user's birth year and calculates their approximate age.

```python
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(f"You are approximately {age} years old.")
```

**Challenge 2:** Write a program that converts a distance in miles to kilometers (1 mile = 1.60934 km).

```python
miles = float(input("Enter distance in miles: "))
km = miles * 1.60934
print(f"{miles} miles = {km:.2f} kilometers")
```

**Challenge 3:** Write a program that takes a sentence and reports: the number of characters, the number of words, and the sentence in reverse.

```python
sentence = input("Enter a sentence: ")
print(f"Characters: {len(sentence)}")
print(f"Words: {len(sentence.split())}")
print(f"Reversed: {sentence[::-1]}")
```

**Challenge 4:** Write a program that creates a personalized email template using f-strings.

```python
name = input("Recipient name: ")
product = input("Product name: ")
price = float(input("Product price: "))

email = f"""Dear {name},

Thank you for your interest in {product}!
The current price is ${price:.2f}.

Best regards,
The Sales Team"""

print(email)
```

---

# Module 2 – Decision Making in Python

This module focuses on teaching you how to make decisions in Python programs using comparison operators and conditional statements. You will learn to compare values, evaluate conditions, and control the flow of your programs.

### Learning Objectives

- Understand how comparison operators are used to compare values in Python.
- Gain proficiency in using comparison operators to make decisions.
- Learn about conditional statements and their role in controlling program flow.
- Acquire practical skills in implementing conditional statements to execute code based on specific conditions.

---

## Comparison Operators

Comparison operators compare two values and return a boolean result (`True` or `False`).

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`==`|Equal to|`5 == 5`|`True`|
|`!=`|Not equal to|`5 != 3`|`True`|
|`>`|Greater than|`5 > 3`|`True`|
|`<`|Less than|`5 < 3`|`False`|
|`>=`|Greater than or equal to|`5 >= 5`|`True`|
|`<=`|Less than or equal to|`3 <= 5`|`True`|

```python
print(10 == 10)    # True
print(10 == 20)    # False
print(10 != 20)    # True
print(10 > 5)      # True
print(10 < 5)      # False
print(10 >= 10)    # True
print(10 <= 5)     # False
```

### Comparing Strings

Strings are compared lexicographically (dictionary order, based on Unicode values):

```python
print("apple" == "apple")      # True
print("apple" == "Apple")      # False (case-sensitive)
print("apple" < "banana")      # True (a comes before b)
print("Zebra" < "apple")       # True (uppercase Z < lowercase a in Unicode)
print("abc" < "abd")           # True (c < d)
```

### Common Pitfall: `=` vs `==`

- `=` is the **assignment** operator (sets a value).
- `==` is the **comparison** operator (checks equality).

```python
x = 5       # Assignment: x is now 5
x == 5      # Comparison: is x equal to 5? → True
```

---

### Hands-on Lab: Comparison Operators

**Lab Goal:** Practice using comparison operators with numbers and strings.

**Exercise 1:** Compare numbers entered by the user.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"{a} == {b} → {a == b}")
print(f"{a} != {b} → {a != b}")
print(f"{a} >  {b} → {a > b}")
print(f"{a} <  {b} → {a < b}")
print(f"{a} >= {b} → {a >= b}")
print(f"{a} <= {b} → {a <= b}")
```

**Exercise 2:** Compare two strings provided by the user.

```python
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

print(f"'{word1}' == '{word2}' → {word1 == word2}")
print(f"'{word1}' < '{word2}' → {word1 < word2}")
print(f"Case-insensitive equal → {word1.lower() == word2.lower()}")
```

**Exercise 3:** Write expressions to test various comparisons and predict the results before running.

```python
# Predict the output first, then run to check!
print(5 > 3)               # ?
print(5 == 5.0)            # ?
print("hello" == "Hello")  # ?
print(10 != 10)            # ?
print(1 > True)            # ?
print(0 == False)          # ?
```

---

## Conditional Statements

Conditional statements let your program make decisions — execute different code depending on whether a condition is true or false.

### The `if` Statement

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

The indented block (4 spaces) runs only if the condition is `True`. If the condition is `False`, the block is skipped entirely.

### The `if-else` Statement

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### The `if-elif-else` Statement

When you have multiple conditions to check:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

Python checks each condition from top to bottom and executes the **first** block whose condition is `True`. The rest are skipped.

### Nested Conditions

You can place `if` statements inside other `if` statements:

```python
age = 25
has_license = True

if age >= 16:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license first.")
else:
    print("You are too young to drive.")
```

### The Ternary (Conditional) Expression

A compact way to write simple if-else logic:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)    # adult
```

---

### Hands-on Lab: Conditional Statements

**Lab Goal:** Write programs that make decisions based on conditions.

**Exercise 1:** Write a program that checks if a number is positive, negative, or zero.

```python
num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")
```

**Exercise 2:** Write a grading program that converts a numerical score (0-100) to a letter grade.

```python
score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score!")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Exercise 3:** Build a simple ticket pricing system.

```python
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()

if age < 5:
    price = 0
    category = "Free (under 5)"
elif age < 13:
    price = 8
    category = "Child"
elif age < 65:
    if is_student == "yes":
        price = 10
        category = "Student discount"
    else:
        price = 15
        category = "Adult"
else:
    price = 10
    category = "Senior discount"

print(f"Category: {category}")
print(f"Ticket price: ${price}")
```

**Exercise 4:** Write a leap year checker.

```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

**Exercise 5:** Create a simple rock-paper-scissors judge (two-player, no AI).

```python
player1 = input("Player 1 — rock, paper, or scissors? ").lower()
player2 = input("Player 2 — rock, paper, or scissors? ").lower()

if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "scissors" and player2 == "paper") or \
     (player1 == "paper" and player2 == "rock"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
```

---

### Graded Assessment: Decision Making

**Challenge 1:** Write a BMI calculator that reads weight (kg) and height (m), calculates BMI, and prints the category (Underweight < 18.5, Normal 18.5–24.9, Overweight 25–29.9, Obese >= 30).

```python
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.1f} — {category}")
```

**Challenge 2:** Write a program that determines the type of triangle given three side lengths (equilateral, isosceles, or scalene), and also checks if the sides can form a valid triangle.

```python
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check triangle inequality
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("These sides cannot form a valid triangle.")
```

---

# Module 3 – Iteration in Python

This module introduces loops — structures that let you repeat code. You will learn `while` loops (repeat while a condition is true) and `for` loops (iterate over a sequence).

### Learning Objectives

- Understand the concept of loops in Python, including `while` and `for` loops.
- Gain proficiency in using `while` loops to iterate based on conditions.
- Acquire practical skills in implementing both loop types through hands-on exercises.

---

## Loops – while

A `while` loop repeats a block of code as long as its condition remains `True`.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

### How It Works

1. Python evaluates the condition (`count <= 5`).
2. If `True`, the indented body executes.
3. After the body finishes, Python goes back to step 1.
4. When the condition becomes `False`, the loop ends and execution continues after the loop.

### Infinite Loops

If the condition never becomes `False`, the loop runs forever. Press `Ctrl+C` to stop it:

```python
# WARNING: This will run forever!
# while True:
#     print("This never ends...")
```

### `break` Statement

Use `break` to exit a loop early:

```python
count = 1
while True:
    print(count)
    if count == 5:
        break
    count += 1
```

### `continue` Statement

Use `continue` to skip the rest of the current iteration and go to the next:

```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue         # Skip even numbers
    print(count)         # Prints: 1, 3, 5, 7, 9
```

### `while` with `else`

The `else` block runs when the loop condition becomes `False` (but NOT when `break` is used):

```python
count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("Loop completed normally.")
```

---

### Hands-on Lab: Loops – while

**Lab Goal:** Practice using while loops for repetitive tasks.

**Exercise 1:** Print numbers from 1 to 20.

```python
num = 1
while num <= 20:
    print(num, end=" ")
    num += 1
print()  # Newline at the end
```

**Exercise 2:** Write a countdown timer from 10 to 1, then print "Liftoff!"

```python
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Liftoff!")
```

**Exercise 3:** Write a program that repeatedly asks for a password until the correct one is entered.

```python
secret = "python123"

password = input("Enter the password: ")
while password != secret:
    print("Incorrect. Try again.")
    password = input("Enter the password: ")

print("Access granted!")
```

**Exercise 4:** Calculate the sum of all numbers from 1 to 100 using a while loop.

```python
total = 0
num = 1

while num <= 100:
    total += num
    num += 1

print("Sum of 1 to 100:", total)   # 5050
```

**Exercise 5:** Write a number guessing game.

```python
import random

secret_number = random.randint(1, 50)
attempts = 0

print("I'm thinking of a number between 1 and 50.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break
```

---

## Loops – for

A `for` loop iterates over a sequence (like a string, list, or range).

### Iterating Over a Range

The `range()` function generates a sequence of numbers:

```python
# range(stop) — 0 to stop-1
for i in range(5):
    print(i, end=" ")    # 0 1 2 3 4
print()

# range(start, stop) — start to stop-1
for i in range(1, 6):
    print(i, end=" ")    # 1 2 3 4 5
print()

# range(start, stop, step) — with custom step
for i in range(0, 20, 3):
    print(i, end=" ")    # 0 3 6 9 12 15 18
print()

# Counting backward
for i in range(10, 0, -1):
    print(i, end=" ")    # 10 9 8 7 6 5 4 3 2 1
print()
```

### Iterating Over a String

```python
word = "Python"
for char in word:
    print(char)
```

### Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

### `break` and `continue` in `for` Loops

```python
# break: stop when you find the target
for num in range(1, 100):
    if num == 42:
        print("Found 42!")
        break

# continue: skip specific values
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num, end=" ")    # 1 2 4 5 7 8 10
print()
```

### Nested Loops

```python
# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()
```

Output:

```
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

### `for` with `else`

```python
for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        # This runs if the inner loop did NOT break
        print(f"{num} is prime")
```

---

### Hands-on Lab: Loops – for

**Lab Goal:** Practice for loops with ranges, strings, and nested loops.

**Exercise 1:** Print all even numbers from 2 to 50.

```python
for num in range(2, 51, 2):
    print(num, end=" ")
print()
```

**Exercise 2:** Calculate the factorial of a number entered by the user.

```python
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
```

**Exercise 3:** Print a right triangle pattern of stars.

```python
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)
```

Example output for `rows = 5`:

```
*
**
***
****
*****
```

**Exercise 4:** Count how many times each character appears in a string.

```python
text = input("Enter a string: ").lower()

# Track which characters we've already counted
counted = ""

for char in text:
    if char not in counted and char != " ":
        print(f"'{char}' appears {text.count(char)} time(s)")
        counted += char
```

**Exercise 5:** Generate a multiplication table for a given number.

```python
num = int(input("Enter a number: "))

for i in range(1, 13):
    print(f"{num} x {i:2} = {num * i}")
```

---

### Graded Assessment: Iteration in Python

**Challenge 1:** Write a program that prints the Fibonacci sequence up to `n` terms.

```python
n = int(input("How many Fibonacci terms? "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

**Challenge 2:** Write a program that prints a diamond pattern for a given size.

```python
n = int(input("Enter diamond size (odd number): "))

# Upper half including middle
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)

# Lower half
for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)
```

**Challenge 3:** Write a program that finds all prime numbers between 2 and 100.

```python
print("Prime numbers between 2 and 100:")

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
```

---

# Module 4 – Exploring Logic and Bit Operations in Python

This module introduces logic operators (`and`, `or`, `not`) and bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`). You will learn how to combine conditions with logical operators and how to manipulate individual bits within integers.

### Learning Objectives

- Understand the usage of logic operators in Python to perform logical operations.
- Gain proficiency in using logic operators to evaluate conditions and make decisions.
- Acquire practical skills in implementing logic operators through hands-on exercises.
- Learn about bitwise operators and their role in performing bitwise operations on binary numbers.
- Develop proficiency in using bitwise operators through hands-on exercises.

---

## Logic Operators

Logic operators combine boolean expressions and return a boolean result.

### The `and` Operator

Returns `True` only if **both** operands are `True`:

```python
print(True and True)     # True
print(True and False)    # False
print(False and True)    # False
print(False and False)   # False
```

**Truth Table for `and`:**

|A|B|A and B|
|---|---|---|
|`True`|`True`|`True`|
|`True`|`False`|`False`|
|`False`|`True`|`False`|
|`False`|`False`|`False`|

**Practical example:**

```python
age = 25
has_license = True

if age >= 16 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")
```

### The `or` Operator

Returns `True` if **at least one** operand is `True`:

```python
print(True or True)      # True
print(True or False)     # True
print(False or True)     # True
print(False or False)    # False
```

**Truth Table for `or`:**

|A|B|A or B|
|---|---|---|
|`True`|`True`|`True`|
|`True`|`False`|`True`|
|`False`|`True`|`True`|
|`False`|`False`|`False`|

**Practical example:**

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")
else:
    print("Time to go to work.")
```

### The `not` Operator

Reverses a boolean value:

```python
print(not True)     # False
print(not False)    # True
```

**Practical example:**

```python
is_raining = False

if not is_raining:
    print("Let's go for a walk!")
```

### Combining Logic Operators

You can chain logic operators together. Operator precedence (highest to lowest): `not`, `and`, `or`.

```python
age = 25
is_student = True
has_coupon = False

# Complex condition
if (age < 18 or is_student) and not has_coupon:
    print("Standard student discount applies.")

# Without parentheses, 'not' binds tightest, then 'and', then 'or'
print(True or False and False)         # True  (and first: False and False = False, then True or False = True)
print((True or False) and False)       # False (parentheses force 'or' first)
```

### Short-Circuit Evaluation

Python stops evaluating as soon as the result is determined:

```python
# 'and' short-circuits: if the first operand is False, the second is never evaluated
x = 0
if x != 0 and 10 / x > 2:    # 10/x is never evaluated because x != 0 is False
    print("This won't cause an error")

# 'or' short-circuits: if the first operand is True, the second is never evaluated
result = True or print("This never prints")
```

### Truthy and Falsy Values

In Python, all values have a truth value. The following are considered **Falsy**:

- `False`
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]` (empty list), `()` (empty tuple), `{}` (empty dict)
- `None`

Everything else is **Truthy**.

```python
print(bool(0))         # False
print(bool(42))        # True
print(bool(""))        # False
print(bool("hello"))   # True
print(bool([]))        # False
print(bool([1, 2]))    # True
```

---

### Hands-on Lab: Logic Operators

**Lab Goal:** Practice using `and`, `or`, and `not` in conditions and expressions.

**Exercise 1:** Write a program that checks if a number is within a specified range.

```python
num = int(input("Enter a number: "))
low = 10
high = 50

if num >= low and num <= high:
    print(f"{num} is within the range {low}-{high}.")
else:
    print(f"{num} is outside the range {low}-{high}.")
```

**Exercise 2:** Write a login system that checks both username and password.

```python
correct_user = "admin"
correct_pass = "secret123"

username = input("Username: ")
password = input("Password: ")

if username == correct_user and password == correct_pass:
    print("Login successful!")
elif username != correct_user and password != correct_pass:
    print("Both username and password are incorrect.")
elif username != correct_user:
    print("Username is incorrect.")
else:
    print("Password is incorrect.")
```

**Exercise 3:** Write a program to determine eligibility for a special discount. Eligibility: Must be a student OR a senior (65+), AND must not already have a discount card.

```python
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
has_discount_card = input("Do you have a discount card? (yes/no): ").lower() == "yes"

is_senior = age >= 65

if (is_student or is_senior) and not has_discount_card:
    print("You are eligible for the special discount!")
else:
    print("You are not eligible for the special discount.")
```

**Exercise 4:** Experiment with truthy and falsy values.

```python
# Test various values
values = [0, 1, -1, "", "hello", [], [1], None, True, False, 0.0, 3.14]

for val in values:
    if val:
        print(f"{str(val):>10} is Truthy")
    else:
        print(f"{str(val):>10} is Falsy")
```

---

## Bitwise Operators

Bitwise operators work on the binary (bit-level) representation of integers. Each integer is stored as a series of bits (0s and 1s).

### Understanding Binary

```python
# Decimal to binary representation
print(bin(10))    # 0b1010
print(bin(7))     # 0b111
print(bin(255))   # 0b11111111

# Binary to decimal
print(int('1010', 2))    # 10
print(int('111', 2))     # 7
```

### Bitwise AND (`&`)

Compares each bit — result is `1` only if **both** bits are `1`:

```python
a = 12    # Binary: 1100
b = 10    # Binary: 1010

print(a & b)       # 8 (Binary: 1000)
print(bin(a & b))  # 0b1000
```

```
  1100  (12)
& 1010  (10)
------
  1000  (8)
```

### Bitwise OR (`|`)

Result is `1` if **either** bit is `1`:

```python
a = 12    # Binary: 1100
b = 10    # Binary: 1010

print(a | b)       # 14 (Binary: 1110)
print(bin(a | b))  # 0b1110
```

```
  1100  (12)
| 1010  (10)
------
  1110  (14)
```

### Bitwise XOR (`^`)

Result is `1` if the bits are **different**:

```python
a = 12    # Binary: 1100
b = 10    # Binary: 1010

print(a ^ b)       # 6 (Binary: 0110)
print(bin(a ^ b))  # 0b110
```

```
  1100  (12)
^ 1010  (10)
------
  0110  (6)
```

### Bitwise NOT (`~`)

Inverts all bits (flips 0s and 1s). In Python, `~x` equals `-(x+1)`:

```python
a = 10    # Binary: 1010

print(~a)          # -11
print(bin(~a))     # -0b1011
```

### Left Shift (`<<`)

Shifts bits to the left, filling with zeros. Each shift left multiplies by 2:

```python
a = 5     # Binary: 101

print(a << 1)      # 10  (Binary: 1010) — multiply by 2
print(a << 2)      # 20  (Binary: 10100) — multiply by 4
print(a << 3)      # 40  (Binary: 101000) — multiply by 8
```

### Right Shift (`>>`)

Shifts bits to the right. Each shift right divides by 2 (floor division):

```python
a = 20    # Binary: 10100

print(a >> 1)      # 10  (Binary: 1010) — divide by 2
print(a >> 2)      # 5   (Binary: 101) — divide by 4
```

---

### Hands-on Lab: Bitwise Operators

**Lab Goal:** Practice bitwise operations and understand binary representation.

**Exercise 1:** Write a program that shows the binary representation of two numbers and the result of all bitwise operations.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"\na = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")
print(f"\na & b  = {a & b:>5}  (binary: {bin(a & b)})")
print(f"a | b  = {a | b:>5}  (binary: {bin(a | b)})")
print(f"a ^ b  = {a ^ b:>5}  (binary: {bin(a ^ b)})")
print(f"~a     = {~a:>5}  (binary: {bin(~a)})")
print(f"~b     = {~b:>5}  (binary: {bin(~b)})")
print(f"a << 1 = {a << 1:>5}  (binary: {bin(a << 1)})")
print(f"a >> 1 = {a >> 1:>5}  (binary: {bin(a >> 1)})")
```

**Exercise 2:** Use bitwise AND to check if a number is even or odd. (Hint: the last bit of an odd number is always 1.)

```python
num = int(input("Enter a number: "))

if num & 1:
    print(f"{num} is odd")
else:
    print(f"{num} is even")
```

**Exercise 3:** Swap two numbers using XOR (without a temporary variable).

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"Before: a = {a}, b = {b}")

a = a ^ b
b = a ^ b
a = a ^ b

print(f"After:  a = {a}, b = {b}")
```

**Exercise 4:** Use left shift to calculate powers of 2.

```python
print("Powers of 2 using left shift:")
for i in range(11):
    print(f"1 << {i:2} = {1 << i:>5}")
```

Expected Output:

```
Powers of 2 using left shift:
1 <<  0 =     1
1 <<  1 =     2
1 <<  2 =     4
1 <<  3 =     8
1 <<  4 =    16
1 <<  5 =    32
1 <<  6 =    64
1 <<  7 =   128
1 <<  8 =   256
1 <<  9 =   512
1 << 10 =  1024
```

---

### Graded Assessment: Logic and Bitwise Operators

**Challenge 1:** Write a program that determines if a year is valid for a specific event. The event runs in years that are divisible by 4 but not by 100, OR divisible by 400. Also, the year must be between 2000 and 2100 inclusive.

```python
year = int(input("Enter a year: "))

is_valid_year = year >= 2000 and year <= 2100
is_special = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_valid_year and is_special:
    print(f"The event runs in {year}.")
else:
    if not is_valid_year:
        print(f"{year} is outside the valid range (2000-2100).")
    else:
        print(f"No event in {year}.")
```

**Challenge 2:** Write a program that uses bitwise operations to set, clear, and toggle specific bits in a number. Display the binary representation after each operation.

```python
num = int(input("Enter a number: "))
bit_pos = int(input("Enter bit position (0-based): "))

mask = 1 << bit_pos

print(f"\nOriginal: {num} (binary: {bin(num)})")

# Set the bit (turn it ON)
set_result = num | mask
print(f"Set bit {bit_pos}: {set_result} (binary: {bin(set_result)})")

# Clear the bit (turn it OFF)
clear_result = num & ~mask
print(f"Clear bit {bit_pos}: {clear_result} (binary: {bin(clear_result)})")

# Toggle the bit (flip it)
toggle_result = num ^ mask
print(f"Toggle bit {bit_pos}: {toggle_result} (binary: {bin(toggle_result)})")

# Check the bit
is_set = (num >> bit_pos) & 1
print(f"Bit {bit_pos} is {'set' if is_set else 'not set'}")
```

---

# Module 5 – Exploring Python Lists

This module covers Python lists — ordered, mutable collections that can hold any type of data. You will learn to create lists, use list methods, iterate over them, slice them, search them, and work with nested (2D and 3D) lists.

### Learning Objectives

- Understand the concept of lists and their importance in storing and manipulating data.
- Gain proficiency in using list methods to add, remove, and modify elements.
- Learn how to iterate over lists to access and process individual elements.
- Develop proficiency in slicing lists to extract subsets of elements.
- Work with nested list structures (2D and 3D).

---

## Lists

A list is an **ordered, mutable** collection of items. Lists are created with square brackets:

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
empty = []

print(fruits)      # ['apple', 'banana', 'cherry']
print(numbers)     # [1, 2, 3, 4, 5]
print(mixed)       # [1, 'hello', 3.14, True, None]
print(empty)       # []
```

### Accessing Elements

Lists are **zero-indexed** — the first element is at index 0:

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])      # apple
print(fruits[1])      # banana
print(fruits[-1])     # date (last element)
print(fruits[-2])     # cherry (second to last)
```

### Modifying Elements

Since lists are mutable, you can change elements directly:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)    # ['apple', 'blueberry', 'cherry']
```

### List Length

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))    # 3
```

### Checking Membership

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)       # True
print("grape" in fruits)        # False
print("grape" not in fruits)    # True
```

---

### Hands-on Lab: Lists

**Lab Goal:** Practice creating and accessing list elements.

**Exercise 1:** Create a list of 5 favorite movies and print each one with its index.

```python
movies = ["Inception", "The Matrix", "Interstellar", "Gladiator", "Arrival"]

print("My favorite movies:")
for i in range(len(movies)):
    print(f"  {i + 1}. {movies[i]}")
```

**Exercise 2:** Modify elements in a list.

```python
colors = ["red", "green", "blue", "yellow", "purple"]
print("Original:", colors)

colors[0] = "crimson"
colors[-1] = "violet"
print("Modified:", colors)
```

**Exercise 3:** Check if items exist in a list.

```python
shopping = ["milk", "bread", "eggs", "butter", "cheese"]

item = input("What are you looking for? ")
if item in shopping:
    print(f"'{item}' is on the shopping list.")
else:
    print(f"'{item}' is NOT on the shopping list.")
```

---

## Lists – Methods

Lists have many built-in methods for manipulation.

### Adding Elements

```python
fruits = ["apple", "banana"]

# append: add to the end
fruits.append("cherry")
print(fruits)    # ['apple', 'banana', 'cherry']

# insert: add at a specific position
fruits.insert(1, "blueberry")
print(fruits)    # ['apple', 'blueberry', 'banana', 'cherry']

# extend: add multiple items from another list
fruits.extend(["date", "elderberry"])
print(fruits)    # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']
```

### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# remove: remove the first occurrence of a value
fruits.remove("banana")
print(fruits)    # ['apple', 'cherry', 'banana', 'date']

# pop: remove and return element at index (default: last)
last = fruits.pop()
print(last)      # date
print(fruits)    # ['apple', 'cherry', 'banana']

second = fruits.pop(1)
print(second)    # cherry
print(fruits)    # ['apple', 'banana']

# clear: remove all elements
fruits.clear()
print(fruits)    # []
```

### Sorting and Reversing

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort: sort in place
numbers.sort()
print(numbers)    # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)    # [9, 6, 5, 4, 3, 2, 1, 1]

# reverse: reverse in place
numbers.reverse()
print(numbers)    # [1, 1, 2, 3, 4, 5, 6, 9]

# sorted: return new sorted list (original unchanged)
original = [3, 1, 4, 1, 5]
new_list = sorted(original)
print(original)    # [3, 1, 4, 1, 5]
print(new_list)    # [1, 1, 3, 4, 5]
```

### Other Useful Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print(numbers.count(1))      # 2 (how many times 1 appears)
print(numbers.index(5))      # 4 (index of first occurrence of 5)

# Copy a list
copy = numbers.copy()
print(copy)
```

---

### Hands-on Lab: Lists – Methods

**Lab Goal:** Practice using list methods.

**Exercise 1:** Build a to-do list application.

```python
todo_list = []

# Add items
todo_list.append("Buy groceries")
todo_list.append("Clean house")
todo_list.append("Walk the dog")
todo_list.append("Read a book")
print("To-do list:", todo_list)

# Insert an urgent task at the beginning
todo_list.insert(0, "Pay electricity bill")
print("Updated list:", todo_list)

# Complete (remove) a task
completed = todo_list.pop(2)   # Remove "Clean house"
print(f"Completed: {completed}")
print("Remaining:", todo_list)

# Sort the list
todo_list.sort()
print("Sorted:", todo_list)
```

**Exercise 2:** Sort a list of names alphabetically and reverse alphabetically.

```python
names = ["Charlie", "Alice", "Eve", "Bob", "Dave"]

print("Original:", names)

names.sort()
print("A-Z:", names)

names.sort(reverse=True)
print("Z-A:", names)
```

**Exercise 3:** Remove all duplicates from a list while preserving order.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original:", numbers)
print("Unique:", unique)
```

---

## Iterating Lists

### Using a `for` Loop

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Using `enumerate()` for Index and Value

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

Output:

```
0: apple
1: banana
2: cherry
```

### Using `range()` and `len()`

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"fruits[{i}] = {fruits[i]}")
```

---

### Hands-on Lab: Iterating Lists

**Lab Goal:** Practice different techniques for iterating over lists.

**Exercise 1:** Sum all numbers in a list.

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Sum: {total}")         # 150
print(f"Average: {total / len(numbers)}")  # 30.0
```

**Exercise 2:** Find the largest and smallest values in a list without using `min()`/`max()`.

```python
numbers = [34, 7, 23, 89, 12, 56, 3, 45]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"Largest: {largest}")     # 89
print(f"Smallest: {smallest}")   # 3
```

**Exercise 3:** Use `enumerate` to create a numbered menu.

```python
menu_items = ["Pizza", "Burger", "Salad", "Pasta", "Sushi"]

print("=== MENU ===")
for i, item in enumerate(menu_items, start=1):
    print(f"  {i}. {item}")

choice = int(input("Pick a number: "))
if 1 <= choice <= len(menu_items):
    print(f"You selected: {menu_items[choice - 1]}")
else:
    print("Invalid choice!")
```

---

## Understanding Lists

### Lists Are Mutable Objects

When you assign a list to another variable, both variables point to the **same** list:

```python
a = [1, 2, 3]
b = a              # b points to the same list as a

b.append(4)
print(a)           # [1, 2, 3, 4] — a is also changed!
print(b)           # [1, 2, 3, 4]
```

To create an independent copy:

```python
a = [1, 2, 3]
b = a.copy()       # or b = list(a) or b = a[:]

b.append(4)
print(a)           # [1, 2, 3] — a is unchanged
print(b)           # [1, 2, 3, 4]
```

### List Concatenation and Repetition

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(combined)    # [1, 2, 3, 4, 5, 6]

repeated = [0] * 5
print(repeated)    # [0, 0, 0, 0, 0]
```

### List Comprehensions

A compact way to create lists:

```python
# Traditional approach
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension (same result)
squares = [x ** 2 for x in range(10)]
print(squares)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With a condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)    # [0, 4, 16, 36, 64]
```

---

### Hands-on Lab: Understanding Lists

**Lab Goal:** Deepen your understanding of list behavior.

**Exercise 1:** Demonstrate the difference between aliasing and copying.

```python
# Aliasing
original = [1, 2, 3, 4, 5]
alias = original

alias[0] = 99
print("Original:", original)   # [99, 2, 3, 4, 5] — changed!
print("Alias:", alias)         # [99, 2, 3, 4, 5]

# Copying
original = [1, 2, 3, 4, 5]
copy = original.copy()

copy[0] = 99
print("Original:", original)   # [1, 2, 3, 4, 5] — unchanged!
print("Copy:", copy)           # [99, 2, 3, 4, 5]
```

**Exercise 2:** Use list comprehensions to create various lists.

```python
# First 10 cubes
cubes = [x ** 3 for x in range(1, 11)]
print("Cubes:", cubes)

# All uppercase letters from a string
text = "Hello World 123"
letters = [ch for ch in text if ch.isalpha()]
print("Letters:", letters)

# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print("Fahrenheit:", fahrenheit)
```

---

## Slicing Lists

Slicing extracts a subset of a list using the syntax `list[start:stop:step]`.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])       # [2, 3, 4] (index 2 up to but not including 5)
print(numbers[:4])        # [0, 1, 2, 3] (from the start to index 3)
print(numbers[6:])        # [6, 7, 8, 9] (from index 6 to the end)
print(numbers[::2])       # [0, 2, 4, 6, 8] (every other element)
print(numbers[1::2])      # [1, 3, 5, 7, 9] (odd-indexed elements)
print(numbers[::-1])      # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
print(numbers[-3:])       # [7, 8, 9] (last 3 elements)
```

### Modifying with Slices

```python
numbers = [0, 1, 2, 3, 4, 5]

# Replace a range
numbers[2:4] = [20, 30]
print(numbers)    # [0, 1, 20, 30, 4, 5]

# Insert with slices
numbers[2:2] = [15, 16]
print(numbers)    # [0, 1, 15, 16, 20, 30, 4, 5]

# Delete with slices
numbers[2:4] = []
print(numbers)    # [0, 1, 20, 30, 4, 5]
```

---

### Hands-on Lab: Slicing Lists

**Lab Goal:** Practice slicing to extract and manipulate subsets of lists.

**Exercise 1:** Extract various slices from a list.

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print("First 3:", letters[:3])
print("Last 3:", letters[-3:])
print("Middle:", letters[3:7])
print("Every 2nd:", letters[::2])
print("Reversed:", letters[::-1])
print("Every 3rd from index 1:", letters[1::3])
```

**Exercise 2:** Rotate a list to the left by `n` positions.

```python
data = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3

rotated = data[n:] + data[:n]
print(f"Rotated left by {n}:", rotated)   # [4, 5, 6, 7, 8, 1, 2, 3]
```

---

## Finding in Lists

### Using `index()` and `count()`

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

print(fruits.index("banana"))      # 1 (first occurrence)
print(fruits.count("banana"))      # 2
```

### Safe Searching with `in`

```python
fruits = ["apple", "banana", "cherry"]

search = "grape"
if search in fruits:
    print(f"Found '{search}' at index {fruits.index(search)}")
else:
    print(f"'{search}' not found in the list.")
```

### Finding All Occurrences

```python
numbers = [1, 3, 5, 3, 7, 3, 9]
target = 3

indices = [i for i, num in enumerate(numbers) if num == target]
print(f"All indices of {target}: {indices}")    # [1, 3, 5]
```

---

### Hands-on Lab: Finding in Lists

**Lab Goal:** Practice searching for elements in lists.

**Exercise 1:** Write a program that searches for a value and reports all its positions.

```python
data = [10, 20, 30, 20, 40, 20, 50]
target = int(input("Search for: "))

positions = []
for i in range(len(data)):
    if data[i] == target:
        positions.append(i)

if positions:
    print(f"Found {target} at positions: {positions}")
else:
    print(f"{target} not found.")
```

**Exercise 2:** Find the second-largest number in a list.

```python
numbers = [45, 12, 89, 67, 23, 89, 34]

unique_sorted = sorted(set(numbers), reverse=True)
if len(unique_sorted) >= 2:
    print(f"Second largest: {unique_sorted[1]}")
else:
    print("Not enough unique values.")
```

---

## Nested Lists – 2D

A 2D list is a list of lists — like a table or matrix.

```python
# A 3x3 grid
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
print(matrix[0])        # [1, 2, 3] (first row)
print(matrix[0][0])     # 1 (row 0, column 0)
print(matrix[1][2])     # 6 (row 1, column 2)
print(matrix[2][1])     # 8 (row 2, column 1)
```

### Iterating a 2D List

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(f"{element:3}", end="")
    print()
```

---

### Hands-on Lab: Nested Lists – 2D

**Lab Goal:** Work with 2D lists as tables and matrices.

**Exercise 1:** Create and display a 2D list representing student grades.

```python
grades = [
    ["Alice", 85, 92, 78],
    ["Bob", 79, 88, 95],
    ["Carol", 92, 85, 90]
]

print(f"{'Name':<10}{'Test1':>6}{'Test2':>6}{'Test3':>6}{'Avg':>8}")
print("-" * 36)

for student in grades:
    name = student[0]
    scores = student[1:]
    avg = sum(scores) / len(scores)
    print(f"{name:<10}{scores[0]:>6}{scores[1]:>6}{scores[2]:>6}{avg:>8.1f}")
```

**Exercise 2:** Transpose a matrix (swap rows and columns).

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
cols = len(matrix[0])

transposed = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

print("Original:")
for row in matrix:
    print(row)

print("\nTransposed:")
for row in transposed:
    print(row)
```

---

## Nested Lists – 3D

A 3D list is a list of 2D lists — think of it as a cube or a stack of matrices.

```python
# 3D list: 2 layers, each 3x3
cube = [
    [  # Layer 0
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [  # Layer 1
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
]

print(cube[0])            # First layer (a 2D list)
print(cube[0][1])         # First layer, second row: [4, 5, 6]
print(cube[0][1][2])      # First layer, second row, third element: 6
print(cube[1][2][0])      # Second layer, third row, first element: 16
```

---

### Hands-on Lab: Nested Lists – 3D

**Lab Goal:** Practice accessing and iterating through 3D data.

**Exercise 1:** Create and navigate a 3D list representing a building (floors → rooms → items).

```python
building = [
    [  # Floor 0 (Ground)
        ["reception desk", "chairs", "coffee table"],
        ["printer", "scanner", "shredder"]
    ],
    [  # Floor 1
        ["desk", "computer", "bookshelf"],
        ["whiteboard", "projector", "conference table"]
    ],
    [  # Floor 2
        ["server rack", "UPS", "network switch"],
        ["fire extinguisher", "first aid kit"]
    ]
]

for floor_idx, floor in enumerate(building):
    print(f"\n--- Floor {floor_idx} ---")
    for room_idx, room in enumerate(floor):
        print(f"  Room {room_idx}: {', '.join(room)}")
```

**Exercise 2:** Sum all elements in a 3D list of numbers.

```python
data_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

total = 0
for layer in data_3d:
    for row in layer:
        for value in row:
            total += value

print(f"Total sum: {total}")   # 78
```

---

### Graded Assessment: Lists

**Challenge 1:** Write a program that merges two sorted lists into a single sorted list without using the `sort()` method.

```python
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

merged = []
i, j = 0, 0

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

# Add remaining elements
merged.extend(list1[i:])
merged.extend(list2[j:])

print("Merged:", merged)
```

**Challenge 2:** Write a tic-tac-toe board display using a 2D list. Include a function to check if someone has won.

```python
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", " ", "X"]
]

# Display the board
print("  0   1   2")
for i, row in enumerate(board):
    print(f"{i} {'|'.join(f' {cell} ' for cell in row)}")
    if i < 2:
        print("  -----------")

# Check for a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

winner = check_winner(board)
if winner:
    print(f"\n{winner} wins!")
else:
    print("\nNo winner yet.")
```

---

# Module 6 – Python Functions

This module introduces functions — reusable blocks of code that perform a specific task. You will learn to define functions, pass arguments, return values, understand scope, and use lists as arguments.

### Learning Objectives

- Understand the concept and purpose of functions in Python.
- Gain proficiency in defining and calling functions.
- Learn about function arguments (positional and keyword).
- Acquire practical skills in using the `return` statement.
- Understand variable scopes (local vs. global).

---

## Functions

A **function** is a named block of code that runs only when called. Functions help you organize code, avoid repetition, and make programs easier to understand.

### Defining and Calling a Function

```python
def greet():
    print("Hello, World!")

# Call the function
greet()       # Output: Hello, World!
greet()       # You can call it as many times as you want
```

### Functions with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")      # Hello, Alice!
greet("Bob")        # Hello, Bob!
```

### Functions with Multiple Parameters

```python
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(3, 5)       # 3 + 5 = 8
add(10, 20)     # 10 + 20 = 30
```

---

### Hands-on Lab: Functions

**Lab Goal:** Practice defining and calling functions.

**Exercise 1:** Write a function that prints a box around a message.

```python
def print_box(message):
    border = "+" + "-" * (len(message) + 2) + "+"
    print(border)
    print(f"| {message} |")
    print(border)

print_box("Hello, Python!")
print_box("Welcome to functions!")
```

**Exercise 2:** Write a function that calculates the area of a circle.

```python
def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    print(f"A circle with radius {radius} has area {area:.2f}")

circle_area(5)
circle_area(10)
circle_area(2.5)
```

**Exercise 3:** Write a function that prints a multiplication table for a given number.

```python
def multiplication_table(n, up_to=12):
    print(f"\n--- Multiplication Table for {n} ---")
    for i in range(1, up_to + 1):
        print(f"{n} x {i:2} = {n * i:3}")

multiplication_table(7)
multiplication_table(13, 5)
```

---

## Arguments

### Positional Arguments

Arguments are matched by position:

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Buddy")       # I have a dog named Buddy.
describe_pet("cat", "Whiskers")    # I have a cat named Whiskers.
```

### Keyword Arguments

You can specify arguments by name, regardless of order:

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Buddy", animal="dog")    # Same result
```

### Default Values

Parameters can have default values:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                  # Hello, Alice!
greet("Bob", "Good morning")   # Good morning, Bob!
```

### Arbitrary Arguments (`*args`)

Accept any number of positional arguments:

```python
def total(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"Total: {result}")

total(1, 2, 3)              # Total: 6
total(10, 20, 30, 40, 50)   # Total: 150
```

### Arbitrary Keyword Arguments (`**kwargs`)

Accept any number of keyword arguments:

```python
def print_info(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=30, city="New York")
```

---

### Hands-on Lab: Arguments

**Lab Goal:** Practice using different types of function arguments.

**Exercise 1:** Write a function with default arguments for formatting a price.

```python
def format_price(amount, currency="$", decimals=2):
    print(f"{currency}{amount:.{decimals}f}")

format_price(19.99)                         # $19.99
format_price(19.99, "€")                    # €19.99
format_price(1234.5, "¥", 0)               # ¥1234
format_price(0.12345, decimals=4)           # $0.1235
```

**Exercise 2:** Write a function that accepts any number of scores and prints the average.

```python
def average(*scores):
    if len(scores) == 0:
        print("No scores provided.")
        return
    avg = sum(scores) / len(scores)
    print(f"Scores: {scores}")
    print(f"Average: {avg:.1f}")

average(85, 92, 78)
average(100, 90, 95, 88, 92)
```

**Exercise 3:** Write a function that builds a user profile using keyword arguments.

```python
def build_profile(first, last, **details):
    profile = {"first_name": first, "last_name": last}
    for key, value in details.items():
        profile[key] = value
    return profile

user = build_profile("Ada", "Lovelace", age=36, field="Mathematics", hobby="Piano")
for key, value in user.items():
    print(f"  {key}: {value}")
```

---

## Return Statement

The `return` statement sends a value back to the caller and exits the function.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)          # 8
print(add(10, 20))     # 30 (use directly)
```

### Returning Multiple Values

Python can return multiple values as a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 7, 1, 9, 4])
print(f"Min: {low}, Max: {high}")    # Min: 1, Max: 9
```

### Functions Without `return`

If a function doesn't have a `return` statement, it returns `None`:

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")
print(result)    # None
```

---

### Hands-on Lab: Return Statement

**Lab Goal:** Practice writing functions that return values.

**Exercise 1:** Write a function that returns whether a number is prime.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test it
for num in range(1, 21):
    if is_prime(num):
        print(num, end=" ")
print()
# Output: 2 3 5 7 11 13 17 19
```

**Exercise 2:** Write a function that returns basic statistics for a list of numbers.

```python
def statistics(numbers):
    n = len(numbers)
    total = sum(numbers)
    average = total / n
    sorted_nums = sorted(numbers)

    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]

    return total, average, min(numbers), max(numbers), median

data = [23, 45, 12, 67, 34, 89, 56]
total, avg, low, high, med = statistics(data)

print(f"Sum: {total}")
print(f"Average: {avg:.2f}")
print(f"Min: {low}")
print(f"Max: {high}")
print(f"Median: {med}")
```

---

## List as Argument

When you pass a list to a function, the function receives a **reference** to the original list. Changes inside the function affect the original list.

```python
def double_values(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2

my_list = [1, 2, 3, 4, 5]
print("Before:", my_list)    # [1, 2, 3, 4, 5]

double_values(my_list)
print("After:", my_list)     # [2, 4, 6, 8, 10]
```

### Avoiding Side Effects

If you don't want to modify the original, pass a copy:

```python
def double_values(numbers):
    result = []
    for n in numbers:
        result.append(n * 2)
    return result

original = [1, 2, 3, 4, 5]
doubled = double_values(original)
print("Original:", original)    # [1, 2, 3, 4, 5] — unchanged
print("Doubled:", doubled)      # [2, 4, 6, 8, 10]
```

---

### Hands-on Lab: List as Argument

**Lab Goal:** Practice passing lists to functions and managing side effects.

**Exercise 1:** Write a function that filters a list, returning only values above a threshold.

```python
def filter_above(numbers, threshold):
    return [n for n in numbers if n > threshold]

scores = [45, 82, 67, 91, 53, 78, 95, 60]
passing = filter_above(scores, 70)
print("All scores:", scores)
print("Passing scores:", passing)
```

**Exercise 2:** Write a function that sorts a list without modifying the original.

```python
def safe_sort(items):
    return sorted(items)

original = [5, 2, 8, 1, 9, 3]
sorted_version = safe_sort(original)

print("Original:", original)       # [5, 2, 8, 1, 9, 3]
print("Sorted:", sorted_version)   # [1, 2, 3, 5, 8, 9]
```

---

## Scopes

**Scope** determines where a variable can be accessed. Python has two main scopes:

### Local Scope

Variables created inside a function exist only within that function:

```python
def my_function():
    x = 10          # Local variable
    print(x)

my_function()       # 10
# print(x)          # Error! x is not defined outside the function
```

### Global Scope

Variables created outside any function are global:

```python
message = "Hello"    # Global variable

def greet():
    print(message)   # Can READ global variables

greet()              # Hello
```

### The `global` Keyword

To **modify** a global variable inside a function, use the `global` keyword:

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
increment()
print(counter)    # 3
```

### Best Practice

Avoid using `global` when possible. Instead, pass values as arguments and use `return`:

```python
def increment(counter):
    return counter + 1

count = 0
count = increment(count)
count = increment(count)
count = increment(count)
print(count)    # 3
```

---

### Hands-on Lab: Scopes

**Lab Goal:** Understand local and global scopes.

**Exercise 1:** Predict the output, then run to verify.

```python
x = "global"

def outer():
    x = "outer"

    def inner():
        x = "inner"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)

# Output:
# Inner: inner
# Outer: outer
# Global: global
```

**Exercise 2:** Demonstrate the global keyword.

```python
total = 0

def add_to_total(amount):
    global total
    total += amount
    print(f"Added {amount}. Total is now {total}")

add_to_total(10)
add_to_total(25)
add_to_total(5)
print(f"Final total: {total}")
```

---

## Arguments Explained

A deeper look at how Python passes arguments.

### Mutable vs. Immutable Arguments

- **Immutable** types (int, float, str, tuple): The function cannot change the original value.
- **Mutable** types (list, dict, set): The function CAN change the original value.

```python
def try_change_int(x):
    x = x + 10
    print(f"Inside: x = {x}")

num = 5
try_change_int(num)
print(f"Outside: num = {num}")    # Still 5 — integers are immutable

def try_change_list(lst):
    lst.append(99)
    print(f"Inside: lst = {lst}")

my_list = [1, 2, 3]
try_change_list(my_list)
print(f"Outside: my_list = {my_list}")   # [1, 2, 3, 99] — lists are mutable
```

### Unpacking Arguments

Use `*` to unpack a list into positional arguments:

```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]
print(add(*numbers))    # 60

# Use ** to unpack a dictionary into keyword arguments
def greet(name, greeting):
    print(f"{greeting}, {name}!")

params = {"name": "Alice", "greeting": "Good morning"}
greet(**params)     # Good morning, Alice!
```

---

### Hands-on Lab: Arguments Explained

**Lab Goal:** Understand pass-by-object-reference behavior and argument unpacking.

**Exercise 1:** Demonstrate how mutable and immutable arguments behave.

```python
def modify(num, text, items):
    num += 100
    text += " world"
    items.append("new item")
    print(f"  Inside — num: {num}, text: '{text}', items: {items}")

my_num = 42
my_text = "hello"
my_items = ["a", "b"]

print(f"Before — num: {my_num}, text: '{my_text}', items: {my_items}")
modify(my_num, my_text, my_items)
print(f"After  — num: {my_num}, text: '{my_text}', items: {my_items}")
# num and text are unchanged; items has the new element
```

**Exercise 2:** Use argument unpacking with * and **.

```python
def create_greeting(salutation, name, punctuation):
    return f"{salutation}, {name}{punctuation}"

# Unpack from a list
args = ["Hello", "World", "!"]
print(create_greeting(*args))

# Unpack from a dictionary
kwargs = {"salutation": "Good morning", "name": "Alice", "punctuation": "."}
print(create_greeting(**kwargs))
```

---

### Graded Assessment: Functions

**Challenge 1:** Write a function `caesar_cipher(text, shift)` that encrypts text using a Caesar cipher (shift each letter by `shift` positions).

```python
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

message = "Hello, World!"
encrypted = caesar_cipher(message, 3)
decrypted = caesar_cipher(encrypted, -3)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

**Challenge 2:** Write a function that takes a list of numbers and returns a dictionary with keys "even" and "odd", each containing a list of the corresponding numbers.

```python
def separate_even_odd(numbers):
    result = {"even": [], "odd": []}
    for num in numbers:
        if num % 2 == 0:
            result["even"].append(num)
        else:
            result["odd"].append(num)
    return result

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
separated = separate_even_odd(nums)
print(f"Even: {separated['even']}")
print(f"Odd: {separated['odd']}")
```

---

# Module 7 – Tuples and Dictionaries

This module covers two essential data structures: tuples (immutable sequences) and dictionaries (key-value mappings).

### Learning Objectives

- Understand the concept and usage of tuples as immutable ordered collections.
- Gain proficiency in working with dictionaries for efficient data storage and retrieval.

---

## Tuples

A **tuple** is an **ordered, immutable** collection. Once created, its elements cannot be changed.

### Creating Tuples

```python
# With parentheses
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14, True)

# Without parentheses (packing)
point = 5, 10
print(point)           # (5, 10)

# Single-element tuple (needs trailing comma)
single = (42,)
print(type(single))    # <class 'tuple'>

not_tuple = (42)
print(type(not_tuple)) # <class 'int'> — just parentheses!

# Empty tuple
empty = ()
print(len(empty))      # 0
```

### Accessing Elements

```python
colors = ("red", "green", "blue", "yellow")

print(colors[0])       # red
print(colors[-1])      # yellow
print(colors[1:3])     # ('green', 'blue')
```

### Tuples Are Immutable

```python
colors = ("red", "green", "blue")
# colors[0] = "purple"    # TypeError! Tuples don't support assignment
```

### Tuple Operations

```python
# Concatenation
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)           # (1, 2, 3, 4, 5, 6)

# Repetition
d = (0,) * 5
print(d)           # (0, 0, 0, 0, 0)

# Membership
print(3 in a)      # True
print(7 in a)      # False

# Length, min, max
print(len(a))      # 3
print(min(a))      # 1
print(max(a))      # 3

# Count and index
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2))     # 3
print(nums.index(3))     # 2
```

### Tuple Unpacking

```python
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)      # 10 20 30

# Swapping with tuples
a, b = 1, 2
a, b = b, a
print(a, b)          # 2 1

# Using * to capture remaining items
first, *rest = (1, 2, 3, 4, 5)
print(first)         # 1
print(rest)          # [2, 3, 4, 5]
```

### When to Use Tuples vs. Lists

- Use **tuples** for data that shouldn't change (coordinates, RGB colors, database records).
- Use **lists** for data that needs to be modified (shopping lists, to-do items, user input).

---

### Hands-on Lab: Tuples

**Lab Goal:** Practice creating and using tuples.

**Exercise 1:** Create tuples representing geographic coordinates and calculate the distance between two points.

```python
def distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return (dx ** 2 + dy ** 2) ** 0.5

point_a = (3, 4)
point_b = (7, 1)

dist = distance(point_a, point_b)
print(f"Distance from {point_a} to {point_b}: {dist:.2f}")
```

**Exercise 2:** Use tuple unpacking to process student records.

```python
students = [
    ("Alice", 22, "Computer Science"),
    ("Bob", 20, "Mathematics"),
    ("Carol", 21, "Physics")
]

for name, age, major in students:
    print(f"{name} is {age} years old, studying {major}.")
```

**Exercise 3:** Return multiple values from a function using tuples.

```python
def analyze_text(text):
    words = len(text.split())
    chars = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    return words, chars, sentences

sample = "Hello there. How are you? I hope you are fine!"
word_count, char_count, sentence_count = analyze_text(sample)

print(f"Words: {word_count}")
print(f"Characters: {char_count}")
print(f"Sentences: {sentence_count}")
```

---

## Dictionaries

A **dictionary** stores data as **key-value pairs**. Keys must be unique and immutable (strings, numbers, or tuples). Values can be any type.

### Creating Dictionaries

```python
# With curly braces
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# With dict() constructor
person2 = dict(name="Bob", age=25, city="London")

# Empty dictionary
empty = {}
```

### Accessing Values

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

print(person["name"])          # Alice
print(person.get("age"))       # 30
print(person.get("email", "N/A"))   # N/A (default if key not found)

# person["email"]  # KeyError! Use .get() to avoid errors
```

### Adding and Modifying

```python
person = {"name": "Alice", "age": 30}

# Add a new key-value pair
person["city"] = "New York"

# Modify an existing value
person["age"] = 31

print(person)
# {'name': 'Alice', 'age': 31, 'city': 'New York'}
```

### Removing Items

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# del keyword
del person["city"]
print(person)    # {'name': 'Alice', 'age': 30}

# pop method (returns the removed value)
age = person.pop("age")
print(age)       # 30
print(person)    # {'name': 'Alice'}
```

### Dictionary Methods

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

print(person.keys())       # dict_keys(['name', 'age', 'city'])
print(person.values())     # dict_values(['Alice', 30, 'New York'])
print(person.items())      # dict_items([('name', 'Alice'), ('age', 30), ...])

# Check if a key exists
print("name" in person)    # True
print("email" in person)   # False
```

### Iterating Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Iterate over keys
for key in person:
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehensions

```python
# Create a dictionary of squares
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter items
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)    # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

### Hands-on Lab: Dictionaries

**Lab Goal:** Practice creating and manipulating dictionaries.

**Exercise 1:** Build a contact book.

```python
contacts = {}

# Add contacts
contacts["Alice"] = {"phone": "555-0101", "email": "alice@example.com"}
contacts["Bob"] = {"phone": "555-0202", "email": "bob@example.com"}
contacts["Carol"] = {"phone": "555-0303", "email": "carol@example.com"}

# Look up a contact
name = input("Look up contact: ")
if name in contacts:
    info = contacts[name]
    print(f"  Phone: {info['phone']}")
    print(f"  Email: {info['email']}")
else:
    print(f"'{name}' not found.")
```

**Exercise 2:** Count word frequencies in a sentence.

```python
text = input("Enter a sentence: ").lower()
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord frequencies:")
for word, count in sorted(frequency.items()):
    print(f"  '{word}': {count}")
```

**Exercise 3:** Merge two dictionaries and handle conflicts.

```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

# Method 1: Using update (dict2 values overwrite dict1)
merged = dict1.copy()
merged.update(dict2)
print("Merged (update):", merged)

# Method 2: Using ** unpacking (Python 3.5+)
merged2 = {**dict1, **dict2}
print("Merged (**):", merged2)

# Method 3: Keep the sum of conflicting values
merged3 = {}
for key in set(list(dict1.keys()) + list(dict2.keys())):
    merged3[key] = dict1.get(key, 0) + dict2.get(key, 0)
print("Merged (sum):", merged3)
```

---

### Graded Assessment: Tuples & Dictionaries

**Challenge 1:** Write a program that uses a dictionary to store and look up US state capitals.

```python
capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "New York": "Albany",
    "Florida": "Tallahassee",
    "Illinois": "Springfield"
}

state = input("Enter a US state: ")
capital = capitals.get(state)

if capital:
    print(f"The capital of {state} is {capital}.")
else:
    print(f"Sorry, I don't have data for '{state}'.")
    print(f"Available states: {', '.join(capitals.keys())}")
```

**Challenge 2:** Write a program that converts a list of tuples (name, score) into a dictionary grouped by grade.

```python
students = [
    ("Alice", 92), ("Bob", 78), ("Carol", 85),
    ("Dave", 65), ("Eve", 95), ("Frank", 72)
]

def get_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

grade_groups = {}
for name, score in students:
    grade = get_grade(score)
    if grade not in grade_groups:
        grade_groups[grade] = []
    grade_groups[grade].append((name, score))

for grade in sorted(grade_groups.keys()):
    print(f"\nGrade {grade}:")
    for name, score in grade_groups[grade]:
        print(f"  {name}: {score}")
```

---

# Module 8 – Exceptions

This module covers errors and exceptions in Python — essential concepts for writing robust programs that can handle unexpected situations gracefully.

### Learning Objectives

- Understand the concept of errors and exceptions in Python.
- Learn about the hierarchy of exceptions and how different types are categorized.
- Test understanding through a quiz on errors and exceptions.

---

## Exploring Python Error Handling

### Types of Errors

**Syntax Errors** — detected before the program runs:

```python
# Missing colon
# if True
#     print("hello")

# Unclosed parenthesis
# print("hello"

# Invalid assignment
# 5 = x
```

**Runtime Errors (Exceptions)** — occur during execution:

```python
# ZeroDivisionError
# print(10 / 0)

# NameError
# print(undefined_variable)

# TypeError
# print("hello" + 5)

# IndexError
# my_list = [1, 2, 3]
# print(my_list[10])

# KeyError
# my_dict = {"a": 1}
# print(my_dict["b"])

# ValueError
# int("hello")

# FileNotFoundError
# open("nonexistent.txt")
```

### The `try-except` Block

Catch and handle exceptions to prevent program crashes:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catching Multiple Exceptions

```python
try:
    data = [1, 2, 3]
    index = int(input("Enter an index: "))
    print(data[index])
except (ValueError, IndexError) as e:
    print(f"Error: {e}")
```

### The `else` and `finally` Clauses

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # Runs only if NO exception occurred
    print(f"Result: {result}")
finally:
    # ALWAYS runs, regardless of exceptions
    print("Operation complete.")
```

### Raising Exceptions

You can raise exceptions intentionally:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

try:
    user_age = set_age(-5)
except ValueError as e:
    print(f"Error: {e}")
```

### Creating Custom Exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw ${amount}. Balance is only ${balance}."
        )

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
```

---

## Understanding the Exception Hierarchy

Python's exceptions form a hierarchy. At the top is `BaseException`. Most exceptions you'll encounter inherit from `Exception`.

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── AttributeError
    ├── NameError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── IsADirectoryError
    ├── RuntimeError
    └── StopIteration
```

### Why the Hierarchy Matters

When you catch a parent exception, you also catch all its children:

```python
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except LookupError:
    # Catches both IndexError and KeyError
    print("Lookup failed!")
```

### Best Practices for Exception Handling

1. **Be specific**: Catch specific exceptions, not generic `Exception`.
2. **Don't silence errors**: Always handle or log exceptions meaningfully.
3. **Use `finally` for cleanup**: Close files, database connections, etc.
4. **Don't use exceptions for flow control**: They are for exceptional situations.

```python
# BAD - too broad
try:
    # ... some code ...
    pass
except Exception:
    pass    # Silently ignores ALL errors

# GOOD - specific and informative
try:
    value = int(user_input)
except ValueError:
    print(f"'{user_input}' is not a valid integer. Please try again.")
```

---

### Graded Assessment: Testing Knowledge on Errors and Exceptions

**Challenge 1:** Write a robust input function that keeps asking until the user provides a valid integer within a specified range.

```python
def get_integer(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

age = get_integer("Enter your age (0-150): ", 0, 150)
print(f"Your age is {age}.")
```

**Challenge 2:** Write a simple calculator that handles all possible errors gracefully.

```python
def safe_calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            raise ValueError(f"Unknown operator: '{operator}'")

        print(f"{num1} {operator} {num2} = {result}")

    except ValueError as e:
        print(f"Input error: {e}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Calculator session ended.")

safe_calculator()
```

**Challenge 3:** Write a program that reads a list of numbers from the user (one per line, "done" to finish) and handles invalid inputs.

```python
numbers = []
print("Enter numbers one per line (type 'done' to finish):")

while True:
    user_input = input("> ")
    if user_input.lower() == "done":
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print(f"  '{user_input}' is not a valid number. Skipped.")

if numbers:
    print(f"\nYou entered {len(numbers)} numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers)/len(numbers):.2f}")
else:
    print("\nNo valid numbers were entered.")
```

---

# Module 9 – Python Internals and Conclusion

This module offers a deeper understanding of how Python works under the hood — its interpreter, execution model, and memory management.

### Learning Objectives

- Gain insight into the internal workings of Python, including its interpreter and execution model.
- Understand key aspects of Python's internal architecture and design principles.

---

## Python Internals

### CPython — The Default Interpreter

When you install Python from python.org, you get **CPython** — the reference implementation written in C. Other implementations exist (Jython, PyPy, IronPython), but CPython is by far the most common.

### How Python Executes Your Code

Python execution happens in two phases:

**Phase 1 — Compilation to Bytecode**

Your `.py` source code is compiled into **bytecode** — a low-level, platform-independent set of instructions. This is stored in `.pyc` files inside the `__pycache__` directory.

```python
# You can see the bytecode using the dis module
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

This shows instructions like `LOAD_FAST`, `BINARY_ADD`, and `RETURN_VALUE` — the actual operations the Python Virtual Machine (PVM) executes.

**Phase 2 — Execution by the Python Virtual Machine**

The PVM is a stack-based virtual machine that reads and executes bytecode instructions one at a time.

### Memory Management

**Reference Counting:**

Python keeps track of how many references point to each object. When the count drops to zero, the memory is freed.

```python
import sys

a = "hello"
print(sys.getrefcount(a))    # Shows the reference count

b = a      # Another reference to the same object
print(sys.getrefcount(a))    # Count increases

del b      # Remove a reference
print(sys.getrefcount(a))    # Count decreases
```

**Garbage Collection:**

Python has a garbage collector that handles **circular references** (objects referencing each other), which reference counting alone cannot handle.

```python
import gc

# You can interact with the garbage collector
print(gc.isenabled())       # True (enabled by default)
print(gc.get_count())       # Shows collection counts

# Force garbage collection
gc.collect()
```

### Object Identity and Interning

Every object in Python has a unique identity (memory address):

```python
a = 256
b = 256
print(a is b)      # True — Python caches small integers (-5 to 256)

a = 257
b = 257
print(a is b)      # May be False — larger integers may not be cached

# The 'is' operator checks identity, '==' checks equality
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)      # True (same content)
print(x is y)      # False (different objects)
```

### Everything Is an Object

In Python, everything is an object — integers, strings, functions, classes, even modules:

```python
print(type(42))           # <class 'int'>
print(type("hello"))      # <class 'str'>
print(type([1, 2]))       # <class 'list'>
print(type(print))        # <class 'builtin_function_or_method'>
print(type(type))         # <class 'type'>

# Functions are objects — they can be assigned to variables
def greet():
    return "Hello!"

say_hi = greet     # Assign function to a variable
print(say_hi())    # Hello!
```

### The Global Interpreter Lock (GIL)

CPython has the **Global Interpreter Lock (GIL)**, a mutex that ensures only one thread executes Python bytecode at a time. This simplifies memory management but limits true parallelism in CPU-bound multi-threaded programs. For CPU-intensive parallel work, use the `multiprocessing` module instead of `threading`.

### Python's Dynamic Nature

Python is highly dynamic — you can modify almost anything at runtime:

```python
# Check an object's attributes
print(dir(42))         # Shows all methods of an integer

# Get help on any object
# help(str.split)      # Uncomment to see documentation

# Type checking
x = 42
print(isinstance(x, int))      # True
print(isinstance(x, (int, float)))   # True
```

---

### Hands-on Lab: Python Internals

**Lab Goal:** Explore Python's internal behavior.

**Exercise 1:** Examine bytecode with the `dis` module.

```python
import dis

def multiply(a, b):
    return a * b

print("Bytecode for multiply:")
dis.dis(multiply)

# Compare with a more complex function
def complex_func(x):
    if x > 0:
        return x * 2
    else:
        return x * -1

print("\nBytecode for complex_func:")
dis.dis(complex_func)
```

**Exercise 2:** Explore object identity and interning.

```python
# Integer interning
a = 100
b = 100
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")     # True (small integer caching)
print(f"id(a): {id(a)}, id(b): {id(b)}")

# String interning
s1 = "hello"
s2 = "hello"
print(f"\ns1 = '{s1}', s2 = '{s2}'")
print(f"s1 is s2: {s1 is s2}")     # True (string interning)

# List identity
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(f"\nl1 = {l1}, l2 = {l2}")
print(f"l1 == l2: {l1 == l2}")     # True (equal values)
print(f"l1 is l2: {l1 is l2}")     # False (different objects)
```

**Exercise 3:** Explore reference counting.

```python
import sys

# Create an object and check references
my_list = [1, 2, 3]
print(f"Initial refcount: {sys.getrefcount(my_list)}")
# Note: getrefcount itself creates a temporary reference, so count is 1 higher

another_ref = my_list
print(f"After alias: {sys.getrefcount(my_list)}")

in_a_list = [my_list, my_list]
print(f"After adding to list: {sys.getrefcount(my_list)}")

del another_ref
print(f"After deleting alias: {sys.getrefcount(my_list)}")

del in_a_list
print(f"After deleting list: {sys.getrefcount(my_list)}")
```

**Exercise 4:** Inspect built-in types and their methods.

```python
# See all methods of a string
string_methods = [m for m in dir(str) if not m.startswith('_')]
print("String methods:")
for i, method in enumerate(string_methods, 1):
    print(f"  {i:2}. {method}")

# See all methods of a list
list_methods = [m for m in dir(list) if not m.startswith('_')]
print("\nList methods:")
for i, method in enumerate(list_methods, 1):
    print(f"  {i:2}. {method}")

# Check the size of objects in bytes
import sys
print(f"\nSize of int(0): {sys.getsizeof(0)} bytes")
print(f"Size of int(1): {sys.getsizeof(1)} bytes")
print(f"Size of '': {sys.getsizeof('')} bytes")
print(f"Size of 'hello': {sys.getsizeof('hello')} bytes")
print(f"Size of []: {sys.getsizeof([])} bytes")
print(f"Size of [1,2,3]: {sys.getsizeof([1,2,3])} bytes")
```

---

## Conclusion

Congratulations on completing **Python for the Absolute Beginner**! Here is a summary of what you have learned:

**Module 1 – Python Basics:** You learned the fundamentals — `print()`, literals, operators, variables, comments, `input()`, and string methods. These are the building blocks of every Python program.

**Module 2 – Decision Making:** You learned comparison operators and conditional statements (`if`, `elif`, `else`), enabling your programs to make decisions and branch based on conditions.

**Module 3 – Iteration:** You mastered `while` and `for` loops, giving your programs the ability to repeat actions, process sequences, and iterate over data.

**Module 4 – Logic and Bit Operations:** You explored logical operators (`and`, `or`, `not`) for combining conditions, and bitwise operators for working at the binary level.

**Module 5 – Lists:** You dove into Python's most versatile data structure — creating, modifying, slicing, searching, and nesting lists including 2D and 3D structures.

**Module 6 – Functions:** You learned to organize code into reusable functions with parameters, return values, scope rules, and advanced argument handling.

**Module 7 – Tuples and Dictionaries:** You learned two more essential data structures — immutable tuples for fixed data and dictionaries for key-value mappings.

**Module 8 – Exceptions:** You learned to write robust code that handles errors gracefully using `try`, `except`, `else`, `finally`, and custom exceptions.

**Module 9 – Python Internals:** You peeked under the hood to understand bytecode, the Python Virtual Machine, memory management, reference counting, and the GIL.

### Where to Go Next

Your Python journey has just begun. Here are some areas to explore:

- **File I/O:** Reading and writing files.
- **Object-Oriented Programming:** Classes, objects, inheritance.
- **Modules and Packages:** Organizing code into reusable modules.
- **Standard Library:** Explore `os`, `json`, `datetime`, `re`, `collections`, and more.
- **Web Development:** Flask, Django, or FastAPI.
- **Data Science:** NumPy, pandas, matplotlib.
- **Automation:** Automate tasks with Python scripts.

Keep coding, keep experimenting, and most importantly — have fun!

---

_End of Python for the Absolute Beginner Tutorial_