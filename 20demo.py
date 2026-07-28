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
print('\nString Formatting')
# f-strings
print(f'{math.pi}')            # does nothing really
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:.<9}{10}')        # left justify
# str.format()
print('{} {:.3f}'.format('str.format', math.pi))
# printf-style
print('%s %.3f' % ('printf', math.pi))

# indexes
print('\nIndexes')
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