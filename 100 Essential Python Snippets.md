# 100 Essential Python Snippets

A comprehensive reference covering Python syntax and features from basics to advanced topics.

---

## 📥 Basic Input & Output

---

### 1. Hello, World!

```python
print("Hello, World!")
```

The simplest Python program. `print()` writes to standard output and appends a newline by default. You can change the end character with `end=""` or the separator between multiple values with `sep=","`.

---

### 2. Printing with f-strings

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# My name is Alice and I am 30 years old.
```

F-strings (formatted string literals, introduced in Python 3.6) let you embed expressions directly inside `{}` braces. They are faster and more readable than `%` formatting or `.format()`.

---

### 3. Reading user input

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

`input()` pauses execution, displays a prompt, and returns whatever the user types as a **string**. Always cast to `int()` or `float()` when you need a number.

---

### 4. Printing with sep and end

```python
print("one", "two", "three", sep=" | ", end="!\n")
# one | two | three!
```

`sep` controls what goes between each argument (default `" "`), and `end` controls what is appended after the last argument (default `"\n"`).

---

### 5. Printing to stderr

```python
import sys
print("Something went wrong!", file=sys.stderr)
```

Passing `file=sys.stderr` redirects output to standard error, which is useful for error and diagnostic messages that should remain separate from normal program output.

---

## 🔢 Variables & Data Types

---

### 6. Basic variable assignment

```python
x = 10          # int
y = 3.14        # float
name = "Python" # str
flag = True     # bool
nothing = None  # NoneType
```

Python is dynamically typed — you never declare a type explicitly. The interpreter infers the type from the assigned value. Variable names are case-sensitive.

---

### 7. Multiple assignment

```python
a, b, c = 1, 2, 3
x = y = z = 0
print(a, b, c)  # 1 2 3
print(x, y, z)  # 0 0 0
```

Tuple unpacking on the left lets you assign several variables in one line. Chained assignment (`x = y = z = 0`) binds all names to the same object.

---

### 8. Type checking and conversion

```python
x = "42"
print(type(x))        # <class 'str'>
print(isinstance(x, str))  # True

