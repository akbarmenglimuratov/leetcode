# SOLVED
def numberOfSteps(num):
	step = 0
	while num > 0:
		num = num // 2 if num%2 == 0 else num - 1
		step += 1
	return step

num = 14
print(numberOfSteps(num))
