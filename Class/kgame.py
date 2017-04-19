import pdb
from kmap import *
from kplayer import *

def main():
	print('Main')

class Game():
	def __init__(self, map, player):
		self._map = map
		self._player = player
		self._current_player = 0

	def get_map(self):
		return self._map
	def set_map(self, val):
		self._map = val
	map = property(get_map, set_map)

	def get_player(self):
		return self._player
	def set_player(self, val):
		self._player = val
	player = property(get_player, set_player)

	def get_current_player(self):
		return self._current_player
	def set_current_player(self, val):
		self._current_player = val
	current_player = property(get_current_player, set_current_player)


	def turn(self):
		for sol in self.player[self.current_player].soldier:
			while sol.action_point > 0:
				command = input(" > ")
				command = command.split()
				if command:
					if command[0] in ["move", "mv"]:
						sol.go_to(self.map, [int(command[1]), int(command[2])])
					if command[0] in ["pass", "ps"]:
						sol.pass_turn()
					if command[0] in ["position", "pos"]:
						print(sol.pos)
					if command[0] in ["shoot", "st", "sht"]:
						dammage = self.player[self.current_soldier].weapon[command[1]].shoot
						if dammage > -1:
							self.player[self.current_player].health_point.get_shot(dammage, [command[2],command[3]])
				self.map.print_map(soldiers = self.player[0].soldier + self.player[1].soldier, current_soldier = sol.pos)
				print(sol.action_point)

if __name__ == '__main__':
	main()
