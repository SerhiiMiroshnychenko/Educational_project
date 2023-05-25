from dataclasses import dataclass

@dataclass
class Fraction:
    numerator: int = 1
    denominator: int = 1

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

if __name__ == '__main__':
    f = Fraction(1, 2)
    print(f)
