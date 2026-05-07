"""
Driving License Eligibility Checker
This script takes the user's age as input and determines their eligibility 
for various categories of driving licenses according to standard rules.
"""

try:
    
    age = int(input("Enter your age: "))

    
    if age < 0 or age > 120:
        print("Invalid age")

    elif age < 16:
        print("You are not eligible for DL")
    elif 16 <= age < 18:
        print("You can apply for Learning Licence")
    elif 18 <= age < 20:
        print("You can apply for DL")
    elif 20 <= age < 90:
        print("You can apply for both commercial and personal DL")
    else:
        print("You cannot apply for the DL anymore, stay home and stay healthy")

except ValueError:
    print("Invalid Input, please input a valid age")
