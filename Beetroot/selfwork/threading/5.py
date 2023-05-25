"""
Події
"""

import threading
import time


def produce_(): # Функція, що викликає та видаляє Події
    print(f'{threading.current_thread().name} is preparing (5 sec)...')
    time.sleep(5)
    print(f'{threading.current_thread().name} has created the Product!')
    product.set() # Викликаємо Подію "product". Повідомляємо про це всім Слухачам
    print(f'{threading.current_thread().name} is waiting (4 sec)...')
    time.sleep(4)
    product.clear() # Стираємо Подію "product"
    print(f'{threading.current_thread().name} has cleared the Product.')


def consume_(): # Функція - Слухач: очікує Події
    print(f'{threading.current_thread().name} is waiting for the Product:')
    product.wait() # Очікуємо Подію "product"
    print(f'{threading.current_thread().name} find the Product!')


product = threading.Event() # Задаємо Подію "product"

task_1 = threading.Thread(target=produce_, name="Producer")
task_2 = threading.Thread(target=consume_, name="Consumer")

task_1.start()
task_2.start()

task_1.join()
task_2.join()

print(task_1.is_alive())
print(task_2.is_alive())
