Below are **100 Python code snippets** that collectively cover the vast majority of Python syntax and core programming constructs. Each snippet is accompanied by a brief explanation. They are grouped by topic for clarity, but numbered sequentially from 1 to 100.

---

## 1–5: Basic Syntax, Variables, and Output

### 1. Hello, World!
```python
print("Hello, World!")
```
**Explanation**: The `print()` function outputs text or variables to the console. This classic first program demonstrates basic output.

### 2. Comments
```python
# This is a single-line comment
"""
This is a
multi-line comment (docstring)
"""
```
**Explanation**: Single-line comments start with `#`. Multi-line strings (not assigned to a variable) act as comments or docstrings.

### 3. Variable Assignment
```python
x = 10
name = "Alice"
print(x, name)
```
**Explanation**: Variables are dynamically typed. No declaration is needed; assignment creates them.

### 4. Multiple Assignment
```python
a, b, c = 1, 2, 3
print(a, b, c)   # 1 2 3
```
**Explanation**: You can assign values to multiple variables in one line. This also works for swapping values: `a, b = b, a`.

### 5. Constants (by convention)
```python
MAX_SIZE = 100   # Uppercase signals a constant (not enforced)
print(MAX_SIZE)
```
**Explanation**: Python has no true constants, but by convention, names in all caps indicate a value should not change.

---

## 6–10: Data Types and Type Conversion

### 6. Integers and Floats
```python
age = 25          # int
price = 19.99     # float
print(type(age), type(price))
```
**Explanation**: `int` for whole numbers, `float` for decimals. Use `type()` to check an object’s type.

### 7. Strings
```python
greeting = "Hello"
name = 'Bob'
multi = """This
is
multi-line"""
```
**Explanation**: Strings can use single, double, or triple quotes. Triple quotes allow multi‑line strings.

### 8. Booleans and None
```python
is_valid = True
is_empty = False
nothing = None
```
**Explanation**: `True` and `False` are Boolean literals. `None` represents the absence of a value.

### 9. Type Conversion
```python
num_str = "123"
num_int = int(num_str)      # str -> int
float_val = float(num_int)  # int -> float
str_back = str(float_val)   # float -> str
print(type(str_back))
```
**Explanation**: Use `int()`, `float()`, `str()`, `bool()`, etc. to convert between types.

### 10. Checking Type
```python
value = 42
if isinstance(value, int):
    print("It's an integer")
```
**Explanation**: `isinstance(obj, type)` checks if an object is of a given type (supports inheritance).

---

## 11–15: Operators

### 11. Arithmetic Operators
```python
a, b = 10, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
```
**Explanation**: `+` `-` `*` `/` (float division), `//` (floor division), `%` (modulo), `**` (exponentiation).

### 12. Comparison Operators
```python
x, y = 5, 10
print(x == y, x != y, x < y, x > y, x <= y, x >= y)
```
**Explanation**: Comparisons return Boolean values. `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`.

### 13. Logical Operators
```python
a, b = True, False
print(a and b, a or b, not a)
```
**Explanation**: `and` (both true), `or` (at least one true), `not` (negation). Short‑circuit evaluation applies.

### 14. Assignment Operators
```python
x = 5
x += 3   # same as x = x + 3
x *= 2
print(x)   # 16
```
**Explanation**: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` update a variable in place.

### 15. Identity and Membership Operators
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b, a is c)          # True, False (is checks object identity)
print(2 in a, 5 not in a)      # True, True
```
**Explanation**: `is` / `is not` compare memory addresses. `in` / `not in` test membership in sequences.

---

## 16–20: String Operations

### 16. String Concatenation
```python
first = "John"
last = "Doe"
full = first + " " + last
print(full)
```
**Explanation**: Use `+` to join strings. For many strings, `join()` is more efficient.

### 17. String Formatting (f‑string)
```python
name = "Alice"
age = 30
print(f"{name} is {age} years old.")
```
**Explanation**: f‑strings (Python 3.6+) embed expressions inside `{}` directly in the string.

