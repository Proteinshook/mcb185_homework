# 44randompi.py by Ethan Djou

import random

total = 0
inside_circle = 0
while True:
	x = random.random()
	y = random.random()
	r = (x**2 + y**2) ** 0.5
	if r <= 1:
		inside_circle += 1
	total += 1
	
	pi_estimate = (inside_circle / total) * 4
	print("estimate of pi:", pi_estimate)