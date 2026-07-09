# iterpractice.py by Ricky Cantua

# function that calculates the triangular number (sum of numbers from 1 to n)
def triangular_num(n):
	current = 0 # initialize a variable to store the sum
	for i in range(1, n+1): # end at specified number, end range is n+1
		current = current + i # store the sum in current variable
		# print(i, current)
	return(current)
print('Triangular number of 5 is:', triangular_num(5))

# function that calculates factorial of a number
def factorial(n):
	current = 1 # initialize variable to store product
	for i in range(1, n+1):
		current = current * i # store the product of current variable
		print(i, current)
	return(current)
print('Factorial of 5 is:', factorial(5))