### 18. String Formatting (`.format()` and `%`)
```python
print("{} is {} years old.".format(name, age))
print("%s is %d years old." % (name, age))
```
**Explanation**: Older formatting methods. `.format()` is flexible; `%` is inspired by C’s `printf`.

### 19. Common String Methods
```python
text = "  Hello, World!  "
print(text.strip())        # remove whitespace
print(text.lower())        # lowercase
print(text.replace("World", "Python"))
print(text.split(","))     # split into list
```
**Explanation**: Strings are immutable; these methods return new strings. `strip()`, `lower()`, `replace()`, `split()`.

### 20. String Joining
```python
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)   # "Python is fun"
```
**Explanation**: `join()` concatenates elements of an iterable with a separator. More efficient than `+` in loops.

---

## 21–25: Input/Output

### 21. Basic Input
```python
name = input("Enter your name: ")
print("Hello", name)
```
**Explanation**: `input()` reads a line from stdin as a string. Use `int(input())` to read numbers.

### 22. Print with Separator and End
```python
print("a", "b", "c", sep="-", end="!\n")
# Output: a-b-c!
```
**Explanation**: `sep` defines the separator between arguments; `end` defines the suffix (default newline).

### 23. Reading a File
```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```
**Explanation**: `open()` with mode `"r"` (read). The `with` statement ensures the file is closed automatically.

### 24. Writing to a File
```python
with open("output.txt", "w") as f:
    f.write("Hello, file!\n")
    f.writelines(["Line 2\n", "Line 3\n"])
```
**Explanation**: Mode `"w"` overwrites the file. Use `"a"` to append. `write()` writes a string; `writelines()` writes a list of strings.

### 25. Reading Lines Iteratively
```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```
**Explanation**: Iterating over the file object yields lines one by one (memory‑efficient for large files).

---

## 26–30: Control Flow

### 26. if‑elif‑else
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(grade)   # B
```
**Explanation**: Conditional branching. No parentheses needed, but indentation defines blocks.

### 27. Ternary Conditional Operator
```python
age = 18
status = "adult" if age >= 18 else "minor"
print(status)
```
**Explanation**: Shorthand for `if‑else` assignments: `value_if_true if condition else value_if_false`.

### 28. for Loop over Range
```python
for i in range(5):
    print(i)   # 0 1 2 3 4
```
**Explanation**: `range(stop)` yields numbers 0 to stop‑1. `range(start, stop, step)` gives more control.

### 29. for Loop over Sequence
```python
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
```
**Explanation**: Iterate directly over list, tuple, string, etc. Use `enumerate()` to get index and value.

### 30. while Loop
```python
count = 0
while count < 3:
    print(count)
    count += 1
```
**Explanation**: Repeats as long as the condition is true. Ensure the condition eventually becomes false to avoid infinite loops.

### 31. break, continue, and else on Loops
```python
for i in range(10):
    if i == 3:
        continue    # skip print for 3
    if i == 7:
        break       # exit loop
    print(i)
else:
    print("Loop completed without break")   # not executed because break occurred
```
**Explanation**: `break` terminates the loop; `continue` skips the rest of the iteration. The `else` clause runs only if the loop ends normally (no `break`).

---

## 32–36: Functions

### 32. Basic Function Definition
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```
**Explanation**: `def` keyword, parameters, optional `return`. If no `return`, function returns `None`.

### 33. Default Parameter Values
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(3, 3))   # 27
```
**Explanation**: Default values are evaluated at definition time (caution with mutable defaults like `[]`).

### 34. Keyword Arguments
```python
def describe(person, age, city):
    print(f"{person} is {age} from {city}")

describe(age=25, city="Paris", person="John")
```
**Explanation**: Arguments can be passed by name, allowing out‑of‑order passing.

### 35. Variable‑Length Arguments (`*args`)
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))   # 10
```
**Explanation**: `*args` collects extra positional arguments into a tuple. The name `args` is conventional.

