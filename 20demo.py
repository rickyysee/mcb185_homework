# 20demo.py by Ricky Cantua

import math

# strings are wrapped in quotes
s = 'hello world'
print(s)
# mix quote types to print them
s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
# use backslashes to escape quotes
print('hey "dude" don\'t tell me what to do')

# string methods
print(s.upper())
print(s)
print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

# string formatting
print('\nthere are different ways to work with strings')
# f-strings
print(f'{math.pi}')            # does nothing really
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:.<9}{10}')         # left justify
# str.format()
print('{} {:.3f}'.format('str.format', math.pi))
# printf-style
print('%s %.3f' % ('printf', math.pi))

# indexes
print('\nindexes are used to identify characters in a string')
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])
# iterate through characters in a string
for nt in seq:
	print(nt, end='')
print()
# iterate using indexes
for i in range(len(seq)):
	print(i, seq[i])

# slices
print('\nslices are a portion of a container')
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])             # both ABCDE
print(s[5:len(s)], s[5:])        # both FGHIJ
print(s, s[::], s[::1], s[::-1]) # these are all identical, except last is reversed
# slice dna sequence into codons
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)

# tuples
print('\ntuples store items and are immutable')
tax = ('Homo', 'sapiens', 9606) # make a tuple
print(tax)                      # parentheses will be in the output
# tuples are also immutable (like strings)
# s[0] = 'C' # error
# tax[0] = 'human' # error
print(tax[0])    # index at beginning
print(tax[::-1]) # slice that reverses order

print('\nsometimes we want both indexes and values')
# enumerate()
# enumerate can be used to produce a tuple with index and value of a container
nts = 'ACGT'
print('using range():')
for i in range(len(nts)):
	print(i, nts[i])
print('\nenumerate() produces a tuple with indexes and values:')
for i, nt in enumerate(nts):
	print(i, nt)

# zip()
# zip can be used to iterate through two different containers in parallel
print('\nusing range():')
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
print('\nzip() iterates through two different containers in parallel:')
for nt, name in zip(nts, names):
	print(nt, name)
# enumerate the zip
print('\nenumerate() the zip():')
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

# lists
# similar to tuples but they are made with brackets [,,] and are mutable
print('\nlists store items and are mutable')
nts = ['A', 'T', 'C']
print(nts)
# can change elements of a list
nts[2] = 'G'
print(nts)
# can add element to end of a list with list.append()
nts.append('C')
print(nts)
# can remove elements with list.pop()
last = nts.pop()
print(nts)
# can sort similar type of elements in a list with list.sort()
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
# you can give lists new names (this doesn't create a new list)
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
# to make a copy, use list.copy() (complex data structures will not be copied)

# list()
# can be used to create empty lists
items = list()
print(items)
items.append('eggs')
print(items)
# can also use empty brackets
stuff = []
print(stuff)
stuff.append(3)
print(stuff)
# list() will coerce iterables into lists
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alph)
aas = list(alph)
print(aas)

# split()
print('\nsplit() separates strings into a list')
text = 'good day			to you'
words = text.split()
print(text)
print(words)
# can also be helpful when dealing with TSV or CSV data
line = '1.41,2.72,3.14'
print(line)
print(line.split(','))

# join()
print('\njoin() turns lists into strings')
print(aas)
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# searching
# keyword `in` searches if an item exists in a container
print('\nsearching can be done many ways')
print(alph)
if 'A' in alph: print('A')
if 'a' in alph: print('a')