# Python CLI Calculator

**Author:** Raj

## Description
A simple, fast, and efficient command-line calculator written in Python. This program takes two numbers and an operator as input from the user and performs basic arithmetic calculations. It is designed to be user-friendly and highly resilient against common input errors.

## Features
* Supports standard arithmetic operations: Addition (+), Subtraction (-), Multiplication (* or x), and Division (/).
* Supports exponentiation/power calculation (^).
* Handles floating-point numbers for precise calculations.
* Input sanitization using `.strip()` to prevent errors caused by accidental whitespace.
* Clean and structured execution flow using conditional statements.

## Error Handling & Development Journey
During the development of this calculator, several edge cases and potential crash points were identified and resolved to ensure smooth execution:

1. **Division by Zero:** 
   Initially, dividing a number by zero would crash the program. This was fixed by adding a conditional check (`if y == 0:`) that prints a safe error message ("0 cannot be divided") and returns `None` instead of throwing a runtime exception.

2. **Invalid Operator Input:** 
   If a user entered an unsupported operator, the program would fail silently or execute incorrectly. An `else` block was implemented inside the function to catch invalid operators, alert the user, and safely return `None`, preventing the output statement from printing an undefined result.

3. **Value Errors on Input:** 
   Users entering alphabetical characters or symbols instead of numbers caused the script to break. The entire execution block was wrapped in a `try...except ValueError:` structure to gracefully catch these invalid inputs and display a "Something went wrong...." message instead of a system traceback.

4. **Output Control:** 
   Implemented a strict `if result is not None:` condition before printing the final mathematical equation. This ensures that the terminal remains clean and does not print "None" when an error condition is triggered.