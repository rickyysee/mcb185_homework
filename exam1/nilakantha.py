# estimate pi using nilakantha series
# pi = 3 + 4/2*3*4 - 4/4*5*6 + 4/6*7*8 ...
# terminate when upper and lower bounds are within 1e-6 of actual value

current = 3
n = 2

while True:
	# obtain the next step and increment n
	next = 4 * (-1)**(n) / ((2*n) * (2*n-1) * (2*n-2))
	n += 1

	# update the current estimate
	current = current + next
	print(current)

	# obtain diff between current and prev estimate
	diff = (current - next) - (current)

	# if the distance between estimates is within 2e-6, actual value is halfway
	if abs(diff) <= 2e-6: break
