# SOLVED
def shuffle(nums,n):
	new_list = []
	for i in range(n):
		new_list += [nums[i], nums[n+i]]

	return new_list

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))