import sys
taxs = []

while True:
    print("Select 1/2/3/4 option to continue")

    print("1. View Taxes")
    print("2. Add a new Taxes")
    print("3. Count Taxes")
    print("4. Delete a tax")
    print("5. Exit")

    try:
        main_option = int(input("Enter your choice: "))

        if main_option != 1 and main_option != 2 and main_option != 3 and main_option != 4 and main_option != 5:
            print("Invalid Choice, please select a correct choice")
            sys.exit()

        if main_option == 1:
            if len(taxs) == 0:
                print("\nEmpty List. Nothing to see\n")
            else:
                print("\n-----Here are your taxes:-----\n")
                for idx, item in enumerate(taxs):
                    print(f"{int(idx + 1)}. {item}")
                print("\n")

        elif main_option == 2:
            choice_1 = input("Add a new tax here: ")
            taxs.append(choice_1)
            print("----Successfully added a new tax")

        elif main_option == 3:
            print(f"\n----Total taxes: {len(taxs)}\n")

        elif main_option == 4:
            remove_task = int(input("Enter the tax you want to remove: "))

            if 1 <= remove_task <= len(taxs):
                taxs.pop(remove_task - 1)
                print("\nSuccess: tax removed\n")
            else:
                print("Invalid input, please select the exact tax you want to remove")

        elif main_option == 5:
            print("----Successfully Exited----")
            break
        else:
            print("You selected nothing!")
            break
    except ValueError:
        print("\nSomething went wrong, Please enter correct inputs\n")