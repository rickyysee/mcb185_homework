# 12phred.py by Ricky Cantua
import math

# function to turn an ASCII value to quality score
def ascii_to_qual(n):
	if n >= 33 and n <= 75: return n - 33

# function to get quality and error rate from an ASCII character
def char_to_prob(c):
	q = ascii_to_qual(ord(c)) # calculate the quality score from ASCII value, ord(c)
	p = 10 ** -(q/10) # calculate the error rate, p
	return q, p

print('Get the quality and Phred error rate from the following ASCII characters:')
print('Char: (Q , Prob)')
print('A   :', char_to_prob('A'))

# function to get the ASCII character from an error rate
def prob_to_char(x):
	q = -10 * math.floor(math.log10(x)) # calculate the quality score, q
	return q, chr(q)

print('\nGet the quality value and ASCII character from the following error rates:')
print('Prob : (Q , Char)')
print('0.001:', prob_to_char(0.001))