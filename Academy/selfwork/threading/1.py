"""
Порівняння швидкості обчислення в одному окремому потоці та в основному потоці
"""

import threading
import time


def handler(started=0, finished=0):
    result = sum(range(started, finished))
    print('Value:', result)

params = {'finished': 2 ** 28}

task = threading.Thread(target=handler, kwargs=params) # target -> функція яку ми хочемо виконувати паралельно
started_at = time.time()
print('\nRESULTS 1 В окремому потоці:')
task.start() # запускаємо thread
task.join() # блокуємо інтерпретатор до того моменту поки не відпрацює наш thread
print(f'Time: {time.time() - started_at}')

started_at = time.time()
print('\nRESULTS 2 В основному потоці:')
handler(**params)
print(f'Time: {time.time() - started_at}')
