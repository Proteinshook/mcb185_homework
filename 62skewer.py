# 62skewer by Ethan Djou, Coauthored with George Mo, Jordan, Khalid

import gzip
import dogma
import sys
import mcb185

path = sys.argv[1]
w    = int(sys.argv[2])





for defline, seq in mcb185.read_fasta(path):
	fullseq = list(seq)
	window = fullseq[:w]
	gccomp = dogma.gc_comp(window)
	gcskew = dogma.gc_skew(window)
	gnum = window.count('G')
	cnum = window.count('C')
	
	for i in range(len(seq) - w):
		drop   = seq[i]
		pickup = seq[i + w]
		
		if   drop == 'G':   gnum -= 1
		elif drop == 'C':   cnum -= 1
		
		if   pickup == 'G': gnum += 1
		elif pickup == 'C': cnum += 1
		
		gccomp2 = (gnum + cnum) / w
		if (gnum + cnum) > 0: gcskew2 = (gnum - cnum) / (gnum + cnum)
		else:                 gcskew2 = 0
		print(f'{i}\t{gccomp2:.3f}\t{gcskew2:.3f}')








