import mcb185
import sys
import re

print('D-K-T-G-T')
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if 'DKTGT' in seq: print(defline)

print('\nD-K-T-G-T')
# can also do this with regular expressions (re library)
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT', seq): print(defline)

print('\nD-K-T-G-T-[LIVM]-[TI]')
# regular expressions are more flexible than `in`
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT[LIVM][TI]', seq): print(defline)

print('\nC-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H')
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)

# regular expressions can extract matching text
pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	m = re.search(pat, seq)
	if m: print(m.group(1))