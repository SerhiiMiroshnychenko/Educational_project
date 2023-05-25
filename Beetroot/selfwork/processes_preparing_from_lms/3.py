import multiprocessing
import os

def test(name):
    print(f'here {name}, process: {os.getpid()}, parent process: {os.getppid()}')

def main():
    processes = []
    for i in range(5):
        t = multiprocessing.Process(target=test, args=(i,))
        processes.append(t)
        t.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
        main()
