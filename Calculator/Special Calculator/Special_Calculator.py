import sys
class Calculator:
    def calculation(self, num_1, ope, num_2):
        if ope == '+':
            return num_1 + num_2
        elif ope == '-':
            return num_1 - num_2
        elif ope == '*' or ope == 'x':
            return num_1 * num_2
        elif ope == '/':
            if num_2 == 0:
                return None
            else:
                return num_1 / num_2
        elif ope == '^' or ope == '**': # Use this for also root
            return num_1 ** num_2
        elif ope == '%':
            return num_1 % num_2
        else:
            return None

def main():
    try:
        num_1 = float(input("First num: "))
        ope = input("Operator: ")
        num_2 = float(input("Second num: "))

        if num_2 == 0 and ope in ['/', '%']:
            print("Error!")
            sys.exit()

        if ope not in ['+', '-', '*', '/', 'x', '**', '^', '%']:
            print("Invalid operator!")
            sys.exit()

        calculate = Calculator()
        result = calculate.calculation(num_1, ope, num_2)

        print(f"{num_1} {ope} {num_2} = {result}")
    except ValueError:
        print("Something went wrong!")

if __name__ == "__main__":
    main()