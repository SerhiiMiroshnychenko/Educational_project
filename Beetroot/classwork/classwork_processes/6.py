import multiprocessing

def square_list(mylist, q):
    for num in mylist:
        q.put(num * num)


def read_from_queue(q):
    while not q.empty():
        print(q.get())


if __name__ == "__main__":

    temp = [1, 2, 3, 4]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=square_list, args=(temp, q))
    p2 = multiprocessing.Process(target=read_from_queue, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
