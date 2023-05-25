def timer(func):
    """Декоратор для вимірювання часу роботи функцій"""
    import time
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Час роботи функції {func.__name__}'
              f' склав: {(end - start)} сек')
        return result
    return wrapper

if __name__ == '__main__':
    @timer
    def power_list(number_elements: int, power: int) -> list:
        """Створення списку чисел у степені"""
        result = []
        for i in range(number_elements):
            result.append(power ** i)
        return result

    print(power_list(10000, 2)[:5])
    print(power_list(10000, 3)[:5])
    print(power_list(10000, 10)[:5])
    @timer
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(10000)])

    waste_some_time(1)
    waste_some_time(999)
