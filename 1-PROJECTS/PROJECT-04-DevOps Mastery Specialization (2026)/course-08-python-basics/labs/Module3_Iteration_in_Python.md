Here are 3 exercises for each topic covered in Module 3:

---

## Loops – while

**Exercise 1: Countdown Timer**

Write a program that starts at 10 and counts down to 0 using a `while` loop, printing each number. When it reaches 0, print `"Liftoff!"`.

_Explanation:_ This exercise helps you understand how a `while` loop continues executing as long as a condition is `True`. You'll practice initializing a variable, defining a condition (`count > 0`), and updating the variable inside the loop to eventually make the condition `False` and stop the loop.

---

**Exercise 2: Sum Until Limit**

Write a program that asks the user to enter numbers one at a time and keeps adding them to a total. The loop should stop as soon as the total reaches or exceeds 100, then print the final sum and how many numbers were entered.

_Explanation:_ This exercise demonstrates how `while` loops can react to dynamic conditions that depend on user input. You'll practice using an accumulator variable and a counter, showing that the number of iterations isn't always known in advance — the loop runs _while_ a condition holds.

---

**Exercise 3: Password Checker**

Write a program that stores a password (`"python123"`) and keeps asking the user to enter it using a `while` loop. If the input is wrong, print `"Incorrect, try again."` If the input is correct, print `"Access granted."` and stop the loop.

_Explanation:_ This exercise reinforces the idea that a `while` loop is ideal when you don't know how many attempts will be needed. You'll practice combining user input with conditional logic inside a loop, and understand how to use `break` or a boolean flag to exit cleanly when the goal is met.

---

## Loops – for

**Exercise 1: Multiplication Table**

Write a program that uses a `for` loop to print the multiplication table of a number entered by the user (from 1 to 10). For example, if the user enters `5`, it should print `5 x 1 = 5`, `5 x 2 = 10`, and so on.

_Explanation:_ This exercise introduces the `for` loop with Python's `range()` function, which gives you a predictable sequence of numbers to iterate over. You'll practice using the loop variable directly inside calculations and string formatting, which is one of the most common patterns in Python.

---

**Exercise 2: Vowel Counter**

Write a program that takes a sentence from the user and uses a `for` loop to count how many vowels (`a, e, i, o, u`) it contains. Print the total at the end.

_Explanation:_ This exercise shows how `for` loops can iterate over characters in a string, not just numbers. You'll practice using `in` to check membership and combining a `for` loop with an `if` statement — a very common pattern when processing text data in Python.

---

**Exercise 3: FizzBuzz**

Write a program that uses a `for` loop to print numbers from 1 to 30. For multiples of 3, print `"Fizz"` instead; for multiples of 5, print `"Buzz"`; and for multiples of both 3 and 5, print `"FizzBuzz"`.

_Explanation:_ This classic exercise strengthens your ability to use `for` loops alongside conditional logic (`if/elif/else`) and the modulo operator (`%`). It also teaches the importance of checking combined conditions before individual ones — a subtle but important concept in control flow.