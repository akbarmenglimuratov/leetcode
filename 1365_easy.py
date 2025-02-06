# SOLVED
def smallerNumbersThanCurrent(nums):
	count = [0] * 102
	for num in nums:
		count[num+1] += 1

	for i in range(1, 101):
		count[i] += count[i-1]

	return [count[num] for num in nums]



nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))
