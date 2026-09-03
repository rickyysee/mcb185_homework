# estimate e (2.71828...) by computing inf sum of 1/n!
# stop calculation when value is repeated
# print current estimate at each loop

from math import factorial

current = 0
next = 0
n = 0
while True:
	next = 1/factorial(n)
	n += 1
	current = current + next
	print(current)
	if current == (current + next): break
