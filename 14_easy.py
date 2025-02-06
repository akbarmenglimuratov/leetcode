def longestCommonPrefix(strs):
	if strs == []:
		return ""
	strs = sorted(strs)
	str1 = strs[0]
	str2 = strs[-1]
	res = ""
	i = j = 0
	n1 = len(str1)
	n2 = len(str2)
	while i <= n1-1 and j <= n2-1:
		if str1[i] != str2[i]:
			break
		res += str1[i]
		i += 1
		j += 1

	return res

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))