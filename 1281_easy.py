# SOLVED
def subtractProductAndSum(n):
	k = 1
	s = 0
	for i in str(n):
		k *= int(i)
		s += int(i)
	return k - s

n = 234
print(subtractProductAndSum(n))
