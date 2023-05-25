from copy import copy, deepcopy

a = 10
b = '33'
s = 'abc'
xxx = [1, s]
numbers = [a, b, s, xxx]
num1 = numbers
num2 = numbers[:]
num3 = copy(numbers)
num4 = deepcopy(numbers)
print(f'{numbers=}\n{num1=}\n{num2=}\n{num3=}\n{num4=}\n')
a = 1
print(f'{numbers=}\n{num1=}\n{num2=}\n{num3=}\n{num4=}\n')
num1[1] = '3'
print(f'{numbers=}\n{num1=}\n{num2=}\n{num3=}\n{num4=}\n')
xxx[0] = 10
print(f'{numbers=}\n{num1=}\n{num2=}\n{num3=}\n{num4=}\n')

