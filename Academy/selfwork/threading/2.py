"""
Порівняння швидкості обчислення у двох конкурентних потоках та в основному потоці
"""

import threading
import time


def handler(started=0, finished=0):
    result = sum(range(started, finished))
    results.append(result)

results =[]

# Ділимо виконання задачі на два рівних потоки

task_1 = threading.Thread(
    target=handler,
    kwargs={'started': 0, 'finished': 2**14}
)

task_2 = threading.Thread(
    target=handler,
    kwargs={'started': 2**14, 'finished': 2**28}
)

started_at = time.time()

task_1.start()
task_2.start()

task_1.join()
task_2.join()

print('RESULT 1 використовуючи два конкурентні потоки:')
print(f'Time: {time.time() - started_at}')
print('Value: ', sum(results))

# Розрахуємо те ж саме в основному потоці:

results = []
started_at = time.time()
handler(finished=2**28)

print('RESULT 2 використовуючи основний потік:')
print(f'Time: {time.time() - started_at}')
print('Value: ', sum(results))
