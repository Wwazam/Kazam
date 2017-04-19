import random
result = {}
tab = {0:1, 1:53, 2:30, 3:15, 4:1}
for i in range(0,5):
	result[i]=0
for i in range(0,1000000):
	nbr = random.randrange(0,100)
	for j, k in tab.items():
		nbr -= k
		if nbr < 0:
			result[j] += 1
			break
print(result) 
