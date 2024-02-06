# 35nchoosek by Ethan Djou Coauthored with Khalid Saif

def factorial(n):
	total = 1
	for j in range(1, n + 1):
		total = total * j
	return total

def choose(n, k):
	if n < 0 or k < 0 or k > n: return 0
	return factorial(n) / (factorial(k) * factorial(n - k))

print(choose(3, 4))
print(choose(2, 1))
print(choose(22, 6))
print(choose(7, 9))
