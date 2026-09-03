# print numbers 1-100
# if divisible by 3: print Fizz instead
# if divisible by 5: print Buzz instead
# if divisible by both: print FizzBuzz

def fizzbuzz(n):
	if n % 5 == 0 and n % 3 == 0: return 'FizzBuzz'
	elif n % 3 == 0:              return 'Fizz'
	elif n % 5 == 0:              return 'Buzz'
	else:                         return n

for i in range(1, 101):
	print(fizzbuzz(i))