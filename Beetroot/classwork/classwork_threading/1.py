import threading
import time
import random
def worker(name):
    print(f'Inside thread {name}')
    for x in range(10):
        x ** 2
        time.sleep(random.random())
    print(f'Worker {name} finished')


w = threading.Thread(target=worker, args=(1,))
w2 = threading.Thread(target=worker, args=(2,))
w.start()
w2.start()

# w.join()
print('OK')
# w2.join()
print('OK2')