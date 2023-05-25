# Task 3 - Words combination
# Create a program that reads an input string and then creates
# and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should
# print 5 random strings(words) that combine characters
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …

from random import shuffle
from itertools import permutations


def combination():
    """Words combination function"""
    word = list(input('Введіть слово для комбінацій: '))
    for variant in range(5):
        shuffle(word)
        print(''.join(word))


combination()


def mutation():
    """The function that prints all possible
     combinations of characters in a word"""
    for word in set(permutations(input('Введіть слово для комбінацій: '))):
        print(''.join(word))


mutation()