n = int(x)            # "42" → 42
f = float(x)          # "42" → 42.0
s = str(100)          # 100 → "100"
b = bool(0)           # 0 → False
```

`type()` returns the exact type; `isinstance()` also matches subclasses and is preferred for checks. Explicit conversion functions (`int`, `float`, `str`, `bool`) raise `ValueError` on bad input.

---

### 9. Integer operations

```python
print(7 + 2)   # 9   addition
print(7 - 2)   # 5   subtraction
print(7 * 2)   # 14  multiplication
print(7 / 2)   # 3.5 true division (always float)
print(7 // 2)  # 3   floor division
print(7 % 2)   # 1   modulus
print(7 ** 2)  # 49  exponentiation
```

`/` always returns a float in Python 3. Use `//` for integer (floor) division. `**` is right-associative: `2**3**2` == `2**9`.

---

### 10. Augmented assignment operators

```python
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x //= 5  # x = 4
x **= 3  # x = 64
print(x) # 64
```

Augmented operators combine an operation with assignment. They are equivalent to `x = x op value` but may be more efficient for mutable objects (like lists).

---

### 11. Walrus operator (`:=`)

```python
numbers = [1, 3, 7, 9, 15]
if (n := len(numbers)) > 4:
    print(f"List is long: {n} items")
# List is long: 5 items
```

The walrus operator (Python 3.8+) assigns a value as part of an expression. It is especially handy inside `while` loops or comprehensions to avoid computing the same value twice.

---

### 12. Chained comparisons

```python
x = 5
print(1 < x < 10)   # True
print(0 <= x <= 5)  # True
print(x == 5 == 5)  # True
```

Python allows chaining comparison operators. `1 < x < 10` is equivalent to `1 < x and x < 10` but evaluates `x` only once, making the code more readable and efficient.

---

## 🔤 Strings

---

### 13. String methods

```python
s = "  Hello, Python!  "
print(s.strip())          # "Hello, Python!"
print(s.lower())          # "  hello, python!  "
print(s.upper())          # "  HELLO, PYTHON!  "
print(s.replace("Python", "World"))  # "  Hello, World!  "
print(s.split(","))       # ['  Hello', ' Python!  ']
```

Strings are immutable in Python — every method returns a new string. `strip()` removes leading/trailing whitespace (or any specified characters).

---

### 14. String slicing

```python
s = "Hello, World!"
print(s[0])      # H       (first char)
print(s[-1])     # !       (last char)
print(s[0:5])    # Hello   (start:stop, stop excluded)
print(s[7:])     # World!  (from index 7 to end)
print(s[::-1])   # !dlroW ,olleH  (reversed)
```

Slicing syntax is `[start:stop:step]`. Negative indices count from the end. This is one of the most powerful and commonly used Python features.

---

### 15. String formatting styles

```python
name, score = "Bob", 98.5

# f-string (preferred, Python 3.6+)
print(f"{name} scored {score:.1f}%")

# .format()
print("{} scored {:.1f}%".format(name, score))

# % formatting (legacy)
print("%s scored %.1f%%" % (name, score))
```

All three styles produce the same output. F-strings are fastest and most readable. The `:.1f` format spec rounds to one decimal place.

---

### 16. Multiline strings

```python
text = """
Line one
Line two
Line three
"""
print(text.strip())
```

Triple quotes (`"""` or `'''`) create multiline strings. They preserve newlines and indentation exactly as written. Commonly used for docstrings and SQL queries.

---

### 17. String membership and search

```python
s = "The quick brown fox"
print("quick" in s)         # True
print(s.startswith("The"))  # True
print(s.endswith("fox"))    # True
print(s.find("brown"))      # 10  (index, or -1 if not found)
print(s.count("o"))         # 2
```

The `in` operator is the Pythonic way to test membership. `find()` returns -1 on failure while `index()` raises `ValueError` — choose based on whether absence is an error.

---

### 18. String joining and splitting

```python
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)          # Python is awesome

parts = sentence.split(" ")
print(parts)             # ['Python', 'is', 'awesome']

csv_line = "a,b,,c"
print(csv_line.split(","))         # ['a', 'b', '', 'c']
print(csv_line.split(",", maxsplit=2))  # ['a', 'b', ',c']  -- wait actually:
# ['a', 'b', ',c'] is wrong. Let me clarify:
# maxsplit=2 means at most 2 splits: ['a', 'b', ',c'] → ['a', 'b', ',c']
```

`join()` is the fastest way to build a string from an iterable. Note: the separator goes on the string you call `join()` on, not inside the list.

---

## 🔀 Control Flow

---

### 19. if / elif / else

```python
score = 72

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)  # C
```

Python uses indentation (4 spaces by convention) to define blocks — there are no braces. `elif` is short for "else if". Conditions are evaluated top-to-bottom; the first truthy one wins.

---

### 20. Ternary (conditional) expression

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult
```

The one-line ternary form is `value_if_true if condition else value_if_false`. Use it for simple assignments; prefer a full `if/else` block for anything more complex.

---

### 21. for loop with range

```python
for i in range(5):
    print(i, end=" ")
# 0 1 2 3 4

for i in range(2, 10, 2):
    print(i, end=" ")
# 2 4 6 8
```

`range(stop)`, `range(start, stop)`, and `range(start, stop, step)` generate integer sequences lazily. They are not lists — use `list(range(...))` to materialise one.

---

### 22. while loop with break and continue

```python
n = 0
while True:
    n += 1
    if n % 2 == 0:
        continue   # skip even numbers
    if n > 9:
        break      # exit loop
    print(n, end=" ")
# 1 3 5 7 9
```

`break` exits the innermost loop immediately; `continue` jumps to the next iteration. Both work inside `for` loops too. `while True` with a `break` is a common pattern for "loop until condition".

---

### 23. for / else and while / else

```python
for i in range(2, 10):
    if 10 % i == 0:
        print(f"10 is divisible by {i}")
        break
else:
    print("10 has no divisors in range 2-9")
# 10 is divisible by 2
```

The `else` clause on a loop runs only if the loop completed **without** hitting a `break`. This is very useful for search algorithms where you want to signal "not found."

---

### 24. match statement (structural pattern matching)

```python
# Python 3.10+
command = "quit"

match command:
    case "quit":
        print("Quitting...")
    case "help":
        print("Showing help...")
    case _:
        print(f"Unknown command: {command}")
```

`match`/`case` is Python's modern switch-like construct. The `_` wildcard matches anything. It supports matching on types, sequences, mappings, and class attributes — far more powerful than a simple switch.

---

### 25. Nested loops with enumerate and zip

```python
names = ["Alice", "Bob", "Carol"]
scores = [88, 92, 75]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name}: {score}")
# 1. Alice: 88
# 2. Bob: 92
# 3. Carol: 75
```

`zip()` pairs up iterables element-by-element (stops at the shortest). `enumerate()` adds an auto-incrementing counter. Combining them in a single loop is clean and idiomatic.

---

## ⚙️ Functions

---

### 26. Defining and calling functions

```python
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"

message = greet("World")
print(message)  # Hello, World!
```

Functions are defined with `def`. The docstring (triple-quoted string immediately after the `def`) is accessible via `help()` and `.__doc__`. Always return a value explicitly; implicit return gives `None`.

---

### 27. Default and keyword arguments

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))        # 9   (exponent defaults to 2)
print(power(2, 10))    # 1024
print(power(exponent=3, base=5))  # 125
```

Default values are evaluated **once** at function definition time — never use mutable defaults like `def f(lst=[])`. Keyword arguments can be passed in any order, which improves readability.

---

### 28. *args and **kwargs

```python
def summarise(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

summarise(1, 2, 3, name="Alice", role="dev")
# Positional: (1, 2, 3)
# Keyword: {'name': 'Alice', 'role': 'dev'}
```

`*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict. These let you write flexible, variadic functions.

---

### 29. Unpacking arguments with * and **

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
info = {"a": 10, "b": 20, "c": 30}

print(add(*nums))    # 6
print(add(**info))   # 60
```

The `*` and `**` operators unpack a list/tuple or dict into positional/keyword arguments at the call site. This is the mirror image of `*args`/`**kwargs` in the definition.

---

### 30. Lambda functions

