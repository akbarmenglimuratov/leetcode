# SOLVED
def countMatches(items, ruleKey, ruleValue):
	d = {"type": 0, "color": 1, "name": 2, }
	count = 0
	for i in items:
		if i[d[ruleKey]] == ruleValue:
			count += 1

	return count


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(countMatches(items, ruleKey, ruleValue))
