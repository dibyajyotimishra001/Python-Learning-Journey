try:
    inventory_codes = [101, 105, 110, 115]

    while True:
        print("\nPress 1 to add a code to the list")
        print("Press 2 to exit the code")
        print("Press 3 to view the list\n")

        user_inp = input("Enter your option: ")

        if user_inp == '1':
            new_item = int(input("Enter a new id: "))
            inventory_codes.append(new_item)
            print("Successfully added")
        elif user_inp == '2':
            print("Loop exited")
            break
        elif user_inp == '3':
            print(inventory_codes)
        else:
            print("Invalid option chosen")
            break
        
except ValueError:
    print("Somthing went wrong")