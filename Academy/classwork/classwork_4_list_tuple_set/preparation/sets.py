"""Sets"""
nums = {11, 22, 33, 44, 55, 66}  # множина
nums.add(77)  # додавання
nums.remove(66)  # видалення
print(nums)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)  # об'єднання
print(first & second)  # перетин (загальні елементи)
print(first - second)  # (елем з першого яких нема в другому)
print(second - first)  # (елем з другого яких нема в першому)
print(first ^ second)  # (тільки не загальні елементи)
print((first | second) - (first & second))

# Last two lines are symmetric difference

print((first - second) == first.difference(second))
print((first | second) == first.union(second))
print((first & second) == first.intersection(second))
print((first ^ second) == first.symmetric_difference(second))
