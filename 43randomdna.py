# 43randomdna.py by Ethan Djou

import random

nts = 'ACGT'
trials = 3

for i in range(trials):
	length = random.randint(50, 60)
	print(f'seq-{i+1}')
	for i in range(length):
		print(random.choice(nts), end='')
	print()
	