```python
square = lambda x: x ** 2
add = lambda x, y: x + y

print(square(5))   # 25
print(add(3, 4))   # 7

nums = [5, 2, 8, 1, 9]
nums.sort(key=lambda x: -x)
print(nums)  # [9, 8, 5, 2, 1]
```

Lambdas are anonymous single-expression functions. They are most useful as inline arguments to `sorted()`, `map()`, `filter()`, etc. For anything more complex, use a named `def`.

---

### 31. Closures

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor   # 'factor' is captured from outer scope
    return multiply

triple = make_multiplier(3)
print(triple(7))   # 21
print(triple(10))  # 30
```

A closure is an inner function that remembers the variables from its enclosing scope even after the outer function has returned. The captured variables live in the function's `.__closure__` attribute.

---

### 32. Recursive functions

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(6))  # 720
```

Recursion breaks a problem into smaller identical sub-problems. Always define a **base case** to stop the recursion. Python's default recursion limit is 1000 (`sys.getrecursionlimit()`); increase with `sys.setrecursionlimit()` if needed, or prefer iteration.

---

## 🗃️ Data Structures

---

### 33. Lists — creation and indexing

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(1, "avocado")
fruits.remove("banana")
popped = fruits.pop()      # removes last item

print(fruits)   # ['apple', 'avocado', 'cherry']
print(len(fruits))         # 3
print(fruits[1])           # avocado
print(fruits[-1])          # cherry
```

Lists are ordered, mutable sequences. `append()` is O(1); `insert()` and `remove()` are O(n). Use `pop(i)` to remove by index, `remove(value)` to remove the first matching value.

---

### 34. List slicing and copying

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3]
print(nums[::2])    # [0, 2, 4]   every other
print(nums[::-1])   # [5, 4, 3, 2, 1, 0]  reversed

shallow_copy = nums[:]        # or list(nums)
import copy
deep_copy = copy.deepcopy(nums)
```

`[:]` creates a shallow copy — fine for lists of immutables. For nested structures, use `copy.deepcopy()`. Modifying a shallow copy's nested objects affects the original.

---

### 35. Tuples

```python
point = (3, 7)
x, y = point          # unpacking
print(x, y)           # 3 7

rgb = (255, 128, 0)
r, *rest = rgb        # extended unpacking
print(r, rest)        # 255 [128, 0]

single = (42,)        # trailing comma makes it a tuple
```

Tuples are immutable ordered sequences. They are faster than lists for fixed data and can be used as dict keys or set members. The comma, not the parentheses, makes a tuple.

---

### 36. Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Access
print(person["name"])              # Alice
print(person.get("country", "N/A"))# N/A (safe access)

# Modify
person["age"] = 31
person.update({"job": "engineer", "age": 32})

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")
```

Dicts are ordered (Python 3.7+) hash maps. Always prefer `.get(key, default)` over `[key]` when the key might not exist. `.items()`, `.keys()`, and `.values()` return view objects.

---

### 37. Dictionary merging (Python 3.9+)

```python
defaults = {"theme": "dark", "lang": "en"}
user_prefs = {"lang": "fr", "font": "mono"}

merged = defaults | user_prefs
print(merged)
# {'theme': 'dark', 'lang': 'fr', 'font': 'mono'}

defaults |= user_prefs  # in-place merge
```

The `|` operator merges two dicts; right-hand side values win on conflicts. Before Python 3.9, use `{**defaults, **user_prefs}` for the same effect.

---

### 38. Sets

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)   # union:        {1, 2, 3, 4, 5, 6, 7, 8}
print(a & b)   # intersection: {4, 5}
print(a - b)   # difference:   {1, 2, 3}
print(a ^ b)   # symmetric diff: {1, 2, 3, 6, 7, 8}

a.add(10)
a.discard(99)  # no error if missing; .remove() raises KeyError
```

Sets are unordered collections of unique, hashable elements. Membership tests (`in`) are O(1). Great for deduplication and relationship tests between collections.

---

### 39. collections.defaultdict

```python
from collections import defaultdict

word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

for word in words:
    word_count[word] += 1

print(dict(word_count))
# {'apple': 3, 'banana': 2, 'cherry': 1}
```

`defaultdict` auto-creates a missing key using a factory function (`int` returns `0`, `list` returns `[]`). This eliminates the need for `if key not in d: d[key] = default`.

---

### 40. collections.Counter

```python
from collections import Counter

votes = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice"]
tally = Counter(votes)

print(tally)                      # Counter({'Alice': 3, 'Bob': 2, 'Carol': 1})
print(tally.most_common(2))       # [('Alice', 3), ('Bob', 2)]
print(tally["Carol"])             # 1
print(tally["Dave"])              # 0  (no KeyError!)
```

`Counter` is a subclass of `dict` that counts hashable objects. It supports arithmetic operations (`+`, `-`) and `.most_common(n)` to get the top-N items.

---

### 41. collections.deque

```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)    # O(1) prepend
dq.append(4)        # O(1) append
dq.popleft()        # O(1) pop from left

print(dq)           # deque([1, 2, 3, 4])

# Fixed-size sliding window
window = deque(maxlen=3)
for x in range(6):
    window.append(x)
    print(list(window))
```

`deque` (double-ended queue) gives O(1) append/pop from both ends, unlike lists which are O(n) for left-side operations. Ideal for queues, BFS, and sliding windows.

