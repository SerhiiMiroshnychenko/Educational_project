from functools import wraps


class Star:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(self.n*'*')
            result = fn(*args, **kwargs)
            print(result)
            print(self.n*'*')
            return result
        return wrapper


@Star(5)
def add(a, b):
    return a + b


add(10, 20)