# dogma.py 

def transcribe(dna):
	return dna.replace('T', 'U')


def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)




def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)
	
	
def translate(dna):
	codons = ('TTT', 'TTC', 'TTA', 'TTG', 'TCT', 'TCC', 'TCA', 'TCG', 'TAT', 'TAC',
              'TAA', 'TAG', 'TGT', 'TGC', 'TGA', 'TGG', 'CTT', 'CTC', 'CTA', 'CTG',
              'CCT', 'CCC', 'CCA', 'CCG', 'CAT', 'CAC', 'CAA', 'CAG', 'CGT', 'CGC',
              'CGA', 'CGG', 'ATT', 'ATC', 'ATA', 'ATG', 'ACT', 'ACC', 'ACA', 'ACG',
              'AAT', 'AAC', 'AAA', 'AAG', 'AGT', 'AGC', 'AGA', 'AGG', 'GTT', 'GTC',
              'GTA', 'GTG', 'GCT', 'GCC', 'GCA', 'GCG', 'GAT', 'GAC', 'GAA', 'GAG',
              'GGT', 'GGC', 'GGA', 'GGG')
	aminos = ('F', 'F', 'L', 'L', 'S', 'S', 'S', 'S', 'Y', 'Y', '*', '*', 'C', 'C', '*', 'W',
				'L', 'L', 'L', 'L', 'P', 'P', 'P', 'P', 'H', 'H', 'Q', 'Q', 'R', 'R', 'R', 'R',
				'I', 'I', 'I', 'M', 'T', 'T', 'T', 'T', 'N', 'N', 'K', 'K', 'S', 'S', 'R', 'R',
				'V', 'V', 'V', 'V', 'A', 'A', 'A', 'A', 'D', 'D', 'E', 'E', 'G', 'G', 'G', 'G')
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
	
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)



def kd(aa):
	aminos = 'IVLFCMAGTWSYPHEQDNKR'
	kd_values = ('4.5', '4.2', '3.8', '2.8', '2.5', '1.9', '1.8', 
				'-0.4', '-0.7', '-0.9', '-0.8', '-1.3','-1.6', 
				'-3.2', '-3.5', '-3.5', '-3.5', '-3.5', '-3.9', '-4.5')
	index = aminos.find(aa)
	return kd_values[index]

	
	
	
