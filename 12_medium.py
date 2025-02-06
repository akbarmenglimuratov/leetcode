def intToRoman(num):
	roman = {
		1: "I", 
		4: "IV", 
		5: "V", 
		9: "IX", 
		10: "X", 
		40: "XL",
		50: "L", 
		90: "XC",
		100: "C", 
		400: "CD", 
		500: "D",
		900: "CM",
		1000: "M"
	}
	res = ""
	for key in reversed(roman.keys()):
		if num / key >= 1:
			res += roman[key] * (num//key)
			num %= key
	return res
	
num = 58
print(intToRoman(num))