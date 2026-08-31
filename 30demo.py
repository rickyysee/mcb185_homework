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