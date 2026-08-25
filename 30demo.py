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
