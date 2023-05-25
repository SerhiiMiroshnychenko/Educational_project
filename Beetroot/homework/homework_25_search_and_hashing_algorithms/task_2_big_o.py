import matplotlib.pyplot as plt  # type: ignore
from random import randint


def iterative_binary_search(sorted_array, element):
    """
    Modified to calculate the Big O
    """

    big_o_counter = 0 # Big O

    counter = 0
    start = 0
    end = len(sorted_array) - 1
    while counter < len(sorted_array):
        big_o_counter += 1 # Big O
        middle = (start + end) // 2
        if sorted_array[middle] == element:
            return big_o_counter # Big O
        elif sorted_array[middle] < element:
            start = middle + 1
        else:
            end = middle - 1
        counter += 1
    return big_o_counter


def recursive_binary_search(elements, element, start=None, end=None, big_o_counter=None):
    """
    Modified to calculate the Big O
    """

    if big_o_counter is None:
        big_o_counter = 0 # Big O
    if start is None:
        start = 0
    if end is None:
        end = len(elements) - 1

    big_o_counter += 1

    if end >= start:
        middle = start + (end - start) // 2
        if elements[middle] == element:
            return big_o_counter # Big O
        elif elements[middle] > element:
            return recursive_binary_search(elements, element, start, middle-1, big_o_counter) # Big O
        else:
            return recursive_binary_search(elements, element, middle + 1, end, big_o_counter) # Big O
    else:
        return big_o_counter


def fibonacci_search(elements, element):
    """
    Modified to calculate the Big O
    """

    big_o_counter = 0 # Big O

    length = len(elements)
    eliminated = -1
    fibonacci_2 = 0
    fibonacci_1 = 1
    fibonacci = fibonacci_1 + fibonacci_2
    while fibonacci < length:
        fibonacci_1, fibonacci_2 = fibonacci, fibonacci_1
        fibonacci = fibonacci_1 + fibonacci_2
    while fibonacci > 1:

        big_o_counter += 1 # Big O

        current = min(eliminated + fibonacci_2, length - 1)
        if elements[current] == element:
            return big_o_counter # Big O
        elif elements[current] > element:
            fibonacci = fibonacci_2
            fibonacci_1 = fibonacci_1 - fibonacci_2
            fibonacci_2 = fibonacci_2 - fibonacci_1
        else:
            fibonacci = fibonacci_1
            fibonacci_1 = fibonacci_2
            fibonacci_2 = fibonacci - fibonacci_1
            eliminated = current
    return big_o_counter


if __name__ == "__main__":
    itera = []
    recurs = []
    fibo = []

    for number in (lambda x: x // 10, lambda x: x // 9, lambda x: x // 8, lambda x: x // 7, lambda x: x // 6,
                   lambda x: x // 5, lambda x: x // 4, lambda x: x // 3, lambda x: x // 2, lambda x: int(x * 0.9)):
        itera = [iterative_binary_search(list(range(length)), number(length)) for length in range(10, 10000, 2)]
        recurs = [recursive_binary_search(list(range(length)), number(length)) for length in range(10, 10000, 2)]
        fibo = [fibonacci_search(list(range(length)), number(length)) for length in range(10, 10000, 2)]

        fig, ax = plt.subplots()

        plt.title(f'For number "{number(10000)}" from 10000 items.')
        ax.plot(list(range(10, 10000, 2)), fibo, color='green', linewidth=10)
        ax.plot(list(range(10, 10000, 2)), itera, color='blue', linewidth=20)
        ax.plot(list(range(10, 10000, 2)), recurs, color='red', linewidth=2)

        plt.show()

