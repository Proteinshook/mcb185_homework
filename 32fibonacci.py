# 32fibonacci by Ethan Djou

def fibo(n):
	n1 = 0
	n2 = 1
	if n >= 1: print(n1)
	if n >= 2: print(n2)
	for x in range(n-2):
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		print(n3)

fibo(10)
		