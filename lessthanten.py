
def lessThanTen(list):
	#ret = []

	#for elem in list:
	#	if elem <= 5:
	#		ret.append(elem)

	#return ret
	ret = [elem for elem in list if elem <= 5]

example = [1, 2, 4, 3.5, 6, 8, 15, 85]
result = lessThanTen(example)

for elem in result:
	print(elem)

