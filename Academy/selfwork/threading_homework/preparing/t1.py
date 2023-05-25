import threading

counter = 0
rounds = 100000

def increment():
    global counter
    counter += 1


def thread_task():
    global counter
    global rounds
    for _ in range(counter, rounds):
        increment()
    return counter

class Counter(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return


def main_task():
    global counter
    # setting global variable x as 0
    counter = 0

    # creating threads
    counter_1 = Counter(target=thread_task)
    counter_2 = Counter(target=thread_task)

    # start threads
    counter_1.start()
    counter_2.start()
    print(counter_1.join())
    print(counter_2.join())
    # wait until threads finish their job
    # t1.join()
    # t2.join()



if __name__ == "__main__":
    for i in range(10):
        main_task()
        print(f"Iteration {i}: x = {counter}")