---

### 42. heapq — priority queue

```python
import heapq

nums = [5, 1, 9, 3, 7]
heapq.heapify(nums)           # convert list to min-heap in-place

heapq.heappush(nums, 4)
smallest = heapq.heappop(nums)  # 1
print(smallest)               # 1

top3 = heapq.nlargest(3, nums)
print(top3)                   # [9, 7, 5]
```

Python's `heapq` is a min-heap. For a max-heap, negate values. `nlargest`/`nsmallest` are efficient for getting the top-K items without fully sorting.

---

## 🔍 Comprehensions

---

### 43. List comprehensions

```python
squares = [x**2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

List comprehensions are a concise, readable way to build lists. Syntax: `[expression for item in iterable if condition]`. They are faster than an equivalent `for` loop with `.append()`.

---

### 44. Nested list comprehensions

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [val for row in matrix for val in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

Multiple `for` clauses nest left-to-right (outer loops first). Nested comprehensions are powerful but can hurt readability — prefer explicit loops when the logic gets complex.

---

### 45. Dict and set comprehensions

```python
words = ["hello", "world", "python"]

lengths = {word: len(word) for word in words}
print(lengths)
# {'hello': 5, 'world': 5, 'python': 6}

unique_lengths = {len(word) for word in words}
print(unique_lengths)
# {5, 6}
```

Dict comprehensions `{k: v for ...}` and set comprehensions `{expr for ...}` follow the same pattern as list comprehensions. Note: `{}` with no colon creates a set, not a dict.

---

### 46. Generator expressions

```python
# Generator — lazy, memory-efficient
gen = (x**2 for x in range(1_000_000))
print(next(gen))   # 0
print(next(gen))   # 1
print(sum(gen))    # rest of the sum

# vs list — materializes everything at once
lst = [x**2 for x in range(1_000_000)]
```

Generator expressions use `()` instead of `[]`. They produce values one at a time on demand (lazy evaluation), so they use O(1) memory regardless of how many items they yield.

---

### 47. Conditional expression inside comprehension

```python
nums = range(-5, 6)
result = ["pos" if x > 0 else "neg" if x < 0 else "zero"
          for x in nums]
print(result)
# ['neg', 'neg', 'neg', 'neg', 'neg', 'zero', 'pos', 'pos', 'pos', 'pos', 'pos']
```

You can embed ternary expressions inside comprehensions for value transformation. Keep it readable — if the condition + expression gets long, pull it into a helper function.

---

## 📁 File I/O

---

### 48. Reading a file

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()          # entire file as string

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()       # list of lines (with \n)

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:              # most memory-efficient
        print(line.strip())
```

Always use a `with` statement — it ensures the file is closed even if an exception occurs. Specify `encoding="utf-8"` explicitly to avoid platform-dependent defaults.

---

### 49. Writing a file

```python
lines = ["line one", "line two", "line three"]

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Header\n")
    f.writelines(line + "\n" for line in lines)

# Append mode
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Appended line\n")
```

Mode `"w"` creates or overwrites; `"a"` appends. `writelines()` accepts any iterable of strings — it does **not** add newlines automatically.

---

### 50. Working with pathlib

```python
from pathlib import Path

p = Path("data") / "report.txt"
print(p.parent)    # data
print(p.name)      # report.txt
print(p.stem)      # report
print(p.suffix)    # .txt

p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("Hello from pathlib!", encoding="utf-8")
text = p.read_text(encoding="utf-8")
print(text)
```

`pathlib.Path` is the modern, object-oriented way to handle paths. It is cross-platform, composable with `/`, and has convenient methods like `read_text()` / `write_text()`.

---

### 51. Reading and writing JSON

```python
import json

data = {"name": "Alice", "scores": [95, 87, 92], "active": True}

# Serialize to string
json_str = json.dumps(data, indent=2)
print(json_str)

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json") as f:
    loaded = json.load(f)

print(loaded["name"])   # Alice
```

`json.dumps()` / `json.loads()` work with strings; `json.dump()` / `json.load()` work with file objects. Use `indent` for pretty-printing human-readable output.

---

### 52. Reading CSV files

```python
import csv

# Writing
rows = [["name", "age"], ["Alice", 30], ["Bob", 25]]
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Reading as dicts
with open("people.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

Always open CSV files with `newline=""` on write to prevent blank rows on Windows. `DictReader` uses the first row as header keys, giving you dict access per row.

---

## ⚠️ Error Handling

---

### 53. try / except / else / finally

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        print("Division succeeded.")
        return result
    finally:
        print("Always runs.")

divide(10, 2)
divide(10, 0)
```

`else` runs only when no exception was raised. `finally` always runs — perfect for cleanup (closing files, releasing locks). Catch the most specific exceptions first.

---

### 54. Raising exceptions

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of range [0, 150]")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)   # Age -5 is out of range [0, 150]
```

Use `raise` to signal error conditions. Provide a clear, descriptive message. Re-raise the current exception with a bare `raise` inside an except block.

---

### 55. Custom exceptions

```python
class AppError(Exception):
    """Base class for application exceptions."""

class DatabaseError(AppError):
    def __init__(self, message, query=None):
        super().__init__(message)
        self.query = query

