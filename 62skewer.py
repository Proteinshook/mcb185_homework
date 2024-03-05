# 62skewer by Ethan Djou, Coauthored with George Mo, Jordan, Khalid

import gzip
import dogma
import sys
import mcb185

path = sys.argv[1]
w    = int(sys.argv[2])





for defline, seq in mcb185.read_fasta(path):
	fullseq = list(seq)
	window = fullseq[0:w]
	gnum = window.count('G')
	cnum = window.count('C')
	
	for i in range(len(seq) - w):
		drop   = seq[i]
		pickup = seq[i + w]
		
		if   drop == 'G':   gnum -= 1
		elif drop == 'C':   cnum -= 1
		
		if   pickup == 'G': gnum += 1
		elif pickup == 'C': cnum += 1
		
		gccomp = (gnum + cnum) / w
		if (gnum + cnum) > 0: gcskew = (gnum - cnum) / (gnum + cnum)
		else:                 gcskew = 0
		print(f'{i}\t{gccomp:.3f}\t{gcskew:.3f}')


