import math
from own_input import numbers_input

elements_to_calc = input('Write a list of numbers separated by comma:')
what_to_calculate = input('Choose cos or sin:')
new_numbers = numbers_input(elements_to_calc)

if what_to_calculate == 'sin':
    position = 0
    while position < len(new_numbers):
        result = math.sin(new_numbers[position])
        print(result)
        position += 1
elif what_to_calculate == 'cos':
    position = 0
    while position < len(new_numbers):
        result = math.cos(new_numbers[position])
        print(result)
        position += 1
else:
    print("Smth wrong")
