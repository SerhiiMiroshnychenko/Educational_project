# Створіть новий файл numbers.txt у текстовому редакторі і запишіть у нього 10 чисел, кожне з нового рядка.
# Напишіть програму, яка зчитує ці числа з файла і обчислює їх суму, виводить цю суму на екран і, водночас,
# записує цю суму у інший файл з назвою sum_numbers.txt.

# New school
with open('numbers.txt', 'w') as file:
    file.writelines([str(x)+'\n' if x < 10 else str(x) for x in range(1, 11)])

with open('numbers.txt') as file:
    print(sum([int(x) for x in file.readlines()]))

# Old school
sum_n = 0
for line in open('numbers.txt', 'r'):
    sum_n += int(line.rstrip())
print(sum_n)
open('numbers.txt', 'r').close()
