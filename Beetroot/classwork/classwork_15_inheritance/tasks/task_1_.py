from math import tan, pi
from random import randint, choice

class Figure:
    def __init__(self, number_of_sides, side_length):
        self.number_of_sides = number_of_sides
        self.side_length = side_length
        self.angle =float(pi / float(number_of_sides))
        self.apotema = (float(side_length) / 2) / tan(self.angle)

    def square(self):
        return round((self.number_of_sides * self.side_length * self.apotema) / 2, 2)


f = Figure(4, 4)
print(f.square())

class TreeAngle(Figure):
    def __init__(self, side_length):
        super().__init__( 3,  side_length)



class FourAngle(Figure):
    def __init__(self, side_length):
        super().__init__(4,  side_length)



class CalculatorFigure:
    def __init__(self):
        self.figure_list = [Figure, TreeAngle, FourAngle]

    def generate(self, figure_number):
        for _ in range(figure_number):
            figure = choice(self.figure_list)
            length = randint(2, 11)
            if figure == Figure:
                number = randint(3, 10)
                print(f'{figure.__name__} class with parameters {(number, length)}:'
                      f' {figure(number, length).square()}')
            else:
                print(f'{figure.__name__} class with parameters {length}:'
                      f' {figure(length).square()}')

if __name__ == '__main__':
    test = CalculatorFigure()
    test.generate(10)

