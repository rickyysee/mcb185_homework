# 12phred.py by Ricky Cantua

# function to get quality and error rate from an ASCII character
def char_to_prob(c):
	p = 10 ** -(ord(c)/10) # ord(c) returns the ASCII value of a character, which is Q
	return ord(c), p

print('Get the quality and Phred error rate from the following ASCII characters:')
print('Char, ')
print('', char_to_prob('A'))