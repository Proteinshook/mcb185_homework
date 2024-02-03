# 35nchoosek by Ethan Djou

def factorial(input):
	total = 1
	for x in range(1, input + 1):
		total = total * x
	return total

def choose(n, k):
	return factorial(n) / factorial(k) * factorial(n - k)

print(choose(3, 4))
print(choose(10, 15))
print(choose(22, 6))
print(choose(7, 9))
	
	