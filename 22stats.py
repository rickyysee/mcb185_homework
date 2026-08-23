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

# median without sorting (use the median of medians method)
# adapted from brillian.org

# handles function calls for odd or even numbered lists
def get_median(list):
	i = len(list)
	if i % 2 == 1: 
		return median_medians(list, i//2)
	if i % 2 == 0: 
		return (median_medians(list, i//2) + median_medians(list, i//2 - 1)) / 2

def median_medians(list, i):
	# make lists of 5 or less, then find their medians
	sublists = [list[j:j+5] for j in range(0, len(list), 5)]
	medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

	# choose a good pivot point
	if len(medians) <= 5: pivot = sorted(medians)[len(medians)//2]
	else:                 pivot = median_medians(medians, len(medians)//2)

	# partition list to values smaller/bigger than pivot
	lo = [j for j in list if j < pivot]
	hi = [j for j in list if j > pivot]

	k = len(lo)
	if i < k:   return median_medians(lo, i)
	elif i > k: return median_medians(hi, i - k - 1)
	else:         return pivot

print('number of values:', len(nums))
print('min and max:', min(nums), max(nums))
print('mean and sd:', mean(nums), sd(nums))
print('median:', get_median(nums))