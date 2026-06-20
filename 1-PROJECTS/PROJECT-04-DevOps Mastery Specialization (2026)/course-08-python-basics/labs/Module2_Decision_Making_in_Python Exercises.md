# Module 2 – Decision Making in Python Exercises

This document contains 3 exercises for each of the two main topics in Module 2:

1. **Comparison Operators** – how Python compares values
2. **Conditional Statements** – how to control program flow using `if`, `elif`, and `else`

---

## Topic 1: Comparison Operators

Comparison operators evaluate two values and return a Boolean result: either `True` or `False`. Python's comparison operators are:

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`==`|Equal to|`5 == 5`|`True`|
|`!=`|Not equal to|`5 != 3`|`True`|
|`>`|Greater than|`7 > 4`|`True`|
|`<`|Less than|`2 < 9`|`True`|
|`>=`|Greater than or equal to|`5 >= 5`|`True`|
|`<=`|Less than or equal to|`3 <= 10`|`True`|

These operators work with numbers, strings (alphabetically), and other comparable types.

---

### Exercise 1.1 – Grade Checker

**Objective:** Use comparison operators to determine whether a test score meets passing thresholds.

**Instructions:**

A school defines grades as follows: 90 or above is an A, 80–89 is a B, 70–79 is a C, and below 70 is a failing grade. Write a program that asks the user for a numeric score and uses comparison operators to print a series of True/False evaluations.

```python
# Exercise 1.1 – Grade Checker

score = int(input("Enter your test score (0-100): "))

# Evaluate the score against each threshold
print("=== Grade Threshold Checks ===")
print("Score is 90 or above (A grade):   ", score >= 90)
print("Score is 80 or above (B+ grade):  ", score >= 80)
print("Score is 70 or above (passing):   ", score >= 70)
print("Score is below 70 (failing):      ", score < 70)
print("Score is exactly 100 (perfect):   ", score == 100)
print("Score is not 0 (attempted):       ", score != 0)
```

**Sample Run 1 (score = 85):**

```
Enter your test score (0-100): 85
=== Grade Threshold Checks ===
Score is 90 or above (A grade):    False
Score is 80 or above (B+ grade):   True
Score is 70 or above (passing):    True
Score is below 70 (failing):       False
Score is exactly 100 (perfect):    False
Score is not 0 (attempted):        True
```

**Sample Run 2 (score = 65):**

```
Enter your test score (0-100): 65
=== Grade Threshold Checks ===
Score is 90 or above (A grade):    False
Score is 80 or above (B+ grade):   False
Score is 70 or above (passing):    False
Score is below 70 (failing):       True
Score is exactly 100 (perfect):    False
Score is not 0 (attempted):        True
```

**Explanation:**

- `score >= 90` checks whether the value is 90 or higher, using the "greater than or equal to" operator.
- `score < 70` returns `True` only if the score is strictly less than 70.
- `score == 100` uses the equality operator (two equal signs). Note the difference from assignment (`=`).
- `score != 0` returns `True` when the score is anything other than zero.
- Each comparison produces an independent Boolean result that you can print, store, or use in a condition.

---

### Exercise 1.2 – Password Strength Meter

**Objective:** Use comparison operators on strings and numbers to evaluate password length rules.

**Instructions:**

Many websites require passwords to meet length requirements. Write a program that reads a password from the user and checks it against three rules using comparison operators: it must be at least 8 characters, it must be at most 20 characters, and it must be longer than a "minimum secure length" of 12.

```python
# Exercise 1.2 – Password Strength Meter

password = input("Enter a password to evaluate: ")
length = len(password)

MIN_LENGTH = 8
MAX_LENGTH = 20
SECURE_LENGTH = 12

print(f"\nPassword length: {length} characters")
print("=== Length Rule Checks ===")
print(f"Meets minimum ({MIN_LENGTH} chars):      ", length >= MIN_LENGTH)
print(f"Within maximum ({MAX_LENGTH} chars):     ", length <= MAX_LENGTH)
print(f"Considered secure ({SECURE_LENGTH}+ chars): ", length >= SECURE_LENGTH)
print(f"Too short (under {MIN_LENGTH}):           ", length < MIN_LENGTH)
print(f"Too long (over {MAX_LENGTH}):             ", length > MAX_LENGTH)
print(f"Exactly the minimum length:          ", length == MIN_LENGTH)
```

