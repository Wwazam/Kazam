def main():
	tab = get_map('map.txt')
	
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

def is_in_tab(tab, case):
	return tab[case[0]][case[1]] and case[0] >= 0 and case[1] >= 0

def calc_G(tab, case):
	check = [[-1, 0], [0, -1], [1, 1], [2, 2]]
	min = -1
	for ch in check:
		x = case[0] + ch[0]
		y = case[1] + ch[1]
		test = tab[x][y]
		if min == -1:
			min = tab[x][y].G
			continue
		if is_in_tab(tab, [x,y]) and tab[x][y].G != -1 and tab[x][y].G < min:
			min = tab[x][y].G
	return min + 1

def calc_H(case, goal):
	return abs(case[0] - goal[0]) + abs(case[1] - goal[1])

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

if __name__ == '__main__':
	main()
