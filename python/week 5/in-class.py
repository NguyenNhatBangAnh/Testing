# This is code for Week 5 (Loop)

#Execise 1
for i in range(11):
    print(i, end=" ")

#Execise 2:
for i in range(2, 21, 2):
    print(i, end=" ")
#Execise 3:
user_input = int(input("Enter your number: "))
sum = 0
for i in range(user_input + 1):
    sum += i
print(f"The sum is {sum}")
#Execise 4:
word = input("Enter your word: ")
number = int(input("Enter your number: "))
for i in range(number):
    print(word, end=" ")
#Execise 5:
user_input = int(input("Enter your number: "))
while user_input > 0:
    print(user_input, end=' ')
    user_input -= 1
print("Blast off!")
#Execise 6:
total = 0
for i in range(5):
    user_input = int(input(f"Enter your number for item {i+1}: "))
    total += user_input
print(f"Total: {total}")
#Execise 7:
password = "python123"
user_input = input("Enter your password: ")
while password != user_input:
    user_input = input("Enter your password again, please: ")
print("Access granted.")
#Execise 8:
import math
for i in range(1,6):
    print(i, "-->", int(math.pow(i,2)))
#Execise 9:
user_input = int(input("Enter your number: "))
while user_input != 7:
    user_input = int(input("Enter your number again: "))
print("Correct!")
#Execise 10:
user_input = int(input("Enter your number: "))
sum = 0
while user_input != 0:
    sum += user_input
    user_input = int(input("Enter your number: "))
print(f"Total sum = {sum}")