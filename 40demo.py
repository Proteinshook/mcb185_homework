# 40demo.py by Ethan Djou
import random

for i in range(5):
	print(random.random())
	
nts = 'ACGT'

for i in range(50):
	print(random.choice(nts), end='')
print()

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')
	else:       print(random.choice('CG'), end='')
print()

for i in range(3):
	print(random.randint(1, 6))
	
for i in range(5):
	print(random.gauss(0.0, 1.0))


z1 = 0
z2 = 0
z3 = 0
limit = 1000
for i in range(limit):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 1
print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)


print('this line\n has some\n line breaks')
print('a\tb\tcat\tdogma')
print(10, 20, 30, 40, sep='\t')
print(100, 2000, 30000, 40000, sep='\t')



i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')

print(f'formatted string {i} {pi:.3f}')

import sys
print('logging', file=sys.stderr)

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())

d1 = random.randint(1, 6)