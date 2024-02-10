import random 

for i in range(3000):
	score = 0
	for roundnumber in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1+d2 == roundnumber:
			score += roundnumber
			
	print(score)