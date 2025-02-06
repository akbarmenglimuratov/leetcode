'''Solved'''
def arrayPairSum(arr):
	arr.sort()
	max_sum = 0
	for i in range(0,len(arr)-1, 2):
		m = min(arr[i], arr[i+1])
		max_sum += m
	return max_sum

nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))