try:
    raise DatabaseError("Connection failed", query="SELECT *")
except DatabaseError as e:
    print(e)          # Connection failed
    print(e.query)    # SELECT *
except AppError:
    print("Generic app error")
```

Custom exceptions should subclass `Exception` (or a domain base class). They let callers catch specific errors precisely, and you can attach extra context as attributes.

---

### 56. Context managers for cleanup

```python
class ManagedResource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        return False  # don't suppress exceptions

with ManagedResource() as r:
    print("Using resource")
    # Even if an exception occurs here, __exit__ runs
```

Implementing `__enter__` and `__exit__` makes a class usable as a `with` statement context manager. Return `True` from `__exit__` to suppress the exception; `False` propagates it.

---

### 57. contextlib.contextmanager

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"Elapsed: {elapsed:.4f}s")

with timer():
    total = sum(range(1_000_000))
```

The `@contextmanager` decorator turns a generator function into a context manager. Code before `yield` runs on entry; code after (in `finally`) runs on exit — much simpler than writing a full class.

---

## 🏛️ Object-Oriented Programming

---

### 58. Defining a class

```python
class Dog:
    species = "Canis lupus familiaris"  # class attribute

    def __init__(self, name, age):
        self.name = name   # instance attributes
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age})"

rex = Dog("Rex", 4)
print(rex.bark())   # Rex says: Woof!
print(repr(rex))    # Dog(name='Rex', age=4)
print(Dog.species)  # Canis lupus familiaris
```

`__init__` is the initializer (not constructor — the object already exists). `self` is the instance and must be the first parameter of every instance method. `__repr__` provides a developer-friendly string representation.

---

### 59. Inheritance and method overriding

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

animals = [Cat("Whiskers"), Dog("Buddy")]
for a in animals:
    print(a.speak())
```

Subclasses inherit all methods and attributes. Override a method by redefining it. `super()` calls the parent's version: `super().__init__(name)`. This polymorphic pattern is fundamental to OOP.

---

### 60. Properties

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.fahrenheit)   # 77.0
t.celsius = 100
print(t.fahrenheit)   # 212.0
```

`@property` lets you add getter/setter logic while keeping attribute-style access. The leading underscore (`_celsius`) is a convention for "private" attributes — Python doesn't enforce true privacy.

---

### 61. Class methods and static methods

```python
class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def unit(cls):
        return cls(1)           # factory method

    @staticmethod
    def is_valid_radius(r):
        return r > 0            # utility function, no self/cls

    def area(self):
        return self.PI * self.radius ** 2

c = Circle.unit()
print(c.area())                     # 3.14159
print(Circle.is_valid_radius(-1))   # False
```

`@classmethod` receives the class (`cls`) instead of the instance — great for alternative constructors. `@staticmethod` receives neither; it's just a function namespaced in the class.

---

