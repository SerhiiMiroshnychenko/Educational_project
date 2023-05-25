"""
Теж саме, що і в (6), але з join
"""

import threading
import time
import random


def work(times):
    print(f'{times}) Inside thread {threading.current_thread().name}')
    y = 0
    for x in range(10):
        y += x ** random.randint(1, 3)
        time.sleep(random.random())
    print(f'{times}) Worker {threading.current_thread().name} finished with {y=}')


def main(iter):
    print(f'\nIteration № {iter}:')
    worker_1 = threading.Thread(target=work, args=(iter,), name="Worker 1")
    worker_2 = threading.Thread(target=work, args=(iter,), name="Worker 2")
    worker_1.start()
    worker_2.start()
    worker_1.join()
    worker_2.join()


if __name__ == "__main__":
    for i in range(5):
        main(i)