"""
ARRAY
"""
import multiprocessing
import random
import time


def add_value(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        vtime = time.ctime()
        array[index] = num
        print(f'Process: {multiprocessing.current_process().name}; Array[{index}] = {num}, sleep = {vtime}')
        time.sleep(1)


lock = multiprocessing.Lock()
arr = multiprocessing.Array('i', range(1, 11))
# print(arr[3])
def main():
    processes = []

    for i in range(10):
        pr = multiprocessing.Process(target=add_value, args=(lock, arr, i,))
        processes.append(pr)
        pr.start()

    for i in processes:
        i.join()

    print(list(arr))


if __name__ == "__main__":
    main()
