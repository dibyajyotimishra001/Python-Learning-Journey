user_mail = input("Enter your Email Address: ")

# Check all validation rules together using logical operators
if (
    (user_mail.endswith(".com") or user_mail.endswith(".org")) 
    and (user_mail.count("@") == 1) 
    and (not user_mail.startswith("@"))
):
    print("Email submitted successfully!")
else:
    print("Invalid Email Format! Please check the rules.")