### 36. Variable‑Length Keyword Arguments (`**kwargs`)
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)
```
**Explanation**: `**kwargs` collects extra keyword arguments into a dictionary.

---

## 37–40: Lambda Functions

### 37. Simple Lambda
```python
square = lambda x: x ** 2
print(square(5))   # 25
```
**Explanation**: Anonymous function defined with `lambda`. Useful for short, throwaway functions.

### 38. Lambda with Multiple Arguments
```python
add = lambda a, b: a + b
print(add(3, 7))
```
**Explanation**: Lambda can take any number of arguments, but only one expression.

### 39. Lambda with `map()`
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)   # [1, 4, 9, 16]
```
**Explanation**: `map()` applies a function to each element of an iterable.

### 40. Lambda with `filter()`
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6]
```
**Explanation**: `filter()` keeps elements for which the function returns `True`.

---

## 41–50: Data Structures (Lists, Tuples, Dicts, Sets)

### 41. List Basics
```python
fruits = ["apple", "banana"]
fruits.append("orange")          # add to end
fruits.insert(1, "grape")        # insert at index
print(fruits)                    # ['apple', 'grape', 'banana', 'orange']
```
**Explanation**: Lists are ordered, mutable, and allow duplicates.

### 42. List Slicing
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])      # [1, 2, 3]
print(nums[:3])       # [0, 1, 2]
print(nums[::2])      # [0, 2, 4]
```
**Explanation**: `[start:stop:step]` extracts sublists. Negative indices count from the end.

### 43. List Comprehension
```python
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]
```
**Explanation**: Concise way to create lists. Can include conditionals: `[x for x in range(10) if x % 2 == 0]`.

### 44. Tuple (Immutable Sequence)
```python
point = (10, 20)
x, y = point                # unpacking
print(x, y)
# point[0] = 5             # TypeError: tuple doesn't support item assignment
```
**Explanation**: Tuples are immutable and often used for fixed collections. They can be used as dictionary keys, unlike lists.

### 45. Dictionary Basics
```python
person = {"name": "Alice", "age": 30}
print(person["name"])
person["city"] = "New York"   # add new key
print(person.keys(), person.values())
```
**Explanation**: Dictionaries store key‑value pairs. Keys must be immutable (strings, numbers, tuples).

### 46. Dictionary Comprehension
```python
squares_dict = {n: n**2 for n in range(4)}
print(squares_dict)   # {0: 0, 1: 1, 2: 4, 3: 9}
```
**Explanation**: Similar to list comprehension but produces a dictionary.

### 47. Set (Unordered Unique Elements)
```python
colors = {"red", "green", "blue", "red"}  # duplicates removed
print(colors)           # {'blue', 'green', 'red'}
colors.add("yellow")
```
**Explanation**: Sets are unordered, mutable, and cannot contain duplicates. Useful for membership tests and mathematical operations.

### 48. Set Operations
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # union: {1,2,3,4,5}
print(a & b)   # intersection: {3}
print(a - b)   # difference: {1,2}
```
**Explanation**: `|` union, `&` intersection, `-` difference, `^` symmetric difference.

### 49. `enumerate()` in Loops
```python
items = ["a", "b", "c"]
for idx, value in enumerate(items):
    print(idx, value)   # 0 a, 1 b, 2 c
```
**Explanation**: `enumerate()` adds a counter to an iterable, returning pairs of (index, item).

### 50. `zip()` for Parallel Iteration
```python
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```
**Explanation**: `zip()` aggregates elements from multiple iterables; stops when the shortest iterable ends.

---

## 51–55: Modules and Packages

### 51. Importing a Module
```python
import math
print(math.sqrt(16))   # 4.0
```
**Explanation**: Use `import module_name` to bring the entire module into the namespace.

### 52. Import Specific Functions
```python
from math import sqrt, pi
print(sqrt(25), pi)
```
**Explanation**: Import only what you need to avoid namespace clutter.

### 53. Import with Alias
```python
import numpy as np   # common alias for NumPy
print(np.array([1,2,3]))
```
**Explanation**: Alias long module names for convenience.

### 54. `__name__ == "__main__"` Guard
```python
def main():
    print("This runs only when executed directly")

if __name__ == "__main__":
    main()
