def f(value):
    while True:
        value = (yield value)


a = f(10)
print(next(a))
print(next(a))
print(a.send(20))