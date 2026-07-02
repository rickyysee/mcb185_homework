# 12phred.py by Ricky Cantua
import math

"""
Phred quality scores are a way to encode error rate information.
They are used to tell how likely a base is to be incorrect after sequencing.
Phred scores have a respective error rate and ASCII character.
The commonly used standard is Phred+33 (allowing values 0-93).
"""

# function to get quality and error rate from an ASCII character
def char_to_prob(c):
	# calculate q and p only if c is a string
	if type(c) == str:
		q = ord(c) - 33 # calculate the quality score from ASCII value, ord(c)
	else: return None

	# check that q is within 0-93, which are the limits for Phred+33 scores
	if q >= 0 and q <= 93:
		p = 10 ** -(q/10) # calculate the error rate, p
		return q, p

print('Get the quality and Phred error rate from the following ASCII characters:')
print('Char : (Q , Prob)')
print('A    :', char_to_prob('A'))
print('<TAB>:', char_to_prob('	'))
print('0.001:', char_to_prob(0.001))

# function to get the ASCII character from an error rate
def prob_to_char(x):
	# calculate q only if x is a number
	if type(x) == float or type(x) == int:
		q = -10 * math.log10(x) # calculate the quality score, q
	else: return None # return None if the probability is a string
	
	# calculate ascii only if q is an integer
	if q % 1 == 0: # integers have mod 1 = 0
		q = math.floor(q) # remove decimal from q
		ascii = chr(q + 33) # convert q to its respective ascii character
		return q, ascii

print('\nGet the quality value and ASCII character from the following error rates:')
print('Prob : (Q , Char)')
print('0.001:', prob_to_char(0.001))
print('A    :', prob_to_char('A'))