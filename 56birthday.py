# 56birthday.py by Ethan Djou

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])





def finddup(list):
	discovered = []
	for i in list:
		if i in discovered: return True 
		else: discovered.append(i)
		
	
total_duplicates = 0
for i in range(trials):
	birthday = []
	for j in range(people):
		n = random.randint(1, days)
		birthday.append(n)					#created list of 23 birthdays
	if finddup(birthday) == True: total_duplicates += 1
probability = total_duplicates / trials * 100


print(probability)


	