import sys
import math

# add args to a probability list
probs = []
for prob in sys.argv[1:]:
	p = float(prob)
	if p <= 0 or p >= 1: sys.exit('Error: probabilities must be between 0 and 1.')
	probs.append(p)

# ensure total is roughly 1
total = 0
for p in probs: total += p
if not math.isclose(total, 1): sys.exit('Error: probabilities must add up to 1.')

# calculate shannon entropy
h = 0
for p in probs: h -= p * math.log2(p)

print(f'{h:.3f}')