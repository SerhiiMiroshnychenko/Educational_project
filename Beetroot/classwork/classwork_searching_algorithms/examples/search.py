import timeit


def sequential_search(array, item):
    # pos = 0
    # found = False
    # while pos < len(array) and not found:
    #     if array[pos] == item:
    #         found = True
    #     else:
    #         pos = pos + 1
    # return found

    found = False
    for i in array:
        if i == item:
            found = True
            break
    return found

    # for i in range(len(array)):
    #     if array[i] == item:
    #         return i
    # return None


def sequential_search_2(array, item):
    return any(i == item for i in array)

def binary_search(array, item):
    first = 0  # low
    last = len(array) - 1  # height
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            # found = True
            return midpoint
        if item < array[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found


if __name__ == "__main__":
    seq_timer = timeit.timeit(
        stmt="sequential_search(list(range(200000)), 167000)",
        number=100,
        setup="from __main__ import sequential_search"
    )
    print(seq_timer)


    seq2_timer = timeit.timeit(
        stmt="sequential_search_2(list(range(200000)), 167000)",
        number=100,
        setup="from __main__ import sequential_search_2"
    )
    print(seq2_timer)

    bin_timer = timeit.timeit(
        stmt="binary_search(list(range(200000)), 167000)",
        number=100,
        setup="from __main__ import binary_search"
    )
    print(bin_timer)

    # print(binary_search(list(range(100)), 150))