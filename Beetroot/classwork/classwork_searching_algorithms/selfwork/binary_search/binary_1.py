## searching function
def search_element(sorted_arr, n, element):

	## array index for iteration
	i = 0

	## variables to track the search area
	## initializing them with start and end indexes
	start = 0
	end = n - 1

	## iterating over the array
	while i < n:
		## getting the index of the middle element
		middle = (start + end) // 2

		## checking the middle element with required element
		if sorted_arr[middle] == element:
			## returning True since the element is in the array
			return True
		elif sorted_arr[middle] < element:
			## moving the start index of the search area to right
			start = middle + 1
		else:
			## moving the end index of the search area to left
			end = middle - 1
		i += 1
	return False


if __name__ == '__main__':
	## initializing the array, length, and element to be searched
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	n = 10
	element_to_be_searched = 9
	# element_to_be_searched = 11

	if search_element(arr, n, element_to_be_searched):
		print(element_to_be_searched, "is found")
	else:
		print(element_to_be_searched, "is not found")