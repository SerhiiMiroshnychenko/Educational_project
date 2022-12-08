import inspect


def function(a, b):
    """Multiple of two numbers"""
    return a * b


print(inspect.getsource(function))
