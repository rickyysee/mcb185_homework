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
