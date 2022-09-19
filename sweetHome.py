class Wall:
	def __init__(self, shape):
		self.shape = shape
		self.windows = []
		self.doors = []
		self.outlets = []

	def netArea(self):
		total = 0
		for i in [*self.doors, *self.windows, *self.outlets]:
			total += i.area
		return self.shape.area - total

class Door:
	def __init__(self, shape):
		self.shape = shape

class Window:
	def __init__(self, shape):
		self.shape = shape

class Outlet:
	def __init__(self, shape):
		self.shape = shape		