numbers = input('Введіть число: ')
sum_ = 0
for char in numbers:
    if char.isdigit():
        sum_ += int(char)
print(sum_)