**Sample Run 1 (password = "hello123"):**

```
Enter a password to evaluate: hello123

Password length: 8 characters
=== Length Rule Checks ===
Meets minimum (8 chars):       True
Within maximum (20 chars):     True
Considered secure (12+ chars): False
Too short (under 8):           False
Too long (over 20):            False
Exactly the minimum length:    True
```

**Sample Run 2 (password = "MySecureP@ssw0rd!"):**

```
Enter a password to evaluate: MySecureP@ssw0rd!

Password length: 17 characters
=== Length Rule Checks ===
Meets minimum (8 chars):       True
Within maximum (20 chars):     True
Considered secure (12+ chars): True
Too short (under 8):           False
Too long (over 20):            False
Exactly the minimum length:    False
```

**Explanation:**

- `len(password)` returns the integer number of characters in the string.
- Comparison operators work on integers returned by `len()` just like on any number.
- Using named constants (`MIN_LENGTH`, `MAX_LENGTH`) instead of "magic numbers" makes code more readable and easier to update.
- Multiple comparisons can be performed independently on the same value.
- `length == MIN_LENGTH` is `True` only when the password is exactly 8 characters — not longer, not shorter.

---

### Exercise 1.3 – Temperature Comparator

**Objective:** Compare two values and explore all six comparison operators together.

**Instructions:**

Write a program that takes two temperatures from the user (in Celsius) and applies all six comparison operators to them, printing each result. Then, determine which temperature is the coldest using `<`.

```python
# Exercise 1.3 – Temperature Comparator

print("=== Temperature Comparator ===")
temp1 = float(input("Enter first temperature (°C): "))
temp2 = float(input("Enter second temperature (°C): "))

print(f"\nComparing {temp1}°C and {temp2}°C:")
print(f"  temp1 == temp2 : {temp1 == temp2}")
print(f"  temp1 != temp2 : {temp1 != temp2}")
print(f"  temp1 >  temp2 : {temp1 > temp2}")
print(f"  temp1 <  temp2 : {temp1 < temp2}")
print(f"  temp1 >= temp2 : {temp1 >= temp2}")
print(f"  temp1 <= temp2 : {temp1 <= temp2}")

print("\n--- Interpretation ---")
is_equal = temp1 == temp2
is_first_colder = temp1 < temp2
print(f"Temperatures are equal: {is_equal}")
print(f"First temperature is colder: {is_first_colder}")
```

**Sample Run 1 (18.5 and 25.0):**

```
Enter first temperature (°C): 18.5
Enter second temperature (°C): 25.0

Comparing 18.5°C and 25.0°C:
  temp1 == temp2 : False
  temp1 != temp2 : True
  temp1 >  temp2 : False
  temp1 <  temp2 : True
  temp1 >= temp2 : False
  temp1 <= temp2 : True

--- Interpretation ---
Temperatures are equal: False
First temperature is colder: True
```

**Sample Run 2 (22.0 and 22.0):**

```
Enter first temperature (°C): 22.0
Enter second temperature (°C): 22.0

Comparing 22.0°C and 22.0°C:
  temp1 == temp2 : True
  temp1 != temp2 : False
  temp1 >  temp2 : False
  temp1 <  temp2 : False
  temp1 >= temp2 : True
  temp1 <= temp2 : True

--- Interpretation ---
Temperatures are equal: True
First temperature is colder: False
```

**Explanation:**

- Comparison results (`True`/`False`) can be stored in variables just like any other value. This makes code easier to read and reuse.
- `float()` is used instead of `int()` to accept decimal temperatures like 18.5.
- When two values are equal, `==`, `>=`, and `<=` all return `True`, while `>`, `<`, and `!=` return `False`.
- Storing the result of a comparison in a descriptive variable (e.g., `is_first_colder`) makes the meaning of the expression self-documenting.

---

## Topic 2: Conditional Statements

Conditional statements allow a program to choose which code to execute based on whether a condition is `True` or `False`. Python provides three keywords:

- **`if`** – runs a block of code when a condition is True
- **`elif`** (else if) – tests another condition when the previous `if` was False
- **`else`** – runs when none of the preceding conditions were True

**Syntax:**

