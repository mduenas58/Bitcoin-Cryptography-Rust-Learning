Based on the text provided, the two main topics are **Loops – while** and **Loops – for**. Here are 3 hands-on exercises for each topic, complete with explanations tailored to the module's learning objectives.

### Topic 1: Loops – `while`
*Focus: Iterating over code blocks based on specific conditions and gaining practical implementation skills.*

**Exercise 1: The Countdown Timer**
*   **Task:** Write a Python program that asks the user for a starting number. Using a `while` loop, print a countdown from that number down to 1, and then print "Blastoff!".
*   **Explanation:** This exercise directly applies the concept of repetitive execution based on a condition. Participants must initialize a variable, set a condition for the `while` loop (e.g., `while number > 0:`), and crucially, remember to decrement the variable inside the loop so the condition eventually becomes false, preventing an infinite loop.

**Exercise 2: Password Validator**
*   **Task:** Create a simple login script. Set a correct password variable to `"python_rules"`. Use a `while` loop to continuously ask the user to input a password until they type the exact correct password. Print "Access Granted" when they succeed.
*   **Explanation:** This exercise demonstrates how `while` loops handle unpredictable, dynamic conditions (user input). Unlike a fixed countdown, the loop must run an unknown number of times until the specific condition of the password matching is met, highlighting the flexibility of `while` loops.

**Exercise 3: Adding Up Savings**
*   **Task:** Write a program that starts with a savings balance of $0. Using a `while` loop, simulate adding $50 to the savings every week. The loop should stop once the savings reach or exceed $500. Print the final balance.
*   **Explanation:** This lab exercise combines iteration with accumulation (a running total). Participants practice updating multiple variables inside a loop (the balance and the week counter) and using a mathematical threshold as the specific condition to break the loop.

---

### Topic 2: Loops – `for`
*Focus: Understanding the concept of `for` loops as introduced in the module objectives.*

**Exercise 1: Printing a Grocery List**
*   **Task:** Create a list of grocery items: `["Apples", "Bananas", "Milk", "Bread"]`. Use a `for` loop to iterate through this list and print each item on a new line prefixed with "- " (e.g., "- Apples").
*   **Explanation:** This exercise introduces the fundamental mechanic of the `for` loop in Python: iterating over a sequence (like a list). It teaches participants how to read and process each item in a collection without needing to manage an index or a conditional statement manually.

**Exercise 2: The `range()` Multiplier**
*   **Task:** Using a `for` loop and the `range()` function, print the 5 times table from 1 to 10 (e.g., "5 x 1 = 5", "5 x 2 = 10", up to "5 x 10 = 50").
*   **Explanation:** While `while` loops are great for unknown endpoints, `for` loops paired with `range()` are the standard Pythonic way to run a block of code a specific, predetermined number of times. This exercise builds proficiency in using `range()` to control loop execution.

**Exercise 3: Finding the Maximum Value**
*   **Task:** Given a list of random numbers: `[14, 89, 32, 5, 102, 47]`. Use a `for` loop to iterate through the list and find the highest number without using Python's built-in `max()` function. Print the highest number at the end.
*   **Explanation:** This exercise bridges iteration with basic logic. Participants must set an initial "maximum" variable before the loop, and then use a conditional statement *inside* the `for` loop to compare each item against the current maximum. It demonstrates how `for` loops are used to analyze and extract data from sequences.