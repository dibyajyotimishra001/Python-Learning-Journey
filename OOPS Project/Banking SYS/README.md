readme_content = """# Secure Banking System (OOP Encapsulation)

A Python-based banking simulation designed to demonstrate core Object-Oriented Programming (OOP) principles, with a strict focus on Encapsulation and data security.

## Features and Concepts Covered

| Concept | Implementation Details |
|---------|------------------------|
| **Encapsulation (Data Hiding)** | All sensitive user data (Account Number, Password, PIN, Balance, Name) is heavily protected using Python's private attributes (`__`). |
| **Secure Authentication** | Implements a robust PIN verification system with a maximum limit of 3 failed attempts before initiating a 24-hour account lockout protocol. |
| **Data Parsing & Formatting** | Utilizes string manipulation (`split()`) to dynamically extract and format user details like First Name and Date of Birth. |

## How User Data is Protected

In this system, raw data cannot be accessed or modified directly from outside the class. 
By prefixing attributes with double underscores (e.g., `self.__balance`, `self.__pin`), Python applies name mangling. If an external user or script attempts to bypass the authentication method and directly call `user_1.__balance`, the program will intentionally throw an `AttributeError`. 

The only way to retrieve the account balance is by invoking the `access_money()` method and successfully passing the PIN verification, mimicking real-world banking security architectures.

## How to Run

1. Ensure Python is installed on your system.
2. Open your terminal or command prompt.
3. Run the script using the following command: