import threading


x = 0

def increment():
    global x
    x += 1


def thread_task(lock):
    for _ in range(1000000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global x
    lock = threading.RLock()
    # setting global variable x as 0
    x = 0

    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    # t1.join()
    # t2.join()


for i in range(10):
    main_task()
    print(f"Iteration {i}: x = {x}")