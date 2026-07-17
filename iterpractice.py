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
	return current
print('Factorial of 5 is:', factorial(5))
print('Factorial of 0 is:', factorial(0))

# Poisson probability of k events occurring with an expectation of n:
# n^k e^-n / k!
"""
A coffee shop receives an average of 6 (n) customers every hour.
The probability of getting exactly 9 (k) customers in one hour is a Poisson calculation.
"""
def poisson(n, k): 
	return (n**k) * (math.e**-n) / factorial(k) # previous factorial() fxn
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

# determine if a number is prime
def is_prime(n):
	if n == 0 or n == 1: return False # 0 and 1 are not prime
	if n == 2:           return True  # 2 is prime
	if n % 2 == 0:       return False # even numbers are not prime
	factors = 0 # set the number of factors to 0
	for i in range(1, n):
		if n % i == 0:   factors = factors + 1 # count number of factors to n-1
		if factors > 1:  return False # if more than 1 factors (1 is known)
	return True # if not enough factors found, number is prime
print('Prime numbers:')
print('0:', is_prime(0))
print('1:', is_prime(1))
print('2:', is_prime(2))
print('3:', is_prime(3))
print('4:', is_prime(4))
print('5:', is_prime(5))
print('6:', is_prime(6))
print('7:', is_prime(7))
print('8:', is_prime(8))
print('9:', is_prime(9))
print('10:', is_prime(10))
print('11:', is_prime(11))
print('1035:', is_prime(1035))
print('9677:', is_prime(9677))
# print('4393139:', is_prime(4393139))

# estimate pi (3.14159...) using Nilakantha series
def pi_est(n):
	nilak = 3
	for i in range(0, n+1): 
		nilak = nilak + (4 * (-1)**i) / (factorial(4 + 2*i) / factorial(1 + 2*i))
	return nilak
print('Pi estimated with 10 iterations:', pi_est(10))