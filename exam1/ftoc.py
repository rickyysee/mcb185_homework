def ftoc(F):
	C = (F - 32) * (100/(212-32))
	return C

for i in range(0, 220, 8):
	print(f'{i} deg F is {ftoc(i):.2f} deg C')