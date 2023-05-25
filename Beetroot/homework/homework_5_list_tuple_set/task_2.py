# Task 2 - Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial
# lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

from random import randint


def create_numbers():
    """The function that creates a list of numbers"""
    numbers = []
    while len(numbers) < 11:
        numbers.append(randint(1, 10))
    return numbers


def generate_numbers(length):
    """The function that generates a list of numbers of a given length"""
    return [randint(1, 10) for _ in range(length)]


list_of_numbers_1, list_of_numbers_2 = create_numbers(), generate_numbers(10)
list_of_numbers_3 = list(set(list_of_numbers_1) & set(list_of_numbers_2))

print(f'First list: {list_of_numbers_1}\nSecond list: {list_of_numbers_2}\nThird list: {list_of_numbers_3}')
