# 31cdslength.py by Ricky Cantua

import gzip
import sys

gff = sys.argv[1]

with gzip.open(gff, 'rt') as fp:
	for line in fp:
		if not line.startswith('#'):
			fields = line.split()
			if fields[2] == 'CDS':
				id = fields[8].split(';')[0].split('-')[1] # grab the ID in last field
				len = int(fields[4]) - int(fields[3]) + 1 # calculate length of CDS
				print(id, fields[2], len, sep='\t')