def puiss_rec(n):
	total = 1
	if n > 0:
		total = puiss_rec(n-1)*2
	return total

print(puiss_rec(5))