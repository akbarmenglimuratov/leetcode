# SOLVED
def runningSum(nums):
	# for i in range(1,len(nums)):
	# 	nums[i] = nums[i] + nums[i-1]

	# return nums
	return [sum(nums[0:i+1]) for i in range(len(nums))]

nums = [1,2,3,4,5]
print(runningSum(nums))