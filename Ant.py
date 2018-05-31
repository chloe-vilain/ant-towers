from random import randint

class Ant(object):
	""" Represents a single ant in the Ant-Towers game
	"""

	def __init__(self, strength, toughness, location, orientation, carrying = None, path_density):
		""" Create the Ant object
		"""
		self.carrying = carrying  
		self.location = location
		self.strength = strength
		self.toughness = toughness
		self.orientation = orientation
		self.path_density = path_density

	def move(self, grid):
		"""Updates the ant's location based on weighted options
		"""
		grid.update_path(self.path_density)
		options = grid.get_adjacent_locations(self.location, self.orientation)
		self.location = self.choose_new_locations(options)

		#TO ADD: grid.get_adjacent_locations

	

	def choose_location(locations):
		"""From a list of options with various weights, make a weighted
		random selection for the next location
		"""
		#TO OPTIMIZE: Need to make this more efficiant
		levels = []
		sum = 0
		for location in locations:
			sum += location.weight
			levels.append(sum)
		choice = random.randint(1, sum)
		for i in range(len(levels)):
			if levels[i] >= choice:
				return locations[i]





