# 25scoringmatrix.py by Ricky Cantua

import sys

# take in args
args = sys.argv
if len(args) != 4:
	sys.exit('this command expects three arguments')

# assign variables to arguments for easier handling
alph = list(args[1])
match = int(args[2])
if match > 0:   match = f'+{match}'
elif match < 0: match = f'{match}'
mismatch = int(args[3])
if mismatch > 0:   mismatch = f'+{mismatch}'
elif mismatch < 0: mismatch = f'{mismatch}'

# print header row
for i in alph: print('\t', i, end='')
print()
# generate matrix for alph
for i, nti in enumerate(alph):
	matrix = []
	for j, ntj in enumerate(alph):
		# fill this line of matrix with correct value
		if nti == ntj: matrix.append(match)
		else:          matrix.append(mismatch)
	# print this line of matrix
	print(nti, end='\t')
	for i in matrix: print(i, end='\t')
	print()
