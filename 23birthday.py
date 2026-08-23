# 23birthday.py by Ricky Cantua

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


sameBirthday = 0 # initialize a counter
for i in range(0, trials):

	# generate a random list of birthdays
	birthdays = []
	for i in range(0, people):
		birthdays.append(random.randint(0, days))

	# create a half matrix to check each birthday combo
	birthdayBreak = False
	for i in range(0, len(birthdays)):
		for j in range(i+1, len(birthdays)):
			if birthdays[i] == birthdays[j]: 
				sameBirthday += 1
				birthdayBreak = True
				break

		# break out of outer loop if birthdayBreak is triggered
		if birthdayBreak:
			break

print(f'Probability of a shared birthday in {people} people:', sameBirthday/trials)