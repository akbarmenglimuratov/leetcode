# SOLVED
# from functools import reduce
def xorOperation(n, start):
	l = []
	for i in range(n):
		l.append(start + 2*i)

	bit = l[0]
	for i in l:
		bit ^= i

	return bit

	# return reduce(lambda x, y: x ^ y, l)

n = 5
start = 0
print(xorOperation(n,start))
