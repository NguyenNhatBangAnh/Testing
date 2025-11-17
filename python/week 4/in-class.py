# Execise 1:
user_input = int(input("Input: "))
if user_input > 0 :
    print("Positive")
elif user_input < 0 :
    print("Negative")
else : 
    print("Zero")

# Execise 2:
user_input = int(input("Input: "))
if user_input % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Execisen 3:
user_age = int(input("Enter your age: "))
if user_age < 13:
    print("Child")
elif user_age < 19:
    print("Teen")
elif user_age >= 20:
    print("Adult")

#Execise 4:
user_year = int(input("Enter your year:"))
if user_year % 4 == 0:
    print(f"{user_year} is a leap year")
else:
    print(f"{user_year} is not a leap year")

#Execise 5:
user_amount = int(input("Enter your purchase amount: "))
if user_amount >= 500000: 
    print("You get a discount!")
else:
    print("No discount")

#Execise 6:
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
if first_number > second_number:
    print(f"{first_number} is larger than {second_number}")
else:
    print(f"{second_number} is larger than {first_number}")

#Execise 7:
user_score = int(input("Enter your grade: "))
if user_score < 50:
    print("Fail")
elif user_score < 70:
    print("Average")
elif user_score < 90:
    print("Good")
elif user_score >= 90:
    print("Excellent")

#Execise 8:
user_time = int(input("Enter your time: "))
if 5 <= user_time < 12:
    print("Morning")
elif 12 <= user_time <18:
    print("Afternoon")
elif 18<= user_time < 22:
    print("Night")

#Execise 9:
user_income = int(input("Enter your income: "))
if user_income < 10000000:
    print("Low income")
elif user_income <= 30000000:
    print("Medium income")
elif user_income > 30000000:
    print("High income")

#Execise 10:
user_string = input("Enter your string: ")
if user_string.lower() == "banganh123":
    print("Access granted")
else:
    print("Access denied")
    