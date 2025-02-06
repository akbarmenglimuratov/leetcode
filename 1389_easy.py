# SOLVED
def createTargetArray(nums, index):
	new_list = []
	for i, val in enumerate(index):
		new_list.insert(val, nums[i])

	return new_list


nums = [1]
index = [0]
print(createTargetArray(nums, index))
