import sys
class Calculator:
    def Calculation(self, num_1, ope, num_2):

        if ope == '+':
            return num_1 + num_2
        elif ope == '-':
            return num_1 - num_2
        elif ope == '*':
            return num_1 * num_2
        elif ope == '/':
            if num_2 == 0:
                return None
            else:
                return num_1 / num_2
        else:
            return None
try:
    print("Use (+) or (-) or (*) or (/) for calculation")  
    num_1 = float(input("Enter the first num: "))
    ope = input("Enter the operator: ")
    num_2 = float(input("Enter the second num: "))

    if ope == '/' and num_2 == 0:
        print("0 Cannot be divided")
        sys.exit()

    calculate = Calculator()
    result = calculate.Calculation(num_1, ope, num_2)

    print(f"{num_1} {ope} {num_2} = {result}")

except ValueError:
    print("Somthing went wrong, please enter your requires correctly")