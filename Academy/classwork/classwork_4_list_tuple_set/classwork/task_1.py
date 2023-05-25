our_string = sorted(list(input('Ведіть рядок: ').split(' ')), reverse=True)
summa = 0
number = ''
for char in our_string:
    number += char
    summa += int(char)
print(int(number), summa)

