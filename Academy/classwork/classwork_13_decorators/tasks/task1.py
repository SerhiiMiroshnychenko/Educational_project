# Створити декоратор який записує час та дату виконання функції.
# Вивід інформації має містити назву функції
# та дату і час у форматі hh:mm dd-mm-yy. Використати бібліотеку datetime.
def super_logger(func):
    """Print the function arguments and return result"""
    import functools
    import datetime
    import pytz
    import inspect
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        date = datetime.datetime.now(tz=pytz.timezone('Europe/Kyiv'))
        now = date.strftime("%d/%m/%Y")
        print(f'Викликана функція: {func.__name__}')
        print(f'Дата виклику: {now}')
        print(f'Лістинг коду функції:\n{inspect.getsource(func)}')
        return func
    return wrapper

@super_logger
def simple_print():
    print('Hello there!')

simple_print()
