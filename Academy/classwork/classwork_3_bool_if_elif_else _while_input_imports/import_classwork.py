from own_input import float_input


def f(arg):
    print(arg)


x = float_input('12.3')

if __name__ == '__main__':
    f("We are here")
else:
    print(x, type(x))

if __name__ != '__main__':
    f("We are here")
else:
    print(x, type(x))
