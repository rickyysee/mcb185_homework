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

# solve for 'n choose k': n! / k!(n-k)!
def combination(n, k): return factorial(n) / (factorial(k) * factorial(n-k))
print('5 choose 3 is:', combination(5, 3))
print('5 choose 5 is:', combination(5, 5))

# estimate Euler's number (e = 2.71828...)
# infinite sum of 1/n!
# choose finite number of iterations
def euler_est(n):
	current = 0
	for i in range(n): current = current + 1/factorial(i)
	return current
print('Estimating Euler\'s number with 10 iterations is:', euler_est(10))