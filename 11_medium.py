# NOT SOLVED
def maxArea(height):
	res = []
	left = 0
	right = len(height) - 1

	while left < right:
		l_height = height[left]
		r_height = height[right]

		if  l_height <= r_height:
			res.append(l_height * (right - left))
			left += 1
		else:
			res.append(r_height * (right - left))
			right -= 1

	return max(res)


# height = [1,8,6,2,5,4,8,3,7]
height = [1,2,1]
print(maxArea(height))