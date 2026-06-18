readme_content = """# Special Calculator

A Python-based command-line calculator designed with a strong focus on robust error handling and input validation.

## Features

### 1. Advanced Arithmetic Operations
Beyond standard addition (+), subtraction (-), multiplication (* or x), and division (/), this calculator includes:
* **Exponentiation / Power (^ or **):** Calculate the power of a number (can also be used for roots by using decimal exponents).
* **Modulo (%):** Find the remainder of a division operation.

### 2. Comprehensive Error Handling
Special attention has been given to make this program crash-proof and user-friendly through background checks:
* **Input Validation:** Uses try-except blocks to catch `ValueError`, preventing crashes when a user inputs text or symbols instead of numeric values.
* **Zero Division Prevention:** Background logic automatically blocks division (/) or modulo (%) operations by zero, instantly stopping the process and alerting the user safely.
* **Operator Validation:** Strictly verifies the inputted operator against a predefined list of valid symbols, rejecting invalid characters before any calculation is attempted.

## How to Run
1. Ensure Python is installed on your system.
2. Open your terminal or command prompt.
3. Run the script using the following command: