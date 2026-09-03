# print out the first 100 numbers of the Fibonacci seq

def fibonacci(n):
	fibos = [0, 1]
	for i in range(0, n-1):
		sum = fibos[i] + fibos[i+1]
		fibos.append(sum)
	return fibos

for i, j in enumerate(fibonacci(100)):
	print(f'{i}:\t{j:,}')