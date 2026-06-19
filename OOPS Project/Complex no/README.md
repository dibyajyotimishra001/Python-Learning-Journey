# Complex Number Operations in Python

A professional implementation of complex number arithmetic using Python's Object-Oriented Programming (OOP) principles. This script demonstrates how to create custom data types and overload standard operators using Python's dunder (magic) methods.

## Features and Concepts Covered

| Concept | Description |
|---------|-------------|
| **Object-Oriented Design** | Encapsulates real and imaginary parts into a dedicated `Complex` class. |
| **Operator Overloading** | Utilizes `__add__`, `__sub__`, and `__mul__` to allow standard mathematical operators (`+`, `-`, `*`) to work directly with custom objects. |
| **String Representation** | Uses `__str__` to automatically format the output as standard complex numbers (e.g., `3 + 4i`). |

## Mathematical Logic

A complex number is represented as $z = a + bi$, where $a$ is the real part and $b$ is the imaginary part. This script strictly follows standard algebraic rules for complex numbers:

* **Addition:** $(a+bi) + (c+di) = (a+c) + (b+d)i$
* **Subtraction:** $(a+bi) - (c+di) = (a-c) + (b-d)i$
* **Multiplication:** $(a+bi)(c+di) = (ac-bd) + (ad+bc)i$

## How to Run

1. Ensure Python is installed on your system.
2. Open your terminal or command prompt.
3. Run the script using the following command:
   ```bash
   python complex_numbers.py