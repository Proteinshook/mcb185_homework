# 50demo.py by Ethan Djou


seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])


s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])

print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s[0])
print(s[0:1])

print(s, s[::], s[::1], s[::-1])

tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0])
print(tax[::-1])

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
	
x1, x2 = quadratic(5, 6, 1)
print(x1, x2)


nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])


for i, nt, in enumerate(nts):
	print(i, nt)


names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

print()

for nt, name in zip(nts, names):
	print(nt, name)

print()

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)


nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)



items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day    to you'
words = text.split()
print(words)

line = '1.41, 2.72, 3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z')) gives error


print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# if thing in list: idx = list.index(thing)


# Practice problems


list = [4, 1, 5, 2, 3]
sort = list.sort()
print(list[0])					# minimum value

print(list[0], list[-1])		# max value


total = 0
for i in range(len(list)):
	add = list[i]
	total += add
mean = total / len(list)
print(mean)						# mean of list


with open(path) as fp:
	for line in fp:
		do_something_with(line)

import gzip
with gzip.open(path, 'rt') as fp:
	for line in fp:
		print(line, end='')

		
i = int('42')
x = float('0.61803')
print(i, x)


import math

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))