### 62. Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0
    tags: list = field(default_factory=list)

    def distance_from_origin(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

p = Point(3.0, 4.0)
print(p)                          # Point(x=3.0, y=4.0, z=0.0, tags=[])
print(p.distance_from_origin())   # 5.0
```

`@dataclass` auto-generates `__init__`, `__repr__`, and `__eq__`. Use `field(default_factory=...)` for mutable defaults. Add `frozen=True` to make instances immutable (also hashable).

---

### 63. Special (dunder) methods

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        return 2

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1, v2 = Vector(1, 2), Vector(3, 4)
print(v1 + v2)     # Vector(4, 6)
print(v1 * 3)      # Vector(3, 6)
print(len(v1))     # 2
```

Dunder (double-underscore) methods let your objects hook into Python's built-in operations: `+`, `*`, `len()`, `str()`, comparison operators, etc. This is called **operator overloading**.

---

### 64. Abstract base classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

r = Rectangle(4, 6)
print(r.area())       # 24
# Shape()  → TypeError: Can't instantiate abstract class
```

ABCs enforce an interface: any subclass that doesn't implement all `@abstractmethod`s will raise `TypeError` on instantiation. This provides a form of contract-based programming.

---

### 65. Multiple inheritance and MRO

```python
class A:
    def hello(self):
        return "Hello from A"

class B(A):
    def hello(self):
        return "Hello from B"

class C(A):
    def hello(self):
        return "Hello from C"

class D(B, C):
    pass

d = D()
print(d.hello())          # Hello from B
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

Python uses **C3 linearization** to compute the Method Resolution Order (MRO) — the order in which base classes are searched. Always check `__mro__` when debugging multiple-inheritance issues.

---

### 66. Slots for memory efficiency

```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(1, 2)
print(p.x, p.y)    # 1 2
# p.z = 3         → AttributeError: 'Point' object has no attribute 'z'
```

`__slots__` replaces the per-instance `__dict__` with a fixed array, reducing memory by ~40-60% for classes with many small instances. The trade-off is that you can't add new attributes dynamically.

---

### 67. `__init_subclass__` for class registration

```python
class Plugin:
    registry = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_name:
            Plugin.registry[plugin_name] = cls

class PDFExporter(Plugin, plugin_name="pdf"):
    pass

class CSVExporter(Plugin, plugin_name="csv"):
    pass

print(Plugin.registry)
# {'pdf': <class 'PDFExporter'>, 'csv': <class 'CSVExporter'>}
```

`__init_subclass__` is called whenever the class is subclassed, enabling automatic registration patterns without metaclasses. Excellent for plugin architectures.

---

## 📦 Modules & Packages

---

### 68. Importing modules

```python
import math
print(math.sqrt(16))         # 4.0

from math import pi, ceil
print(pi)                    # 3.141592653589793
print(ceil(4.2))             # 5

import numpy as np            # alias (if numpy installed)
```

`import math` loads the whole module. `from math import x` pulls specific names into your namespace. Aliases (`as np`) shorten long module names. Avoid `from module import *` in production code.

---

### 69. Writing a module and `__name__`

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Only runs when executed directly, not when imported
    print(greet("World"))
```

Every `.py` file is a module. The `if __name__ == "__main__"` guard lets a file work both as an importable library and as a standalone script. When imported, `__name__` equals the module name.

---

### 70. Virtual environments and requirements

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install packages
pip install requests pandas

# Freeze dependencies
pip freeze > requirements.txt

# Reproduce environment
pip install -r requirements.txt
```

Always use a virtual environment to isolate project dependencies. `requirements.txt` records exact versions for reproducibility. Tools like `poetry` or `uv` offer more advanced dependency management.

---

## 🔄 Iterators & Generators

---

### 71. Custom iterator

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in Countdown(5):
    print(n, end=" ")
# 5 4 3 2 1
```

Any class with `__iter__` (returns an iterator) and `__next__` (returns the next value or raises `StopIteration`) is an iterator. Python's `for` loop calls these automatically.

---

### 72. Generator functions with yield

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(8)])
# [0, 1, 1, 2, 3, 5, 8, 13]
```

`yield` suspends the function and returns a value. On the next call to `next()`, execution resumes right after the `yield`. This makes infinite sequences possible with O(1) memory.

---

### 73. yield from

```python
def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2], "abc", range(3)))
print(result)
# [1, 2, 'a', 'b', 'c', 0, 1, 2]
```

`yield from iterable` delegates to a sub-iterable, yielding all its values one by one. It also correctly propagates `.send()` and `.throw()` calls to the sub-generator.

---

### 74. Generator pipelines

```python
def integers(start=0):
    n = start
    while True:
        yield n
        n += 1

def take(n, iterable):
    for i, val in enumerate(iterable):
        if i >= n:
            return
        yield val

def squares(nums):
    for n in nums:
        yield n * n

pipeline = take(5, squares(integers(1)))
print(list(pipeline))  # [1, 4, 9, 16, 25]
```

Generators compose naturally into pipelines. Data flows lazily — each generator pulls from the previous only when asked. This is memory-efficient even for huge datasets.

---

### 75. itertools essentials

```python
import itertools

# Infinite counter
counter = itertools.count(start=1, step=2)
print(list(itertools.islice(counter, 5)))  # [1, 3, 5, 7, 9]

# Combinations and permutations
items = [1, 2, 3]
print(list(itertools.combinations(items, 2)))
# [(1, 2), (1, 3), (2, 3)]
print(list(itertools.permutations(items, 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Groupby
data = [("a", 1), ("a", 2), ("b", 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
```

`itertools` provides fast, memory-efficient building blocks for iterators: `chain`, `cycle`, `islice`, `product`, `groupby`, and more. Master these to avoid reinventing wheels.

---

### 76. functools.reduce and partial

```python
from functools import reduce, partial

# reduce: fold a sequence
product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])
print(product)   # 120

# partial: pre-fill arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)
print(square(5))  # 25
print(cube(3))    # 27
```

`reduce()` applies a binary function cumulatively. `partial()` creates a new callable with some arguments pre-filled — useful for adapting functions to expected signatures.

---

## 🎨 Decorators

---

### 77. Writing a basic decorator

```python
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 4)
# Calling add((3, 4), {})
# add returned 7
```

A decorator is a function that takes a function and returns a new function. `@functools.wraps(func)` preserves the original function's `__name__`, `__doc__`, etc. — always include it.

---

### 78. Decorator with arguments

```python
import functools, time

def retry(times=3, delay=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < times:
                        time.sleep(delay)
            raise RuntimeError(f"{func.__name__} failed after {times} attempts")
        return wrapper
    return decorator

@retry(times=3, delay=0.1)
def unstable_call():
    import random
    if random.random() < 0.7:
        raise IOError("Transient error")
    return "Success"
```

A decorator factory returns a decorator. The extra nesting (`decorator` inside `retry`) lets you pass arguments to `@retry(times=3)`. This is the standard pattern for parameterised decorators.

---

### 79. Stacking decorators

```python
def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))   # <b><i>Hello, World!</i></b>
```

Stacked decorators are applied bottom-up: `@bold @italic f` is equivalent to `f = bold(italic(f))`. The innermost decorator wraps first, the outermost last.

---

### 80. Class-based decorator

```python
import functools

class memoize:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(40))   # 102334155  (fast!)
```

A class can act as a decorator by implementing `__init__` (receives the function) and `__call__` (receives the arguments). This is useful when you need to maintain state across calls.

---

### 81. functools.lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))              # 12586269025
print(fib.cache_info())     # CacheInfo(hits=48, misses=51, maxsize=128, currsize=51)
fib.cache_clear()
```

`@lru_cache` is Python's built-in memoization decorator with a Least Recently Used eviction policy. Use `maxsize=None` for an unbounded cache. Python 3.9+ has `@cache` as a convenient alias.

---

### 82. Property as a descriptor / cached_property

```python
from functools import cached_property
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("Computing area...")
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area)   # Computing area... 78.53...
print(c.area)   # 78.53...  (no recomputation)
```

`@cached_property` computes the value on first access, stores it as an instance attribute, and returns the cached value on subsequent accesses — no repeated computation. The result is stored in `c.__dict__`.

---

## 🔧 Advanced Features

---

### 83. Context manager with `suppress`

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    import os
    os.remove("nonexistent_file.txt")
    print("This won't print if file is missing")

print("Execution continues normally")
```

