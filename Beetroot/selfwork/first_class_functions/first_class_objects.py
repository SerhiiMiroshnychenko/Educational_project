def add_five(x):
    return x + 5


def do_twice(func):
    def result_func(x):
        return func(func(x))
    return result_func


result = do_twice(add_five)

print(result(2))
print(result)
print(type(result))


def adder(x, y):
    return x + y

def stringer(x):
    return str(x)

def func_blander(func1, func2):
    def resulter(x, y):
        return func1(func2(x), func2(y))
    return resulter

super_func = func_blander(adder, stringer)
print(super_func(5, 6))
