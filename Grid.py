
#from numpy import zeros

class Grid(object):
	"""Represents the grid of space open to explore
	"""

	def __init__(self, height, width):
		"""Create Grid object
		Grids are hexagonal
		To simplify, the matrix conforms to a rectangular
		shape with dimensions defined by height and width
		"""
		self.height = height
		self.width = width
		self.world = {}


	def update_path(self, location, density):
		""" Takes tuple of x, y coordinates and updates path 
		density at that location
		"""
		if is_true_location(location):
			if location in self.world:
				self.world[location][0] += density
			else:
				self.world[location][0] = density
		else:
			raise ValueError 

	def update_occupancy(self, location):
		"""Takes a tuple of x, y coordinates of location and 
		updates the occupancy status at that location
		"""	
		if is_true_location(location):
			if location in self.world.keys():
				self.world[location][1] = not self.world[location][1]	

	def is_true_location(self, location):
		"""Checks if the location is allowed in the grid
		"""
		if (location[0] % 2 == location[1] % 2) and location[0] < height and location[1] < width:
			return True 
		else:
			return False

	def get_adjacent_densities(self, location):
		"""Gets the densities of all adjecent locations
		Density is set to None if the location is occupied or it does not exist.
		"""
		x, y = location
		possibilities = [(x, y + 2), (x + 1, y + 1), (x + 1, y - 1), (x, y - 2 ), (x - 1, y - 1), (x - 1, y + 1)]
		densities = [0, 0, 0, 0, 0, 0]
		for i in range(len(possibilities)):
			if not is_true_location(possibilities[i]):
				densities[i] = None 
			elif location in self.world.keys() and self.world[possibilities[i]][1]:
				densities[i] = None 
			elif possibilities[i] in self.world.keys():
					densities[i] = self.world[possibilities[i]][0]
		return densities


grid = Grid(20, 20)
print grid.height
print grid.width
print grid.world
