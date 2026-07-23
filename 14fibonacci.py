# 14fibonacci.py by Ricky Cantua

# return first 10 numbers from Fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# define a function that has initial values for Fibonacci
def fibonacci(n):
	if n < 0 : return None
	if n == 0: return 0
	if n == 1: return 1
	return fibonacci(n - 1) + fibonacci(n - 2) # recursively call fibonacci()

# print the first 10 digits
for i in range(0, 10):
	print(fibonacci(i))