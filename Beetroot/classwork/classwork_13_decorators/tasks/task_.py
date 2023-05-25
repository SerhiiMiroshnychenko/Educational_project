from functools import wraps
from time import perf_counter
import tracemalloc
import inspect

def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        end_time = perf_counter()
        print(f'Викликана функція:\n{inspect.getsource(func)}')
        print(f'Memory usage:{current / 10 ** 5:.6f}',
                f'\nPeak usage:\t{peak / 10 ** 6:.6f}')
        print(f'Time elapsed in seconds {end_time - start_time:.6f}')
        print('-' * 40)
        tracemalloc.stop()

    return wrapper

@measure_performance
def list_maker_1(num):
    """I make list by append"""
    l = []
    for i in range(num):
        l.append(i)
    return l

@measure_performance
def list_maker_2(num):
    """I make list by range"""
    return list(range(num))

@measure_performance
def list_maker_3(num):
    """I make list comprehension"""
    return [i for i in range(num)]

@measure_performance
def list_maker_4(num):
    """I make list by concatenation"""
    my_list = []
    for item in range(num):
        my_list += [item]

if __name__ == '__main__':
    for i in range(3):
        print(f'Attempt {i}')
        list_maker_1(1000000)
        list_maker_2(1000000)
        list_maker_3(1000000)
        list_maker_4(1000000)
        print('=' * 40)
