import sequence

print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAAAAACCGTA'))
print(sequence.translate('ATGCCCTAA'))

s = 'ACGTGGGGGGCATATGC'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))