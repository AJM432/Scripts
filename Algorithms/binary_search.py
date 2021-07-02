import random

data_list = [x for x in range(1000000)]

def binary_search(data, item):
	search_start = 0
	search_end = len(data)
	index = (search_start + search_end) // 2
	while data[index] != item:
		index = (search_start + search_end) // 2
		if item > data[index]:
			search_start = index

		elif item < data[index]:
			search_end = index
	return data[index]


print(binary_search(data_list, random.randint(0, len(data_list)-1)))