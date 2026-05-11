'''
==================================================
        PROJECT: *** To-Do-List ***
==================================================
Author: Dibyajyoti Mishra
Description: A simple Python program to manage 
daily tasks. It allows users to add, view, and 
delete tasks interactively using a command-line 
interface.
'''
tasks = []

while True:
    print("\nTo-Do-List: select one option\n")
    print("I. Add New Task")
    print("II. View Tasks")
    print("III. Remove a task")
    print("IV. Exit")

    user_input = input("Enter 1/2/3/4 to excute: ").strip()

    if user_input == "1":
        new_task = input("\nEnter a Task: ")
        tasks.append(new_task)
        print("\nSuccess: Task Added")
    
    elif user_input == "2":
        if len(tasks) == 0:
            print("\nYour Task Is Empty, Nothing To See")
        else:
            print("\n-----Tasks are available:-----")
            for items in range(len(tasks)):
                print(f"{str(items + 1)}. {tasks[items]}")

    elif user_input == "3":
        try:
            remove_task = int(input("\nEnter the no. of the task you want to remove: "))

            if 1 <= remove_task <= len(tasks):
                tasks.pop(remove_task - 1)
                print("\n---Task Removed Successfully---")
            else:
                print("Invalid input, please select the exact no. of task you want to remove")
        except ValueError:
            print("\nError: Please enter a valid number, not text!")

    elif user_input == "4":
        print("\n---Exited successfully---")
        break
    else:
        print("\nInvalid input, Please select from above options")