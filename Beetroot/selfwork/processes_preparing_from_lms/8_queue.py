"""
The effective use of multiple processes usually requires some communication between them, so that work can be divided and results can be aggregated.
Multiprocessing supports two types of communication channels between processes:

- Queue
- Pipe

Ефективне використання кількох процесів зазвичай вимагає певного зв'язку між ними, щоб можна було розділити роботу та звести результати.
Багатопроцесорна обробка підтримує два типи каналів зв'язку між процесами:

- Черга
- Труба
"""

"""
QUEUE
"""
import multiprocessing


def square_list(mylist, q):
    for num in mylist:
        q.put(num * num)

def read_from_queue(q):
    while not q.empty():
        print(q.get())

def main():
    temp = [1, 2, 3, 4]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=square_list, args=(temp, q))
    p2 = multiprocessing.Process(target=read_from_queue, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()



if __name__ == "__main__":
    main()
