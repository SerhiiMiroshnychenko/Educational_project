"""
QUEUE
"""
import random
import multiprocessing


def get_value(q):
    value = random.randint(0, 10)
    q.put(str(value))

queue = multiprocessing.Queue()
def main():
    pr_list = []
    for _ in range(10):
        pr = multiprocessing.Process(target=get_value, args=(queue,))
        pr_list.append(pr)
        pr.start()
    for i in pr_list:
        i.join()

    for elem in iter(queue.get, None):
        print(elem, end='..')


if __name__ == "__main__":
    main()
