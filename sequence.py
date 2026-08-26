
# transcribe dna to rna
def transcribe(dna):
	return dna.replace('T', 'U')

# get the reverse complement of a dna sequence
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc) 

# get GC composition of a dna sequence
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

# get the GC-skew along length of a dna sequence
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

# translate a dna sequence to amino acid sequence
def translate(dna):
	codons = ('ATG', 'TAA', 'TAG', 'TGA')
	aminos = 'M***'
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