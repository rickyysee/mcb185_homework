a = 38
b = 45

c = (a**2 + b**2) ** (0.5)
mid = (a + b) / 2
if a < b: 
	min = a
	max = b
elif a > b:
	min = b
	max = a
else: min = max = a

print(f'hypotenuse of {a} and {b} is {c:.2f}')
print(f'midpoint between {a} and {b} is {mid:.2f}')
print(f'min is {min}, max is {max}')