```
**Explanation**: Prevents code from running when the module is imported. Useful for scripts.

### 55. Listing Module Contents
```python
import math
print(dir(math))   # shows all attributes of the module
```
**Explanation**: `dir()` returns a list of names in the current scope or in a given object.

---

## 56–60: Exception Handling

### 56. Basic try‑except
```python
try:
    x = int("not a number")
except ValueError:
    print("Conversion failed")
```
**Explanation**: Catches a specific exception type. The program continues after the `except` block.

### 57. Multiple Except Clauses
```python
try:
    lst = [1,2,3]
    print(lst[5])
except IndexError:
    print("Index out of range")
except Exception as e:
    print(f"Other error: {e}")
```
**Explanation**: You can handle different exception types separately. `Exception` catches all built‑in exceptions.

### 58. else and finally
```python
try:
    f = open("missing.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print("File opened successfully")
    f.close()
finally:
    print("This always runs")
```
**Explanation**: `else` runs if no exception; `finally` runs no matter what (cleanup actions).

### 59. Raising Exceptions
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)
```
**Explanation**: Use `raise` to signal an error. You can create custom exception classes.

### 60. Custom Exception Class
```python
class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age negative")
```
**Explanation**: Inherit from `Exception` to create your own exception types.

---

## 61–65: Classes and Object-Oriented Programming

### 61. Simple Class Definition
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Rex")
print(my_dog.bark())
```
**Explanation**: `__init__` is the constructor. `self` refers to the instance.

### 62. Class Variable vs. Instance Variable
```python
class Counter:
    count = 0   # class variable (shared)

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count   # instance variable

c1 = Counter()
c2 = Counter()
print(c1.id, c2.id, Counter.count)   # 1 2 2
```
**Explanation**: Class variables belong to the class; instance variables belong to each object.

### 63. Instance, Class, and Static Methods
```python
class MyClass:
    def instance_method(self):
        return "instance method"

    @classmethod
    def class_method(cls):
        return "class method"

    @staticmethod
    def static_method():
        return "static method"

print(MyClass.class_method())
print(MyClass.static_method())
obj = MyClass()
print(obj.instance_method())
```
**Explanation**: `@classmethod` receives the class as first argument; `@staticmethod` receives no special first argument.

### 64. Property Decorator (Getters/Setters)
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

p = Person("Alice")
print(p.name)   # getter
p.name = "Bob"  # setter
```
**Explanation**: `@property` allows you to define getters/setters that behave like attributes.

### 65. `__str__` and `__repr__`
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("1984", "Orwell")
print(str(book))   # human‑readable
print(repr(book))  # unambiguous representation
```
**Explanation**: `__str__` is used by `print()`; `__repr__` is used by interactive interpreter and for debugging.

---

## 66–70: Inheritance and Polymorphism

### 66. Single Inheritance
```python
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

cat = Cat()
print(cat.speak())   # Meow (overrides parent)
```
**Explanation**: Child class inherits all methods of parent class. Override by redefining.

### 67. `super()` to Call Parent Method
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # call Parent's __init__
        self.age = age

c = Child("Alice", 10)
print(c.name, c.age)
```
**Explanation**: `super()` returns a proxy object that delegates method calls to the parent class.

### 68. Multiple Inheritance
```python
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

d = Duck()
print(d.fly(), d.swim())
```
**Explanation**: A class can inherit from multiple parents. Method resolution order (MRO) defines which parent is used first.

### 69. Abstract Base Classes (ABC)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

# s = Shape()   # TypeError: Can't instantiate abstract class
c = Circle(5)
print(c.area())
```
**Explanation**: Abstract methods must be implemented by concrete subclasses. ABCs are used for defining interfaces.

### 70. `isinstance()` and `issubclass()`
```python
class Base:
    pass
class Derived(Base):
    pass

obj = Derived()
print(isinstance(obj, Derived))   # True
print(isinstance(obj, Base))      # True (polymorphism)
print(issubclass(Derived, Base))  # True
```
**Explanation**: Check object types and class relationships.

---

## 71–75: Decorators

### 71. Simple Function Decorator
```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello"

print(greet())   # "HELLO"
```
**Explanation**: A decorator is a function that takes another function and extends its behavior without modifying it directly.

### 72. Decorator with Arguments
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()   # prints "Hi!" three times
```
**Explanation**: Nested decorators allow passing parameters to the decorator factory.

### 73. Preserving Metadata with `functools.wraps`
```python
import functools

def log(func):
    @functools.wraps(func)   # preserves func.__name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add.__name__)   # "add" (without wraps would be "wrapper")
```
**Explanation**: `@wraps` copies the original function’s metadata to the wrapper, essential for debugging.

### 74. Class Decorator
```python
def add_repr(cls):
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(3, 4)
print(p)   # Point({'x': 3, 'y': 4})
```
**Explanation**: Decorators can be applied to classes to add methods or modify them.

### 75. Chaining Decorators
```python
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def hello():
    return "Hello"

print(hello())   # <b><i>Hello</i></b>
```
**Explanation**: Multiple decorators are applied from bottom to top (the one nearest the function runs first).

---

## 76–80: Generators and Iterators

### 76. Simple Generator (`yield`)
```python
def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)   # 0,1,2,3
```
**Explanation**: Generators produce values on the fly using `yield`. They are memory‑efficient for large sequences.

### 77. Generator Expression
```python
squares = (x**2 for x in range(5))
print(next(squares))   # 0
print(next(squares))   # 1
print(list(squares))   # [4, 9, 16]
```
**Explanation**: Similar to list comprehension but uses parentheses; yields items one at a time.

### 78. `send()` Method to Communicate with Generator
```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)            # prime the generator (advance to first yield)
print(gen.send(5))   # 5
print(gen.send(3))   # 8
gen.close()
```
**Explanation**: `send()` sends a value into the generator, which becomes the result of `yield`. Used for coroutines.

### 79. Generator with `yield from`
```python
def chain(*iterables):
    for it in iterables:
        yield from it   # delegates to sub‑iterator

result = list(chain("AB", [1,2,3]))
print(result)   # ['A', 'B', 1, 2, 3]
```
**Explanation**: `yield from` yields all values from another iterable, simplifying nested generators.

### 80. Infinite Generator
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")   # 0 1 1 2 3 5 8 13 21 34
```
**Explanation**: Generators can represent infinite sequences; stop when you choose.

---

## 81–85: Context Managers

### 81. `with` Statement for Files (Built‑in)
```python
with open("file.txt", "w") as f:
    f.write("Hello")
# File automatically closed after the block
```
**Explanation**: Context managers set up and tear down resources. `with` guarantees cleanup even if an exception occurs.

### 82. Custom Context Manager (Class‑based)
```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile("test.txt") as f:
    f.write("Hello, context!")
```
**Explanation**: Implement `__enter__` and `__exit__` to create a context manager.

### 83. Custom Context Manager (Generator‑based with `contextlib`)
```python
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    f = open(name, "w")
    try:
        yield f
    finally:
        f.close()

with managed_file("test2.txt") as f:
    f.write("Using contextlib")
```
**Explanation**: `@contextmanager` turns a generator into a context manager. The `yield` point is where the `with` block runs.

### 84. Suppressing Exceptions
```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("missing_file.txt")   # No error raised
```
**Explanation**: `suppress` temporarily suppresses specified exceptions.

### 85. Redirecting Standard Output
```python
import io
from contextlib import redirect_stdout

f = io.StringIO()
with redirect_stdout(f):
    print("This goes to f")
output = f.getvalue()
print("Captured:", output)
```
**Explanation**: `redirect_stdout` temporarily reroutes `print()` and `sys.stdout`.

---

## 86–90: File I/O (Advanced)

### 86. Reading Binary File
```python
with open("image.jpg", "rb") as f:
    data = f.read(1024)   # read 1024 bytes
print(f"First 20 bytes: {data[:20]}")
```
**Explanation**: Mode `"rb"` reads binary data. Write binary with `"wb"`.

### 87. Writing CSV File
```python
import csv
data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```
**Explanation**: The `csv` module handles CSV formatting. `newline=""` prevents extra blank lines on Windows.

### 88. Reading JSON
```python
import json
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)   # from string
print(data["name"])

