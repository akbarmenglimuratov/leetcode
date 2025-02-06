
# My solution
def longset_sub(s):
	all_counts = [0]
	uniq = []
	for i, e in enumerate(s):
		if e in uniq:
			all_counts.append(len(uniq))
			uniq = uniq[uniq.index(e) + 1:]

		uniq.append(e)

		if i == len(s) - 1:
			all_counts.append(len(uniq))
		
	return max(all_counts)

s = "abcabcbb"
print(longset_sub(s))


# Better solution

# def longset_sub(s):
# 	max_substr = 0
# 	uniq = ""
# 	for e in s:
# 		if e in uniq:
# 			max_substr = max(max_substr, len(uniq))
# 			uniq = uniq[uniq.index(e) + 1:]
# 		uniq += e
# 	max_substr = max(max_substr, len(uniq))

# 	return max_substr
