from math import atan2, sqrt

# Najprostsza reprezentacja punktu wraz z metoda do liczenia wyznacznika

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y  = y
		# self.active = True

	def __str__(self):
		return "({},{})".format(self.x, self.y)

	def __repr__(self):
		return "Point({},{})".format(self.x, self.y)

	def angle_for_anchor(self, anchor):
		""" Wyznaczanie kata polarnego wzgledem podanego punktu """
		y_span = self.y - anchor.y
		x_span = self.x - anchor.x
		return atan2(y_span, x_span)
