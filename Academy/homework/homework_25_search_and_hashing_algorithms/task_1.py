# Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

def recursive_binary_search(elements, element, start=None, end=None):
    """
    The function of recursive binary search

    :param elements: the sorted collection of elements
    :param element: the element we want to search for in the collection
    :param start: search starting point
    :param end: the end point of the search
    :return: the index of the element found or False if no such element
    """

    if start is None:
        start = 0
    if end is None:
        end = len(elements) - 1

    if end >= start:

        middle = start + (end - start) // 2

        if elements[middle] == element:
            return middle

        elif elements[middle] > element:
            return recursive_binary_search(elements, element, start, middle-1)

        else:
            return recursive_binary_search(elements, element, middle + 1, end)

    else:
        return False


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 60, 70, 80, 900, 1000]
    numbers = 5, 10, 70, 900

    for number in numbers:
        if result := recursive_binary_search(my_list, number):
            print(f'element "{number}" is present at index <{result}>.')
        else:
            print(f'element "{number}" is not present in the elements.')
