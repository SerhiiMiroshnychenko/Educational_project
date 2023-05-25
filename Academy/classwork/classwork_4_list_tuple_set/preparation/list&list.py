# Шукаємо перетин двох lists
list17 = ["one", "two", "three", "four", "five", "six", "seven"]
list410 = ["four", "five", "six", "seven", "eight", "nine", "ten"]
list_ = []  # засновуємо пустий list
for number in list17:
    if number in list410:
        print(number)  # виводимо перетин
        list_.append(number)  # додаємо перетин до пустого list
print(list_)  # друк всіх елементів перетину
