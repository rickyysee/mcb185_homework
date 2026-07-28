# 16savingthrows.py by Ricky Cantua

import random

# simulate saving throws against DCs of 5, 10, and 15

def saving_throw(DC, adv):
	# check if there is advantage and roll two dice in either scenario
	if adv == 'disadvantage': roll = min(random.randint(1, 20), random.randint(1, 20))
	elif adv == 'advantage':  roll = max(random.randint(1, 20), random.randint(1, 20))
	else:                     roll = random.randint(1, 20)
	# check if the roll passes the difficulty class (DC)
	if roll >= DC:  return 'Success'
	elif roll < DC: return 'Failure'
# test code
print('DC', 'ADV', 'Result', sep='\t')
print('05', 'None', saving_throw(5, None), sep='\t')
print('10', 'None', saving_throw(10, None), sep='\t')
print('15', 'None', saving_throw(15, None), sep='\t')
print('05', 'Dis', saving_throw(5, 'disadvantage'), sep='\t')
print('10', 'Dis', saving_throw(10, 'disadvantage'), sep='\t')
print('15', 'Dis', saving_throw(15, 'disadvantage'), sep='\t')
print('05', 'Adv', saving_throw(5, 'advantage'), sep='\t')
print('10', 'Adv', saving_throw(10, 'advantage'), sep='\t')
print('15', 'Adv', saving_throw(15, 'advantage'), sep='\t')
