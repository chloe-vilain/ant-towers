
class Grid(object):
	"""Represents the grid of space open to explore
	"""

	def __init__(self, heigh, width):
		"""Create Grid object
		Grids are hexagonal
		To simplify, the matrix conforms to a rectangular
		shape with dimensions defined by height and width
		"""
		self.height = height
		self.width = width
		self.world = {}


	def update_path(self, location, density):
		""" Takes tuple of x, y coordinates and updates update_path
		density at that location
		"""
		if is_true_location(location):
			if location in self.world:
				self.world[location][0] += density
			else:
				self.world[location][0] = density
		else:
			raise ValueError 
					

	def is_true_location(self, location):
		"""Checks if the location is allowed in the grid
		"""
		if (location[0] % 2 == location[1] % 2) and location[0] < height and location[1] < width:
			return True 
		else:
			return False

	def get_adjacent_locations(self):
		pass


		