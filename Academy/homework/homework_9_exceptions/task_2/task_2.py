# Task 2
# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given
# by the input function were not numbers, and if value b was zero (cannot divide by zero).

def calculation_function():
    """The function that returns the value of squared first number divided by second number"""
    try:
        a, b = input('Введіть два числа через пробіл: ').split(' ')
        a = float(a) if '.' in a else int(a)
        b = float(b) if '.' in b else int(b)
        return round(a**2 / b, 3)
    except Exception as err:
        print(f'\nПомічена помилка: {err.__class__}.')
        print('Причина:', err)
        return 'Розрахунок не відбувся через некоректно введені данні.'


class NoNumbersInputError(ValueError):
    def __init__(self, x, y):
        super(NoNumbersInputError, self).__init__()
        if x == y == '':
            self.msg = 'Hey! Enter first and second numbers!'
        elif x == '':
            self.msg = 'Hey! Enter first number!'
        elif y == '':
            self.msg = 'Hey! Enter second number!'

    def __str__(self):
        return self.msg


class NotNumbersInputError(BaseException):
    def __init__(self, x, y):
        super(NotNumbersInputError, self).__init__()
        if not (x.isnumeric() or y.isnumeric()):
            self.msg = f'Hey! Enter only numbers here, not "{x}" and "{y}"!'
        elif not x.isnumeric():
            self.msg = f'Hey! The first number cannot be "{x}"! Enter only numbers here!'
        elif not y.isnumeric():
            self.msg = f'Hey! The second number cannot be "{y}"! Enter only numbers here!'

    def __str__(self):
        return self.msg


def calculation_function_v2():
    """The function (version 2) that returns the value of squared first number divided by second number"""
    try:
        a = input('Введіть перше число: ')
        b = input('Введіть друге число: ')
        if not (a and b):
            raise NoNumbersInputError(a, b)
        if not (a.isnumeric() and b.isnumeric()):
            raise NotNumbersInputError(a, b)
    except (NoNumbersInputError, NotNumbersInputError) as err:
        print(f'\nПомічена помилка: {err.__class__}.')
        print('Причина:', err)
        return 'Розрахунок не відбувся через некоректно введені данні.'
    try:
        a = float(a) if '.' in a else int(a)
        b = float(b) if '.' in b else int(b)
        assert b != 0, 'Hey! No more division by zero!'
        return round(a**2 / b, 3)
    except AssertionError as err:
        print(f'\nПомічена помилка: {err.__class__}.')
        print('Причина:', err)
        return 'Розрахунок не відбувся через некоректно введені данні.'


if __name__ == '__main__':
    print(calculation_function())
    print(calculation_function_v2())
