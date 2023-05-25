import multiprocessing

def greeting(name):
    print(f'here {name}')


if __name__ == "__main__":
    process_1 = multiprocessing.Process(target=greeting, args=('Process One',))

    process_1.start()
    process_1.join()
