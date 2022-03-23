#!/usr/bin/python3

def my_fun(**arg):
  print("My string is " + arg["fname"])

my_fun(fname="Sumit", mname="Kumar", lname="nimesh")
my_fun(fname="Python", mname="Language", lname="scripting")
