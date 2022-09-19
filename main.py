# Paint it Black, a paint calculator!

import myShape, sweetHome


SQ_FT_COVERAGE = 350
CM_TO_FT       = 30.48
CM_TO_M        = 100


print("So you want to paint your house?")
print("Let's start with the wall!")
w = float(input("Enter width: "))
h = float(input("Enter height: "))
wall1 = sweetHome.Wall(myShape.Rectangle(w, h))

n = int(input("How many doors? "))
wall1.doors = []
for i in range(n):
	w = float(input("Enter width: "))
	h = float(input("Enter height: "))
	wall1.doors.append(myShape.Rectangle(w, h))


n = int(input("How many windows? "))
wall1.windows = []
for i in range(n):
	w = float(input("Enter width: "))
	h = float(input("Enter height: "))
	wall1.windows.append(myShape.Rectangle(w, h))


area = wall1.netArea() / (CM_TO_FT ** 2)

paint = area / SQ_FT_COVERAGE
print(f'You will need {paint:.2f} gallons of paint!')

