# 33triples by Ethan Djou
import math
def triple(n):
	for a in range(1, n):
		for b in range(a + 1, n): 
			c = (a**2 + b**2)**(1/2)
			if c % 1 == 0: 
				print(a, b, c)

triple(100)

