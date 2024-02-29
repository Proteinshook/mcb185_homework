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
























"""
w = int(sys.argv[2])
ecoli = sys.argv[1]



seq_split = []

gc_comp_list = []
gc_skew_list = []


for defline, seq in mcb185.read_fasta(ecoli):
	seq_split.append(seq)
seq_joined = ''.join(seq_split)         # could place seq join in next line
gclist = list(seq_joined)
initial_window = gclist[0:w]

initial_gc_comp = dogma.gc_comp(initial_window)
initial_gc_skew = dogma.gc_skew(initial_window)
gc_comp_list.append(initial_gc_comp) # remove replace with print
gc_skew_list.append(initial_gc_skew) # remove replace with print




for i in range(1, len(gclist) -w +1):					
	initial_window.pop(0)
	initial_window.append(gclist[i + w - 1])
	new_gc_comp = dogma.gc_comp(initial_window)
	new_gc_skew = dogma.gc_skew(initial_window)
	gc_comp_list.append(new_gc_comp)
	gc_skew_list.append(new_gc_skew)



print(done)
"""

	





































"""
w = int(sys.argv[2])
ecoli = sys.argv[1]


list_comp = []
list_skew = []

for defline, seq in mcb185.read_fasta(ecoli):
	sequence = seq
	print(len(seq))
initial_window = sequence[0:w]
initial_gc_comp = dogma.gc_comp(initial_window)
initial_gc_skew = dogma.gc_skew(initial_window)
list_comp.append(initial_gc_comp)
list_skew.append(initial_gc_skew)
#print(f'0\t{initial_gc_comp:.3f}\t{initial_gc_skew:.3f}')	#i=0 first w
#print(list_comp[0], list_skew[0])
print(sequence)


for i in range(1, len(sequence) -w +1):
	left = sequence[i]									#left of window
	right = sequence[i + w]								#right of windowprint(left)
	previous_comp = list_comp[i-1]
	if left == 'G' or left == 'C': 
		new_gc_comp = previous_comp + 1/w		
	else : 
		new_gc_comp = previous_comp - 1/w
	if 
	list_comp.append(new_gc_comp)
print(list_comp)
"""