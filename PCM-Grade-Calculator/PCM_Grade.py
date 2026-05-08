"""
Student Grade Calculator
Author: Dibyjyoti Mishra
Description: A Python script that takes marks for Physics, Chemistry, and Math 
as input, validates them, calculates the total percentage, and assigns a grade 
based on the passing criteria. It includes error handling for invalid inputs.
"""
try:
    phy = float(input("Enter the marks of your Physics: "))
    che = float(input("Enter the marks of your Chemistry: "))
    math = float(input("Enter the marks of your Math: "))

    if phy > 100 or phy < 0 or che > 100 or che < 0 or math > 100 or math < 0:
        print("Invalid marks, please enter a valid marks")
    else:
        total_marks = (phy + che + math)
        # Rounded off the percentage to 2 decimal places
        total_percentage = round(total_marks/3, 2)

        print("Total percentage secured: ", total_percentage)

        if((phy >= 33 and che >= 33 and math >= 33) and total_percentage >= 40):
            print("Congratulations, You passed the examination")

            if total_percentage >= 95:
                print("Grade - A+")
            elif total_percentage >= 90:
                print("Grade A1")
            elif total_percentage >= 80:
                print("Grade A2")
            elif total_percentage >= 70:
                print("Grade B1")
            elif total_percentage >= 60:
                print("Grade B2")
            elif total_percentage >= 50:
                print("Grade C1")
            elif total_percentage >= 40:
                print("Grade C2")

        else:
            print("You failed the examination")

except ValueError:
    print("Please enter a valid number")