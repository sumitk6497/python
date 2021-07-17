#!/usr/bin/python3

# Python3 program to get multiple input from user

num1, num2 = input("Enter num1 and num2 : ").split()
num3 = int(input("Enter num3 : "))

num1 = int(num1)
num2 = int(num2)

num9 = num1 * num2
print("Product is : ", num9)

num4 = num1 + num2
print("Addition is : ", num4)

num5 = num1 - num2
print("Subtraction is : ", num5)

num6 = num1 / num2
print("Divison is : ", num6)

num7 = num3 % num2
print("Modulous is : ", num7)

