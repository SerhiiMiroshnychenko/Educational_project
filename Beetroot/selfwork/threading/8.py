import os
import threading

def execute_watch():
    timer = threading.Timer(5.0, print_files)
    timer.start()

def print_files():
    """
    Друкує файли з поточної директорії
    :return: None
    """
    for i in os.listdir('.'):
        print(i)
    # execute_watch() => в цьому разі буде друкувати файли через кожні 5 сек

execute_watch()
