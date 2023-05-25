class Constructor:
    def __init__(self, name: str):
        self.name = name
        self.houses_number = 0

    def construct(self):
        self.houses_number += 1
        number = self.houses_number
        return House(number, constructor=self.object)

class House:
    def __init__(self, number: int, constructor: Constructor):
        self.number = number
        self.constructor = constructor