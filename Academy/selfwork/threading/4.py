"""
Захищене від потоків зберігання даних
"""

import threading

thread_data = threading.local()
thread_data.value = 5

def print_results():
    print(f'Поточний тред: {threading.current_thread().name}. Результат для нього: {thread_data.value=}\n')


def count_(started, to_value):
    has_value = hasattr(thread_data, 'value') # чи має поточний тред атрибут 'value'
    print(f'Тред {threading.current_thread().name} має атрибут "value": {has_value}')
    thread_data.value = started
    for _ in range(to_value):
        thread_data.value += 1
    print_results()


task_1 = threading.Thread(target=count_, args=(0, 10), name="Task_1")
task_2 = threading.Thread(target=count_, args=(100, 3), name="Task_2")

task_1.start()
task_2.start()

print_results()

task_1.join()
task_2.join()

print_results()
