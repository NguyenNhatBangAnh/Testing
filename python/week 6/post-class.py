#Execise 1:
for i in range(1,51):
    if i % 7 == 0 and i % 5 == 0:
        print(i, "(stop)")
        break
    else:
        print(i, end=" ")
#Execise 2:
for i in range(1,21):
    if i % 4 == 0:
        continue
    else:
        print(i, end=" ") 
#Execise 3:
for i in range(1,101):
    if (i ** 0.5).is_integer():
        print(i, "(stop)")
        break
#Execise 4:
for i in range(1,11):
    pass
#Execise 5:
total = 0
while True:
    user_input = int(input("Enter your number: "))
    total += user_input
    if total > 100:
        break
print(total)
#Execise 6:
for i in range(1,6):
    for j in range(1,6):
        if j < 5:
            print(j * i, end=" ")
        else:
            print(j* i)
#Execise 7:
for i in range (1,4):
    for j in range(1,4):
        if (i + j) % 2 == 0:
            continue
        else:
            print(i+j)
#Execise 8:
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print("")
#Execise 9:
count = 0
while True:
     count+= 1
     if count % 4 == 0 and count % 6 == 0:
         print("Smallest common multiple:",count)
         break

#Execise 10:
stop = False
for i in range(1,6):
    for j in range(1,6):
        if i * j > 12:
            stop = True
            break
        print(f"({i},{j})")
    if stop:
        break
