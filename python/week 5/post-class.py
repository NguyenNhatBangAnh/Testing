#Execise 1:
user_input = int(input("Enter your number: "))
total = 0
for i in range(1,user_input):
    if i % 2 == 1:
        total += i
print(f"Sum of add numbers = {total}")
#Execise 2:
user_input = int(input("Enter your number: "))
for i in range(1,11):
    print(f"{user_input} x {i} = {user_input*i}")
#Execise 3:
i = 1
while i % 3 != 0 or i % 5 != 0:
    i += 1 
print(i)
#Execise 4:
user_input = int(input("Enter your input: "))
while user_input > 0:
    print(user_input, end=" ")
    user_input -= 1
print("Go!")
#Execise 5
user_input = int(input("Enter your number: "))
total = 0
while user_input >= 0:
    total += user_input
    user_input = int(input("--> "))
print(f"Total {total}")
#Execise 6:
user_input = int(input("Enter your number: "))
output = 1
for i in range(1,user_input + 1):
    output *= i
print("Factorial =", output)
#Execise 7:
user_input = int(input("Enter your number: "))

reversed_num = 0

while user_input > 0:
    digit = user_input % 10
    reversed_num = reversed_num * 10 + digit
    user_input //= 10
print(reversed_num)
#Execise 8:
s = input("Enter your word: ")
vowels = "aeiou"
count = 0
for i in s:
    if i in vowels:
        count += 1
print("Number of vowels =", count)
#Execise 9:
user = int(input("Enter your number: "))
step = 0
while user != 1:
    if user % 2 == 0:
        user /= 2
    else:
        user *= 3
        user += 1
    step += 1
print(f"It took {step} steps to reach 1")
#Execise 10:
user = int(input("Enter your number: "))
for i in range(1,user+1):
    if i != user:
        print(i, end=" --> ")
    else:
        print(i)