# SuperFastPython.com
# example of wait/notify with a condition
from time import sleep
from threading import Thread
from threading import Condition
# target function to prepare some work
def task(condition, work_list):
    # block for a moment
    sleep(1)
    # add data to the work list
    work_list.append(33)
    # notify a waiting thread that the work is done
    print('Thread sending notification...')
    with condition:
        condition.notify()
# create a condition
condition = Condition()
# prepare the work list
work_list = list()
# wait to be notified that the data is ready
print('Main thread waiting for data...')
with condition:
    # start a new thread to perform some work
    worker = Thread(target=task, args=(condition, work_list))
    worker.start()
    # wait to be notified
    condition.wait()
# we know the data is ready
print(f'Got data: {work_list}')



