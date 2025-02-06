# SOLVED
def maximumWealth(accounts):
	max_wealth = sum(accounts[0])
	for i in range(len(accounts)):
		max_temp = sum(i)
		if max_temp > max_wealth:
			max_wealth = max_temp

	return max_wealth


accounts = [[1,5],[7,3],[3,5]]
print(maximumWealth(accounts))