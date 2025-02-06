#SOLVED
def toHex(d):
	if d < 0:
		d = 2**32 + d
	digits = "0123456789abcdef"
	r = d % 16
	if d - r == 0:
		return digits[r]
	return toHex(d//16) + digits[r]

num = 10
print(toHex(num))
