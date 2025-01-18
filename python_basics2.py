#Conditions

flag = True
flag2 = False

if flag:
    print("Flag is True")
elif flag2:
    print("Flag2 is True")
else:
    print("Flag is False")


# lang = input("What's the programming language you want to learn? ")

# match lang:
#     case "Python":
#         print("Python is a great choice!")
#     case "Java":
#         print("Java is a good choice!")
#     case "C++":
#         print("C++ is a good choice!")
#     case _:
#         print("I don't know that language")


#Loops

for item in range(1,100):
    if item % 2 == 0:
        continue
    if item==9:
        break
    print(item)
else:
    print("Loop is done")


#While loop
count = 0

while count < 10:
    print(count)
    count += 1
else:
    print("Loop is done")


