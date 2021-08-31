#!/usr/bin/python3

a=100
print(id(a))
def some():
    a=6
    x=globals()['a']
    print(id(x))
    print("in func",a)
    globals()['a']=15


some()
print(a)
