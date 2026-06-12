# # for loop
# for i in range(1,10):
#     print (i)


# # while loop
# num= 1 
# while num<=5:
#     print(num)
#     num+= 1

# # sum of numbers 1 to 5
# total=0
# for i in range(1,5):
#     total+= i
#     print ("sum=", total)

# # FizzBuzz programs.. using while loop

# num =1
# while num<= 50:
#     if num%3 ==0 and num%5 ==0:
#         print("fizzbuzz")
#     elif num%3 ==0:
#         print("fizz")
#     elif num%5 ==0:
#         print("buzz")
#     else :
#         print (num)
    
#     num += 1

# guessing game - for loop

# result = 20
# for i in range (1,3):
#     guess = int(input("Enter your guess: "))

#     if guess ==result:
#         print(" You guessed correctly")
#         break

#     elif guess < result:
#         print("Too Low")

#     else:
#         print("Too High")


# rows= 5
# for i in range(rows):
#     for j in range(rows):
#         print("*", end=" ")
#     print()     

# patterns programs..., (*)   

# n= int (input("enter the number:"))
# for i in range (n):
#     for j in range (n-i):
#         print("*",end =" ")
#     print()    

# n= int (input("enter the number:"))
# for i in range (n-1):
#     for j in range (n):
#         print("*",end =" ")
#     print()    

# n= int (input("enter the number:"))
# for i in range (n):
#     for j in range (n-i-1):
#         print(" ",end =" ")

#     for j in range(i+1):
#         print("*", end=" ")   
#     print()


n= int (input("enter the number:"))
for i in range (n):
    for j in range (i):
        print(" ",end =" ")

    for j in range(n-i):
        print("*", end=" ")   
    print()
