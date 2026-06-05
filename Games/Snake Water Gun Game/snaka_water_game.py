"""
1 for snake
0 for water
-1 for Gun
"""

properties = {
    "s" : 1,
    "w" : 0,
    "g" : -1,
}
reverse_properties = {
    1 : "Snake",
    0 : "Water",
    -1 : "Gun",
}

import random

computer = random.choice([-1, 0, 1])

print("Enter s, w, g for snake, water, gun")

try:
    user = input("Enter your choice: ").strip().lower()
    choice = properties[user]
except KeyError:
    print("Invalid input. Please enter s, w, or g.")
    raise SystemExit

print(f"Computer choose '{reverse_properties[computer]}' \nYou choose '{reverse_properties[choice]}'")

if choice == computer:
    print("Draw")
else:
    if(
    (choice == 1 and computer == 0) or
    (choice == 0 and computer == -1) or
    (choice == -1 and computer == 1)
    ):
        print("Result: You won!")
    else:
        print("Result: You Loss")