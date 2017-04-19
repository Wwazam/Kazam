file = open('map.txt', 'r')
content = file.readlines()

class Case():
	def __init__(self, value, G, H, F):
		self.value = value
		self._G = G
		self._H = H
		self.F = F
	def _set_G(self, G):
		self._G = G
		self.F = self.G + self.H
	def _get_G(self):
		return self._G
	G = property(_get_G, _set_G)
	def _set_H(self, H):
		self._H = H
		self.F = self.H + self.G
	def _get_H(self):
		return self._H
	H = property(_get_H, _set_H)

def calc_H(tab, goal):
	for y, row in enumerate(tab):
		for x, col in enumerate(row):
			col.H = abs(x - goal[0]) + abs(y - goal[1])

def calc_G(tab, case):
	check = [[-1,0], [0,1], [1,0], [0,-1]]
	min = -1
	for ch in check:
		test = tab[ case[0] + ch[0] ][ case[1] + ch[1] ]
		if test and test.G != -1:
			if min == -1:
				min = test.G
			if test.G < min:
				min = test.G
	return min+1

def get_next(tab, open):
	if open[0]:
		next = open[0]
	for case in open[1:]:
		if tab[case[0]][case[1]].F < tab[next[0]][next[1]].F:
			next = case
			continue
		if tab[case[0]][case[1]].F == tab[next[0]][next[1]].F and tab[case[0]][case[1]].H < tab[next[0]][next[1]].H:
			next = case
	return next

def pop_case(open, next):
	for i in range(len(open)):
		if open[i] == next:
			open.pop(i)
			break
	return next

def append_neighbors(tab, open, close, next):
	check = [[-1,0], [0,1], [1,0], [0,-1]]
	for ch in check:
		neighbor = [ next[0] + ch[0], next[1] + ch[1] ]
		neighbor_case = tab[neighbor[0]][neighbor[1]]
		if neighbor_case and neighbor_case.value != 1 and neighbor not in close and neighbor not in open:
			neighbor_case.G = calc_G(tab, neighbor)
			open.append(neighbor)

def turn(tab, open, close):
	next = get_next(tab, open)
	pop_case(open, next)
	close.append(next)

	append_neighbors(tab, open, close, next)
	return next

def print_map(tab, close=[], start=[-1,-1], end=[-1,-1]):
		for y, row in enumerate(tab):
			for x, col in enumerate(row):
				if [x,y] == start:
					print('o', end='')
					continue
				if [x,y] == end:
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
		for a in close:
			print(str(a[0]) + ',' + str(a[1]) + ' ', end='')
			print('G=' + str(tab[a[0]][a[1]].G) + ' H=' + str(tab[a[0]][a[1]].H) + ' F=' + str(tab[a[0]][a[1]].F)) 

def astar(tab, start, end):
	open = [start]
	close = []
	current = start
	tab[start[0]][start[1]].H = 0
	calc_H(tab, end)
	while current != end and len(open) >  0:
		current = turn(tab, open, close)
	
	if current == end:
		print_map(tab,close,start,end)

tab = []
for line in content:
	row = []
	for char in line:
		if char != '\n':
			i = Case(int(char), -1, 0, 0)
			row.append(i)
	tab.append(row)

start = [1,1]
goal = [5,2]

#print_map(tab)
#astar(tab, start, goal)

print(calc_G(tab,[2,1]))

file.close()