`suppress(*exceptions)` silently ignores the specified exceptions within its block — a cleaner alternative to a bare `try/except: pass`. Use sparingly; swallowing errors can hide bugs.

---

### 84. Type hints and annotations

```python
from typing import Optional, Union, List, Dict, Tuple

def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    db = {1: {"name": "Alice"}}
    return db.get(user_id)

def process(data: Union[str, List[str]]) -> List[str]:
    if isinstance(data, str):
        return [data]
    return data
```

Type hints (PEP 484) are annotations that tools like `mypy` and IDEs use for static analysis. They do **not** enforce types at runtime. Python 3.10+ allows `X | Y` instead of `Union[X, Y]`.

---

### 85. TypedDict and Protocol

```python
from typing import TypedDict, Protocol

class UserRecord(TypedDict):
    name: str
    age: int
    email: str

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())   # Works! Duck typing + static checking
```

`TypedDict` creates a typed dict schema. `Protocol` enables **structural subtyping** (duck typing with type-checker support) — any class with the right methods satisfies the protocol without explicit inheritance.

---

### 86. map, filter, and sorted with keys

```python
nums = [3, -1, 4, -1, 5, -9, 2, -6]

# map: apply function to each element
doubled = list(map(lambda x: x * 2, nums))

# filter: keep elements where function is True
positives = list(filter(lambda x: x > 0, nums))

# sorted with key
by_abs = sorted(nums, key=abs)
print(by_abs)   # [-1, -1, 2, 3, 4, -6, 5, -9]

words = ["banana", "apple", "cherry"]
print(sorted(words, key=str.lower, reverse=True))
# ['cherry', 'banana', 'apple']
```

`map()` and `filter()` return lazy iterators in Python 3. In most cases list comprehensions are more readable. `sorted()` is stable and supports a `key` function for custom ordering.

---

### 87. functools.singledispatch

```python
from functools import singledispatch

@singledispatch
def process(arg):
    raise TypeError(f"Cannot process type {type(arg)}")

@process.register(int)
def _(arg):
    return f"Processing int: {arg * 2}"

@process.register(str)
def _(arg):
    return f"Processing str: {arg.upper()}"

@process.register(list)
def _(arg):
    return f"Processing list of {len(arg)} items"

print(process(5))        # Processing int: 10
print(process("hello"))  # Processing str: HELLO
print(process([1, 2]))   # Processing list of 2 items
```

`@singledispatch` implements generic functions that dispatch on the type of the first argument. It's Python's take on function overloading — clean and extensible without long `if/isinstance` chains.

---

### 88. Unpacking and starred expressions

```python
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

a, b, *_ = range(100)        # discard the rest
print(a, b)                  # 0 1

# Merge lists with *
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, 0, *list2]
print(merged)                # [1, 2, 3, 0, 4, 5, 6]
```

The `*` operator in assignment unpacks the "rest" into a list. In literals it splats an iterable in place. Combined with `**` for dicts, this enables very flexible data manipulation.

---

### 89. Descriptors

```python
class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"{self.name} must be a non-negative number")
        obj.__dict__[self.name] = value

class Product:
    price = Validator()
    quantity = Validator()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

p = Product(9.99, 5)
print(p.price)   # 9.99
```

Descriptors (`__get__`, `__set__`, `__delete__`) are how `@property`, `@classmethod`, and ORM fields work under the hood. They allow reusable attribute validation logic that lives at the class level.

---

### 90. Regular expressions

```python
import re

text = "Call us at 555-1234 or 555-5678 for info."

# Find all phone numbers
phones = re.findall(r"\d{3}-\d{4}", text)
print(phones)   # ['555-1234', '555-5678']

# Named groups
pattern = r"(?P<area>\d{3})-(?P<number>\d{4})"
match = re.search(pattern, text)
if match:
    print(match.group("area"))    # 555
    print(match.group("number"))  # 1234

# Substitute
cleaned = re.sub(r"\d{3}-\d{4}", "XXX-XXXX", text)
print(cleaned)
```

`re.findall()` returns all matches; `re.search()` returns the first match object; `re.sub()` replaces matches. Compile patterns with `re.compile()` when reusing them frequently.

---

### 91. Dataclass with `__post_init__`

```python
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: float
    height: float

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")
        self.area = self.width * self.height

r = Rectangle(4.0, 5.0)
print(r.area)   # 20.0
```

