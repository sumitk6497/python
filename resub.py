#!/usr/bin/python
import re

p = "2004-959-559 #hi"

num = re.sub(r'\D', "", p)    
print("Phone Num : ", num)		#2004959559
