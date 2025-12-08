#Execise 1:
def greet(name):
    print("Hello", name)
greet("BA")
#Execise 2:
def add(a, b):
    return a + b
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
print( "Your number is:",add(first, second))
#Execise 3:
def area(width, height):
    return width * height
width = int(input("Enter your width: "))
height = int(input("Enter your height: "))
print("Your rectangle area:", area(width, height))
#Execise 4:
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
user_input = int(input("Enter your number: "))
if user_input:
    print("Even")
else:
    print("Odd")
#Execise 5:
def format_name(first, last):
    return f"{last}, {first}"
input_first = input("Enter your first name: ")
input_last = input("Enter your last name: ")
print(format_name(input_first,input_last))
#Execise 6:
def calculate_age(birth_year):
    return 2025 - birth_year
user_birth_year = int(input("Enter your birth year: "))
print("Your age is:", calculate_age(user_birth_year))
#Execise 7:
def vnd_to_usd(amount_vnd):
    return amount_vnd // 25000
vnd = int(input("Enter your VND amount: "))
print("Your USD amount is:", vnd_to_usd(vnd))
#Execise 8:
def count_chars(text):
    return len(text)
user_input = input("Give me your sentence: ")
print(count_chars(user_input))
#Execise 9:
def check_password(pw):
    return pw == "python123"
guess = input("Enter your password: ")
if check_password(guess):
    print("Correct")
else:
    print("Wrong")
#Execise 10:
def triple(x):
    return x * 3
user_input = int(input("Enter your number: "))
print(triple(user_input))
#Execise 11:
def is_prime(n):
    if n <= 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
user_input = int(input("Enter your number: "))
if is_prime(user_input):
    print("It's a prime number.")
else:
    print("It's not a prime number.")
#Execise 12:

#Execise 
#Execise 
#Execise 
#Execise 
#Execise 
#Execise 