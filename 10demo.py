# 10demo.py by Ricky Cantua

# import libraries
import math

print('hello, again') # greeting

# this is a single line comment
"""
this is a
multi-line
comment
"""

# general math
print('\nGeneral Math')
print('1.5e-2 is:', 1.5e-2) # scientific notation
print('1 + 3 is:', 1 + 3) # addition; 4
print('1 - 4 is:', 1 - 4) # subtraction; -3
print('2 * 8 is:', 2 * 8) # multiplication; 16
print('1 / 2 is:', 1 / 2) # division; 0.5
print('2 ** 5 is:', 2 ** 5) # exponentiation; 32
print('10 // 3 is:', 10 // 3) # integer divide; 3
print('10 % 3 is:', 10 % 3) # modulo; 1
print('5 * (2+1) is:', 5 * (2+1)) # precedence; 15

# math library
print('\nMath Library')
print('math.ceil(5.6) is:', math.ceil(5.6)) # round up; 6
print('math.floor(5.6) is:', math.floor(5.6)) # round down; 5
print('math.log(math.e**5) is:', math.log(math.e**5)) # log base e; 5
print('math.log2(2**4) is:', math.log2(2**4)) # log base 2; 4
print('math.log10(10**3) is:', math.log10(10**3)) # log base 10; 3
print('math.sqrt(16) is:', math.sqrt(16)) # square root; 4
print('math.pow(3, 2) is:', math.pow(3, 2)) # exponentiation; 3^2 = 9
print('math.factorial(5) is:', math.factorial(5)) # factorial; 5! = 120

# computer math is imprecise
print('\nMath is Imprecise')
print('0.1 * 1 is:', 0.1 * 1) # returns 0.1
print('0.1 * 3 is:', 0.1 * 3) # returns 0.30000000000000004

# variables
print('\nVariables')
a = 3 # one side of triangle
b = 4 # other side of triangle
c = math.sqrt(a**2 + b**2) # calculate the hypotenuse
print(c) # print value of c
print(type(a), type(b), type(c), sep=', ', end='!\n') # print the types of our variables

# functions
print('\nFunctions')

# geometry
def pythagoras(a, b): # initiates the function, which takes two arguments
    return math.sqrt(a**2 + b**2) # return pythagorean theorem result
def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): w * h
def trangle_area(w, h): return rectangle_area(w, h) / 2 # divide rectangle area by 2

print(pythagoras(3, 4)) # print the result of the pythagoras function

# temperature
def cels_2_far(x): return (x * (9/5)) + 32
def far_2_cels(x): return (5/9) * (x-32)

print('\n0 deg Celsius to Farenheit')
print(cels_2_far(0))
print('\n98.6 deg Farenheit to Celsius')
print(far_2_cels(98.6))

# speed
def mi_2_km(x): return (x * 1.609344) # roughly 1.5X
def km_2_mi(x): return (x / 1.609344)

print('\n65 mph to kph')
print(mi_2_km(65))
print('\n105 kph to mph')
print(km_2_mi(105))

# DNA conc (ng/uL) from OD260
def od260_2_dna(x): return x * 50

print('\nDNA concentration (ng/uL) from OD260 of 0.42')
print(od260_2_dna(0.42))

# strings
print('\nStrings')
s = 'hello world'
print(s, type(s))

# conditionals
print('\nConditionals')
a = 2
b = 2
if a == b:
    print('a equals b')
    print(a,'equals', b)

# boolean
c = a == b
print(c, type(c))

def is_even(x):
    if x % 2 == 0: return True
    return False

print('2 is even:', is_even(2))
print('3 is even:', is_even(3))

# if-elif-else
a = 0.3
b = 0.1 * 3

if   a < b:  print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print')

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

# never! test for equality with floats
# instead, see if their difference is below some threshold
print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

# math.isclose() also does this
if math.isclose(a, b): print('close enough')

# strings
print('\nStrings')
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

a = 1
s = 'G'
# if a < s: print('a < s') # TypeError

# 'None' type
print('\nNone Type')
def silly(m, x, b):
    y = m*x + b # y is computed but not returned
print(silly(2, 3, 4))

# function practice
# check if number is integer
def is_integer(x):
    if x % 1 == 0: return True # integers modulo 1 will be 0
    return False

print('\nAre the following numbers integers:')
print('3', is_integer(3))
print('13', is_integer(17))
print('3.14', is_integer(3.14))
print('-3', is_integer(-3))
print('-3.14', is_integer(-3.14))
print('0', is_integer(0))

# check if a number is a valid probability
def is_prob(x):
    if x >= 0 and x <= 1: return True # probability must be within 0-1
    return False

print('\nAre the following numbers valid probabilities:')
print('0.3', is_prob(0.3))
print('-0.3', is_prob(-0.3))
print('1e-9', is_prob(1e-9))
print('5/9', is_prob(5/9))
print('e', is_prob(math.e))

# return molecular weight of a DNA base, otherwise None
def dna_weight(nt):
    if nt == 'A' or nt == 'a': return 313.2
    if nt == 'T' or nt == 't': return 304.2
    if nt == 'G' or nt == 'g': return 329.2
    if nt == 'C' or nt == 'c': return 289.2

print('\nWhat are the molecular weights (g/mol) of the following DNA bases:')
print('A', dna_weight('A'))
print('c', dna_weight('c'))
print('U', dna_weight('U'))
print('N', dna_weight('N'))
print('5', dna_weight(5))

# return complement of DNA letter, otherwise None
def dna_complement(nt):
    if nt == 'A' or nt == 'a': return 'T'
    if nt == 'T' or nt == 't': return 'A'
    if nt == 'G' or nt == 'g': return 'C'
    if nt == 'C' or nt == 'c': return 'G'

print('\nGet complementary base of following DNA bases:')
print('A', dna_complement('A'))
print('c', dna_complement('c'))
print('U', dna_complement('U'))
print('N', dna_complement('N'))
print('5', dna_complement(5))

# return largest of 3 numbers
def max_of_3(x, y, z):
	if x >= y and x >= z: return x 
	if y >= x and y >= z: return y 
	if z >= y and z >= x: return z 

print('\nFind the max in a set of three numbers:')
print('1, 2, 3:', max_of_3(1, 2, 3))
print('1, 3, 2:', max_of_3(1, 3, 2))
print('2, 1, 3:', max_of_3(2, 1, 3))
print('2, 3, 1:', max_of_3(2, 3, 1))
print('3, 1, 2:', max_of_3(3, 1, 2))
print('3, 2, 1:', max_of_3(3, 2, 1))
print('1, 2, 2:', max_of_3(1, 2, 2))
print('2, 2, 2:', max_of_3(2, 2, 2))

# return sensitivity, specificity, and F1 score from positives and negatives
def bin_classify(tp, tn, fp, fn):
	sens = tp / (tp + fn) # rate of correct positives out of actual positives
	spec = tn / (tn + fp) # rate of correct negatives out of actual negatives
	prec = tp / (tp + fp) # rate of correct positives out of detected positives
	f1   = 2 * (prec * sens)/(prec + sens)
	return sens, spec, f1

print('\nFind the sensitivity, specificity, and F1 scores for the following confusion matrices:')
print('TP, TN, FP, FN: (Sensitivity, Specificity, F1 Score)')
print('05, 05, 02, 01:', bin_classify(5, 5, 2, 1))