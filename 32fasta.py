# 32fasta.py by Ricky Cantua

# modules are searched for in several places, including your current directory
import mcb185
import sys

# the read_fasta() function from mcb185.py
# returns a tuple of defline and sequence (string) for each record
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))
