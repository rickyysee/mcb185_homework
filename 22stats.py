# 22stats.py by Ricky Cantua

import math
import sys

# report descriptive stats of numbers on the command line
# number of values, min and max, mean and sd, median

# get numbers from command line
nums = []
if len(sys.argv) <= 1: sys.exit('Please provide a list of numbers as arguments.')
for i in sys.argv[1:]:
	num = float(i)
	nums.append(num)
print(nums)

# min and max
def min(list):
	min = list[0]
	for x in list:
		if x < min: min = x
	return min

def max(list):
	max = list[0]
	for x in list:
		if x > max: max = x
	return max

# mean and std
def mean(list):
	total = 0
	for x in list: total += x
	return total / len(list)

def sd(list):
	if len(list) <= 1: return 0
	total = 0
	m = mean(list)
	for x in list: 
		total += (x - m) ** 2
	total = total / (len(list) - 1)
	return total ** (1/2)

# nevermind, median of medians seemed to exceed recursion depth on large lists?
# median by sorting
def median(list):
	n = len(list)
	list.sort()
	if n % 2 == 0:
		return (list[n//2] + list[n//2 - 1]) / 2
	else:
		return list[n//2]

print('number of values:', len(nums))
print('min and max:', min(nums), max(nums))
print('mean and sd:', mean(nums), sd(nums))
print('median:', get_median(nums))