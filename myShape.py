# from math import pi, sqrt

class Shape:
	def __init__(self):
		self.area = None

class Rectangle(Shape):
	def __init__(self, height, width):
		# self.width = width
		# self.height = height
		self.area = width * height

# class Circle(Shape):
# 	def __init__(self, radius):
# 		# self.radius = radius
# 		self.area = pi * (radius ** 2)

# class Triangle(Shape):
# 	def __init__(self, a, b, c):
# 		# self.side_a = a
# 		# self.side_b = b
# 		# self.side_c = c
		
# 		# Heron's formula for a triangle's area
# 		self.s = (a + b + c ) / 2
# 		self.area = sqrt(s * (s - a) * (s - b) * (s - c))