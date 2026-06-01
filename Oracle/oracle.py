from datetime import datetime

today = datetime.now()

day = today.day
month = today.month
year = today.year

today_date = [day, month, year]

name = input("Enter you name: ")

with open("data.txt", "w") as data_1:
    data_1.write("Name: " + name)

print("1. Engineering")
print("2. Medical")

choice = (input("Enter your choice: ")).strip()

if choice == '1':
    print("A. Entrance succeed")
    print("B. Non Entrance succeed")

    choice_1 = input("Enter your choice: ").upper().strip()

    if choice_1 == 'A':
        with open("entrance_succeed.txt") as file_1:
            read_1 = file_1.read()
        print(read_1)
    
    elif choice_1 == 'B':
        with open("entrance_non_succeed.txt") as file_2:
            read_2 = file_2.read()
        print(read_2)
    else:
        print("Somthing went wrong, please try selecting corrrect option")

if choice == '2':
    print("A. Entrance succeed")
    print("B. Non Entrance succeed")

    choice_2 = input("Enter your choice: ").upper().strip()

    if choice_2 == 'A':
        with open("ES_medical.txt") as file_1:
            read_1 = file_1.read()
        print(read_1)
    
    elif choice_2 == 'B':
        with open("ENS_medical.txt") as file_2:
            read_2 = file_2.read()
        print(read_2)
    else:
        print("Somthing went wrong, please try selecting corrrect option")

print("\nIf you like to provide some information, press y or n")
print("y: yes")
print("n: No")

choice_3 = input("Enter your choice: ").lower().strip()
# For user privacy I am not storing these personal info

if choice_3 == 'y':

    print("INPUT IN INTEGER")
    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month: "))
    birth_date = int(input("Enter your birth date: "))
    print("Thanks for visiting our site")
elif choice_3 == 'y':
    print("Thanks for visiting our site")
else:
    print("Somthing went wrong!")

user_dob = [birth_date, birth_month, birth_year]
user_current_age = today_date[2] - user_dob[2]