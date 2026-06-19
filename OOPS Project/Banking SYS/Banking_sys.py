class Bank:
    def __init__(self, account_num = "12345AB0954", password = "123%7888e3ee", balance = 100000, pin = 5678):
        self.__account_num = account_num
        self.__password = password
        self.__name = "Abhishek Gahan"
        self.__dob = "31/1/2007"
        self.__location = "Dhankanala"
        self.__balance = balance
        self.__pin = pin
    
    def user_details(self):
        
        return f"Name: {self.__name}\nDOB: {self.__dob}\nLocation: {self.__location}"
    
    def breaking_data(self):
        fname, lname = self.__name.split(" ")
        bdate, bmonth, byear = self.__dob.split("/")
        return f"Hello {fname} {lname}, your dob is {bdate}/{bmonth}/{byear}"
        
    def greet(self):
        return f"Hello, {self.__name.split(' ')[0]}"
    
    def access_money(self):
        count = 1
        while count<=3: 
            pin = int(input("Enter Your Pin: "))
            if pin > 9999 or pin < 1000:
                count += 1
                continue
            if pin != self.__pin:
                print("Error!")
            else:
                return f"Balance: {self.__balance}"
            count += 1
        return "Your account is locked for 24 hours"
    
user_1 = Bank()
print(user_1.greet())
print(user_1.access_money())