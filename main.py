# Paint it Black, a paint cost calculator!

import myShape, sweetHome, myColors, myCalc

def askDim(question):
	print(question)
	valid = False
	while not valid:
		try:
			w = float(input("Enter width : (ft.) "))
			h = float(input("Enter height: (ft.) "))
			assert w > 0 and h > 0
			valid = True
		except (AssertionError, ValueError):
			print("Behave yourself and start over!")
	return w, h

def askWall(rooms, name):
	r = name
	v = rooms[name]

	valid = False
	while not valid:
		try:
			m = int(input(f"How many walls in the {r}?\n"))
			assert m <= 5
			valid = True
		except (AssertionError, ValueError):
			print("Please be serious...")

	for i in range(m):
		# Account for offset by 1
		question = f"Wall #{i + 1} in the {r}:"
		c = myColors.pickColor(question)
		w, h = askDim(question)
		v.walls.append(sweetHome.Wall(myShape.Rectangle(w, h), c))

		tare = "door"
		askTare(i, v.walls[i].doors, r, tare)

		tare = "window"
		askTare(i, v.walls[i].windows, r, tare)

def askTare(i, v, r, tare):
	valid = False
	while not valid:
		try:
			n = int(input(f"How many {tare}s? "))
			assert n >= 0
			valid = True
		except (AssertionError, ValueError):
			print("Speak 'non-negative int' and enter")
	for j in range(n):
		question = f"Wall #{i + 1}, {tare} #{j + 1} in {r}" 
		w, h = askDim(question)
		v.append(myShape.Rectangle(w, h))

def intro():
	rooms = {}
	print("Welcome to Paint it Black! So you want to paint your house?\n\
Let's start with a room! Pick a name:")
	while True:
		name = input()
		rooms[name] = sweetHome.Room(name)
		askWall(rooms, name)

		choice = input("How about another room? (y/n) ").lower()
		match choice[0]:
			case 'y':
				print("Pick a name:")
			case 'n':
				break
			case _:
				print("Moving on...")
				break
	return rooms

def printSummary(rooms):
	paint = {}
	for r, v in rooms.items():
		# print(f"The {r} has {len(v.walls)} wall(s)")
		for w in v.walls:
			if w.color in paint.keys():
				paint[w.color] += w.netArea()
			else:
				paint[w.color] = w.netArea()
	
	total = 0
	txt = "Summary"
	print(txt)
	print(len(txt) * '-')
	for k, v in paint.items():
		v = myCalc.volCalc(v)
		v = myCalc.costCalc(v)
		# v now holds a 2 x 4 list

		txt = f"{k}\n"
		iter = []
		# Retrieve indices of non-zero elements in v
		for j in range(len(v[0])):
			if v[0][j] == 0:
				continue
			else:
				iter.append(j)
		# Generate subtotal summary text
		for j in iter:
			txt += f"\t{v[0][j]} x "
			txt += f"{myCalc.PAINT[1][j]:4} "
			txt += f"Subtotal: ${v[1][j]:.2f}\n"
			total += v[1][j]
		print(txt)
	txt = "Total"
	print(f"{txt:>32}")
	txt = f"{len(txt) * '-':>32}"
	print(txt)
	txt = '$' + f"{total:.2f}"
	print(f"{txt:>32}")

if __name__ == "__main__":
	rooms = intro()
	printSummary(rooms)