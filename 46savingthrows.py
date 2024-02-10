# 46savingthrows.py by Ethan Djou Coauthored with Khalid Saif


import random




trials = 1000

print('advantage')
for i in range(5, 16, 5):
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 > d2: 
			a = d1
		else: 
			a = d2
		if a >= i:
			success += 1
	print(success / trials)
print('\ndisadvantage')

for i in range(5, 16, 5):							
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 < d2:
			a = d1
		else:
			a = d2
		if a >= i:
			success += 1
	print(success / trials)
print('\nnormal')

for i in range(5, 16, 5):						
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d = random.randint(1, 20)
		if d >= i:
			success += 1
	print(success / trials)
	
	
