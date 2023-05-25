# Task 1 - The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint


def greatest_number():
    """The greatest number function"""
    numbers = []
    while len(numbers) <= 10:
        numbers.append(randint(-100, 100))
    return max(numbers)


print(greatest_number())


def short_greatest_number():
    """The greatest number function in a shorter version"""
    return max([randint(-100, 100) for _ in range(10)])


print(short_greatest_number())
