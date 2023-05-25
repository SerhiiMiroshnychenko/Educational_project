# Створити декоратор-клас, який буде обмежувати кількість викликів функції,
# яка приймає додатковий параметер
# та виводити порядковий номер виклику функції

class CallCounter:
    def __init__(self, func, limit=10):
        self.func = func
        self.call_count = 0
        self.limit = limit
    def __call__(self, *args, **kwargs):
        if self.call_count < self.limit:
            self.call_count += 1
            print(f"Called {self.func.__name__} for the {self.call_count}th time")
            return self.func(*args, **kwargs)
        else:
            print(f"Limit reached for {self.func.__name__}")
            return None


def set_limit_calls(limit=10):
    def set_limit_wrap(func):
        return CallCounter(func, limit)
    return set_limit_wrap

if __name__ == '__main__':
    @set_limit_calls(limit=1)
    def simple_print():
        print('Hello there!')
    for i in range(10):
        simple_print()
