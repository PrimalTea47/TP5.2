def fibonacci(n):
	total = 1
	if n > 1:
		total = fibonacci(n-2) + fibonacci(n-1)
		return total
	elif n == 1:
		return 1
	elif n == 0:
		return 0

print(fibonacci(33))