```python
if condition1:
    # runs when condition1 is True
elif condition2:
    # runs when condition1 is False and condition2 is True
else:
    # runs when all conditions above were False
```

Indentation (4 spaces or 1 tab) defines the block of code belonging to each branch.

---

### Exercise 2.1 – Number Classifier

**Objective:** Use `if`, `elif`, and `else` to classify a number as positive, negative, or zero, and as even or odd.

**Instructions:**

Write a program that reads an integer from the user and classifies it in two independent ways: first, whether it is positive, negative, or zero; second, whether it is even or odd (zero is even).

```python
# Exercise 2.1 – Number Classifier

number = int(input("Enter an integer: "))

# Classification 1: positive, negative, or zero
print("\n--- Sign Classification ---")
if number > 0:
    print(f"{number} is a POSITIVE number.")
elif number < 0:
    print(f"{number} is a NEGATIVE number.")
else:
    print(f"{number} is ZERO.")

# Classification 2: even or odd
print("\n--- Parity Classification ---")
if number % 2 == 0:
    print(f"{number} is an EVEN number.")
else:
    print(f"{number} is an ODD number.")
```

**Sample Run 1 (number = 7):**

```
Enter an integer: 7

--- Sign Classification ---
7 is a POSITIVE number.

--- Parity Classification ---
7 is an ODD number.
```

**Sample Run 2 (number = -4):**

```
Enter an integer: -4

--- Sign Classification ---
-4 is a NEGATIVE number.

--- Parity Classification ---
-4 is an EVEN number.
```

**Sample Run 3 (number = 0):**

```
Enter an integer: 0

--- Sign Classification ---
0 is ZERO.

--- Parity Classification ---
0 is an EVEN number.
```

**Explanation:**

- The `if`/`elif`/`else` chain for sign classification tests three mutually exclusive outcomes. Only one branch runs per execution.
- The `else` clause acts as a "catch-all" — it runs only when all preceding conditions are `False`. Here it handles the one remaining case: zero.
- The even/odd check uses only `if`/`else` (no `elif`) because there are exactly two outcomes.
- `number % 2 == 0` uses the modulo operator (`%`) which returns the remainder after division. Any number divisible by 2 has a remainder of 0.
- Each classification block is independent; Python runs both regardless of the other's result.

---

### Exercise 2.2 – Ticket Price Calculator

**Objective:** Use nested `if`/`elif`/`else` statements to calculate a price based on two criteria: age and day of the week.

**Instructions:**

A movie theater uses this pricing policy:

- Children (under 12): $5.00 on weekdays, $7.00 on weekends
- Adults (12–64): $12.00 on weekdays, $15.00 on weekends
- Seniors (65 and above): $8.00 on weekdays, $10.00 on weekends

Write a program that asks for the customer's age and whether it is a weekend, then calculates and prints the ticket price.

```python
# Exercise 2.2 – Ticket Price Calculator

age = int(input("Enter customer age: "))
day_type = input("Is it a weekend? (yes/no): ").strip().lower()

is_weekend = day_type == "yes"

print(f"\nAge: {age}, Weekend: {is_weekend}")
print("--- Ticket Price ---")

if age < 12:
    # Child pricing
    if is_weekend:
        price = 7.00
    else:
        price = 5.00
    category = "Child"
elif age <= 64:
    # Adult pricing
    if is_weekend:
        price = 15.00
    else:
        price = 12.00
    category = "Adult"
else:
    # Senior pricing
    if is_weekend:
        price = 10.00
    else:
        price = 8.00
    category = "Senior"

print(f"Category: {category}")
print(f"Ticket price: ${price:.2f}")
```

**Sample Run 1 (age = 8, weekend = yes):**

```
Enter customer age: 8
Is it a weekend? (yes/no): yes

Age: 8, Weekend: True
--- Ticket Price ---
Category: Child
Ticket price: $7.00
```

**Sample Run 2 (age = 35, weekend = no):**

```
Enter customer age: 35
Is it a weekend? (yes/no): no

Age: 35, Weekend: False
--- Ticket Price ---
Category: Adult
Ticket price: $12.00
```

**Sample Run 3 (age = 70, weekend = yes):**

```
Enter customer age: 70
Is it a weekend? (yes/no): yes

Age: 70, Weekend: True
--- Ticket Price ---
Category: Senior
Ticket price: $10.00
```

