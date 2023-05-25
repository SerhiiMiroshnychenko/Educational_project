import threading

print(threading.active_count())
current = threading.current_thread()
print(current.name)
print(current.is_alive())
# що відбудеться при повторному запуску
try:
    current.start()
except RuntimeError as e:
    print(e.__class__, e)

# змінюємо ім'я треда
current.name = 'SuperThread'
print(current.name)

current.name = 'MegaThread'
print(current.name)

# вивід усіх запущених та живих тредів
print(threading.enumerate())

# напишемо приклад для демонстрації захищеного від потоків зберігання даних
thread_data = threading.local()
thread_data.value = 5

def print_results():
    print(f'\nПоточний тред: {threading.current_thread().name}. Результат для нього: {thread_data.value=}\n')


def count_(started, to_value):
    print(hasattr(thread_data, 'value'))
    thread_data.value = started
    for _ in range(to_value):
        thread_data.value += 1
    print_results()


task_1 = threading.Thread(target=count_, args=(0, 10), name="Task_1")
task_2 = threading.Thread(target=count_, args=(100, 3), name="Task_2")
task_1.name = "task_1"
task_2.name = "task_2"

task_1.start()
task_2.start()

print_results()

task_1.join()
task_2.join()
print_results()
