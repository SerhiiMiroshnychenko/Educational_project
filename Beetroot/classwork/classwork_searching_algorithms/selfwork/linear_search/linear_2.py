## searching function
def search_element(arr, n, element):

	return any(arr[i] == element for i in range(n))


if __name__ == '__main__':
	## initializing the array, length, and element to be searched
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	n = 10
	element_to_be_searched = 6
	# element_to_be_searched = 11

	if search_element(arr, n, element_to_be_searched):
		print(element_to_be_searched, "is found")
	else:
		print(element_to_be_searched, "is not found")