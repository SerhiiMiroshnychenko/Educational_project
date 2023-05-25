# функція створює генератор який генерує числа від х в ступені р до у в ступені р
def gen1(x, y, p):
    for i in range(x, y):
        yield i ** p


a = gen1(1, 11, 2)
print(a)
for n in a:
    print(n)


# функція створює ітератор який генерує числа від х в ступені р до у в ступені р
def iter1(x, y, p):
    return [i ** p for i in range(x, y)]


b = iter1(1, 11, 2)
print(b)
for n in b:
    print(n)

# генератор можна перетворити на ітератор за допомогою функції list
c = list(gen1(1, 11, 2))
print(c)

# ітератор створює послідовність і зберігає в пам'яті кожен елемент
my_iterator = [x * 2 for x in range(1, 11)]
print(my_iterator)
print(my_iterator[1])
for x in my_iterator:
    print(x)

# генератор створює елементи під час визову і не зберігає у пам'яті
my_generator = (x * 2 for x in range(1, 11))
print(my_generator)
try:
    print(my_generator[1])
except TypeError as error:
    print(error)
for x in my_generator:
    print(x)
