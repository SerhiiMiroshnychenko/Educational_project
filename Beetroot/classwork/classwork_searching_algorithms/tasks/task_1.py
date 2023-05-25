def peak_search(array):

    start = 0
    end = len(array) - 1

    while start <= end:


        middle = start + end // 2


        if (middle == 0 or array[middle - 1] <= array[middle]) \
                and (middle == len(array) - 1 or array[middle + 1] <= array[middle]):
            break


        if middle > 0 and array[middle - 1] > array[middle]:
            end = middle - 1


        else:
            start = middle + 1

    return middle, array[middle]

if __name__ == '__main__':
    my_list = [20, 30, 40, 50, 600, 70, 80, 90, 100]
    result = peak_search(my_list)
    print(f'The peak element has index <{result[0]}> and value "{result[1]}".')

