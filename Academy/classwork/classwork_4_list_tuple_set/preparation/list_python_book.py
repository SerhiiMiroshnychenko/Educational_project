string1 = "абракадабра"
list1 = list(string1)
print(list1)
list2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
list3 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
list4 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


def pl2():
    print(list2)


pl2()
print(list2[1].title())
print(list2[-1].upper())
list2[0] = "first"
pl2()
list2.append("eleven")
pl2()
list2.insert(1, "one")
print(list2)
del list2[0]
pl2()
eleven = list2.pop()
print(eleven, list2)
three = list2.pop(2)
print(three, list2)
list2.remove("eight")
pl2()
svn7 = "seven"
list2.remove(svn7)
pl2()
print(svn7.title())
list2.append("one hundred")
list2.insert(1, "one hundred")
pl2()
list2.remove("one hundred")
pl2()
list2.sort()
pl2()
print(list3, list4)
numbers = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
print(numbers)
numbers.sort()
print(numbers)
num_word = numbers + list3
word_num = list4 + numbers
print(num_word)
print(word_num)
list_num_word = ["one", 1, 2, "two", 3, 4, "three", "four", 5]
list_num = [11, 22, 33, 44, 55, 66, 77, 88, 99]
list_num.sort(reverse=True)
print(list_num)
print(list3)
print(sorted(list3))
print(list3)
List = ["one", "two", "three", "four", "five"]
LiSt = ["one", "Two", "three", "Four", "five"]
print(sorted(List))
print(sorted(LiSt))
List.reverse()
print(List)
print(len(List))
