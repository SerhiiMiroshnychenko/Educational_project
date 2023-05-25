import threading
import time
import logging
import random


def main():
    def worker():
        print(threading.current_thread().name, 'Starting')
        time.sleep(random.random() * 5)
        print('Inside worker')
        print(threading.current_thread().name, 'Exiting')

    def worker2():
        print(threading.current_thread().name, 'Starting')
        time.sleep(random.random())
        print('Inside worker 2')
        print(threading.current_thread().name, 'Exiting')

    def worker3():
        print(threading.current_thread().name, 'Starting')
        time.sleep(5)
        print('Inside worker 3')
        print(threading.current_thread().name, 'Exiting')

    w = threading.Thread(name='worker', target=worker)
    w2 = threading.Thread(name='worker2', target=worker2)
    w3 = threading.Thread(name='worker3', target=worker3, daemon=True)

    w.start()
    w2.start()
    w3.start()


if __name__ == "__main__":
    for i in range(3):
        print(i)
        main()
