# SOLVED
def isSumEqual(firstWord, secondWord, targetWord):
	alpha = 'abcdefghij'
	fun = lambda word: int(''.join(str(alpha.index(i)) for i in word))
	return fun(firstWord) + fun(secondWord) == fun(targetWord)


res = isSumEqual("aaa", "a", "aaaa")
print(res)
