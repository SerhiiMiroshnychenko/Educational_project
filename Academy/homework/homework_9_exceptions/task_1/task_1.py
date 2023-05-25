# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?
import sys


def oops():
    """The function that raise IndexError"""
    raise IndexError('індекс послідовності виходить за межі діапазону.')


def oops_key():
    """The function that raise KeyError"""
    raise KeyError('ключ не знайдено у множині існуючих ключів.')


def run_function(func):
    """The function to run functions and handle IndexError & KeyError"""
    try:
        func()
    except (IndexError, KeyError) as err:
        f_name = f'{func}'.split(' ')
        print(f'\nПри виклику функції <{f_name[1]}> помічена помилка: {err.__class__}.')
        print('Причина:', sys.exc_info()[1])


def run_any_function(func):
    """The function to run any functions and handle any errors"""
    try:
        func()
    except Exception as err:
        f_name = f'{func}'.split(' ')
        print(f'\nПри виклику функції <{f_name[1]}> помічена помилка: {err.__class__}.')
        print('Причина:', sys.exc_info()[1])


if __name__ == '__main__':
    run_function(oops)
    run_function(oops_key)
    run_any_function(oops)
    run_any_function(oops_key)
