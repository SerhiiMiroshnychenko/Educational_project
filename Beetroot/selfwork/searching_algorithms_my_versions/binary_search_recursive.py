def recursive_binary_search(array, element, start=None, end=None):

    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    if end >= start:

        middle = start + (end - start) // 2

        if array[middle] == element:
            return middle

        elif array[middle] > element:
            return recursive_binary_search(array, element, start, middle-1)

        else:
            return recursive_binary_search(array, element, middle + 1, end)

    else:
        return False


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 60, 70, 80, 900, 1000]
    numbers = 5, 10, 70, 900

    for number in numbers:
        if result := recursive_binary_search(my_list, number):
            print(f'element "{number}" is present at index <{result}>.')
        else:
            print(f'element "{number}" is not present in the array.')
