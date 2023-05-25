import threading


x = 0

def increment():
    global x
    x += 1


def thread_task():
    for _ in range(1000000):
        increment()


def main_task():
    global x
    # setting global variable x as 0
    x = 0

    # creating threads
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


sum_result = 0
for i in range(10):
    main_task()
    print(f"Iteration {i}: x = {x}")
    sum_result += x
print(sum_result/1000000, 'millions')
