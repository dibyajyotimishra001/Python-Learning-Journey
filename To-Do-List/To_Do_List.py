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
# Empty List 
my_to_do_list = []

while True:
    print("\n === TO DO LIST ===")
    print("1. Add a Task")
    print("2. View Task")
    print("3. Delete a Task")
    print("4. Exit")

    task = input("Enter 1/2/3/4 to select a option: ")

    if task == '1':
        new_task = input("Add a task: ")
        my_to_do_list.append(new_task)
        print("---Task Added Successfully!---")

    elif task == '2':
        if len(my_to_do_list) == 0:
            print("List is empty now, nothing to see")
        else:
            print("\n--- Your Current Tasks ---")
            for i in range(len(my_to_do_list)):

                another_task = my_to_do_list[i]
                print(str(i + 1), ". ", another_task)

    elif task == '3':
        if len(my_to_do_list) == 0:
            print("List is empty now, nothing to delete")
        else:
            print("Tasks are available to delete")

            for i in range(len(my_to_do_list)):
             print(str(i + 1), ". ", my_to_do_list)
             

            delete_task = int(input("Enter the task num you want to delete: "))

            if delete_task > 0 and delete_task <= len(my_to_do_list):
                delete_task = my_to_do_list.pop(delete_task - 1)
                print("Success: Task '" + delete_task + "' has been deleted.")
            else:
               print("Error: Invalid task number entered.")
    elif task == '4':
       print("exit success")
       break

    else:
      print("Invalid input! please enter a valid number")