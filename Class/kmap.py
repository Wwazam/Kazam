import pdb
import copy

class Tile():
	def __init__(self, free=True):
		self._free = free
	def get_free(self):
		return self._free
	def set_free(self, free):
		self._free = free
	free = property(get_free, set_free)

class Empty_tile(Tile):
	def __init__(self):
		Tile.__init__(self, True)
	def __str__(self):
		return " "

class Wall(Tile):
	def __init__(self):
		Tile.__init__(self, False)
	def __str__(self):
		return '#' 

class Map():
	def __init__(self, map=[[]]):
		if type(map) == str:
			self.map = Map.read_map_from_file(map)
		else:
			self.map = map

	def print_map(self, soldiers = [], path = [], current_soldier = []):
		tmp = copy.deepcopy(self)
		for p in path:
			tmp[p] = '.'
		for sol in soldiers:
			if current_soldier and current_soldier == sol.pos:
				tmp.map[sol.pos[1]][sol.pos[0]] = sol.symbol.upper()
			else:
				tmp.map[sol.pos[1]][sol.pos[0]] = sol
		for i, row in enumerate(tmp.map):
			for j, col in enumerate(row):
				print(col, end='')
			print()

	# get map from file
	def read_map_from_file(map_name):
		file = open(map_name, 'r')
		content = file.readlines()
		tab = []
		for line in content:
			row = []
			for char in line:
				if char != '\n':
					if char == '1':
						i = Wall()
					if char == '0':
						i = Empty_tile()
					row.append(i)
			tab.append(row)
		return tab
		
	def __getitem__(self, key):
		y, x = key
		return self.map[x][y]
	def __setitem__(self, key, val):
		y, x = key
		self.map[x][y] = val
	def __delitem__(self, key):
		y, x = key
		del self.map[x][y]


#----------------------------------------------------------------------------------------------------

def main():
	ma_map = Map('map.txt')
	ma_map.print_map()
	print()
	print(ma_map[2, 3])

if __name__ == '__main__':
	main()
