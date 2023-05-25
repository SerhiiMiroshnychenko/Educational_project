"""
RLOCK - замок, ключ від якого є тільки в одного
"""
import multiprocessing

lock = multiprocessing.RLock() # його може розблокувати тільки той процес, що його заблокував

def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f'Process [{pr_name}] is running')
    l.release()


def main():
    multiprocessing.Process(target=get_value, args=(lock,)).start()
    multiprocessing.Process(target=get_value, args=(lock,)).start()
    multiprocessing.Process(target=get_value, args=(lock,)).start()


if __name__ == "__main__":
    main()
