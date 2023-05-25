import multiprocessing


def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


def main():
    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))

    print(num.value)
    print(arr[:])

    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])


if __name__ == "__main__":
    main()
