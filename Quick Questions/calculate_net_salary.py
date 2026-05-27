def calculate_net_salary(base_pay, tax_deduction_rate = 10.0):
    if base_pay <= 0:
        return 0.0
    
    tax_amount  = base_pay * (tax_deduction_rate / 100)
    final_payment = base_pay - tax_amount

    return final_payment

user_inp = float(input("Enter your salary: "))

print(f"Here is your final salary after the tax:")
print(calculate_net_salary(user_inp))