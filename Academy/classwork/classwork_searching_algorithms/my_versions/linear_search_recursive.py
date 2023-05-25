def recursive_linear_search(array, element, size=None):

    if size is None:
        size = len(array)

    if size == 0:
        return False

    elif array[size - 1] == element:
        return size - 1
    else:
        return recursive_linear_search(array, element, size - 1)

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 60, 70, 80, 900, 1000]
    numbers = 5, 10, 70, 900

    for number in numbers:
        if result := recursive_linear_search(my_list, number):
            print(f'element "{number}" is present at index <{result}>.')
        else:
            print(f'element "{number}" is not present in the array.')
