# 36poisson by Ethan Djou
import math

def poisson(n, k):
	return n**k * math.e**(-n) / math.factorial(k)
	
print(poisson(2, 4))
print(poisson(8, 6))
print(poisson(10, 20))
print(poisson(5, 9))


