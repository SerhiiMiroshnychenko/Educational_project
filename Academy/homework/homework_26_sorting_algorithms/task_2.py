# Task 2

# Implement the mergeSort function without using the slice operator.

def merge_sort(elements):
    """
    The merge sort function without using the slice operator.
    :param elements: unordered collection of numbers
    :return: ordered collection of numbers
    """

    if len(elements) <= 1:
        return elements

    mid = len(elements) // 2
    left_half = [elements[index] for index in range(mid)]
    right_half = [elements[index] for index in range(mid, len(elements))]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            elements[k] = left_half[i]
            i += 1
        else:
            elements[k] = right_half[j]
            j += 1
        k = k + 1

    while i < len(left_half):
        elements[k] = left_half[i]
        i += 1
        k = k + 1

    while j < len(right_half):
        elements[k] = right_half[j]
        j += 1
        k = k + 1

    return elements


if __name__ == "__main__":
    my_list = [10, 2, 7, 4, 9, 5, 6, 1, 3, 0, 8]
    print(merge_sort(my_list))
