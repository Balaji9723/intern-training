# print the 1-10 multiplication table for a chosen number using a for loop

num= int (input("Enter a number :"))
for i in range (1,11):
    print (num, "x", i,"=", num* i)


# sum every number from 1 to 100 with an accumulator 

total=0
for i in range(1,101):
    total+= i
    print ("sum=", total)

# FizzBuzz for 1-50 (Fizz/Buzz/FizzBuzz rules

for i in range (1,51):
    if i%3 ==0 and i%5 ==0:
        print ("fizzbuzz")
    elif i%3 ==0:
        print("fizz")
    elif i%5 ==0:
        print ("buzz")
    else :
        print(i) 

# FizzBuzz and verify the output for tricky values like 15 and 30
for i in range (15,31):
    if i % 3 == 0 and i%5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# a number-guessing game with a while loop - higher/lower hints

result = 20
while True:
    guess = int(input("Enter your guess: "))

    if guess == result:
        print(" You guessed correctly")
        break

    elif guess < result:
        print("Too Low")

    else:
        print("Too High ")




