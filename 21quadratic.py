"""
21quadratic.py by Ethan Djou
Program for solving the quadratic formula 
(can calculate for one, two and zero roots)
"""
import math
def quad(a, b, c):
	if 0 > ((b**2) - 4 * a * c):
		return 'error: cannot square root a negative number'
	x1 = (-b - math.sqrt((b**2) - 4 * a * c)) / (2 * a)
	x2 = (-b + math.sqrt((b**2) - 4 * a * c)) / (2 * a)
	if 0 < ((b**2) - 4 * a * c):	
		return x1, x2
	else:
		return x1

# Testing the program

print(quad(1, 13, 3))
print(quad(15, 21, 5))
print(quad(1, 15, 1))
print(quad(565, 1000, 67))







	
