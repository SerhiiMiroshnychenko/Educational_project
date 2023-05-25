"""Примітка: декоратор @timer чудово підходить, якщо ви просто хочете
отримати уявлення про час виконання ваших функцій. Якщо ви хочете зробити
більш точні вимірювання коду, вам слід замість цього розглянути timeit модуль
у стандартній бібліотеці. Він тимчасово вимикає збирання сміття та запускає
кілька випробувань, щоб усунути шум під час швидких викликів функцій."""
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

if __name__ == "__main__":
    @timer
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])

    waste_some_time(1)
    waste_some_time(999)
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
