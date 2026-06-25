# 10demo.py by Ricky Cantua

# import libraries
import math

print('hello, again') # greeting

# this is a single line comment
"""
This is a
multi-line
comment
"""

# general math
print('\nGeneral Math')
print(1.5e-2) # scientific notation
print(1 + 3) # addition; 4
print(1 - 4) # subtraction; -3
print(2 * 8) # multiplication; 16
print(1 / 2) # division; 0.5
print(2 ** 5) # exponentiation; 32
print(10 // 3) # integer divide; 3
print(10 % 3) # modulo; 1
print(5 * (2 + 1)) # precedence; 15

# math library
print('\nMath Library')
print(math.ceil(5.6)) # round up; 6
print(math.floor(5.6)) # round down; 5
print(math.log(math.e**5)) # log base e; 5
print(math.log2(2**4)) # log base 2; 4
print(math.log10(10**3)) # log base 10; 3
print(math.sqrt(16)) # square root; 4
print(math.pow(3, 2)) # exponentiation; 3^2 = 9
print(math.factorial(5)) # factorial; 5! = 120

# computer math is imprecise
print('\nMath is Imprecise')
print(0.1 * 1) # returns 0.1
print(0.1 * 3) # returns 0.30000000000000004

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
def cels_2_far(c): return (c * (9/5)) + 32
def far_2_cels(f): return (5/9) * (f-32)

print('\n0 deg Celsius to Farenheit')
print(cels_2_far(0))
print('\n98.6 deg Farenheit to Celsius')
print(far_2_cels(98.6))

# speed
def mi_2_km(m): return (m * 1.609344) # roughly 1.5X
def km_2_mi(k): return (k / 1.609344)

print('\n65 mph to kph')
print(mi_2_km(65))
print('\n105 kph to mph')
print(km_2_mi(105))

# DNA conc (ng/uL) from OD260
def od260_2_dna(o): return o * 50

print('\nDNA concentration (ng/uL) from OD260 of 0.42')
print(od260_2_dna(0.42))

# strings
print('\nStrings')
s = 'hello world'
print(s, type(s))

# Conditionals
print('\nConditionals')
a = 2
b = 2
if a == b:
    print('a equals b')
    print(a,'equals', b)