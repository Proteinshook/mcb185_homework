# 45dndstats.py by Ethan Djou Coauthored Khalid Saif, George Mo
import random


# 3D6

trials = 10000

total = 0
for i in range(trials):
	score = 0
	for j in range(3):
		dice = random.randint(1, 6)
		score += dice
	total += score
avg = total / trials
print(avg)


# 3D6r1


total = 0
for i in range(trials):
	score = 0
	for j in range(3):
		dice = random.randint(1, 6)
		if dice == 1: dice = random.randint(1, 6)
		score += dice
	total += score
avg = total / trials
print(avg)


# 3D6x2


total = 0
for i in range(trials):
	score = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2: score += d1
		else: score += d2
	total += score
avg = total / trials
print(avg)


# 4D6d1


total = 0
for i in range(trials):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if   d1 <= d2 and d1 <= d3 and d1 <= d4: score += d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: score += d1 + d3 + d4
	elif d3 <= d1 and d3 <= d2 and d3 <= d4: score += d1 + d2 + d4
	elif d4 <= d1 and d4 <= d2 and d4 <= d3: score += d1 + d2 + d3
	total += score
avg = total / trials
print(avg)