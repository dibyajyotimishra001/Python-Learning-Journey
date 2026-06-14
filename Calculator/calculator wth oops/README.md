# Calculator Utility

A simple command-line calculator written in Python that performs addition, subtraction, and multiplication using operator codes.

## Requirements

* Python 3.x

## How to Run

1. Save the file as `calculator.py`.
2. Open a terminal in the project directory.
3. Run:

```bash
python calculator.py
```

## Operator Codes

| Code | Operation          |
| ---- | ------------------ |
| 1    | Addition (+)       |
| 2    | Subtraction (-)    |
| 3    | Multiplication (*) |

## Example

Input:

```text
Use 1/2/3 for +/-/*
Enter the first num: 10
Enter the operator as integer: 1
Enter the second num: 20
```

Output:

```text
30.0
Explanation: 10.0 + 20.0 = 30.0
```

## Invalid Input

If the operator is not `1`, `2`, or `3`, the program prints:

```text
Invalid input
```

and exits immediately using `sys.exit()`.

## Author

**Dibyajyoti Mishra**
