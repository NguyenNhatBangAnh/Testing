name = input("Name: ")
print(f"Hello, {name}!. Welcome to Python !")

first_name = input("First Name: ")
lats_name = input("Last Name: ")
first_name = first_name.lower()
lats_name = lats_name.lower()
print(f"Your email: {first_name}.{lats_name}@gmail.com")

user_input = input("Enter your input: ")
user_input = user_input.title()
print(user_input)

given_input = input("Shout out:")
given_input = given_input.upper()
print(given_input)

username = input("Give me your name: ")
print(f"Your name has {len(username)} letters")

name = input("What is your name: ")
age = input("What is your age: ")
print(f"({name} is {age} years old today!")

item = input("Item: ")
price = input("Price: ")
print(f"Price: {price} -- Item: {item}")

quote = input("Quote: ")
author = input("Author: ")
print(f"\"{quote}\" -- {author}")

user_input = input("Give me whatever: ")
user_input = user_input.replace("bad", "good")
print(user_input)

word = input("Word: ")
number = input("Number: ")
output = word * int(number)
print(output)

