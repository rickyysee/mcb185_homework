# 16savingthrows.py by Ricky Cantua

import random

# simulate saving throws against DCs of 5, 10, and 15

def saving_throw(DC, adv):
	# check if there is advantage and roll two dice in either scenario
	if adv == 'disadvantage': roll = min(random.randint(1, 20), random.randint(1, 20))
	elif adv == 'advantage' : roll = max(random.randint(1, 20), random.randint(1, 20))
	else                    : roll = random.randint(1, 20)
	# check if the roll passes the difficulty class (DC)
	if roll >= DC : return 'Success'
	elif roll < DC: return 'Failure'
# test code
print('DC of 5:', saving_throw(5, None))
print('DC of 10:', saving_throw(10, None))
print('DC of 15:', saving_throw(15, None))
print('\nDisadvantage:')
print('DC of 5:', saving_throw(5, 'disadvantage'))
print('DC of 10:', saving_throw(10, 'disadvantage'))
print('DC of 15:', saving_throw(15, 'disadvantage'))
print('\nAdvantage:')
