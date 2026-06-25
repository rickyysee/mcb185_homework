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
print("\nGeneral Math")
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
print("\nMath Library")
print(math.ceil(5.6)) # round up; 6
print(math.floor(5.6)) # round down; 5
print(math.log(math.e**5)) # log base e; 5
print(math.log2(2**4)) # log base 2; 4
print(math.log10(10**3)) # log base 10; 3
print(math.sqrt(16)) # square root; 4
print(math.pow(3, 2)) # exponentiation; 3^2 = 9
print(math.factorial(5)) # factorial; 5! = 120

# computer math is imprecise
print("\nMath is Imprecise")
print(0.1 * 1) # returns 0.1
print(0.1 * 3) # returns 0.30000000000000004

# variables
print("\nVariables")
a = 3 # one side of triangle
b = 4 # other side of triangle
c = math.sqrt(a**2 + b**2) # calculate the hypotenuse
print(c) # print value of c
print(type(a), type(b), type(c), sep=', ', end='!\n') # print the types of our variables

# functions
print("\nFunctions")
def pythagoras(a, b): # initiates the function, which takes two arguments
    return math.sqrt(a**2 + b**2) # return pythagorean theorem result

print(pythagoras(3, 4)) # print the result of the pythagoras function
