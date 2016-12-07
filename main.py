import random
world=""

def Random():
	MAXSIZE = 10
	grid = []
	for row in range(MAXSIZE):
		line=[]
		for col in range(MAXSIZE):
			x=random.randint(1,100)
			if x <=10:
				line.append("G")
			elif x>10 and x <=20:
				line.append("U")
			elif x>20 and x<=30:
				line.append("S")
			else:
				line.append("*")
		grid.append(line)
	return grid

user_Choice=input("Would you like to use (P)reset Board or (R)andomly Generated World?").upper()

if user_Choice == "P":
	file = open("presetWorld.txt","r")
	world = file.read()
	print(world)
elif user_Choice == "R":
	world=Random()
	for row in range(len(world)):
		print("")
		for col in range(len(world[row])):
			print (world[row][col], end='')
