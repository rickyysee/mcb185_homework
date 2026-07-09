# 13fizzbuzz.py by Ricky Cantua
"""
Print numbers 1-100.
If number is divisible by 3, print Fizz instead.
If number is divisible by 5, print Buzz instead.
If number is divisible by both, print FizzBuzz instead.
"""

for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz') # check the intersection first
	elif i % 3 == 0:              print('Fizz')
	elif i % 5 == 0:              print('Buzz')
	else:                         print(i)