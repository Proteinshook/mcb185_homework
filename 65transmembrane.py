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



def hydrophobic_signal(sequence):
	if len(sequence) >= 30:
		signal_peptide = sequence[:30]
		for i in range(len(signal_peptide) -8 +1):
			s = signal_peptide[i:i+8]
			avg_kd = calculate_avg_kd(s)
			if avg_kd >= 2.5 and 'P' not in s:
				return True
	return False
	
def transmembrane_region(sequence):
	if len(sequence) >= 30:
		transmembrane_region = sequence[30:]
		for i in range(len(transmembrane_region) -11 +1):
			s = transmembrane_region[i:i+11]
			avg_kd = calculate_avg_kd(s)
			if avg_kd >= 2.0 and 'P' not in s:
				return True
	return False


total_transmembrane = 0
for defline, seq in mcb185.read_fasta(path):
	if hydrophobic_signal(seq) == True and transmembrane_region(seq) == True:
		print(defline[:60])
		total_transmembrane +=1
print(total_transmembrane)


	

	
	















