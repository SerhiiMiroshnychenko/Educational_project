# Визначте складність алгоритму та порівняйте його з бінарним пошуком.
import timeit


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


def recursive_binary_search(elements, element, start=None, end=None):

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


def fibonacci_search(elements, element):

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
    numbers = range(0, 2001, 1000)
    iterative_binary_time: list = []
    recursive_binary_time: list = []
    fibonacci_time: list = []
    count_time: list = []
    index_time: list = []
    remove_time: list = []
    in_time: list = []

    for number in numbers:

        iterative_binary_timer = timeit.timeit(
            stmt=f"iterative_binary_search(list(range(200000)), {number})",
            number=100,
            setup="from __main__ import iterative_binary_search"
        )
        iterative_binary_time.append(iterative_binary_timer)

        recursive_binary_timer = timeit.timeit(
            stmt=f"recursive_binary_search(list(range(200000)), {number})",
            number=100,
            setup="from __main__ import recursive_binary_search"
        )
        recursive_binary_time.append(recursive_binary_timer)

        fibonacci_timer = timeit.timeit(
            stmt=f"fibonacci_search(list(range(200000)), {number})",
            number=100,
            setup="from __main__ import fibonacci_search"
        )
        fibonacci_time.append(fibonacci_timer)

        count_timer = timeit.timeit(
            stmt=f"list(range(200000)).count({number})",
            number=100,
        )
        count_time.append(count_timer)

        index_timer = timeit.timeit(
            stmt=f"list(range(200000)).index({number})",
            number=100,
        )
        index_time.append(index_timer)

        remove_timer = timeit.timeit(
            stmt=f"list(range(200000)).remove({number})",
            number=100,
        )
        remove_time.append(remove_timer)

        in_timer = timeit.timeit(
            stmt=f"{number} in list(range(200000))",
            number=100,
        )
        in_time.append(in_timer)

    print(f'Середня швидкість "iterative binary search": {sum(iterative_binary_time)/len(iterative_binary_time)}')
    print(f'Середня швидкість "recursive binary search": {sum(recursive_binary_time)/len(recursive_binary_time)}')
    print(f'Середня швидкість "fibonacci search": {sum(fibonacci_time)/len(fibonacci_time)}')
    print(f'Середня швидкість "count for list": {sum(count_time)/len(count_time)}')
    print(f'Середня швидкість "index for list": {sum(index_time)/len(index_time)}')
    print(f'Середня швидкість "remove for list": {sum(remove_time)/len(remove_time)}')
    print(f'Середня швидкість "in for list": {sum(in_time)/len(in_time)}')
