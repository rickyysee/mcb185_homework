# 17deathsaves.py by Ricky Cantua

import random

# determine if you get closer to death, stability, or revival with a D20
# need 3 failures (death), 3 successes (stability) or a 20 (revival)
# failure = less than 10
# 1       = critical failure (2 failures)
# success = greater than 10
# 20      = critical success (instant revive)

def death_throw(option):
	# initialize counters to keep track of rolls
	stable = death  = 0
	while stable < 3 and death < 3: # roll until stable or death reach 3
		roll = random.randint(1, 20)
		if option == 'print': print(roll) # shows each roll if specified
		# check the result of the roll and either revive or increment counters
		if roll == 20  : return 'Revive'
		elif roll >= 10: stable += 1
		elif roll == 1 : death  += 2
		else           : death  += 1
	# if while loop exits, you are either stable or dead
	if stable >= 3 : return 'Stable'
	elif death >= 3: return 'Death'
# test code
print(death_throw('print'))

# calculate probabilities through boot strap method
# use None as the option to avoid printing each roll
stable = death = revive = total = 0 # reinitialize counters
for i in range(1, 10000):
	if death_throw(None) == 'Revive': revive += 1
	if death_throw(None) == 'Stable': stable += 1
	if death_throw(None) == 'Death' : death  += 1
	total += 1
# test code
print()
print('Result', 'Probability',  sep='\t')
print('Revive', revive / total, sep='\t')
print('Stable', stable / total, sep='\t')
print('Death', death / total, sep='\t')


