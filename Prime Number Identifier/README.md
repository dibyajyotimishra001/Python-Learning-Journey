# Prime Number Identifier

A simple, optimized, and crash-proof Python program to check whether a given number is a prime number or not. 

## Features & Logic

* **Optimized Loop:** Instead of checking all numbers up to `n`, the program uses a `while` loop to check for factors only up to the square root of the number (`i * i <= num`). This makes the mathematical logic highly efficient.
* **Edge Case Management:** Properly handles numbers less than or equal to 1, immediately notifying the user to enter a valid number greater than 1.
* **Robust Error Handling:** The program is enclosed within a `try-except` block. If a user accidentally inputs a string, character, or symbol instead of an integer, the program catches the `ValueError` and displays a user-friendly message (`"Invalid input, please enter a valid input"`) instead of abruptly crashing.

## How to Run

1. Make sure Python is installed on your system.
2. Open your terminal or command prompt.
3. Run the script using the following command:
   ```bash
   python "Prime Number Identifier.py"