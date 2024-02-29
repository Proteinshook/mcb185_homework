# 64profinder.py by Ethan DjoU 
#(some lines of code inspired by Alexandria Skinner during coderie)

import sys
import dogma
import mcb185


path = sys.argv[1]
minlen = int(sys.argv[2])

def translate_frame(seq):
	frames = []
	for frame in range(3):
		frames.append(dogma.translate(seq[frame:]))
		frames.append(dogma.translate(dogma.revcomp(seq)[frame:]))
	return frames

def profinder(seq, minlen):
	proteins = []
	for frame_seq in translate_frame(seq):
		for trans in frame_seq.split('*'):
			if 'M' in trans:
				start = trans.find('M')
				protein = trans[start:]
				if len(protein) >= minlen:
					proteins.append(protein)
	return proteins

n = 1
for defline, seq in mcb185.read_fasta(path):
	for protein in profinder(seq, minlen):
		print(f'>{defline[:11]}-prot-{n}')
		n += 1
		print(f'{protein}*')
	
	















