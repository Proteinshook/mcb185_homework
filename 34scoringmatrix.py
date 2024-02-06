# 34scoring matrix by Ethan Djou Coauthored with Khalid Saif

print('   ', end='')
nucleotide = 'ACGT'
for n in nucleotide:
	print(n, end='  ')
print()
for nt1 in nucleotide:
	print(nt1, end=' ')
	for nt2 in nucleotide:
		if nt1 == nt2: print('+1', end=' ')
		else:          print('-1', end=' ')
	print()
		