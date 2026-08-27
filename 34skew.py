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
		if line[0] == '#' or line[0] == '\n': continue
		line = line.strip()
		seqs.append(line)
	seq = ''.join(seqs)

# count GCs in first window
firstw = seq[0:w]
g = firstw.count('G')
c = firstw.count('C')
comp = g + c / w
if g + c == 0: skew = 0
else         : skew = (g - c) / (g + c) 
print(0, comp, skew)

# get gc-skew by checking preceeding and final base of each window
for i in range(1, len(seq) -w +1):
	s = seq[i-1] + seq[i+w-1]
	if s[0] == 'G': g -= 1
	if s[0] == 'C': c -= 1
	if s[1] == 'G': g += 1
	if s[1] == 'C': c += 1
	comp = g + c / w
	if g + c == 0: skew = 0
	else         : skew = (g - c) / (g + c)
	print(i, comp, skew) 

