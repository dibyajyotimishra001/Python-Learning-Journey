def calculator(num_1, operator, num_2):

    if operator == "+":
        return num_1 + num_2

    elif operator == "-":
        return num_1 - num_2

    elif operator == "*":
        return num_1 * num_2

    elif operator == "/":
        if num_2 == 0:
            
            return "Error Cannot divided by 0"
        
        return num_1 / num_2
    else:
        return "Error: Invalid input"
    

if __name__ == "__main__":
    try:
        # Input handling outside the logic function
        num_1 = float(input("Enter the 1st number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num_2 = float(input("Enter the 2nd number: "))

        # Calling the function
        result = calculator(num_1, operator, num_2)
        
        # Professional output format
        print(f"The result is: {result}")
        
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")