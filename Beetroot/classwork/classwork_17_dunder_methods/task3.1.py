# Створити власний клас List та спробувати відтворити основні його властивості за допомогою dunder методів:
# 1. Конкатенацію __add__
# 2. Різницю списків __sub__
# 3. Обчислення довжини __len__
# 4. Отримання елемента за індексом __getitem__
# 5. Задання едемента за індексом __setitem__
# А також описати метод класу append який буде додавати елемент в список не на кінець, а на початок

class Lystopad:

    def __init__(self, item):
        self.content = []
        if type(item) is str:
            self.content.append(int(item))

        elif type(item) is int:
            self.content.append(item)

        elif type(item) is list:
            for el in item:
                if type(el) is int:
                    self.content.append(el)

    def __add__(self, other):
        sum_list = []
        if isinstance(other, Lystopad):
            sum_list = self.content.copy()
            for element in other.content:
                sum_list.append(element)
        return sum_list

    def __sub__(self, other):
        result = []
        for i in self.content:
            if i not in other.content:
                result.append(i)
        return result

    def __len__(self):
        # sum([1 for i in self.content])
        return len(self.content)

    def __getitem__(self, item):
        for index, value in enumerate(self.content):
            if index == item:
                return value

    def __setitem__(self, key, value):
        mod_list = []
        for index, index_value in enumerate(self.content):
            if index == key:
                mod_list.append(value)
                # mod_list.append(index_value)
            else:
                mod_list.append(index_value)
        self.content = mod_list

    def reverse_append(self, item):
        mod_list = []
        mod_list.append(item)
        for element in self.content:
            mod_list.append(element)
        self.content = mod_list

l1 = Lystopad('2')
l2 = Lystopad([1, 3, 2, 4, 5, 12])

print(l1.content)
print(l2.content)
print(l1 + l2)
print(l2 - l1)
print(len(l2))
print(l2[3])
l2[1] = 111
print(l2.content)
l2.reverse_append(1991)
print(l2.content)