# Simple Arithmetic Calculator

A robust, modular Python-based calculator designed to perform essential arithmetic operations while ensuring a crash-free user experience through rigorous error handling and clean code architecture.

## Key Features
- **Core Operations:** Supports Addition, Subtraction, Multiplication, and Division.
- **Modular Architecture (New):** The core calculation logic is cleanly separated into a dedicated `calculator()` function, making the code reusable and easy to maintain.
- **Input Sanitization (New):** Utilizes `try-except` blocks to handle non-numeric inputs gracefully, and implements `.strip()` to automatically remove accidental whitespaces from operator inputs.
- **Zero Division Protection:** Explicitly checks and prevents division by zero, returning a clear error string instead of crashing or printing prematurely.
- **Modern Output:** Utilizes Python's f-strings for clear and readable results.
- **Standard Execution (New):** Implements the `if __name__ == "__main__":` idiom to ensure professional script execution.

## What's Updated in this Version
- **Separation of Concerns:** Moved all `print()` and `input()` statements outside the main calculator logic function. The function now strictly returns values, adhering to industry standards.
- **Whitespace Handling:** Added the `.strip()` method to the operator input handling. This prevents the program from failing if a user accidentally types extra spaces (e.g., " + " instead of "+").
- **Improved Error Returns:** Division by zero and invalid operators now return standard error string messages to the main block rather than executing isolated print statements inside the function.

## How to Use
1. Ensure you have Python 3.x installed on your system.
2. Run the script from your terminal:
   ```bash
   python calculator.py