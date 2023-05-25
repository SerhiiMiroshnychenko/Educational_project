"""Fraction
Створіть клас Fraction, який буде представляти
всю базову арифметичну логіку для дробів (+, -, /, *)
з належною перевіркою й обробкою помилок.
Потрібно додати магічні методи для математичних операцій
та операції порівняння між об'єктами класу Fraction

class Fraction:
    pass

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)"""

class Fraction:

    def __new__(cls, numerator, denominator):
        if isinstance(numerator, int) and isinstance(denominator, int) and denominator != 0:
            return super().__new__(cls)
        try:
            raise TypeError('Invalid data type! Use only integer numbers.\nDenominator can not be zero.')
        except TypeError as e:
            return f'{e.__class__} has been detected.\nThe reason: {e}'

    def __init__(self, numerator: int, denominator: int):
        # Block 1
        self.positive = numerator * denominator >= 0
        self.numerator = abs(numerator)
        self.denominator = abs(denominator)

         # Block 2
        n, d = self.numerator, self.denominator
        if n < d:
            n, d = d, n
        while d:
            n, d = d, n % d

        # Block 3
        self.numerator //= n
        self.denominator //= n

        # Block 4
        self.integer = self.numerator // self.denominator
        self.numerator %= self.denominator

        # Block 5
        self.integer = self.integer if self.positive else - self.integer

        # Block 6
        if not self.integer and not self.positive:
            self.numerator = - self.numerator

    def __float__(self):
        p = 1 if self.positive else -1
        return (
            p * round((abs(self.integer) * self.denominator + self.numerator) / self.denominator, 3)
            if self.integer else p * round((abs(self.numerator) / self.denominator), 3))

    def integer_conversion(self, other):
        if self.integer:
            p = 1 if self.positive else -1
            self.numerator = p * (abs(self.integer) * self.denominator + self.numerator)

        if other.integer:
            o = 1 if other.positive else -1
            other.numerator = o * (abs(other.integer) * other.denominator + other.numerator)

        return self.numerator, other.numerator

    def __add__(self, other):

        other = self.check_other(other)

        self.numerator, other.numerator = self.integer_conversion(other)

        up = self.numerator * other.denominator + self.denominator * other.numerator
        down = self.denominator * other.denominator

        return Fraction(up, down)

    def __radd__(self, other):

        # other.__add__(self) -> Чому не працює?
        other = self.check_other(other)

        self.numerator, other.numerator = self.integer_conversion(other)

        up = self.numerator * other.denominator + self.denominator * other.numerator
        down = self.denominator * other.denominator

        return Fraction(up, down)

    def __sub__(self, other):

        other = self.check_other(other)
        self.numerator, other.numerator = self.integer_conversion(other)

        up = self.numerator * other.denominator - self.denominator * other.numerator
        down = self.denominator * other.denominator

        return Fraction(up, down)

    def __rsub__(self, other):

        other = self.check_other(other)

        self.numerator, other.numerator = self.integer_conversion(other)

        up = self.denominator * other.numerator - self.numerator * other.denominator
        down = self.denominator * other.denominator

        return Fraction(up, down)

    def __mul__(self, other):

        other = self.check_other(other)

        self.numerator, other.numerator = self.integer_conversion(other)

        up =  self.numerator * other.numerator
        down = self.denominator * other.denominator

        return Fraction(up, down)

    def __rmul__(self, other):

        other = self.check_other(other)

        self.numerator, other.numerator = self.integer_conversion(other)

        up =  self.numerator * other.numerator
        down = self.denominator * other.denominator

        return Fraction(up, down)

    def __truediv__(self, other):

        other = self.check_other(other)

        self.numerator, other.numerator = self.integer_conversion(other)

        up =  self.numerator * other.denominator
        down = self.denominator * other.numerator

        return Fraction(up, down)

    def __rtruediv__(self, other):

        other = self.check_other(other)

        self.numerator, other.numerator = self.integer_conversion(other)

        up =  self.numerator * other.denominator
        down = self.denominator * other.numerator

        return Fraction(up, down)

    def __eq__(self, other):

        other = self.check_other(other)
        self.numerator, other.numerator = self.integer_conversion(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self,other):

        other = self.check_other(other)
        self.numerator, other.numerator = self.integer_conversion(other)
        return self.numerator != other.numerator and self.denominator != other.denominator

    def __lt__(self,other):
        result = self - other
        return float(result) < 0

    def __gt__(self, other):
        return float(self - other) > 0

    def __le__(self,other):
        return self == other or self < other

    def __ge__(self,other):
        return self == other or self > other

    def __neg__(self):
        if self.integer:
            numerator = -1 * abs(self.integer) * self.denominator + self.numerator
        else:
            numerator = -1 * self.numerator
        denominator = self.denominator
        return Fraction(numerator, denominator)

    def check_other(self, other):
        other_type = type(other)
        if other_type != type(self):
            other = Fraction.fractionating(other)
        return other

    @staticmethod
    def fractionating(number):

        if isinstance(number, float):
            up = number * 10
            down = 10
            while up != int(up):
                up *= 10
                down *= 10
            up = int(up)
            down = int(down)
            return Fraction(up, down)

        if isinstance(number, int):
            up = number
            down = 1
            return Fraction(up, down)

    def __str__(self):
        if self.integer and self.numerator:
            return f'{self.integer}x({self.numerator}/{self.denominator})'
        elif self.integer:
            return f'{self.integer}'
        elif self.numerator:
            return f'{self.numerator}/{self.denominator}'
        else:
            return f'{self.numerator}'

    def __repr__(self):
        return f'Fractional number = {self}\nInteger part = {self.integer}\n' \
               f'Numerator = {self.numerator}\nDenominator = {self.denominator}'
