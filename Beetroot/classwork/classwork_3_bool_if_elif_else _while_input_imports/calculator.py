from math import sin, cos
from own_input import numbers_input

ask_numbers = input("Введіть список чисел: ")
new_numbers = numbers_input(ask_numbers)
ask_function = input('Виберіть функцію (s == sin, c == cos): ')
if ask_function == 's':
    position = 0
    while position < len(new_numbers):
        print(sin((new_numbers[position])))
        position += 1
elif ask_function == 'c':
    position = 0
    while position < len(new_numbers):
        print(cos((new_numbers[position])))
        position += 1
else:
    print('What\'s wrong!')
