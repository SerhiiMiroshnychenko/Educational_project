from math import tan, pi
from random import randint, choice

class Figure:
    def __init__(self, number, line_length):
        self.number = number
        self.line_length = line_length
        self.angle = float(pi / float(number))
        self.apotema = (float(line_length) / 2) / tan(self.angle)

    def square(self):
        return round((self.number * self.line_length * self.apotema) / 2, 2)

class ThreeAngle(Figure):
    def __init__(self, line_length):
        super().__init__(3, line_length)

class FourAngler(Figure):
    def __init__(self, line_length):
        super().__init__(4, line_length)


class Calculator:
    """
        int([x]) -> integer
        int(x, base=10) -> integer

        Convert a number or string to an integer, or return 0 if no arguments
        are given.  If x is a number, return x.__int__().  For floating point
        numbers, this truncates towards zero.

        If x is not a number or if base is given, then x must be a string,
        bytes, or bytearray instance representing an integer literal in the
        given base.  The literal can be preceded by '+' or '-' and be surrounded
        by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
        Base 0 means to interpret the base from the string as an integer literal.
        >>> int('0b100', base=0)
        4
        """
    def __init__(self):
        self.figure_list = [Figure, ThreeAngle, FourAngler]
    def generate(self, figure_number):
        for _ in range(figure_number):
            figure = choice(self.figure_list)
            length = randint(2, 11)
            if figure is Figure:
                number = randint(3, 10)
                print(f'{figure.__name__} class with parameters {(number, length)}: {figure(number, length).square()}')
            else:
                print(f'{figure.__name__} class with parameters {length}: {figure(length).square()}')


if __name__ == '__main__':
    Calculator().generate(10)