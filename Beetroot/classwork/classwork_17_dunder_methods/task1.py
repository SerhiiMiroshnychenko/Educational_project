# Створити власний клас List та спробувати відтворити основні його властивості за допомогою dunder методів:
# 1. Конкатенацію __add__
# 2. Різницю списків __sub__
# 3. Обчислення довжини __len__
# 4. Отримання елемента за індексом __getitem__
# 5. Задання елемента за індексом __setitem__
# А також описати метод класу append який буде додавати елемент в список не на кінець, а на початок

class Array:
    def __init__(self, *args):
        self.array = list(args)

    def r_append(self, value):

        self.array.append(value)

    def l_append(self, value):
        self.array.insert(0, value)

    def __add__(self, other):
        array = []
        array[:len(self.array)] = self.array
        array[len(self.array):len(self.array)+len(other.array)] = other.array
        return Array(*array)

    def __sub__(self, other):
        array = [i for i in self.array if i not in other.array]
        return Array(*array)

    def __len__(self):
        c = 0
        for _ in range(len(self.array)):
            c += 1
        return c

    def __getitem__(self, item):
        for position, value in enumerate(self.array):
            if position == item:
                return value
    def __setitem__(self, key, value):
        if key <= len(self.array):
            self.array[key] = value
        else:
            print("Key Error")

    def __str__(self):
        return f'Array {self.array}'

m = Array()
m.r_append(2)
m.r_append(1)
m.l_append(4)
print(m)
n = Array()
n.r_append(2)
n.r_append(1)
n.l_append(3)
print(n)

k = n + m
print(k)

p = n - m
print(p)

print(len(k))
