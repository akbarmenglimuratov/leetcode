def findJudge(N, trust):
	trusts = []
	judge = {}
	for i in trust:
		if i[0] not in trusts:
			trusts.append(i[0])

		if i[1] in judge:
			judge[i[1]] += 1
		else:
			judge[i[1]] = 1
	judge =  dict(sorted(judge.items(), key=lambda item: item[1], reverse = True))
	print(judge)
	print(trusts)
	for k,v in judge.items():
		if k not in trusts:
			return k
			break

	return -1


N = 4
trust =  [[1,2],[2,3]]
print(findJudge(N, trust))