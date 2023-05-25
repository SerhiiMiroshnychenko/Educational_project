from prettytable import PrettyTable

upper, lower = 0, 0
with open('result.txt', encoding='utf-8') as file:
    for line in file:
        if line:
            upper += sum(1 for char in line if char.isalpha() and 65 < ord(char) < 90)
            lower += sum(1 for char in line if char.isalpha() and 97 < ord(char) < 122)

uppers = round(upper / ((upper + lower) / 100), 2)
lowers = round(lower / ((upper + lower) / 100), 2)

table = PrettyTable()
table.field_names = ['Upper', 'Lower', 'Upper %', 'Lower %']
table.add_row([upper, lower, uppers, lowers])

print(table)
