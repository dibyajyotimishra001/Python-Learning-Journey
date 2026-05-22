try:
    print("TO FIND THE EXPONENT TYPE '**' in operator")

    num_1 = float(input("Enter 1st num: "))
    operator = input("Enter operator (+ or - or * or /): ").strip()
    num_2 = float(input("Enter 2nd num: "))

    if operator == '+':
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    elif operator == '-':
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    elif operator == '*':
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    elif operator == '/':
        if num_2 == 0:
            print("0 cannot be divided")
        else:
            print(f"{num_1} / {num_2} = {num_1 / num_2}")
    elif operator == '**':
        print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
    else:
        print("Somthing went wrong.......")

except ValueError:
    print("May you have entered some wrong values")