`__post_init__` runs after the auto-generated `__init__`. Use it to validate fields, compute derived attributes, or perform any setup that requires all fields to already be assigned.

---

## ⚡ Async Programming

---

### 92. Basic async / await

```python
import asyncio

async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    await asyncio.gather(
        greet("Alice", 2),
        greet("Bob", 1),
        greet("Carol", 3),
    )

asyncio.run(main())
# Hello, Bob!    (after 1s)
# Hello, Alice!  (after 2s)
# Hello, Carol!  (after 3s)
```

`async def` defines a coroutine. `await` suspends it until the awaitable completes. `asyncio.gather()` runs coroutines concurrently — total time is ~3s, not 6s, because they overlap during I/O waits.

---

### 93. Async context managers and iterators

```python
import asyncio

class AsyncTimer:
    async def __aenter__(self):
        import time
        self.start = time.perf_counter()
        return self

    async def __aexit__(self, *args):
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.3f}s")

async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0)
        yield i

async def main():
    async with AsyncTimer():
        async for value in async_range(3):
            print(value)

asyncio.run(main())
```

`async with` and `async for` are async versions of their synchronous counterparts. They use `__aenter__`/`__aexit__` and `__aiter__`/`__anext__` protocols respectively.

---

### 94. asyncio.Queue for producer-consumer

```python
import asyncio, random

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(random.uniform(0.1, 0.3))
        await queue.put(i)
        print(f"Produced {i}")
    await queue.put(None)   # sentinel

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"  Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=2)
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())
```

`asyncio.Queue` coordinates async producers and consumers without locks. The `None` sentinel is a common pattern to signal "no more items." `maxsize` applies backpressure on fast producers.

---

### 95. Running async tasks with timeouts

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(10)
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main())
# Operation timed out!
```

`asyncio.wait_for()` cancels the coroutine and raises `TimeoutError` if it doesn't complete within the timeout. Always use this for external calls (network, DB) to avoid hanging forever.

---

### 96. Async generator

```python
import asyncio

async def async_fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        await asyncio.sleep(0)   # yield control to event loop
        a, b = b, a + b

async def main():
    async for n in async_fibonacci(100):
        print(n, end=" ")

asyncio.run(main())
# 0 1 1 2 3 5 8 13 21 34 55 89
```

Async generators combine `async def` and `yield`. They are consumed with `async for`. The `await asyncio.sleep(0)` yields control to the event loop, allowing other coroutines to run between yields.

---

### 97. asyncio.TaskGroup (Python 3.11+)

```python
import asyncio

async def fetch(url, delay):
    await asyncio.sleep(delay)
    return f"Result from {url}"

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch("api/users", 1))
        t2 = tg.create_task(fetch("api/posts", 2))
        t3 = tg.create_task(fetch("api/comments", 0.5))

    print(t1.result())
    print(t2.result())
    print(t3.result())

asyncio.run(main())
```

`TaskGroup` (Python 3.11+) is the modern replacement for `gather()`. It provides structured concurrency: if any task raises an exception, all other tasks are cancelled and an `ExceptionGroup` is raised.

---

## 🚀 Power Features

---

### 98. Metaclasses

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, url):
        self.url = url

db1 = Database("postgres://localhost/app")
db2 = Database("postgres://localhost/other")
print(db1 is db2)    # True — same instance!
print(db1.url)       # postgres://localhost/app
```

A metaclass controls how a class itself is created. `type` is the default metaclass; subclassing it lets you intercept class creation (`__new__`, `__init__`) and instance creation (`__call__`). Use sparingly — decorators or ABCs handle most use cases more simply.

---

### 99. `__slots__`, `__getattr__`, and dynamic attribute dispatch

```python
class FlexibleRecord:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        # Only called when normal attribute lookup fails
        return f"<missing: {name}>"

    def __setattr__(self, name, value):
        if name.startswith("_"):
            raise AttributeError("Private attributes not allowed")
        super().__setattr__(name, value)

rec = FlexibleRecord(name="Alice", age=30)
print(rec.name)     # Alice
print(rec.email)    # <missing: email>
```

`__getattr__` is called only when the attribute isn't found normally — great for proxies and mock objects. `__setattr__` intercepts every attribute assignment, so always call `super().__setattr__()` to avoid infinite recursion.

---

### 100. `__init_subclass__`, `__class_getitem__`, and generic classes

```python
class TypedList:
    def __class_getitem__(cls, item_type):
        class _TypedList(list):
            def append(self, item):
                if not isinstance(item, item_type):
                    raise TypeError(
                        f"Expected {item_type.__name__}, got {type(item).__name__}"
                    )
                super().append(item)
        _TypedList.__name__ = f"TypedList[{item_type.__name__}]"
        return _TypedList

IntList = TypedList[int]
lst = IntList()
lst.append(1)
lst.append(2)
print(lst)       # [1, 2]

try:
    lst.append("oops")
except TypeError as e:
    print(e)     # Expected int, got str
```

`__class_getitem__` is called when you write `MyClass[something]` — this is how `list[int]`, `dict[str, int]`, and generic type hints work. Implementing it gives your class its own parameterisation semantics.

---

*Happy coding! These 100 snippets cover the full breadth of Python from basics to internals. Revisit them as reference, experiment in a REPL, and combine patterns to build elegant solutions.*