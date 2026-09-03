# convert Farenheit to Celsius
def ftoc(F):
	C = (F - 32) * (100/(212-32))
	return C

# convert mph to kph
def mph_to_kph(mph): return mph / 0.62137

# determines if input parameter is an integer
def is_int(x):
	if x % 1 == 0: return True
	else:          return False

# determine if a number is a probability
def is_prob(x):
	if x >= 0 or x <= 1: return True
	else:                return False

# return the commplement of a DNA letter
COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
def complement(nt):
	if nt in COMPLEMENT: return COMPLEMENT[nt]
	else:                return None

# convert PHRED quality symbol to an error probability
def phred_to_prob(c):
	Q = ord(c) - 33
	return 10 ** (-Q / 10)

## BEGIN ##
# estimate logs of numbers greater than 2 

# use taylor series to estimate ln of small (0-2) numbers
def taylor_ln(x, n=10):
	L = 0
	for i in range(1, n):
		L = L + ((-1)**(i+1) * ((x-1)**i)/i)
	return L

# estimate larger natural logs with
# ln(a*2^b) = ln(a) + b*ln(2)
ln2 = 0.69314718056
def est_ln(x, n=10):
	b = 0
	if x <= 2: return taylor_ln(x, n)
	while 2**b < x: b += 1
	b -= 1
	remain = x / 2**b
	return taylor_ln(remain, n) + (b * ln2)

# estimate logarithms of other bases
def est_log(x, base=10, n=10): return est_ln(x, n) / est_ln(base, n)
## END ##

# convert error prob to PHRED quality symbol
def prob_to_phred(P):
	Q = -10 * est_log(P, 10)
	Q = int(Q // 1)
	ASCII = Q + 33
	return chr(ASCII)

# return hypotenuse of a right triangle with sides a and b
def pythagoras(a, b):
	c = (a**2 + b**2)**(1/2)
	return c

# return max of 3 numbers
def max3(a, b, c):
	if a >= b and a >= c:   max = a
	elif b >= a and b >= c: max = b
	else:                   max = c
	return max

# compute Cartesian distance between two points on a graph
def distance(x1, y1, x2, y2):
	x = x2 - x1
	y = y2 - y1
	return pythagoras(x, y)