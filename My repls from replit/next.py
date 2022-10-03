print('''NEXT
       ''')
a, b, c = 1, 2, 3
print(a, b, c, sep=',', end='.')
name = "Юра"
age = input('''

Введіть вік Юри: ''')
print('''

Привіт,{1}. Тобі {0} років'''.format(age, name), end=".")
