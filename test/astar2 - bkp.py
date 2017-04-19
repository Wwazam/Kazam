import pdb

def main():
	tab = get_map('map.txt')
	start = [1,1]
	goal = [5,2]
	close = astar(tab, start, goal)
	print_map(tab, start, goal, close)
	
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

def get_map(map_name):
	file = open(map_name, 'r')
	content = file.readlines()
	tab = []
	for line in content:
		row = []
		for char in line:
			if char != '\n':
				i = Tile(int(char), -1, 0, 0)
				row.append(i)
		tab.append(row)
	return tab

def is_in_tab(tab, tile):
	return tab[tile[0]][tile[1]] and tile[0] >= 0 and tile[1] >= 0

def calc_G(tab, tile):
	check = [[-1, 0], [0, -1], [1, 0], [0, 1]]
	min = -1
	for ch in check:
		x = tile[0] + ch[0]
		y = tile[1] + ch[1]
		if is_in_tab(tab, [x,y]):
			test = tab[x][y]
			if min == -1:
				min = tab[x][y].G
				continue
			if tab[x][y].G != -1 and tab[x][y].G < min:
				min = tab[x][y].G
	return min + 1

def calc_H(tile, goal):
	return abs(tile[0] - goal[0]) + abs(tile[1] - goal[1])

def get_next(tab, open):
	if open[0]:
		next = open[0]
	for tile in open[1:]:
		if tab[tile[0]][tile[1]].F < tab[next[0]][next[1]].F:
			next = tile
			continue
		if tab[tile[0]][tile[1]].F == tab[next[0]][next[1]].F and tab[tile[0]][tile[1]].H < tab[next[0]][next[1]].H:
			next = tile
	return next

def pop_tile(open, next):
	for i in range(len(open)):
		if open[i] == next:
			open.pop(i)
			break

def append_neighbors(tab, open, close, next, goal):
	check = [[-1,0], [0,1], [1,0], [0,-10]]
	for ch in check:
		neighbor = [ next[0] + ch[0] , next[1] + ch[1]]
		neighbor_tile = tab[neighbor[0]][neighbor[1]]
		if is_in_tab(tab, neighbor) and neighbor_tile.value != 1 and neighbor not in close:
			neighbor_tile.G = calc_G(tab, neighbor)
			if neighbor not in open:
				neighbor_tile.H = calc_H(neighbor, goal)
				open.append(neighbor)

def print_map(tab, start=[-1,-1], goal=[-1,-1], close=[]):
	for y, row in enumerate(tab):
		for x, col in enumerate(row):
			if [x,y] == start:
				print('o', end='')
				continue
			if [x,y] == goal:
				print('x', end='')
				continue
			if [x,y] in close:
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
	print(close)
	if next != goal:
		append_neighbors(tab, open, close, next, goal)
	return next


def astar(tab, start, goal):
	open = [start]
	close = []
	current = start
	while current != goal and len(open) >  0:
		current = turn(tab, open, close, goal)
	if current == goal:
		return close
	return []

if __name__ == '__main__':
	main()
