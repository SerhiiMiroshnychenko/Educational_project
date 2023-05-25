def sentinel_search(array, element):

    last = array[len(array) - 1]

    array[len(array) - 1] = element
    index = 0

    while array[index] != element:
        index += 1

    array[len(array) - 1] = last

    if index < len(array ) - 1 or array[len(array) - 1] == element:
        print(f'"{element}" is present at index <{index}>.')
    else:
        print("Element Not found")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 60, 70, 80, 900, 1000]
    numbers = 5, 10, 70, 900

    for number in numbers:
        sentinel_search(my_list, number)
