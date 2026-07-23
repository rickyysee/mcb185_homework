# 15triples.py by Ricky Cantua

import math

# find all Pythagorean triples for triangles with sides a and b less than 100
# i.e. 3, 4, and 5 are Pythagorean triples (3^2 + 4^2 = 5^2)

for i in range(1, 100):
	a = i # check every a from 1-99
	for j in range(i+1, 100): # check values of b after a through 99
		b = j
		c = math.sqrt(a**2 + b**2) # calculate c
		if c % 1 == 0: # check if hypotenuse is an integer
			print(a, b, math.floor(c))