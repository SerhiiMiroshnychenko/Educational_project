# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all
# unique words as keys and the number of occurrences as values.
from collections import Counter


sentence = input("Введіть текст: ")

# Вирішення № 1
sentence_ = ''
for char in sentence:
    if char not in '.,!?-:;\'"()':
        sentence_ += char
word_counter = {}
for word in sentence_.split(' '):
    if word not in word_counter:
        word_counter[word.lower()] = 1
    else:
        word_counter[word.lower()] += 1
print(word_counter)

# Вирішення № 2
for char in '.,!?-:;\'"()':
    sentence = sentence.replace(char, '')
word_counter = {word.lower(): sentence.split(' ').count(word) for word in set(sentence.split(" "))}
print(word_counter)

# Вирішення № 3
print(Counter(list(sentence.lower().split(' '))))
