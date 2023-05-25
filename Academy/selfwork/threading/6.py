"""
Блокування

DEAD LOCK
"""

import threading


def produce_():
    print(f'Set locking in {threading.current_thread().name}')
    with lock: # Вхід в оператор with: захоплення блокування, вихід - повернення
        print(f'Done in {threading.current_thread().name}')
        with lock: # повторна спроба захоплення блокування (з Lock - викличе dead lock)
            print(f"It's great in {threading.current_thread().name}!")
    print(f'Lock release in {threading.current_thread().name}!')


# lock = threading.Lock() => в нашому випадку викличе dead lock
lock = threading.RLock() # Можна захоплювати блокування повторно
# __enter__ => lock.acquire()
# __exit__ => lock.release()

ver = 0 # Змінюємо версію тут

task_1 = threading.Thread(target=produce_, name="Task 1")
task_2 = threading.Thread(target=produce_, name="Task 2")

task_1.start()

if ver == 1:
    lock.acquire() # Захоплення блокування
    print(1) # Виконання якогось коду
    print(1) # Поки він не виконається
    print(1) # Інші потоки будуть чекати
    lock.release() # Повернення блокування

task_2.start()

task_1.join()
task_2.join()
