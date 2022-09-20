# Paint it Black, a paint calculator!

import myShape, sweetHome


SQ_FT_COVERAGE = 350
CM_TO_FT       = 30.48
CM_TO_M        = 100

def askDim(question):
	print(question)
	w = float(input("Enter width: "))
	h = float(input("Enter height: "))
	return w, h

def askWall(rooms, name):
	r = name
	v = rooms[name]
	m = int(input(f"How many walls in the {r}?\n"))

	for i in range(m):
		# Account for offset by 1
		question = f"Wall #{i + 1} in the {r}:"
		c = input(f"Pick a color for {question}\n")
		w, h = askDim(question)
		v.walls.append(sweetHome.Wall(myShape.Rectangle(w, h), c))

		n = int(input("How many doors? "))
		askTare(i, n, v.walls[i].doors, r, "door")

		n = int(input("How many windows? "))
		askTare(i, n, v.walls[i].windows, r, "window")

def askTare(i, n, v, r, tare):
	for j in range(n):
		question = f"Wall {i + 1}, {tare} {j + 1} in {r}" 
		w, h = askDim(question)
		v.append(myShape.Rectangle(w, h))

def intro():
	print("Welcome to Paint it Black! So you want to paint your house?\n\
Let's start with a room! Pick a name:")
	while True:
		name = input()
		rooms[name] = sweetHome.Room(name)
		askWall(rooms, name)

		choice = input("How about another room? (y/n) ").lower()
		match choice:
			case 'y':
				print("Pick a name:")
			case 'n':
				break
			case _:
				print("Please try again...")
				break

def printSummary(rooms):
	for r, v in rooms.items():
		print(f"The {r} has {len(v.walls)} wall(s)")
		for w in v.walls:
			area  = w.netArea() / (CM_TO_FT ** 2)
			paint = area / SQ_FT_COVERAGE
			txt =  f"The Wall will need {paint:.2f} gallons of " 
			txt += f"'{w.color}' paint!"
			print(txt)



if __name__ == "__main__":
	rooms = {}
	intro()
	printSummary(rooms)