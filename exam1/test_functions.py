import functions
import random

### test code ###
for i in range(0, 100, 20):
	print(f'{i} deg F is {functions.ftoc(i):.2f} deg C')
print()

for i in range(0, 100, 20):
	print(f'{i} mph is {functions.mph_to_kph(i):.2f} kph')
print()

vals = [0, 0.2, 5, -6.0, -6.1]
for i in vals:
	print(f'is {i} an int? {functions.is_int(i)}')
print()

for i in vals:
	print(f'is {i} a prob? {functions.is_prob(i)}')
print()

bases = ['A', 'C', 'G', 'T']
for nt in bases:
	print(f'{nt} pairs with {functions.complement(nt)}')
print()

chars = ['!', '(', 'A', 'H']
for i in chars:
	print(f'{i} error prob: {functions.phred_to_prob(i):.5f}')
print()

print(f'ln(1.5): {functions.taylor_ln(1.5):.4f}')
print(f'ln(100): {functions.est_ln(100):.4f}')
print(f'log10(100): {functions.est_log(100):.4f}')
print()

probs = []
for i in range(5): probs.append(random.random())
for i in probs:
	print(f'{i:.4f} error prob is: {functions.prob_to_phred(i)}')
print()

sides = [(3, 4), (41, 73), (6, 7), (20, 30)]
for a, b in sides:
	print(f'a: {a}\tb: {b}\tc: {functions.pythagoras(a, b):.2f}')
print()

# generate a list of 5 random numbers
vals = []
for i in range(5): vals.append(random.randint(-100, 100))

# loop through all combinations of numbers
for i in range(len(vals)):
	for j in range(i+1, len(vals)):
		for k in range(j+1, len(vals)):

			# assign variables and call max3() function
			a, b, c = vals[i], vals[j], vals[k]
			print(f'a: {a}\tb: {b}\tc: {c}\tmax: {functions.max3(a, b, c)}')
print()

# test cartesian function
x1, y1, x2, y2 = vals[0], vals[1], vals[2], vals[3]
print(f'x1: {x1}\ty1: {y1}\tx2: {x2}\ty2: {y2}\tdist: {functions.distance(x1, y1, x2, y2):.2f}')
print()

