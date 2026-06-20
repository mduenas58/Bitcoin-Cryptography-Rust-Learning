## List vs Dictionary in Python

Here are the key differences between lists and dictionaries in Python:

### **1. Structure and Syntax**

```python
# List - ordered collection using square brackets
my_list = [1, 2, 3, 'apple', 'banana']

# Dictionary - key-value pairs using curly braces
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

### **2. Accessing Elements**

```python
# List - access by index position (0-based)
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

# Dictionary - access by key
person = {'name': 'Alice', 'age': 30}
print(person['name'])  # Output: Alice
print(person['age'])   # Output: 30
```

### **3. Mutability and Modification**

```python
# List - modify by index
colors = ['red', 'green', 'blue']
colors[1] = 'yellow'  # Replace element at index 1
print(colors)  # Output: ['red', 'yellow', 'blue']
colors.append('purple')  # Add to end

# Dictionary - modify by key
scores = {'math': 90, 'science': 85}
scores['math'] = 95  # Update existing key
scores['history'] = 88  # Add new key-value pair
print(scores)  # Output: {'math': 95, 'science': 85, 'history': 88}
```

### **4. Order Preservation**

```python
# Python 3.7+: Lists and dicts both maintain insertion order
# But the concept differs

# List - order is intrinsic and meaningful
todo_list = ['wake up', 'eat breakfast', 'work']
print(todo_list[0])  # First item is important

# Dictionary - order is preserved but not used for access
config = {'host': 'localhost', 'port': 8080, 'debug': True}
# Order matters less than key names
```

### **5. Performance Characteristics**

```python
# List - O(n) for searching by value
# Good for sequential access and ordered data
numbers = [10, 20, 30, 40, 50]
# Finding 30 requires checking each element
if 30 in numbers:  # O(n) operation
    print("Found!")

# Dictionary - O(1) for key lookup
# Excellent for quick lookups by unique identifier
user_db = {'user123': 'Alice', 'user456': 'Bob', 'user789': 'Charlie'}
# Finding Bob is instantaneous by key
print(user_db['user456'])  # O(1) operation - very fast!
```

### **6. When to Use Each**

```python
# ✅ Use List for:
# - Ordered sequences
# - Duplicates allowed
# - Index-based access
# - Stack/queue operations

shopping_cart = ['apple', 'banana', 'apple']  # Duplicates ok
temperatures = [72, 68, 75, 72, 70]  # Ordered readings

# ✅ Use Dictionary for:
# - Key-value mappings
# - Unique identifiers
# - Fast lookups by name/label
# - Counting occurrences

inventory = {'apples': 10, 'bananas': 5, 'oranges': 8}  # Counts
contacts = {'John': '555-1234', 'Jane': '555-5678'}  # Phone book

# ❌ Wrong usage:
# Using list for phone book - must remember positions
phone_list = ['John', '555-1234', 'Jane', '555-5678']  # Awkward!

# Using dict for ordered sequence - keys unnecessary
days = {0: 'Mon', 1: 'Tue', 2: 'Wed'}  # Just use a list!
```

### **7. Common Operations Comparison**

```python
# Length
my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2}
print(len(my_list))  # 3
print(len(my_dict))  # 2

# Checking existence
print(2 in my_list)  # True (checks value)
print('a' in my_dict)  # True (checks key, NOT value)

# Looping
for item in my_list:
    print(item)  # Prints values

for key in my_dict:
    print(key, my_dict[key])  # Prints keys and values

# Getting all values
print(my_dict.values())  # dict_values([1, 2])
```

### **Summary Table**

| Feature | List | Dictionary |
|---------|------|------------|
| Syntax | `[1, 2, 3]` | `{'a': 1, 'b': 2}` |
| Access by | Index (position) | Key (label) |
| Order | Maintained | Maintained (Python 3.7+) |
| Duplicates | Allowed | Keys must be unique |
| Lookup speed | O(n) for value | O(1) for key |
| Use case | Sequences | Mappings |