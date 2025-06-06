def romanToInt(s):
	roman = {
		"I" : 1   ,
		"IV": 4   ,
		"V" : 5   ,
		"IX": 9   ,
		"X" : 10  ,
		"XL": 40  ,
		"L" : 50  ,
		"XC": 90  ,
		"C" : 100 ,
		"CD": 400 ,
		"D" : 500 ,
		"CM": 900 ,
		"M" : 1000,
	}
	res = 0
	temp = 0
	for i in reversed(s):
		if roman[i] >= temp:
			res += roman[i]
		else:
			res -= roman[i]
		temp = roman[i]
	return res


s = "LIX"
print(romanToInt(s))