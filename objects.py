class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def talks(self,words):
        print(f"{self.name} talks and says {words}")



person1 = Person("James",29,"Male")
print(type(person1))
print(person1.name)
print(person1.age)
print(person1.gender)
person1.talks("Hello, this is OOP ")


person2 = Person("Jane",25,"Female")
print(type(person2))
print(person2.name)
print(person2.age)
print(person2.gender)
person2.talks("Hi, this is Python")

from datetime import datetime
today = datetime.today()


class BankAccount:
    def __init__(self,acc_no,balance,owner_name,date_opened=today):
        self.acc_no = acc_no
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount entered")
        else:
            self.balance += amount
            print(f"Ksh. {amount} added to {self.acc_no} successfully")
            print(f"New balance is: {self.balance}")
        

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount,cannot complete withdrawal")
        else:
            self.balance -= amount
            print(f"{amount} deducted from {self.acc_no} successfully")
            print(f"New balance is: {self.balance}")
        

    def display_info(self):
        print("--------------Bank Acc Details---------------")
        print(f"Acc No: {self.acc_no}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")


account1 = BankAccount("Acc001",1000,"Jack Kamau")
account1.deposit(10_000)
account1.withdraw(2500)
account1.display_info()
       
