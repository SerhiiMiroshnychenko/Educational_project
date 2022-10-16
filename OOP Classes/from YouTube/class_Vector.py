class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y

    def get_norm2(self):
        return self.norm2(self.x, self.y)


vect_1 = Vector(10, 20)
print(vect_1.norm2(1, 2))
print(vect_1.get_norm2())
vect_2 = Vector(100, 200)
print(vect_2.get_norm2())
