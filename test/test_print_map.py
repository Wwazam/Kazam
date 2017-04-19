import os 

file = open('map.txt', 'r')
content = file.readlines()
#tab = {}
#x = 0
#y = 0
#for line in content:
#	for char in line:
#		if char != '\n':
#			tab[x, y] = char
#			x+=1
#	x = 0
#	y+= 1

tab = []
for line in content:
	row = []
	for char in line:
		if char != '\n':
			row.append(char)
	tab.append(row)
	
for row in tab:
	for col in row:
		if col=='1':
			print('#', end='')
		else:
			print(' ', end='')
	print()
