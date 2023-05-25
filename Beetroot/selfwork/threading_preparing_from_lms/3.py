import threading
import time
import random

def work_1():
    print(threading.current_thread().name, 'Starting')
    time.sleep(random.random() * 5)
    print('Inside Worker 1')
    print(threading.current_thread().name, 'Exiting')


def work_2():
    print(threading.current_thread().name, 'Starting')
    time.sleep(random.random())
    print('Inside Worker 2')
    print(threading.current_thread().name, 'Exiting')


worker_1 = threading.Thread(name='Worker One', target=work_1)
worker_2 = threading.Thread(name='Worker Two', target=work_2)


worker_1.start()
worker_2.start()
