from fun import add_contact, find_contact,list_contact

from oop_basics import bank_account

while True:
    print("1. add contact")
    print("2. find contact")
    print("3. list contact")
    print("4. exit")
    i = input("Enter your choice: ")


    if i== "1":
        add_contact()
    elif i== "2":
        find_contact()
    elif i== "3":
        list_contact()
    elif i== "4":
        print("ended ")
        break
        
    else :
        print ("\n Invalid ")



s1= bank_account("balaji", 5000)
s2= bank_account("Raja", 3000)

s1.deposit(1000)
s1.withdrawl(2000)
s1.withdrawl(6000)
s2.deposit(5000)
s2.withdrawl(2300)
s2.withdrawl(2000)
