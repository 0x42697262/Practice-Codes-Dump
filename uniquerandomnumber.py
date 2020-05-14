import random

num = int(input("Number of unique random value: "))

numberList = []
xtries = 0

while len(numberList) != num:
	xtries+=1
	x = random.randrange(num)
	print(f'\nTrying to insert {x}...')
	if x in numberList:
		print(f"{x} already exist.")
		
	else:
		numberList.insert(0, x)
		print(f"Inserted {x}")
		
print(f'\nFinal list: {numberList}\nTries:{xtries}')
