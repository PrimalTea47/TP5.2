def fact(n):
	total = 1
	if n > 0:
		total = fact(n-1)*n
	return total

print(fact(3))