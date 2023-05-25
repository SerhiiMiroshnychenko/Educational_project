list1 = [1, 2, 3, 4]
print(list1)
list1 += [5]
print(list1)
list2 = list(range(6, 11))
print(list2)
list1 += list2
print(list1)
list1.insert(0, 0)
print(list1)
list1.remove(5)
print(list1)
list1.insert(5, "five")
print(list1)
list1 *= 2
print(list1)
