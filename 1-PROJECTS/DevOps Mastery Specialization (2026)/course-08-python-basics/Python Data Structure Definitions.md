# Python Data Structure Definitions

## List

A **list** is an ordered, mutable (changeable) collection of items enclosed in square brackets `[ ]`. Lists can contain items of different data types and allow duplicates.

```python
my_list = [1, "hello", 3.14, True]
```

Key characteristics:

- Ordered (maintains insertion order)
- Mutable (can be modified after creation)
- Allows duplicates
- Accessed by index starting at 0

## Dictionary

A **dictionary** is an unordered, mutable collection of key-value pairs enclosed in curly braces `{ }`. Each key must be unique and is used to access its corresponding value.

```python
my_dict = {"name": "Alice", "age": 25, "city": "NYC"}
```

Key characteristics:

- Unordered (Python 3.7+ maintains insertion order)
- Mutable (can be modified)
- Keys must be unique and immutable
- Accessed by key, not by index

## Tuple

A **tuple** is an ordered, immutable (unchangeable) collection of items enclosed in parentheses `( )`. Once created, tuples cannot be modified, though they can contain mutable objects like lists.

```python
my_tuple = (1, "hello", 3.14, True)
```

Key characteristics:

- Ordered (maintains insertion order)
- Immutable (cannot be changed after creation)
- Allows duplicates
- Slightly faster and uses less memory than lists
- Accessed by index starting at 0

## Key Differences

|Feature|List|Dictionary|Tuple|
|---|---|---|---|
|**Syntax**|`[ ]`|`{ }`|`( )`|
|**Mutable**|Yes|Yes|No|
|**Access**|By index|By key|By index|
|**Ordered**|Yes|Yes (3.7+)|Yes|
|**Duplicates**|Allowed|Keys: No, Values: Yes|Allowed|
|**Use Case**|Ordered collections|Key-value storage|Fixed collections, dict keys|

**When to use each:**

- **List**: When you need an ordered, changeable collection
- **Dictionary**: When you need to map unique keys to values
- **Tuple**: When you need an immutable collection or to use as dictionary keys