# 20demo.py by Ricky Cantua

import math
import random

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
nts[2] = 'G'    # can change elements of a list
print(nts)
nts.append('C')  # add element to list
print(nts)
last = nts.pop() # remove element from list
print(nts)
nts.sort()       # sorts similar types of elements
print(nts)
nts.sort(reverse=True)
print(nts)
nucleotides = nts # can give lists new names but won't copy
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
# to make a copy, use list.copy() (complex data structures will not be copied)

# list()
items = list()   # creates an empty list
print(items)
items.append('eggs')
print(items)
stuff = []       # creates an empty list
print(stuff)
stuff.append(3)
print(stuff)
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alph)
aas = list(alph) # coerce into iterable
print(aas)

# split()
print('\nsplit() separates strings into a list')
text = 'good day			to you'
words = text.split()   # split on whitespace
print(text)
print(words)
line = '1.41,2.72,3.14'
print(line)
print(line.split(',')) # split on comma (good for CSV)

# join()
print('\njoin() turns lists into strings')
print(aas)
s = '-'.join(aas) # join into string with '-' spacers
print(s)
s = ''.join(aas)  # join into string without spacers
print(s)

# searching
# keyword `in` searches if an item exists in a container
print()
print(alph)
print('search with `in`:')
if 'A' in alph: print('A') # search for A in capital alphabet
if 'a' in alph: print('a') # search for a, will not print
# index() method returns index of the first element it finds
print('search with index() method:')
print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))
# find() method returns index of first element or -1 if none found
# note: only used in strings
print('search with find() method:')
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))
# use `in` if you don't know if an element is in a list/tuple
if 'D' in aas: print('D in list?', aas.index('D'))

# practice problems
print('\nPractice Problems:')

# min value of a list
def list_min(list):
	min = list[0]
	for i in list[1:]:
		if i < min: return i
	return min

# min and max values of a list
def min_max(list):
	min = list[0]
	max = list[0]
	for i in list[1:]:
		if i < min:   min = i
		elif i > max: max = i
	return min, max

# mean of values in a list
def list_mean(list):
	sum = 0
	for i in range(0, len(list)):
		sum = sum + list[i]
	return sum / len(list)

# test code
test_list = [6, 31, 10, 4]
print()
print('test list:', test_list)
print('min:', list_min(test_list))
print('min and max:', min_max(test_list))
print('mean:', list_mean(test_list))

# return a random list with probabilities that add up to 1.0
def prob_list(n):
	plist = []
	sum = 0
	for i in range(0, n):          # get random ints from 0-100
		roll = random.randint(0, 100)
		sum = sum + roll
		plist.append(roll)
	for i in range(0, len(plist)): # divide each int by the total
		plist[i] = plist[i] / sum
	return plist

# entropy of a probability distribution
# information(x) = -sum( p(x) * log_2(p(x)) )
def entropy(prob):
	sum = 0
	entropy = 0
	for i in prob:
		if i != 0:
			sum = sum + i
			entropy = entropy - (i * math.log2(i))
	if sum < 0.9 or sum > 1.1: return None
	return entropy

# kullback-leibler distance between two sets of probability distributions
# d(p||k) = sum( p(x) * log((p(x))/(q(x))) )
def kb_dist(prob_p, prob_q):
	sum = 0
	for p, q in zip(prob_p, prob_q):
		if p != 0 and q != 0:
			sum = sum + p * math.log2(p / q)
	return sum

# test code
print('\nentropy of probability distribution')
prob_q = [0.05, 0.15, 0.2, 0.5, 0.1]
prob_p = prob_list(5)
print('prob distribution P:', prob_p)
print('prob distribution Q:', prob_q)
print('entropy of P:', entropy(prob_p))
print('kullback-leibler distance between P and Q:', kb_dist(prob_p, prob_q))

# external data
print()
# input() gets a line of input from user
# line = input('type something and hit return: ')
# print('that line what', len(line), 'characters long')

# sys.argv is the list of words on the command line (argv = argument vector)
# sys.argv[0] is the program name
# sys.argv[1] is the first argument if there is one

import sys

print(sys.argv)

# sys.argv is a list, so it will have brackets
# numeric values have quotes bc they are strings