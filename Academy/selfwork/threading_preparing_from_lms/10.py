import threading
import time
import random


def work(name):
    print(f'Inside thread {name}')
    y = 0
    for x in range(10):
        y += x ** 2
        time.sleep(random.random())
    print(f'Worker {name} finished with {y=}')



if __name__ == "__main__":

    worker_1 = threading.Thread(target=work, args=(1,))
    worker_2 = threading.Thread(target=work, args=(2,))
    worker_1.start()
    worker_2.start()

    worker_1.join()
    print('OK')
    worker_2.join()
    print('OK2')
