# SOLVED
def decode(encoded, first):
	
	new_list = [first]

	for i in encoded:
		new_list.append(i ^ new_list[-1])

	return new_list

encode = [1,2,3]
first = 1
print(decode(encode, first))
