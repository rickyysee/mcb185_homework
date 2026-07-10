# iterpractice.py by Ricky Cantua
import math

# function that calculates the triangular number (sum of numbers from 1 to n)
def triangular_num(n):
	current = 0 # initialize a variable to store the sum
	for i in range(1, n+1): # end at specified number, end range is n+1
		current = current + i # store the sum in current variable
		# print(i, current)
	return current
print('Triangular number of 5 is:', triangular_num(5))

# function that calculates factorial of a number
def factorial(n):
	current = 1 # initialize variable to store product
	for i in range(1, n+1):
		current = current * i # store the product of current variable
		# print(i, current)
	return current
print('Factorial of 5 is:', factorial(5))

# Poisson probability of k events occurring with an expectation of n:
# n^k e^-n / k!
"""
A coffee shop receives an average of 6 (n) customers every hour.
The probability of getting exactly 9 (k) customers in one hour is a Poisson calculation.
"""
def poisson(n, k): return (n**k) * (math.e**-n) / factorial(k) # previous factorial() fxn
print('If expected is 6, probability of 9 is:', poisson(6, 9))
