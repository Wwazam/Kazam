import pdb
import astar

class Soldier():
	def __init__(self, pos, symbol, action_point):
		self.pos = pos
		self.symbol = symbol
		self.action_point = action_point
	def __str__(self):
		return str(self.symbol)
	
	def go_to(self, map, goal):
		pdb.set_trace()
		map[self.pos[0], self.pos[1]].free = True
		path = astar.astar(map.map, self.pos, goal)
		if not path == []:
			if len(path) > self.action_point+1:
				del path[self.action_point+1:]
			self.pos = path[-1]
			map[self.pos[0], self.pos[1]].free = False
			self.action_point -= len(path)-1
		else:
			print("Le chemin est invalide")
		return path

	def pass_turn(self):
		self.action_point = 0
