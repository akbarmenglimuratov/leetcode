# SOLVED
def decompressRLElist(nums):
	new_list = []
	for i in range(0, len(nums), 2):
		new_list += [nums[i+1]]*nums[i]

	return new_list

nums = [1,1,2,3]
print(decompressRLElist(nums))
