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
w = 22
s = 1
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]
	print(subseq)
# sliding windows can be used to create things like codons and k-mers

# sets are mutable containers with unique, unordered elements
s = {'A', 'C', 'G'}
print(s)
# add elements to a set with add() method
s.add('A')
print(s)
# adding A doesn't do anything because it's already in the set
# calling an index will throw an error
# print(s[2]) # TypeError

# dictionaries are like lists but indexes are strings
# items in a dictionary exist as a key:value pair
d = {}
d = dict() 
# both above generate empty dictionary
d = {'dog' : 'woof', 'cat' : 'meow'}
print(d)
print(d['cat'])
# to add items to a dict, assign a key:value pair
d['pig'] = 'oink'
print(d)
# to change value of item, access its key
d['cat'] = 'mew'
print(d)
# to delete an item, use del keyword
del d['cat']
print(d)
# accessing a key that doesn't exist throws an error
# print(d['rat']) # KeyError
# to check if a key exists, use in
if 'dog' in d: print(d['dog'])

# iterating through a dictionary
# for loop iterates over keys in order they were created
for key in d: print(f'{key} says {d[key]}')
# using dict.items() is a common way to iterate
for k, v in d.items(): print(k, 'says', v)
# unpack tuples to avoid the following mess:
for thing in d.items(): print(thing[0], 'says', thing[1])
# there is also dict.keys() and dict.values()
# if you want them as lists, coerce with list()
print(d.keys(), d.values(), list(d.values()))

# dictionaries make counting very fast
count = {}
seq = 'AGCTAGCAATCGCATCACCAATCGATACGGGGGGGGGTACAGGGCGATATAAGG'
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
print(count)
# you can easily sort a dict with the sorted() function
for k in sorted(count): print(k, count[k])
# sorting by values is more complex
# sorted() expects a list of things to sort, which is the keys by default
for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)
# lambda indicates a tiny anonymous function
# this lambda function returns the second element in the item tuple
# below is the same operation done with a real function
def by_value(tuple):
	return tuple[1]

for k, v in sorted(count.items(), key=by_value):
	print(k, v)

# k-mers are sequences of length k
# we can use itertools to generate all possible kmers
import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)

# multiple dimensions
# sys.argv is 2 dimensional (list of strings)
import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[0][1])

d = [
	'hello',
	(3.14, 'pi'),
	[-1, 0, 1],
	{'year' : 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])

# arrays and matrices
# some languages use arrays and lists as the same, not Python
# arrays are linear containers where all elements are the same type (i.e. int)
# matrices are multidimensional arrays and are rectangular

# record is a data type with named fields (dict)
# records are put into a list (catalog)
oligo = {
	'Name' : 'SO116',
	'Length' : '18',
	'Sequence' : 'ATATAGAGTCTCCCGACTAG',
	'Description' : 'SP6 promoter sequencing primer'
}
catalog = []
catalog.append(oligo)
# lists of records can be long, so we usually read them in from spreadsheets
# use this on MCB185/data/primers.csv
def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name' : name,
				'Length' : length,
				'Sequence' : seq,
				'Description' : desc
			}
			catalog.append(record)
	return catalog

catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])
# what if we wanted to count k-mers and record their location
# everytime we find a new k-mer, we need to initialize a list and append its location
seq = 'AGACATCCCGCATGACGATCAGTCACGCGCTAGCTCACGACTGCGCGCCCAAAAAAAAATCGCTAGCT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)
# this behaves differently than counting each k-mer
# running this on a large genome could crash a computer bc memory would run out

# complex data
# we can combine data types to make more complex data sets other than spreadsheets
{
    "locus": "NC_000913",
    "length": 4641652,
    "type": "DNA",
    "definition": "Escherichia coli str. K-12 substr. MG1655, complete...",
    "reference": [
        {
            "authors": "Riley,M., Abe,T., Arnaud,M.B., Berlyn,M.K...",
            "title": "Escherichia coli K-12: a cooperatively...",
            "journal": "Nucleic Acids Res. 34 (1), 1-9 (2006)",
            "pubmed": 16397293
        },
        {
            "authors": "Hayashi,K., Morooka,N., Yamamoto,Y., Fujita,K...",
            "title": "Highly accurate genome sequences of Escherichia...",
            "journal": "Mol. Syst. Biol. 2, 2006 (2006)",
            "pubmed": 16738553
        }
    ]
}
# this is a dict, where the value for reference is a list of dicts
# this format is compatible with JSON (Javascript Object Notation)
# double quotes only, true/false not capital, no trailing commas, no comments
import json
truc = {
	'animals' : {'dog' : 'woof', 'cat' : 'meow', 'pig' : 'oink'},
	'numbers' : [1.09, 2.72, 3.14],
	'is_complete' : False,
}
# json library provides ways to read and write JSON
print(json.dumps(truc, indent=4))
