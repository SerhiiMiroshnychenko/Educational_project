def add_5(x):
    return x + 5

def power_2(x):
    return x**2

def show_function_result(func):
    name = func.__name__
    def shower(x):
        return f'Результат роботи функції {func.__name__}({x}) = {func(x)}'
    return shower

plus_5 = show_function_result(add_5)
pow_2 = show_function_result(power_2)

print(plus_5(10))
print(pow_2(10))
