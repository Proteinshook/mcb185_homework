# 74genefinder.py by Ethan Djou coauthored with Khalid Saif
import sys
import mcb185
import dogma


"""
seq = 'ATGCGGGCTGACGCGTACAGGAAATGACACAGAAATGAAAGCCCGCACCTGA'
# devdata
"""

# Define start and stop codons and minimum ORF length
start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']
min_orf_length = int(sys.argv[2])

# Function to find ORFs in a seq
def find_orfs(seq, frame, strand):
	orfs = []
	index = 0
	while index < len(seq):
		codon = seq[index:index+3]
		if codon != start_codon:
			index += 3
			continue

		start = index  # Record the start position of the ORF

		for j in range(index, len(seq) - 2, 3):
			codon = seq[j:j+3]  # Move to the next codon in the seq
			if codon in stop_codons:
				stop = j + 2  # Record the position of the stop codon
				if (stop - start) >= min_orf_length:
					if strand == '+':
						orfs.append((start + 1 + frame, stop + 3 + frame - 2, strand))
					else:
						orfs.append((len(seq) - stop, len(seq) - start, strand))
				index = j
				break
		index += 3  # Move to the next codon triplet
	return orfs

# converts to GFF style
def format_output(defline, start, end, strand):
	return f'{defline}\tRefSeq\tCDS\t{start}\t{end}\t.\t{strand}'

# Iterate over seq in the FASTA file
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for frame in range(3):
		print(f'frame\t{frame}\n')
		identifier = defline.split()[0]
		orfs_pos_strand = find_orfs(seq[frame:], frame, '+')
		orfs_neg_strand = find_orfs(dogma.revcomp(seq)[frame:], frame, '-')

		# Output positive strand coordinates
		for start, end, strand in orfs_pos_strand:
			print(format_output(identifier, start, end, strand))
        
		# Output negative strand coordinates
		for start, end, strand in orfs_neg_strand:
			print(format_output(identifier, start, end, strand))

		print()














