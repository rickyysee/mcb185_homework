
# transcribe dna to rna
def transcribe(dna):
	return dna.replace('T', 'U')

# get the reverse complement of a dna sequence
def revcomp(dna):
	rc = []
	for nt in dna[::-1]: # iterate backwards through sequence
		# fill in complement of base
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc) # return rc as a string

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3): # step through indexes by 3
		codon = dna[i:i+3] # slice seq into chunks of 3
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)