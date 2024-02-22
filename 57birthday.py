# 57birthday.py by Ethan Djou

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

total_duplicates = 0
for i in range(trials):
	callender = []
	for j in range(days):				# create an empty callender
		callender.append(0)

	for k in range(people):
		birthday = random.randint(0, days - 1)
		callender[birthday] += 1
		if 2 in callender:
			total_duplicates += 1
			break
		
probability = total_duplicates / trials * 100


						
print(probability)



