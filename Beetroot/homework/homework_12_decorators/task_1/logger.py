# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
"""For example:
 "add called with 4, 5"
```
def logger(func):
    pass
@logger
def add(x, y):
    return x + y
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]"""
def logger(func):
    """Show a function with arguments passed to it"""
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        a, k = args, kwargs
        if a and k:
            ak = f'{a} та {k}'
        elif not a and not k:
            ak = 'відсутні'
        elif not k:
            ak = f'{a[0]}' if len(a) == 1 else f'{a}'
        else:
            ak = f'{k}'
        res = func(*args, **kwargs)
        print(f'Функція: {name}()\nПередані аргументи: {ak}')
        return res

    return wrapper


if __name__ == '__main__':
    @logger
    def add(x, y):
        return x + y
    @logger
    def square_all(*args):
        return [arg ** 2 for arg in args]

    @logger
    def simpler():
        return 'I am simpler!'

    @logger
    def str_all(**kwargs):
        return {key: str(value)*2 for key, value in kwargs.items()}

    @logger
    def sum_all(*args, **kwargs):
        sum1 = sum(args)
        sum2 = sum(kwargs.values())
        return sum1 + sum2
    @logger
    def approximate_e(terms=18):
        import math
        math.factorial = logger(math.factorial)
        return sum(1 / math.factorial(n) for n in range(terms))


    res_add = add(5, 6)
    print(f'Результат виконання: {res_add}\n')
    res_square = square_all(1, 2, 3, 4)
    print(f'Результат виконання: {res_square}\n')
    res_simpler = simpler()
    print(f'Результат виконання: {res_simpler}\n')
    res_str = str_all(i=10, j=20)
    print(f'Результат виконання: {res_str}\n')
    res_sum = sum_all(1, 2, 3, 4, i=5, j=6)
    print(f'Результат виконання: {res_sum}\n')
    res_approx = approximate_e(5)
    print(f'Результат виконання: {res_sum}\n')

