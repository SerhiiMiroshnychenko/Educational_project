# https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/

import os
import time
from multiprocessing import current_process, Process
from threading import current_thread, Thread

COUNT = 200000000
SLEEP = 10


def io_bound(sec):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} ---> Start sleeping...")
    time.sleep(sec)
    print(f"{pid} * {processName} * {threadName} ---> Finished sleeping...")


def cpu_bound(n):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} ---> Start counting...")

    while n > 0:
        n -= 1

    print(f"{pid} * {processName} * {threadName} ---> Finished counting...")


if __name__ == "__main__":
    start = time.time()

    # Code snippet for Part 6
    p1 = Thread(target=io_bound, args=(SLEEP,))
    p2 = Process(target=cpu_bound, args=(COUNT,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)
