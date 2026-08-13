# 22stats.py by Ricky Cantua

import math
import sys

# report descriptive stats of numbers on the command line
# number of values, min and max, mean and sd, median

# get numbers from command line
nums = []
for i in sys.argv[1:]:
	num = float(i)
	nums.append(num)

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

# median without sorting (by removing min and max values sequentially)
# revisit this, it seems wildly inefficient
def median(list):
	if len(list) == 1: return list[0]
	if len(list) == 2: return (list[0] + list[1]) / 2
	while len(list) > 1:
		list.pop(list.index(min(list)))
		list.pop(list.index(max(list)))
		if len(list) == 1: return list[0]
		if len(list) == 2: return (list[0] + list[1]) / 2

print('number of values:', len(nums))
print('min and max:', min(nums), max(nums))
print('mean and sd:', mean(nums), sd(nums))
print('median:', median(nums))