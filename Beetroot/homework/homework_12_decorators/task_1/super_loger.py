def super_logger(func):
    """Print the function arguments and return result"""
    import functools
    import inspect
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ar = [repr(a) for a in args]
        kw = [f"{k}={v!r}" for k, v in kwargs.items()]
        print(f'Викликана функція: {func.__name__}({", ".join(ar + kw)})')
        print(f"Функція {func.__name__!r} повертає {func(*args, **kwargs)!r}")
        print(f'Лістинг коду функції:\n{inspect.getsource(func)}')
        return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    @super_logger
    def add(x, y):
        return x + y
    @super_logger
    def square_all(*args):
        return [arg ** 2 for arg in args]

    @super_logger
    def simpler():
        return 'I am simpler!'

    @super_logger
    def str_all(**kwargs):
        return {key: str(value)*2 for key, value in kwargs.items()}

    @super_logger
    def sum_all(*args, **kwargs):
        sum1 = sum(args)
        sum2 = sum(kwargs.values())
        return sum1 + sum2


    @super_logger
    def approximate_e(terms=18):
        import math
        return sum(1 / math.factorial(n) for n in range(terms))


    res_add = add(5, 6)
    res_square = square_all(1, 2, 3, 4)
    res_simpler = simpler()
    res_str = str_all(i=10, j=20)
    res_sum = sum_all(1, 2, 3, 4, i=5, j=6)
    res_approximate = approximate_e(5)