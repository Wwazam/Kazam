import pdb
from kmap import *

# check si la case est vide ou pas
def is_traversable(tile):
	if type(tile) is Wall:
		return False
	return True


#trace un segment entre deux poits (x0,y0) (x1, y1)
def bresenhamLine(x0, y0, x1, y1):
	result = []	#le tableau contenant les coordonnees de tous les points
	end = [x1, y1]	#la case de fin (pour pouvoir l'ajouter a la fin)
	steep = (abs(y1 - y0) > abs(x1 - x0))	#un booleen
	if steep:
		x0, y0 = y0, x0	#swap x0 et y0 (faire une fonction avec les references dans les autres langages)
		x1, y1 = y1, x1	#idem
	if x0 > x1:
		x0, x1 = x1, x0 #idem
		y0, y1 = y1, y0 #idem
	deltax = x1 - x0	#un int
	deltay = y1 - y0	#un int
	error = 0	#un int
	y = y0	#un int
	if y0 < y1:
		ystep = 1
	else:
		ystep = -1
	for x in range(x0, x1):	#for(x = x0, x<x1, x++)
		if steep:
			result.append([y, x])	#ajouter [y,x] a result
		else:
			result.append([x, y])	#ajouter [x,y] a result
		error += deltay
		if 2 * error >= deltax:
			y += ystep
			error -= deltax
	result.append(end)
	return result
	
#verifie que chacune des cases du segment est libre
def get_ray_from_full_ray(map, ray):
	for step in ray:
		if not is_traversable(map[step]):
			index = ray.index(step)
			del ray[index:]
	return ray

#Fonction d'appel
def get_ray(map, start, goal):
	line = bresenhamLine(start[0], start[1], goal[0], goal[1])
	return get_ray_from_full_ray(map, line)
 
def main():
	my_map = Map('map.txt')
	print(is_traversable(my_map[2, 3]))
	start = [11,1]
	goal = [11,9]
	my_map.print_map(path = get_ray(my_map, start, goal))

if __name__ == '__main__':
	main()
