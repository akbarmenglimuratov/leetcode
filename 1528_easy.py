# SOLVED
def restoreString(s, indices):
	d = {indices[i]: v for i, v in enumerate(s)}

	return ''.join([d[k] for k in sorted(d)])

	# n = len(indices)
	# new_s = ['']*n
	# for i in range(n):
	# 	new_s[indices[i]] += s[i]
	# return ''.join(new_s)


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))
