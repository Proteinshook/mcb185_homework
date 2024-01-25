# 25entropy.py by Ethan Djou Co-authored Khalid Saif
import math

def shannon(a, c, g, t):
	total = a + c + g + t
	if a > 0: 
		adenine =		(a / total) * (math.log2(a / total))
	else:
		adenine = 0
		return 'undefined log0 for adenine'
	if c > 0: 
		cytosine =		(c / total) * (math.log2(c / total))
	else:
		cytosine = 0
		return 'undefined log0 for cytosine'
	if g > 0: 
		guanine =		(g / total) * (math.log2(g / total))
	else:
		guanine = 0
		return 'undefined log0 for guanine'
	if t > 0: 
		tyrosine =		(t / total) * (math.log2(t / total))
	else:
		tyrosine = 0
		return 'undefined log0 for tyrosine'
	
	x = -(adenine + cytosine + guanine + tyrosine)
	return x
	
	
	
# Testing the formula
print(shannon(13, 14, 15, 16))
print(shannon(6, 143, 157, 0))
print(shannon(6785, 7, 0, 879))
print(shannon(968, 0, 365, 9))
print(shannon(0, 7, 5, 4))


