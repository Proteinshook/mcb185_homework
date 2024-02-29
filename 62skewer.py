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
	print((f'{0}\t{gccomp:.3f}\t{gcskew:.3f}'))
	for i in range(1, len(seq) - w + 1):
		drop = window[0]
		window.pop(0)
		if i + w < len(seq):
			window.append(seq[i+w])
		pickup = window[-1]
		if drop in 'G': gnum -= 1
		if drop in 'C': cnum -= 1
		if pickup in 'G': gnum += 1
		if pickup in 'C': cnum += 1
		gccomp2 = (gnum + cnum) / len(window)
		gcskew2 = (gnum - cnum) / (gnum + cnum)
		print(f'{i}\t{gccomp2:.3f}\t{gcskew2:.3f}')








