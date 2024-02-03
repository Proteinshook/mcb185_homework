# 37nilakantha by Ethan Djou

def nila(n):
	n1 = 2
	pi = 3
	sign = 1
	for x in range(1, n + 1):
		n3 = n1 + 2
		n2 = n1 + 1
		mult = (n1 * n2 * n3)
		n1 = n3
		pi = pi + (sign * 4 / mult)
		sign = sign * -1
	return(pi)
			
print(nila(4))
		
		