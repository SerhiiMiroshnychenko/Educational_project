# Створити власний клас будь якого реального об'єкту та визначити для нього операцію +
# def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1, m2)
#         return s3
class FractionalNumbers:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        up = self.numerator * other.denominator + self.denominator * other.numerator
        down = self.denominator * other.denominator
        return FractionalNumbers(up, down)

    def __str__(self):
        print(self.numerator/self.denominator)
        # return f'{self.numerator}/{self.denominator}'



first_number = FractionalNumbers(1, 2)
second_number = FractionalNumbers(3, 4)

# first_number.__add__(second_number)
result = first_number + second_number + second_number  # + equal .__add__()
# first_number.__add__(second_number).__add__(second_number)
print(result)
print(result.numerator)
print(result.denominator)