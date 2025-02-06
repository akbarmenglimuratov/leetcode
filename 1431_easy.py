# SOLVED
def kidsWithCandies(candies, extraCandies):
	max_candies = max(candies)
	return [True if max_candies-i <= extraCandies else False for i in candies]

candies = [4,2,1,1,2]
extraCandies =1
print(kidsWithCandies(candies, extraCandies))