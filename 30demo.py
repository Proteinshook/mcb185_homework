

while True:
	print('hello')


i=0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)

i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)



for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)


for i in range(5):
	print(i)

for char in 'hello':
	print(char)
	
seq = 'GAATTC'
for nt in seq:
	print(nt)



for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:         print(nt1, nt2, '-1')

nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, +1)
		else:          print(nt1, nt2, -1)
		
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)


def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total

print(gc_comp('ACAGCGAAT'))

def trinum(sum):
	total = 0
	for x in range(1, sum + 1):
		total = total + x
	return total
	
print(trinum(5))

def factorial(input):
	total = 1
	for x in range(1, input + 1):
		total = total * x
	return total 

print(factorial(5))

def euler(end):
	sum = 0
	for n in range(1, end + 1):
		sum = sum + 1/factorial(n)
	return sum 

print(euler(100))

