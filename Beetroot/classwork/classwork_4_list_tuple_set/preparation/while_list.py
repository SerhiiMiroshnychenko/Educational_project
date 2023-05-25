# While and list
list1 = ["one", 'two', "three", 'four']
list2 = []
k = 1
list1.reverse()
while list1:
    list2.append(k)
    word1 = list1.pop()
    list2.append(word1)
    k += 1
for word in list2:
    if type(word) == int:
        print(word, end='')
    else:
        print(" " + word.title())
