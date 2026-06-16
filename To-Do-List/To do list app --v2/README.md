# To-Do List (Version 2.0)

A clean and efficient command-line interface (CLI) application written in Python to manage tasks/taxes. This project demonstrates fundamental programming concepts including list manipulation, loop control, and robust error handling.

## What's New in v2.0
- **Dynamic Item Counting:** Added a dedicated feature (Option 3) to instantly calculate and display the total number of existing items in the list.

## Core Features

| Feature | Description |
| :--- | :--- |
| **View Items** | Displays all current items using enumeration. Includes logical checks to notify the user if the list is currently empty. |
| **Add Items** | Allows the user to seamlessly append new items to the tracker. |
| **Count Items** | Computes the total number of items currently tracked using Python's native `len()` function. |
| **Delete Items** | Enables safe removal of items via their 1-based index number, strictly including boundary checks to prevent out-of-range errors. |
| **Error Handling** | Implements robust `try-except` blocks to catch `ValueError` exceptions, preventing application crashes if a user inputs text instead of numbers. |

## How to Run

1. Ensure Python is installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the command: `python To-Do-List.py`
5. Follow the on-screen menu prompts to interact with the application.
