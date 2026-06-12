
# a number classifier that reads a number and prints positive/negative/zero AND even/odd
num =int(input("Enter a number: "))
if num>0:
    print("positive number ")
elif num<0:
    print ("negative number")
else:
    print("zero")

if num %2 == 0: 
    print("Even number ")
else:
    print("odd number")


# a letter-grade calculator that converts a 0-100 score to A/B/C/D/F
score= int (input("Enter your score:"))
if score >=90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
elif score >=60:
    print("Grade: D")
else :
    print("Grade :F") 

#a simple login check comparing an entered password to a stored one
emp_username ="balaji"
emp_password="bala123"

username = input("Enter username:")
password = input("Enter password:")

if username == emp_username and password == emp_password:
    print("login successfully")
else:
    print("Login failed")


# a 'largest of three numbers' finder..,

a1= int (input("enter first number "))
a2= int (input("enter second number "))
a3= int (input("enter third number "))

if a1>= a2 and a1>= a3:
    print("\n largest number is:",a1)
elif a2>= a1 and a2>= a3:
    print("largest number is:",a2)
else:
    print("largest number is:", a3)

a4= float (input("enter first number "))
a5= float (input("enter second number "))
a6= float (input("enter third number "))

if a4>= a5 and a5>= a6:
    print("\n largest number is:",a4)
elif a2>= a4 and a2>= a6:
    print("largest number is:",a5)
else:
    print("largest number is:", a6)