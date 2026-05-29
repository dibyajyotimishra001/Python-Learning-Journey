def discount(total_bill, dis):
    bill_final = total_bill - (total_bill * dis)
    return bill_final

total_bill = float(input("Enter your total bill price: "))

if total_bill >= 5000:
    dis = 0.20 # 20% of Discount
    print(f"Your Final Bill is {discount(total_bill, dis)}")
elif total_bill >= 2500:
    dis = 0.10 # 10% of Discount
    print(f"Your Final Bill is {discount(total_bill, dis)}")
elif total_bill >= 1000:
    dis = 0.05 # 5% of Discount
    print(f"Your Final Bill is {discount(total_bill, dis)}")
elif total_bill < 1000 and total_bill > 0:
    dis = 0.0 # No Discount
    print(f"Your Final Bill is {discount(total_bill, dis)}")

else:
    print("Invalid price")