# 73missingkmer.py by Ethan Djou
import sys
import mcb185
import itertools
import dogma


def kmercount(seq, k, dict):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: dict[kmer] = 0
		dict[kmer] += 1
		

path = sys.argv[1]
kcount = {}
missing_kmers = []
k = 0
while len(missing_kmers) <= 0:
	k += 1
	# Runs through the normal and reverse complement sequence, 
	# Adding the kmers and their amount to dictionary
	for defline, seq in mcb185.read_fasta(path):
		kmercount(seq, k, kcount)
		kmercount(dogma.revcomp(seq), k, kcount)
	# Generates all possible kmers, comparing them to the kcount dictionary
	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts)
		if kmer not in kcount:           
			missing_kmers.append(kmer)
	
	
	
kmer_amount = len(missing_kmers)
print(f'{missing_kmers}\nthere are {kmer_amount} missing kmers at k = {k}')



