import random

class Weapon():
	def __init__(self, ammo, range, damage):
		self.ammo = ammo
		self.range = range
		self.damage = damage
	
	def shoot(self):
		if self.ammo ==0:
			return -1
		self.ammo -= 1
		prob = random.randrange(0,100)
		for j, k in self.damage.items():
			prob -= k
			if prob < 0:
				return j
		return -1	
