# Task 1

# A bubble sort can be modified to “bubble” in both directions.
# The first pass moves “up” the list and the second pass moves “down.”
# This alternating pattern continues until no more passes are necessary.
# Implement this variation and describe under what circumstances it might
# be appropriate.


def bubble_sort(numbers):
    """
    The bubble sort algorithm is implemented
    :param numbers: collection of numbers
    :return: sorted collection of numbers
    """

    for counter, pass_num in enumerate(range(len(numbers) - 1, 0, -1), start=1):
        start_numbers = numbers[:]
        print(f'{counter}.{numbers=}')
        for index in range(pass_num):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
        end_numbers = numbers
        if start_numbers == end_numbers:
            return end_numbers
    return numbers


def double_bubble_sort(numbers):
    """
    The double bubble sort algorithm is implemented
    :param numbers: unordered collection of numbers
    :return: ordered collection of numbers
    """

    for counter, pass_num in enumerate(range(len(numbers) - 1, 0, -1), start=1):
        start_numbers = numbers[:]
        print(f'{counter}.{numbers=}')
        current_index = 0
        for index in range(pass_num):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
            current_index = index
        for ind in range(current_index, 0, -1):
            if numbers[ind] < numbers[ind - 1]:
                numbers[ind], numbers[ind - 1] = numbers[ind - 1], numbers[ind]
        end_numbers = numbers
        if start_numbers == end_numbers:
            return end_numbers
    return numbers


if __name__ == "__main__":
    my_list = [10, 2, 7, 4, 9, 5, 6, 1, 3, 0, 8]
    print('Simple bubble sort:')
    print(f'{my_list=}')
    print(bubble_sort(my_list))
    my_list = [10, 2, 7, 4, 9, 5, 6, 1, 3, 0, 8]
    print('\nDouble bubble sort:')
    print(f'{my_list=}')
    print(double_bubble_sort(my_list))
    print('Доцільно використовувати коли в першу чергу треба знайти <max> та <min> елементи.')
