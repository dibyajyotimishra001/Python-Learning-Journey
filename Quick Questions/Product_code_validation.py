pro_code = input("Enter a product code (e.g: PRD-7852-XYZ): ")

code_num_1 = pro_code[4]
code_num_2 = pro_code[5]
code_num_3 = pro_code[6]
code_num_4 = pro_code[7]

# String concatenation (fuga)
code_num = code_num_1 + code_num_2 + code_num_3 + code_num_4

if len(pro_code) != 12 or pro_code[3] != '-' or pro_code[8] != '-':
    print("Invalid product num")
elif '5' not in code_num:
    print("Invalid product num")
else:
    print("Valid product")