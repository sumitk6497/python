#!/usr/bin/python
import re

line = "Cats are smarter than dogs"

m = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if m:
   print ("m.group() : ", m.group())
   print ("m.group(1) : ", m.group(1))
   print ("m.group(2) : ", m.group(2))
else:
   print ("No match!!")
