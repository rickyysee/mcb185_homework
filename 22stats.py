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
def median_medians(list):
	n = len(list)
	mid = n//2
	if n % 2 == 0: mid2 = n//2 - 1
	# use sort if the list is small
	if n <= 10:
		list.sort()
		if n % 2 == 1: return list[mid]
		else:          return (list[mid] + list[mid2]) / 2
	
	# adapted from brilliant.org
	# make lists of 5 or less, then find their medians
	sublists = [list[j:j+5] for j in range(0, len(list), 5)]
	medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

	print(sublists)
	print(medians)

	# choose a good pivot point
	if len(medians) <= 5: pivot = sorted(medians)[len(medians)//2]
	else:                 pivot = median_medians(medians, len(medians)//2)

	print(pivot)

	# partition list to values smaller/bigger than pivot
	lo = [j for j in list if j < pivot]
	hi = [j for j in list if j > pivot]

	print(lo)
	print(hi)

	k = len(lo)
	if mid < k:   return median_medians(lo)
	elif mid > k: return median_medians(hi)
	else:         return pivot

print('number of values:', len(nums))
print('min and max:', min(nums), max(nums))
print('mean and sd:', mean(nums), sd(nums))
print('median:', median_medians(nums))