# 30demo.py by Ricky Cantua

# to read file data: open file, stream data from it, and close
'''
fp = open(path)
for line in fp:
	do_something_with(line)
fp.close()
'''
# to avoid forgetting to close a file, can use `with`
'''
with open(path) as fp:
	for line in fp:
		do_something_with(line)
'''
# to read compressed files, we need to import a library
import gzip
'''
with gzip.open(path, 'rt') as fp:
	for line in fp:
		print(line, end='')
'''

# continue statement jumps to the next iteration of a loop
'''
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		print(line)
'''
# the above code will print lines that do not begin with '#'

# sliding window algorithm
seq = 'abcdefghijklmnopqrstuvwxyz'
w = 10
s = 1
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]
	print(subseq)
# sliding windows can be used to create things like codons and k-mers

