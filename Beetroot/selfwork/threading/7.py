"""
SEMAPHORE
"""

import threading
import time

def produce_():
    with lock:
        print(f'Set locking {lock._value} in {threading.current_thread().name}.')
        time.sleep(3)
        print(f"I'm free from {threading.current_thread().name}.")

max_workers = 2
lock = threading.BoundedSemaphore(value=max_workers) # викличе помилку якщо кількість realise буде більша за acquire
# lock = threading.Semaphore(value=max_workers) => не викличе помилку в цьому ^ випадку

task_1 = threading.Thread(target=produce_, name='Task 1')
task_2 = threading.Thread(target=produce_, name='Task 2')
task_3 = threading.Thread(target=produce_, name='Task 3')
task_4 = threading.Thread(target=produce_, name='Task 4')
task_5 = threading.Thread(target=produce_, name='Task 5')

task_1.start()
task_2.start()
task_3.start()
task_4.start()
task_5.start()

task_1.join()
task_2.join()
task_3.join()
task_4.join()
task_5.join()

# lock.release()
