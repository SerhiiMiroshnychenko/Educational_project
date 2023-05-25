"""Дослідимо затрати часу на блок обробки помилок"""
import time
import timeit


def test_time(func):
    """Decorator for calculating the running time of the function."""
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Час роботи функції: {dt} сек.")
        return res
    return wrapper


@test_time
def create_list(start, end, step):
    """The function that generates a list."""
    result = []
    for number in range(start, end, step):
        result.append(round(1/number, 3))
    return result[-10:]


@test_time
def try_create_list(start, end, step):
    """Error checking function that generates a list."""
    result = []
    for number in range(start, end, step):
        try:
            result.append(round(1 / number, 3))
        except ZeroDivisionError as err:
            print(f'\nПомічена помилка: {err.__class__}.')
            return result[-10:]
    return result[-10:]


print(result1 := create_list(10_000_000, 0, -1))
print(result2 := try_create_list(9_999_999, -1, -1))

mycode1 = '''
def create_list(start, end, step):
    result = []
    for number in range(start, end, step):
        result.append(round(1/number, 3))
    return result[-10:]
'''
mycode2 = '''
def try_create_list(start, end, step):
    result = []
    for number in range(start, end, step):
        try:
            result.append(round(1 / number, 3))
        except ZeroDivisionError as err:
            print('Помічена помилка ZeroDivisionError')
            return result[-10:]
    return result[-10:]
'''

mycodes = [mycode1, mycode2]

for code in mycodes:
    times = timeit.repeat(stmt=code,
                          repeat=3,
                          number=10_000_000)
    print(times)
