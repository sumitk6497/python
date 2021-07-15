#!/usr/bin/python3

num = []

#comments in python
num.append(64)
num.append(97)
num.append("github")

print(num)

num.append("code")
print(num)

num.insert(3,77)
print(num)

num.reverse()
print(num)

num.remove(97)
print(num)

del num[3:]
print(num)


num2 = [99,33,66,1,7]
print(num2)

num2.sort()
print(num2)
