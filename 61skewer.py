# 61skewer.py
import dogma
import sys
import mcb185

# seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
sequence = sys.argv[1]
amount = []
w = 1000
for defline, seq in mcb185.read_fasta(sequence):
	for i in range(len(seq) -w +1):
		print(f'the length is {len(seq)}')
		s = seq[i:i+w]
		print(i, dogma.gc_comp(s), dogma.gc_skew(s))
		amount.append(i)
		
print(len(amount))
		



