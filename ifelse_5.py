#!/usr/bin/python3

a = int(input("Please enter 1st no. : "))

if a > 10:
  print("Above 10,")
  if a > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
    print("Below 10")
