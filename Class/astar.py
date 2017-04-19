#import pdb

def main():
	print("Pas d'exemple pour aller avec ce programme")


class Tile():
	def __init__(self, value, G, H, F):
		self.value = value
		self._G = G
		self._H = H
		self.F = F
	def _get_G(self):
		return self._G
	def _set_G(self, G):
		self._G = G
		self.F = self.G + self.H
	G = property(_get_G, _set_G)
	def _get_H(self):
		return self._H
	def _set_H(self, H):
		self._H = H
		self.F = self.G + self.H
	H = property(_get_H, _set_H)

def get_map(map):
	tab = []
	for line in map:
		row = []
		for char in line:
			if char.free:
				i = Tile(0, -1, 0, 0)
			else:
				i = Tile(1, -1, 0, 0)
			row.append(i)
		tab.append(row)
	return tab

def is_in_tab(tab, tile):
	return tile[0] < len(tab[0]) and tile[1] < len(tab) and tile[0] >= 0 and tile[1] >= 0

def calc_G(tab, tile):
	check = [[-1, 0], [0, -1], [1, 0], [0, 1]]
	min = -1
	for ch in check:
		x = tile[0] + ch[0]
		y = tile[1] + ch[1]
		if is_in_tab(tab, [x,y]):
			test = get_tile(tab, [x,y])
			if min == -1:
				min = get_tile(tab, [x,y]).G
				continue
			if get_tile(tab, [x,y]).G != -1 and get_tile(tab, [x,y]).G < min:
				min = get_tile(tab, [x,y]).G
	return min + 1

def calc_H(tile, goal):
	return abs(tile[0] - goal[0]) + abs(tile[1] - goal[1])

def get_next(tab, open):
	if open[0]:
		next = open[0]
	for tile in open[1:]:
		if get_tile(tab, tile).F < get_tile(tab, next).F:
			next = tile
			continue
		if get_tile(tab, tile).F == get_tile(tab, next).F and get_tile(tab, tile).H < get_tile(tab, next).H:
			next = tile
	return next

def pop_tile(open, next):
	for i in range(len(open)):
		if open[i] == next:
			open.pop(i)
			break

def get_tile(tab, tile):
	return tab[tile[1]][tile[0]]

def get_neighbors(tab, tile):
	neighbors = []
	check = [[-1,0], [0,1], [1,0], [0,-1]]
	for ch in check:
		neighbor = [tile[0] + ch[0], tile[1] + ch[1]]
		if is_in_tab(tab, neighbor):
			neighbors.append(neighbor)
	return neighbors

def append_neighbors(tab, open, close, next, goal):
	for neighbor in get_neighbors(tab, next):
		neighbor_tile = get_tile(tab, neighbor)
		#pdb.set_trace()
		if neighbor_tile.value == 0 and neighbor not in close:
			neighbor_tile.G = calc_G(tab, neighbor)
			if neighbor not in open:
				neighbor_tile.H = calc_H(neighbor, goal)
				open.append(neighbor)

def print_map(tab, start=[-1,-1], goal=[-1,-1], path=[]):
	for y, row in enumerate(tab):
		for x, col in enumerate(row):
			#pdb.set_trace()
			if [x,y] == start:
				print('o', end='')
				continue
			if [x,y] == goal:
				print('x', end='')
				continue
			if [x,y] in path:
				print('.', end='')
				continue
			if col.value == 1:
				print('#', end='')
				continue
			if col.value == 0:
				print(' ', end='')
	print()

def turn(tab, open, close, goal):
	next = get_next(tab, open)
	pop_tile(open, next)
	close.append(next)
	if next != goal:
		append_neighbors(tab, open, close, next, goal)
	return next

def get_path(tab, close, goal):
	path = [goal]
	current = goal
	while get_tile(tab, current).G != 0:
		#pdb.set_trace()
		for neighbor in get_neighbors(tab, current):
			tile = get_tile(tab, neighbor)
			if tile.G == get_tile(tab, current).G-1:
				path.append(neighbor)
				current = neighbor
				break
	return path
		
def set_GHF_tiles(tab):
	for row in tab:
		for col in row:
			col.G = -1
			col.H = 0
			col.F = 0

def astar(map, start, goal):
	open = [start]
	close = []
	current = start
	tab = get_map(map)
	get_tile(tab, start).G = calc_G(tab, start)
	#pdb.set_trace()
	while current != goal and len(open) >  0:
		current = turn(tab, open, close, goal)
	if current == goal:
		return get_path(tab, close, goal)[::-1]
	return []

if __name__ == '__main__':
	main()
