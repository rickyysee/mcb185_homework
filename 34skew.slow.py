import sequence
import sys
import gzip

args = sys.argv
if len(args) > 3 or len(args) < 2:
	sys.exit('Error: unexpected number of arguments')

file = args[1]

w = 10 # default window size
if len(args) == 3: w = int(args[2])

# get a string of the whole sequence in the fasta file
seqs = []
with gzip.open(file, 'rt') as fp:
	for line in fp:
		l = line[0]
		if l == '>' or l == '\n' or l == '#': continue
		line = line.strip()
		seqs.append(line)
	seq = ''.join(seqs)

print(seq)

# get gc-skew by counting within each window
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))