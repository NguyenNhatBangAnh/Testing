s = input("s = ")
print(s[:2] + s[-2:])

s = input("s = ")
print(s[1::2])

s = input("Enter a string: ")
result = s[:-1] + s[-1].upper()
print(result)

s = input("Enter an email: ")
# Find positions of '@' and '.'
at_index = s.find('@')
dot_index = s.find('.', at_index)
# Extract the part between them
domain = s[at_index + 1 : dot_index]
print(domain)

s = input("s = ")
index = s.rfind("a")
print(s[:index] + "@" + s[index+1:])

s = input("s = ")
mid = len(s) // 2
print(s[:mid] + "-" + s[mid:])


