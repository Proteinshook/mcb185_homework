# 65transmembrane by Ethan Djou

import sys
import dogma
import mcb185


path = sys.argv[1]



def calculate_avg_kd(sequence):
	kd_total = 0
	for aa in sequence:
		kd_total += float(dogma.kd(aa))
	kd_avg = kd_total / len(sequence)
	return kd_avg

	
def transmembrane(sequence, w, region, kd):
	if len(sequence) >= 30:
		if w > 8: transmembrane_region = sequence[region:]
		else:     transmembrane_region = sequence[:region]
		for i in range(len(transmembrane_region) -w +1):
			s = transmembrane_region[i:i+w]
			avg_kd = calculate_avg_kd(s)
			if avg_kd >= kd and 'P' not in s:
				return True
	return False


total_transmembrane = 0
for defline, seq in mcb185.read_fasta(path):
	if transmembrane(seq, 8, 30, 2.5) == True:
		if transmembrane(seq, 11, 30, 2.0) == True:
			print(defline[:60])
			total_transmembrane +=1
print(total_transmembrane)


	

	
	















