# 70demo.py by Ethan Djou

"""
d = {}
dict = dict()

d = {'dog': 'wolf', 'cat' : 'meow'}
print(d)

print(d['cat'])

d['pig'] = 'oink'
print(d)


d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

# print(d['rat'])

if 'dog' in d: print(d['dog'])

# Iterations

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

# dont do this, unpack your tuples
for thing in d.items(): print(thing[0], thing[1]) 

# printing only keys or values, or values in a list
print(d.keys(), d.values(), list(d.values()))


# Lookup tables
kdtable = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
	'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
	'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtable[aa]
	return kd/len(seq)
	
# Categorical Data
# for counting things and able to count things it has never seen before
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1


# Sorting

# for k in sorted(count): print(k, count[k])
d['bat'] = 'reeeee'
for i in d: print(i, d[i])
print('sorted')
for i in sorted(d): print(i, d[i])  
# the sorted function will sort keys alphabetical order


for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v) 
"""
# generating all possible kmers

import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)