"""
Leap Year Checker Program

This script prompts the user to input a year and calculates whether it is a leap year 
based on the standard Gregorian calendar rules. It also includes error handling to 
manage invalid non-integer inputs gracefully.
"""
try:
    year = int(input("Enter a year to check whether it is a leap year or not: "))

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"The year {year} is a Leap Year")
    else:
        print(f"The year {year} is not a Leap Year")

except ValueError:
    print("Invalid input, please enter a valid year")