def iterative_linear_search(array, element):

    return next((i for i in range(len(array)) if (array[i] == element)), False)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 60, 70, 80, 900, 1000]
    numbers = 5, 10, 70, 900

    for number in numbers:
        if result := iterative_linear_search(my_list, number):
            print(f'element "{number}" is present at index <{result}>.')
        else:
            print(f'element "{number}" is not present in the array.')
