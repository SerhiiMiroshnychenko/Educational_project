# Task 1
# Create your own implementation of a built-in function enumerate, named
# `with_index`, which takes two parameters: `iterable` and `start`,
# default is 0. Tips: see the documentation for the enumerate function

class WithIndex1:

    def __new__(cls, iterable, start=0, step=1):
        try:
            iter(iterable)
            return super().__new__(cls)
        except Exception as e:
            print(e.__class__, e)


    def __init__(self, iterable, start:int=0, step:int=1):
        self.iterable = iterable
        self.start = start
        self.step = step
        self.ind = 0
        self.end = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind > self.end-1:
            self.ind = 0
            raise StopIteration
        val = (self.ind * self.step + self.start, self.iterable[self.ind])
        self.ind += 1
        return val

    def __str__(self):
        return 'with_index version1:'

class WithIndex2:

    def __new__(cls, iterable, start=0, step=1):
        try:
            iter(iterable)
            return super().__new__(cls)
        except Exception as e:
            print(e.__class__, e)


    def __init__(self, iterable, start:int=0, step:int=1):
        self.iterable = iterable
        self.start = start
        self.step = step
        self.ind = 0
        self.end = len(iterable)

    def __iter__(self):
        while self.end > self.ind:
            yield self.ind * self.step + self.start, self.iterable[self.ind]
            self.ind += 1
        self.ind = 0

    def __str__(self):
        return 'with_index version2:'



if __name__ == '__main__':

    examples = ['a', 'b', 'c', 'd', 'e'], 'Python', 1000

    for example in examples:
        wi1 = WithIndex1(example, 1)
        wi2 = WithIndex2(example, 1)
        try:
            print(wi1, *wi1, '\n')
            print(wi2, *wi2, '\n')
        except TypeError:
            print(type(wi1), wi1, '\n')
