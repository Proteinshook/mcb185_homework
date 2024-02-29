# 46savingthrows.py by Ethan Djou Coauthored with Khalid Saif


import random


def prob(trials, type):
	print(type)
	for i in range(5, 16, 5):
		print(i, end='\t')
		success = 0
		for n in range(trials):
			d1 = random.randint(1, 20)
			d2 = random.randint(1, 20)
			if d1 > d2: 
				a = d1
				b = d2
			else: 
				a = d2
				b = d1
			c = d1
			if type == 'advantage': dice = a
			if type == 'disadvantage': dice = b
			if type == 'normal': dice = c
			if dice >= i:
				success += 1
		print(success / trials)

prob(1000, 'advantage')
prob(1000, 'disadvantage')
prob(1000, 'normal')
