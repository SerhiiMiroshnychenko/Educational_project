"""
LOCK - замок, ключ від якого є у кожного
"""
import multiprocessing

lock = multiprocessing.Lock() # його може заблокувати та розблокувати будь-який процес

def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f'Process [{pr_name}] is running')

def get_value_2(l):
    l.release()
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f'Process [{pr_name}] is running')

def main():
    multiprocessing.Process(target=get_value, args=(lock,)).start()
    multiprocessing.Process(target=get_value_2, args=(lock,)).start()
    multiprocessing.Process(target=get_value_2, args=(lock,)).start()


if __name__ == "__main__":
    main()