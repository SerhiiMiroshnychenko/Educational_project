# Прочитати про Fibonacci search та імплементуйте його за допомогою Python.

def fibonacci_search(elements, element):
    """
    The function of fibonacci search
    :param elements: the sorted collection of elements
    :param element: the element we want to search for in the collection
    :return: the index of the element found or False if no such element
    """

    length = len(elements)
    eliminated = -1
    fibonacci_2 = 0
    fibonacci_1 = 1
    fibonacci = fibonacci_1 + fibonacci_2

    while fibonacci < length:
        fibonacci_1, fibonacci_2 = fibonacci, fibonacci_1
        fibonacci = fibonacci_1 + fibonacci_2

    while fibonacci > 1:
        current = min(eliminated + fibonacci_2, length - 1)
        if elements[current] == element:
            return current

        elif elements[current] > element:
            fibonacci = fibonacci_2
            fibonacci_1 = fibonacci_1 - fibonacci_2
            fibonacci_2 = fibonacci_2 - fibonacci_1
        else:
            fibonacci = fibonacci_1
            fibonacci_1 = fibonacci_2
            fibonacci_2 = fibonacci - fibonacci_1
            eliminated = current
    return False

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 60, 70, 80, 900, 1000]
    numbers = 5, 10, 70, 900

    for number in numbers:
        if result := fibonacci_search(my_list, number):
            print(f'element "{number}" is present at index <{result}>.')
        else:
            print(f'element "{number}" is not present in the elements.')
