from kmap import *
from kplayer import *
from ksoldier import *
from kgame import *

maMap = Map('map.txt')

player = [Player(10, 5, 10, [], []), Player(10, 5, 10, [], [])]
player[0].soldier = [
                        Soldier([2,2],'x',player[0].action_point),
                        Soldier([2,3],'x',player[0].action_point),
                        Soldier([3,2],'x',player[0].action_point),
                        Soldier([3,3],'x',player[0].action_point)
                    ]

player[1].soldier = [
                        Soldier([17,17],'o',player[1].action_point),
                        Soldier([18,17],'o',player[1].action_point),
                        Soldier([17,18],'o',player[1].action_point),
                        Soldier([18,18],'o',player[1].action_point),
                    ]
weapon = {
			"shotgun": Weapon(5, 4, {0:5, 1:10, 2:20, 3:35, 4:25, 5:5}),
			"sniper": Weapon(7, 10, {0:20, 2:20, 3:25, 5:25, 7:10})
		}
player[0].weapon = copy.deepcopy(weapon)
player[1].weapon = copy.deepcopy(weapon)

maMap.print_map(soldiers = player[0].soldier + player[1].soldier)
partie = Game(maMap, player)
partie.turn()
