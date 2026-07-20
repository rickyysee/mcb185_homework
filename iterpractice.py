# iterpractice.py by Ricky Cantua
import math
import random

# function that calculates the triangular number (sum of numbers from 1 to n)
def triangular_num(n):
	current = 0 # initialize a variable to store the sum
	for i in range(1, n+1): # end at specified number, end range is n+1
		current = current + i # store the sum in current variable
		# print(i, current)
	return current
# test code
print('Triangular number of 5 is:', triangular_num(5))

# function that calculates factorial of a number
def factorial(n):
	current = 1 # initialize variable to store product
	for i in range(1, n+1):
		current = current * i # store the product of current variable
	return current
# test code
print('Factorial of 5 is:', factorial(5))
print('Factorial of 0 is:', factorial(0))

# Poisson probability of k events occurring with an expectation of n:
# n^k e^-n / k!
def poisson(n, k): 
	return (n**k) * (math.e**-n) / factorial(k) # previous factorial() fxn
# test code
print('If expected is 6, probability of 9 is:', poisson(6, 9))

# solve for 'n choose k': n! / k!(n-k)!
def combination(n, k): return factorial(n) / (factorial(k) * factorial(n-k))
# test code
print('5 choose 3 is:', combination(5, 3))
print('5 choose 5 is:', combination(5, 5))

# estimate Euler's number (e = 2.71828...)
# infinite sum of 1/n!
# choose finite number of iterations
def euler(n):
	current = 0
	for i in range(n): current = current + 1/factorial(i)
	return current
# test code
print('Estimating Euler\'s number with 10 iterations is:', euler(10))

# determine if a number is prime
def is_prime(n):
	if n == 0 or n == 1: return False # 0 and 1 are not prime
	if n == 2:           return True  # 2 is prime
	if n % 2 == 0:       return False # other even numbers are not prime
	factors = 0 # set the number of factors to 0
	for i in range(1, n//2):
		if n % i == 0:   factors = factors + 1 # count number of factors to n-1
		if factors > 1:  return False # if more than 1 factors (1 is known)
	return True # if not enough factors found, number is prime
# test code
print('Prime numbers:')
for i in range(0,11): print(i, is_prime(i)) # for loop of tests
print('1035', is_prime(1035))
print('9677', is_prime(9677))

# estimate pi (3.14159...) using Nilakantha series
def pi_est(n):
	nilak = 3
	for i in range(0, n): 
		nilak = nilak + (4 * (-1)**i) / (factorial(4 + 2*i) / factorial(1 + 2*i))
	return nilak
# test code
print('Pi estimated up to 10 iterations:')
for i in range(1, 11):
	print(pi_est(i))

# monty pi-thon (estimate pi using monte carlo methods)
# algorithm:
# generate random values for x and y from 0 - 1
# caclulate distance to origin
# if distance is less than 1, point is inside the circular arc
# ratio of points that fall inside compared to total is pi/4
# output each iteration
inside = total = 0
while True:
	x = random.random()
	y = random.random()
	dist = math.sqrt(x**2 + y**2)
	if dist <= 1: inside += 1
	total += 1
	pi = 4 * inside/total
	print(pi)