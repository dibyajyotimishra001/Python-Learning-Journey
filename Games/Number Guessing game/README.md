# Number Guessing Game

## Overview
This project is a logic-based Number Guessing Game built with Python. It challenges the user to guess a randomly generated number between 1 and 10, featuring a custom scoring system and persistent score tracking.

## Edge Case Handling & Error Management
Significant time and thought were invested into making this code robust and unbreakable. I specifically focused on anticipating how a user might try to break the system:

*   **Value Error Handling:** A global `try-except` block is implemented to gracefully catch `ValueError` exceptions. If a user attempts to input strings, special characters, or symbols instead of integers at any point, the program intercepts the error and prevents a system crash, displaying a clean error message instead.
*   **Boundary Checking:** The code actively prevents the user from proceeding if their initial guess falls outside the logical bounds (less than 0 or greater than 10).
*   **Custom Scoring Logic:** The score is calculated dynamically based on the random number and the penalty count. The penalty counter strictly tracks wrong attempts inside the loop, ensuring the user's initial correct guess is never unfairly penalized.
*   **Secure File Handling:** Implemented safe file handling using the `with open` context manager to append and store user scores in `Score.txt` without risking file corruption or memory leaks.

## How to Play
1. Run the Python script.
2. Input a valid integer between 1 and 10.
3. If your guess is incorrect, keep trying until you find the computer's chosen number.
4. Check the generated `Score.txt` file in your directory to see your saved score.