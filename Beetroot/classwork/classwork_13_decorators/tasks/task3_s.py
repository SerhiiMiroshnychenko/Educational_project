# Створити декоратор-клас, який буде обмежувати кількість викликів функції, яка приймає додатковий параметер
# та виводити порядковий номер виклику


class _LimitCalls:

    def __init__(self, func, max_calls=10):
        self.func = func
        self.calls = 0
        self.max_calls = max_calls

    def __call__(self, *args, **kwargs):
        self.calls += 1
        if self.calls <= self.max_calls:
            print(f"<{self.func.__name__}> executed <{self.calls}> times.")
            return self.func(*args, **kwargs)
        print(f"Too much calls to function <{self.func.__name__}>. Only {self.max_calls} allowed.")


def limit_calls(max_calls=10):
    def limit_calls_dec(func):
        return _LimitCalls(func, max_calls)

    return limit_calls_dec


@limit_calls(max_calls=3)
def main():
    print("call me")


if __name__ == "__main__":
    main()
    main()
    main()
    main()
    main()
    main()
    main()
