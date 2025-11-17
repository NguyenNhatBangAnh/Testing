word = input("give me your input: ")
middle = int(len(word) / 2)
print(word[middle-1]+word[middle])

str = input("Please, enter your input: ")
swap = str[-1] + str[1:len(str)-1] + str[0]
print(swap)

str = input("s = ")
reversed = str[::-1]
print(reversed)

str = input("s = ")
sub = input("sub = ")
index = str.find(sub)
output = str[:index] + str[index + len(sub):]
print(output)

str = input("s = ")
sub = input("sub = ")
index = str.rfind(sub)
output = str[:index] + str[index + len(sub):]
print(output)

s = input("s = ")
output = s.title()
print(output)

s = input("s = ")
q = input("q = ")
print("YES" * (q in s) + "NO" * (q not in s))

s = input("s = ")
repeate = (s[0] + s[1]) * 3 
print(repeate + s)

email = input("s = ")
index = email.find("@")
remain = email[:index]
print(remain)

s = input("s = ")
post_s = s.replace(" ","-")
print(post_s)