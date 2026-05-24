"""
Program Name: Python CLI Calculator
Author: Raj

Description:
A simple command-line calculator that takes two numbers and an operator 
from the user to perform basic arithmetic operations.

Features & Error Handling:
- Supports addition (+), subtraction (-), multiplication (* or x), 
  division (/), and power/exponentiation (^).
- Prevents division by zero crashes by returning None.
- Handles invalid operator inputs gracefully using an else condition.
- Uses try-except block to catch ValueError if non-numeric data is entered.
- Result is printed only if no errors occur during calculation (result is not None).
"""
try:

    def operator(ope, x, y):
        if ope == '+': 
            return x + y
        elif ope == '-': 
            return x - y
        elif ope == '*': 
            return x * y
        elif ope == '^': 
            return x ** y
        elif ope == 'x': 
            return x * y
        elif ope == '/':
            if y == 0:
                print("0  cannot be divided")
                return None
            else: 
                return x / y
        else:
            print("Somthing went wrong")
            
        return None
    print("Use (+)or(-)or(* / x) or (/) or (^) :- for sum, sub, multi, divid, power: ")

    num_1 = float(input("Enter 1st num: "))
    ope = input("Enter the operator: ").strip()
    num_2 = float(input("Enter 2nd num: "))

    result = operator(ope, num_1, num_2)

    if result != None:

        print(f"{num_1} {ope} {num_2} = {result}")

except ValueError:
    print("Somthing went wrong....")