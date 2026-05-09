"""
Program: Prime Number Identifier
Author: Dibyajyoti Mishra

Description: 
This program takes an integer input from the user and checks whether it is a prime number. 
It uses an optimized 'while' loop condition (i * i <= num) to reduce the number of iterations.
It also features robust error handling using try-except blocks to prevent crashes if a user 
inputs invalid data (like strings or symbols) instead of a number.
"""
try:
    is_prime = True #assuming prime number
    num = int(input("Enter a num to check wheatear it is a prime number or not: "))
    i = 2

    if num <= 1:
        print("Invalid no, please enter a num greater than 1")
    else:

        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime == True:
            print("It's a prime number")
        else:
            print("It's not a prime number")

except ValueError:
    print("Invalid input, please enter a valid input")