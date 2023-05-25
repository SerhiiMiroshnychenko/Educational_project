set1 = {1, 2, 2, 3, 1}
print(len(set1))
print(set1)
print(1 in set1)
set1.add(5)
set1.remove(3)
set1.discard(6)
set1.pop()
print(set1)
set2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
num1 = int(input("Введіть число: "))
print(num1 in set2)
for x in set2:
    print(x)
set1.clear()
print(set1)
set1.add(22)
print(set1)
del set1
print(set1)
