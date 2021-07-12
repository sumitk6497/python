#!/usr/bin/python3

import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
reg=x+y
print("sum of x and y = ",reg)
print("list : ",sys.argv)
print("length : ",len(sys.argv))
for i in sys.argv:
	print("arg",i)
