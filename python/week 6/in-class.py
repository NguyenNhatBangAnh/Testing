#Execise 1:
while True:
    num = int(input("Enter your number: "))
    if num < 0:
        print("Loop stopped because you entered a negative number")
        break
#Execise 2:
for i in range(1,11):
    if i == 3:
        continue
    print(i, end=" ")
#Execise 3:
user = int(input("Enter your number: "))
total = 0
for i in range(1,user + 1):
    total += i
    print(i)
    if total > 50:
        break
#Execise 4:
for i in range(5):
    pass
#Execise 5:
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}x{j}={i*j}", end = " ")
    print("")
#Execise 6:
while True:
    user = input("Enter your name: ")
    if user == "":
        continue
    elif user == "exit":
        break
#Execise 7:
for i in range(5):
    user = int(input("Enter your number: "))
    if user % 2 == 0:
        print(user)
        break
#Execise 8:
for i in range(1,5):
    for j in range(i):
        print("*", end = "")
    print()
#Execise 9:
for num in range(1, 51):        
    if num % 7 == 0:             
        print("Lucky 7 found!")
        break   
#Execise 10:
for i in range (1,6):
    if i == 3:
        continue
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}", end = " ")
    print("")        