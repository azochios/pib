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

def askInfo(rooms):
	for r, v in rooms.items():
		m = int(input(f"How many walls in the {r}?\n"))
		for i in range(m):
			# Account for offset by 1
			question = f"Wall {i + 1}"
			c = input("Pick a color\n")
			w, h = askDim(question)
			v.walls.append(sweetHome.Wall(myShape.Rectangle(w, h), c))

			n = int(input("How many doors? "))
			for j in range(n):
				question = f"Wall {i + 1}, Door {j + 1} in {r}" 
				w, h = askDim(question)
				v.walls[i].doors.append(myShape.Rectangle(w, h))

			n = int(input("How many windows? "))
			for j in range(n):
				question = f"Wall {i + 1}, Window {j + 1} in {r}" 
				w, h = askDim(question)
				v.walls[i].windows.append(myShape.Rectangle(w, h))


rooms = {}
print("Welcome to Paint it Black! So you want to paint your house?\n\
Let's start with a room! Pick a name:")
name = input()
rooms[name] = sweetHome.Room(name)




askInfo(rooms)

for r, v in rooms.items():
	print(f"The {r} has {len(v.walls)} walls")
	for w in v.walls:
		area  = w.netArea() / (CM_TO_FT ** 2)
		paint = area / SQ_FT_COVERAGE
		txt =  f"The Wall will need {paint:.2f} gallons of " 
		txt += f" '{w.color}' paint!"
		print(txt)