with open("data.json", "r") as f:
    loaded = json.load(f)      # from file
```
**Explanation**: `json.loads()` parses JSON string; `json.load()` reads from file. `json.dumps()` and `json.dump()` write JSON.

### 89. Using `tempfile` for Temporary Files
```python
import tempfile

with tempfile.TemporaryFile(mode="w+") as tmp:
    tmp.write("temporary data")
    tmp.seek(0)
    print(tmp.read())   # prints "temporary data"
# File deleted automatically after the block
```
**Explanation**: `TemporaryFile` creates anonymous temporary files that are automatically cleaned up.

### 90. File Seeking and Telling
```python
with open("data.txt", "rb") as f:
    print(f.tell())     # 0
    f.seek(10)          # move to byte 10
    print(f.read(5))
    print(f.tell())     # 15
```
**Explanation**: `seek(offset, whence)` moves the file pointer; `tell()` returns current position.

---

## 91–95: Built‑in Functions and Functional Tools

### 91. `map()` and `filter()` (Recap with `list`)
```python
nums = [1,2,3,4]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x%2==0, nums))
```
**Explanation**: Already covered, but included for completeness.

### 92. `reduce()` from `functools`
```python
from functools import reduce
nums = [1,2,3,4]
product = reduce(lambda x, y: x*y, nums)
print(product)   # 24
```
**Explanation**: `reduce()` cumulatively applies a function to the items of an iterable, reducing to a single value.

### 93. `zip()` with Unequal Lengths
```python
a = [1,2,3]
b = ['x','y']
zipped = list(zip(a, b))          # [(1,'x'), (2,'y')]
from itertools import zip_longest
zipped_long = list(zip_longest(a, b, fillvalue=0))  # [(1,'x'),(2,'y'),(3,0)]
```
**Explanation**: `zip()` stops at the shortest iterable; `itertools.zip_longest()` fills missing values.

### 94. `sorted()` with Custom Key
```python
words = ["apple", "Banana", "cherry"]
sorted_words = sorted(words, key=str.lower)
print(sorted_words)   # ['apple', 'Banana', 'cherry'] (case‑insensitive)
```
**Explanation**: `sorted()` returns a new sorted list. `key` specifies a function to extract comparison keys.

### 95. `any()` and `all()`
```python
conditions = [True, False, True]
print(any(conditions))   # True (at least one True)
print(all(conditions))   # False (not all are True)
```
**Explanation**: `any()` returns `True` if any element of the iterable is truthy. `all()` returns `True` only if all are truthy.

---

## 96–100: Advanced Topics (Decorators, Closures, Dataclasses, etc.)

### 96. Closures (Function Returning Function)
```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times2 = make_multiplier(2)
print(times2(5))   # 10
```
**Explanation**: Inner function remembers the environment (`n`) where it was created (closure).

### 97. `functools.partial`
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))   # 25
print(cube(5))     # 125
```
**Explanation**: `partial` freezes some arguments of a function, creating a new function with fewer parameters.

### 98. Dataclasses (Python 3.7+)
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
print(p)           # Point(x=1.0, y=2.0)
```
**Explanation**: `@dataclass` automatically adds `__init__`, `__repr__`, `__eq__`, etc., based on type annotations.

### 99. Enums
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)          # Color.RED
print(Color.RED.name)     # RED
print(Color.RED.value)    # 1
```
**Explanation**: Enums define a set of symbolic names bound to unique constant values. Useful for code clarity.

### 100. Simple `async` / `await` (Coroutine)
```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_hello())

# asyncio.run(main())   # Uncomment to run (requires Python 3.7+)
```
**Explanation**: Asynchronous programming with `async def` defines a coroutine; `await` pauses until an awaitable completes. `asyncio.gather()` runs multiple coroutines concurrently.

---

These 100 snippets cover the essential syntax and features of Python, from basic I/O and control flow to advanced topics like decorators, generators, and async code. Mastering them will give you a solid foundation in Python programming.