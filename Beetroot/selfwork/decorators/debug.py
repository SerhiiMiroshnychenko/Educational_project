"""@debug декоратор друкуватиме аргументи, з якими викликається функція, а також її повертане значення кожного разу, коли функція викликається:"""
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

"""Підпис створюється шляхом об’єднання рядкових представлень усіх аргументів. Номери в наведеному нижче списку відповідають пронумерованим коментарям у коді:

Створіть список позиційних аргументів. Використовуйте repr()для отримання гарного рядка, що представляє кожен аргумент.
Створіть список аргументів ключових слів. F - рядок форматує кожен аргумент як key=value де !r специфікатор означає, що repr()використовується для представлення значення.
Списки позиційних аргументів і аргументів ключових слів об'єднані в один рядок підпису, кожен аргумент розділений комою.
Повернене значення друкується після виконання функції."""

if __name__ == '__main__':
    @debug
    def make_greeting(name, age=None):
        if age is None:
            return f"Howdy {name}!"
        else:
            return f"Whoa {name}! {age} already, you are growing up!"

    make_greeting("Benjamin")
    make_greeting("Richard", age=112)
    make_greeting(name="Dorrisile", age=116)

    def approximate_e(terms=18):
        import math
        # Apply a decorator to a standard library function
        math.factorial = debug(math.factorial)
        return sum(1 / math.factorial(n) for n in range(terms))

    approximate_e(5)