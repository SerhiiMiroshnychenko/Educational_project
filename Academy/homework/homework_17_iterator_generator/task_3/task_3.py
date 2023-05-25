# Task 3
# Create your own implementation of an iterable, which could be used inside
# for-in loop. Also, add logic for retrieving elements using square brackets syntax.

class Iterable:

    def __init__(self, *data):
        new_data = []
        for element in data:
            try:
                for elem in element:
                    new_data += [elem]
            except TypeError:
                new_data += [element]
        self.data = tuple(new_data)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            self.index = 0
            raise StopIteration
        self.index += 1
        return self.data[self.index-1]

    def __getitem__(self, ind):
        for counter, element in enumerate(self.data):
            if counter == ind:
                return element
        print('Index out of range.')

    def __len__(self):
        return sum(1 for _ in self.data)

    def __str__(self):
        return f'{self.data}'

if __name__ == '__main__':
    i0 = Iterable('a', 'b', 'c', 'd', 'e', 'f')
    i1 = Iterable('Academy')
    i2 = Iterable('Python', 1, 2, 3, 4, ['a', 'b', 'c', 'd', 'e'])
    examples = i0, i1, i2

    for example in examples:
        print('\n')
        print(f'The instance of Iterable: {example}')
        print('print(*instance, sep="---"): ', end='')
        print(*example, sep='---')
        print(f'Element № 7: {example[7]}')
        print(f'Length of the instance: {len(example)}')
        print('for i in the instance: ')
        print('print(*instance, sep="..."): ', end='')
        for i in example:
            print(i, end='...')