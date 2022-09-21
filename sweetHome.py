class Room:
	def __init__(self, name = None):
		self.name = name
		self.walls = []

class Wall:
	def __init__(self, shape, color = None):
		self.shape = shape
		self.windows = []
		self.doors = []
		self.outlets = []
		self.color = color

	def netArea(self):
		uncovered = 0
		for i in [*self.doors, *self.windows, *self.outlets]:
			uncovered += i.area
		return self.shape.area - uncovered

# class Door:
# 	def __init__(self, shape):
# 		self.shape = shape

# class Window:
# 	def __init__(self, shape):
# 		self.shape = shape

# class Outlet:
# 	def __init__(self, shape):
# 		self.shape = shape		