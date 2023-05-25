def flip(numbers, index):
    start = 0
    while start < index:
        temp = numbers[start]
        numbers[start] = numbers[index]
        numbers[index] = temp
        start += 1
        index -= 1

def search_max(numbers, number):
    my_ind = 0
    for ind in range(number):
        if numbers[ind] > numbers[my_ind]:
            my_ind = ind
    return my_ind

def pancake_sorting(numbers, number):

    current_size = number
    while current_size > 1:
        my_ind = search_max(numbers, current_size)

        if my_ind != current_size-1:

            flip(numbers, my_ind)
            flip(numbers, current_size-1)
        current_size -= 1

def print_numbers(numbers, number):
    print('Sorted Pancakes:')
    for ind in range(number):
        print(numbers[ind], end=' ')


if __name__ == "__main__":
    pancakes = [100, 41, 14, 5, 23, 10, 20, 6, 4, 34, 11, 12, 6, 7]
    n = len(pancakes)
    pancake_sorting(pancakes, n)
    print_numbers(pancakes,n)
