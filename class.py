class Car:
	pass
ford=Car()
honda=Car()
ford.speed=200
honda.speed=220
ford.color='red'
honda.color='black'

print(ford.speed)
print(ford.color)

ford.speed=300
ford.color='white'
print(ford.speed)
print(ford.color)
