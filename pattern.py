#!/ur/bin/python3

for i in range(1,5):
	for j in range(i):
		print(i,end='')
	print()

print("\n")

for i in range(1,5):
	n=1
	for j in range(i):
		print(n,end='')
		n+=1
	print()

print("\n")

m=1
for i in range(1,5):
	for j in range(i):
		print(m,end='')
		m+=1
	print()

print("\n")

c=65
for i in range(1,5):
	for j in range(i):
		ch=chr(c)
		print(ch,end='')
		c+=1
	print()

print("\n")

c=65
for i in range(1,5):
	for j in range(i):
		ch=chr(c)
		print(ch,end='')
	c+=1
	print()
