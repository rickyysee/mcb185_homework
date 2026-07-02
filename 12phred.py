# 12phred.py by Ricky Cantua
import math

# function to get quality and error rate from an ASCII character
def char_to_prob(c):
	p = 10 ** -(ord(c)/10) # calculate the error rate, p, from q, ord(c)
	return ord(c), p

print('Get the quality and Phred error rate from the following ASCII characters:')
print('Char: (Q , Prob)')
print('A   :', char_to_prob('A'))

# function to get the ASCII character from an error rate
def prob_to_char(x):
	q = -10 * math.floor(math.log10(x)) # calculate the quality score, q, from error rate, p
	return q, chr(q) # chr(q) returns the ASCII value of a number

print('\nGet the quality value and ASCII character from the following error rates:')
print('Prob : (Q , Char)')
print('0.001:', prob_to_char(0.001))