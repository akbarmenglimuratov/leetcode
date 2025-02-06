# SOLVED
def numIdenticalPairs(nums):
	d = {}
	for i in nums:
		d[i] = d[i] + 1 if i in d else 0

	res = 0
	for k, v in d.items():
		res += v*(1+v)//2

	return res

nums = [1,2,3]
print(numIdenticalPairs(nums))
