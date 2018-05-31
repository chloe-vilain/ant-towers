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
		options = grid.get_adjacent_densities(self.location, self.orientation)
		if can_move(options) is not null:
			grid.update_occupancy(self.location)
			self.location = self.choose_new_locations(options)
			grid.update_occupancy(self.location)
			grid.update_path(self.path_density)
		else:
			pass 

	def add_directional_weighting(self, locations, orientation):
		"""Adds weight to directional options:
		Going straight is most preferred
		Going slight right or slight left is second most preferred
		Going hard right or hard left is third most preferred
		Going backwards is only allowed if there are no other options 
		"""

	
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





