# a Student class with __init__ setting name and grade, plus a study() method that prints an action

# class student:
 
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade= grade

#     def display(self):
#         print(f"{self.name} studying for grade {self.grade}.")

# s1= student("Balaji", 10)
# s2= student("Raja", 20)

# s1.display()
# s2.display()


# a BankAccount class with a starting balance, deposit(amount) and withdraw(amount) methods that update and print the balance, and that prevent withdrawing more than the balance

class bank_account:

    def __init__(self, name, balance):
        self.name = name 
        self.balance= balance


    def deposit(self,amount):
        self.balance += amount 
        print(f"{self.name} deposit {amount} current balance {self.balance}\n")

    def withdrawl(self,amount):
        if self.balance >=amount:
            self.balance -= amount
            print(f"{self.name} withdrawl {amount} current balance {self.balance}\n") 

        else:   
            print(f"{self.name} Invalid account current balance {self.balance}\n")


s1= bank_account("balaji", 5000)
s2= bank_account("Raja", 3000)

s1.deposit(1000)
s1.withdrawl(2000)
s1.withdrawl(6000)
s2.deposit(5000)
s2.withdrawl(2300)
s2.withdrawl(2000)