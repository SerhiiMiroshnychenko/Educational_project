from functools import wraps
from time import perf_counter
import tracemalloc


def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t{current / 10 ** 6:.6f}',
              f'Peak usage:\t{peak / 10 ** 6:.6f}')
        print(f'Time elapsed in seconds {finish_time - start_time:.6f}')
        print('-' * 40)
        tracemalloc.stop()
    return wrapper


@measure_performance
def make_list1():
    """Range"""
    my_list = list(range(1000000))


@measure_performance
def make_list2():
    """List comprehension"""
    my_list = [l for l in range(1000000)]


@measure_performance
def make_list3():
    """Append"""
    my_list = []
    for item in range(1000000):
        my_list.append(item)


@measure_performance
def make_list4():
    """Concatenation"""
    my_list = []
    for item in range(1000000):
        my_list += [item]


for i in range(3):
    print(f'Attempt {i}')
    make_list1()
    make_list2()
    make_list3()
    make_list4()
    print('=' * 40)