#Execise 1:
user_input = int(input("Input: "))
output = abs(user_input)
print(output)

#Execise 2:
first_number = int(input("First input: "))
second_number = int(input("Second input: "))
third_number = int(input("Third input: "))
if first_number >= second_number and first_number >= third_number:
    print(f"Largest number: {first_number}")
elif second_number >= first_number and second_number >= third_number:
    print(f"Largest number: {second_number}")
elif third_number >= first_number and third_number >= second_number:
    print(f"Largest number: {third_number}")

#Execise 3:
first_number = int(input("First number: "))
second_number = int(input("Second number: "))
if first_number % second_number == 0:
    print(f"{first_number} is divisible by {second_number}")
else:
    print("not divisible")

#Execise 4:
user_month = int(input("Enter your month: "))
match user_month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{user_month} has 31 days")
    case 4 | 6 | 9 | 11:
        print(f"{user_month} has 30 days")
    case 2:
        print(f"{user_month} has 28 or 29 days")

#Execise 5:
user_score = int(input("Input your score: "))
if user_score < 600:
    print("Poor")
elif user_score < 700:
    print("Fair")
elif user_score < 800:
    print("Good")
elif user_score >= 800:
    print("Excellent")

#Execise 6:
sides = int(input("Enter your sides: "))
match sides:
    case 3:
        print("Triangle")
    case 4:
        print("Square")
    case 5:
        print("Pentagon")
    case _:
        print("Unknown shape")
    
#Execise 7:
user_income = int(input("Enter your income: "))
if user_income < 10000000:
    print("No tax")
elif user_income < 30000000:
    print("5% tax")
elif user_income < 50000000:
    print("10% tax")
elif user_income >= 50000000:
    print("20% tax")

#Execise 8 
user_time = int(input("Enter your hours: "))
if 5 <= user_time < 12:
    print("Good morning")
elif user_time < 18:
    print("Good Afternoon")
elif user_time < 22:
    print("Good Night")

#Execise 9:
user_input = input("Enter color: ")
if user_input.lower() == "red":
    print("Stop")
elif user_input.lower() == "yellow":
    print("Ready")
elif user_input.lower() == "go":
    print("Green")
else:
    print("Invalid color.")

#Execise 10:
password = input("Enter your password: ")
if len(password) >= 8:
    if ("@" in password) or ("#" in password):
        print("Strong password")
    else:
        print("Weak password")
else:
    print("Weak password")