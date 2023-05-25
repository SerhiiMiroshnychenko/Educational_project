import threading


x = 0


def increment():
    global x
    x += 1


def thread_task():
    global x
    x = 0
    for _ in range(1000000):
        increment()


class ThreadWithReturnValue(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, Verbose=None):
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
        print(self._target(*self._args, **self._kwargs))


def main_task():
    global x
    # setting global variable x as 0
    x = 0

    # creating threads
    t1 = ThreadWithReturnValue(target=thread_task)
    t2 = ThreadWithReturnValue(target=thread_task)

    # start threads
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # wait until threads finish their job
    # t1.join()
    # t2.join()


sum_result = 0
for i in range(10):
    main_task()
    print(f"Iteration {i}: x = {x}")
    sum_result += x
print(sum_result/1000000, 'millions')
