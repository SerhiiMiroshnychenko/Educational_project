import multiprocessing


result = multiprocessing.Array('i', range(4))

def square_list(mylist):
    print('Inside before calculation', mylist[:], id(mylist))
    for ind, num in enumerate(mylist):
        mylist[ind] = num * num
    print(f"Result(in process p1): {mylist[:]}")


if __name__ == '__main__':
    temp = [1, 2, 3, 4]
    print('Before', result[:], id(result))
    p1 = multiprocessing.Process(target=square_list, args=(result,))
    p1.start()
    p1.join()
    # print(p1.pid)
    print('After finishing process', result[:], id(result))
