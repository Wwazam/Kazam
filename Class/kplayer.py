from kweapon import *
from ksoldier import *

class Player():
	def __init__(self, health_point, respawn, action_point, soldier, weapon):
		self._health_point = health_point
		self._respawn = respawn
		self._action_point = action_point
		self._soldier = soldier
		self._weapon = weapon

	def get_health_point(self):
		return health_point
	def set_health_point(self, val):
		self._health_point = val
		if self._health_point <= 0:
			self.respawn -= 1
	health_point = property(get_health_point, set_health_point)

	def get_action_point(self):
		return self._action_point
	def set_action_point(self, val):
		self._action_point = val
	action_point = property(get_action_point, set_action_point)

	def get_respawn(self):
		return self._respawn
	def set_respawn(self, val):
		self._respawn = val
		if self._respawn < 0:
			respawn = property(get_respawn, set_respawn)

	def get_soldier(self):
		return self._soldier
	def set_soldier(self, val):
		self._soldier = val
	soldier = property(get_soldier, set_soldier)

	def get_weapon(self):
		return self._weapon
	def set_weapon(self, val):
		self._weapon = val
	weapon = property(get_weapon, set_weapon)
