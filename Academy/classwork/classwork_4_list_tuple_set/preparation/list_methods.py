list1 = [1, 2, 3]
print(list1)
list1.append(4)  # додає в кінець
print(list1)
list1.clear()  # очищує лист
print(list1)
list1 = list('1234')  # створюємо через функцію
print(list1)
list2 = [5, 6, 7]
list1.extend(list2)  # додає інший лист
print(list1)
print(list1.index(5))  # повертає індекс елемента
x = list1.pop(0)  # випіхує елем.0 з листа
print(x)
print(list1)
list1.reverse()
print(list1)
list1.remove('2')  # видаляє '2'
list1.remove('3')
list1.remove('4')
print(list1)
list1.extend([1, 2, 3, 4])  # додає
print(list1)
list1.sort()  # сортуємо
print(list1)
print(max(list1), min(list1))  # макс і мін елем.
