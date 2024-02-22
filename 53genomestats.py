# 53genomicstats.py by Ethan Djou

import gzip 
import sys


gffpath = sys.argv[1]
feature = sys.argv[2]
lengths = []

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] == feature:
			beg = int(words[3])
			end = int(words[4])
			lengths.append(end - beg + 1)


count = len(lengths)

def minmax(vals):
	min = vals[0]
	max = vals[0]
	for val in vals:
		if val < min: min = val
		if val > max: max = val
	return min, max
	
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
def stddev(n):
	sum = 0
	for i in range(len(n)):
		sum += (n[i] - mean(n))**2
		variance = sum / count
	return variance**0.5



def med(i):
	i.sort()
	n = len(i)
	if n % 2 == 0:
		median = (i[n//2 - 1] + i[n//2]) / 2
	else:
		median = i[n//2]
	return median

print(count)
print(minmax(lengths))
print(mean(lengths))
print(stddev(lengths))
print(med(lengths))
