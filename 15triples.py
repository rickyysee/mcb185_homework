# 15triples.py by Ricky Cantua

import math

# find all Pythagorean triples for triangles with sides a and b less than 100
# i.e. 3, 4, and 5 are Pythagorean triples (3^2 + 4^2 = 5^2)

for i in range(1, 99):
	a = i
	b = i + 1
	c = math.sqrt(a**2 + b**2)
	if c % 1 == 0:
		print(a, b, c)