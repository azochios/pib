class Shape:
	def __init__(self):
		self.area = None

class Rectangle(Shape):
	def __init__(self, height, width):
		self.width = width
		self.height = height
		self.area = width * height