**Explanation:**

- **Nested conditionals** allow decisions to be refined. The outer `if`/`elif`/`else` determines the age category, and then an inner `if`/`else` inside each branch selects the correct price.
- `day_type == "yes"` is itself a comparison that produces `True` or `False`. Storing it in `is_weekend` makes the nested conditions cleaner to read.
- `category` and `price` are assigned inside each branch; they are available after the `if` block because Python does not create a new scope for conditional branches.
- `f"${price:.2f}"` formats the float to always show exactly two decimal places — standard for currency output.
- The `elif age <= 64` condition is only reached when `age >= 12` (because the first `if` already handled ages below 12), so there is no need to write `12 <= age <= 64`.

---

### Exercise 2.3 – Simple ATM Menu

**Objective:** Combine `if`/`elif`/`else` with user input to build a small interactive menu that performs different actions based on the user's choice.

**Instructions:**

Write a simple ATM simulation that starts with a balance of $1,000. The user chooses an option — check balance, deposit, or withdraw — and the program performs the appropriate action. Use conditional statements to handle each option and to validate the transaction (e.g., prevent overdraft).

```python
# Exercise 2.3 – Simple ATM Menu

balance = 1000.00

print("=================================")
print("     Welcome to Python ATM       ")
print("=================================")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("---------------------------------")

choice = input("Select an option (1/2/3): ").strip()

if choice == "1":
    # Check balance
    print(f"\nYour current balance is: ${balance:.2f}")

elif choice == "2":
    # Deposit
    amount = float(input("Enter deposit amount: $"))
    if amount <= 0:
        print("\nError: Deposit amount must be greater than zero.")
    else:
        balance = balance + amount
        print(f"\nDeposit successful!")
        print(f"Amount deposited: ${amount:.2f}")
        print(f"New balance: ${balance:.2f}")

elif choice == "3":
    # Withdraw
    amount = float(input("Enter withdrawal amount: $"))
    if amount <= 0:
        print("\nError: Withdrawal amount must be greater than zero.")
    elif amount > balance:
        print(f"\nError: Insufficient funds.")
        print(f"Available balance: ${balance:.2f}")
        print(f"Requested amount: ${amount:.2f}")
    else:
        balance = balance - amount
        print(f"\nWithdrawal successful!")
        print(f"Amount withdrawn: ${amount:.2f}")
        print(f"Remaining balance: ${balance:.2f}")

else:
    print(f"\nInvalid option '{choice}'. Please choose 1, 2, or 3.")

print("\nThank you for using Python ATM.")
```

**Sample Run 1 (balance check):**

```
Select an option (1/2/3): 1

Your current balance is: $1000.00

Thank you for using Python ATM.
```

**Sample Run 2 (successful deposit):**

```
Select an option (1/2/3): 2
Enter deposit amount: $250.50

Deposit successful!
Amount deposited: $250.50
New balance: $1250.50

Thank you for using Python ATM.
```

**Sample Run 3 (overdraft attempt):**

```
Select an option (1/2/3): 3
Enter withdrawal amount: $1500

Error: Insufficient funds.
Available balance: $1000.00
Requested amount: $1500.00

Thank you for using Python ATM.
```

**Sample Run 4 (invalid option):**

```
Select an option (1/2/3): 5

Invalid option '5'. Please choose 1, 2, or 3.

Thank you for using Python ATM.
```

**Explanation:**

- This program uses a multi-branch `if`/`elif`/`else` structure to implement a menu — one of the most common patterns in programming. Each `elif` handles one valid menu option, and the final `else` catches anything unexpected.
- Within the deposit branch, a second `if`/`else` validates the input before acting. This is called **input validation** — always check that user input makes sense before using it.
- Within the withdrawal branch, three outcomes are possible: invalid amount, overdraft, or successful withdrawal. This requires two conditions (`amount <= 0` and `amount > balance`) before reaching the success case.
- Notice that code after the `if`/`elif`/`else` block (the "Thank you" line) always executes, regardless of which branch ran. This is because it sits at the same indentation level as the outer `if`.
- Variables defined before the conditional (like `balance`) retain their values and can be modified inside any branch.

---

_End of Module 2 Exercises_