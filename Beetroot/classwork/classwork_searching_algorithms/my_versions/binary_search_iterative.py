def iterative_binary_search(sorted_array, element):

    counter = 0
    start = 0
    end = len(sorted_array) - 1

    while counter < len(sorted_array):
        middle = (start + end) // 2
        if sorted_array[middle] == element:
            return middle
        elif sorted_array[middle] < element:
            start = middle + 1
        else:
            end = middle - 1
        counter += 1
    return False


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 60, 70, 80, 900, 1000]
    numbers = 5, 10, 70, 900

    for number in numbers:
        if result := iterative_binary_search(my_list, number):
            print(f'element "{number}" is present at index <{result}>.')
        else:
            print(f'element "{number}" is not present in the array.')
