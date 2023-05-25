# Task 3

# One way to improve the quicksort is to use an insertion sort on lists
# that are small (call it the “partition limit”). Why does this
# make sense? Re-implement the quicksort and use it to sort a random list
# of integers. Perform  analysis using different list sizes for the partition limit.


def measure_performance(func):
    """Measure performance of a function"""

    from functools import wraps
    import tracemalloc
    from time import perf_counter
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10 ** 6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10 ** 6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(func(*args, **kwargs))
        print(f'{"-" * 40}\n')
        tracemalloc.stop()

    return wrapper


@measure_performance
def quick_sorting(elements, partition_limit):
    """Quick sort with partition limit and using insertion sort"""
    elements = quick_sort(elements, partition_limit)
    return elements


def quick_sort(elements, partition_limit):
    """
    The function of quick sort
    :param elements: unordered collection of numbers
    :param partition_limit: the limit length less than which the division of the sequence stops
    :return: ordered collection of numbers or collection for sorting by insertion sort
    """
    import random
    if len(elements) > partition_limit:
        x = elements[random.randint(0, len(elements)-1)]
        low = [u for u in elements if u < x]
        eq = [u for u in elements if u == x]
        hi = [u for u in elements if u > x]
        elements = quick_sort(low, partition_limit) + eq\
                    + quick_sort(hi, partition_limit)
    else:
        elements = insertion_sort(elements)
    return elements


def insertion_sort(items):
    """
    The insertion sort function
    :param items: unordered collection of numbers
    :return: ordered collection of numbers
    """
    for index in range(1, len(items)):
        current_value = items[index]
        position = index
        while position > 0 and items[position - 1] > current_value:
            items[position] = items[position - 1]
            position = position - 1
        items[position] = current_value
    return items


if __name__ == "__main__":
    my_list = [10, 2, 7, 4, 9, 5, 6, 1, 3, 0, 8]
    for limit in range(1, len(my_list)+1):
        print(f'For partition limit == {limit}:')
        sample = my_list[:]
        quick_sorting(my_list, limit)
