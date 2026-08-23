# 24birthday.py by Ricky Cantua

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

sameBirthday = 0 # initialize a counter
for i in range(0, trials):

	# generate an empty calendar
	calendar = []
	for i in range(0, days):
		calendar.append(0)

	# for every person, increment the calendar at their birthday
	for i in range(0, people):
		birthday = random.randint(0, days-1)
		# if their birthday is taken, increment counter and break loop
		if calendar[birthday] > 0:
			sameBirthday += 1
			break
		calendar[birthday] += 1

print(f'Probability of a shared birthday in {people} people:', sameBirthday/trials)
