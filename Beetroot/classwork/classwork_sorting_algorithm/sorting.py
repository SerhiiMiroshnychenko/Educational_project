import random
from functools import wraps
import tracemalloc
from time import perf_counter


# The Bubble sort
# The Selection sort
# The Insertion sort
# The Shell sort
# The Merge sort
# The Quick sort

def measure_performance(func):
    """Measure performance of a function"""

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
        print(args[0])
        print(f'{"-" * 40}')
        tracemalloc.stop()

    return wrapper


@measure_performance
def bubble_sort(array):
    for pass_num in range(len(array) - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


@measure_performance
def selection_sort(array):
    for fill_slot in range(len(array) - 1, 0, -1):
        position_min = 0
        for location in range(1, fill_slot + 1):
            if array[location] > array[position_min]:
                position_min = location

        array[fill_slot], array[position_min] = array[position_min], array[fill_slot]


@measure_performance
def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = current_value


@measure_performance
def shell_sort(array):
    sublist_count = len(array) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(array, start_position, sublist_count)

        sublist_count = sublist_count // 2


def gap_insertion_sort(array, start, gap):
    for i in range(start + gap, len(array), gap):
        current_value = array[i]
        position = i

        while position >= gap and array[position - gap] > current_value:
            array[position] = array[position - gap]
            position = position - gap

        array[position] = current_value


@measure_performance
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1


@measure_performance
def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, first, last):
    if first < last:
        split_point = partition(array, first, last)

        quick_sort_helper(array, first, split_point - 1)
        quick_sort_helper(array, split_point + 1, last)


def partition(array, first, last):
    pivot_value = array[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            array[left_mark], array[right_mark] = array[right_mark], array[left_mark]

    array[first], array[right_mark] = array[right_mark], array[first]

    return right_mark


@measure_performance
def my_sort(array):
    return array.sort()


if __name__ == "__main__":
    test_list = [random.randint(1, 100) for _ in range(23)]
    for func in (bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort, quick_sort, my_sort):
        copy_test_list = test_list[:]
        func(copy_test_list)
