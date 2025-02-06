# NOT SOLVED
from functools import reduce
def letterninations(digits):
	letters = {
					"2": "abc", "3": "def",

		"4": "ghi", "5": "jkl", "6": "mno",

		"7": "pqrs","8": "tuv", "9": "wxyz"
	}

	if digits == '':
		return []

	n = 1
	for i in digits:
		n *= len(letters[i])

	res = [''] * n
	each = 1
	for i in digits:
		l_digit = len(letters[i])
		sub = n // (l_digit * each)
		z = 0
		for j in range(n):
			letter = letters[i][z]

			if (j + 1) % sub == 0:
				z = 0 if z == l_digit - 1 else z + 1
		
			res[j] += letter

		each *= l_digit

	return res

digits = "2"
print(letterninations(digits))
