# Leap Year Checker

## Overview
This is a simple and efficient Python program that determines whether a given year is a leap year. It takes user input, applies the mathematical rules of the Gregorian calendar, and returns a clear result.

## Features
* **Interactive Input:** Prompts the user to enter a specific year.
* **Accurate Calculation:** Uses standard leap year logic:
  * A year is a leap year if it is divisible by 4.
  * However, if the year is a century year (divisible by 100), it is not a leap year unless it is also divisible by 400.
* **Error Handling:** Includes a `try-except` block to catch `ValueError`. If the user inputs text, symbols, or decimals instead of a valid integer, the program prevents a crash and displays a helpful error message.

## How to Use
1. Make sure you have Python installed on your computer.
2. Download or copy the script into a file named `leap_year_checker.py`.
3. Open your terminal or command prompt.
4. Navigate to the directory where the file is saved.
5. Run the script using the following command:
   python leap_year_checker.py
6. Enter a year when prompted and press Enter.