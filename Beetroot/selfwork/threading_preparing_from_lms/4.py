"""
DAEMON Thread
"""

import threading
import time
import random

def work_1():
    print(threading.current_thread().name, 'Starting')
    time.sleep(random.random() * 5)
    print('Inside Worker 1')
    print(f'Worker 1 representation: {threading.current_thread()}')
    print(f'Worker 1 sees {threading.active_count()} active threads')
    print(threading.current_thread().name, 'Exiting')


def work_2():
    print(threading.current_thread().name, 'Starting')
    time.sleep(random.random())
    print('Inside Worker 2')
    print(f'Worker 2 representation: {threading.current_thread()}')
    print(f'Worker 2 sees {threading.active_count()} active threads')
    print(threading.current_thread().name, 'Exiting')

def work_3():
    print(threading.current_thread().name, 'Starting')
    time.sleep(1)
    print('Inside Daemon')
    print(f'Daemon Thread representation: {threading.current_thread()}')
    print(f'Daemon sees {threading.active_count()} active threads')
    time.sleep(5)
    print(threading.current_thread().name, 'Exiting')


worker_1 = threading.Thread(name='Worker One', target=work_1)
worker_2 = threading.Thread(name='Worker Two', target=work_2)
daemon_1 = threading.Thread(name='Daemon Thread', target=work_3, daemon=True)


worker_1.start()
worker_2.start()
daemon_1.start()
