# Task 1

# A shared counter

# Make a class called Counter, and make it a subclass of the Thread
# class in the Threading module. Make the class have two global variables,
# one called counter set to 0, and another called rounds set to 100.000.
# Now implement the run() method, let it include a simple for-loop that
# iterates through rounds (e.i. 100.000 times) and for each time increments
# the value of the counter by 1. Create 2 instances of the thread and start
# them, then join them and check the result of the counter,
# it should be 200.000, right? Run it a couple of times and consider some
# different reasons why you get the answer that you get.

import threading

counter = 0
rounds = 100000


def thread_task():
    global counter
    global rounds
    for _ in range(rounds):
        counter += 1
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


    def return_counter(self):
        return self.name, counter




if __name__ == "__main__":
    for i in range(3):
        counter = 0
        counter_1 = Counter(target=thread_task, name='Counter_1')
        counter_2 = Counter(target=thread_task, name='Counter_2')

        counter_1.start()
        counter_2.start()

        print(f"Iteration {i}: global counter = {counter}")

        print(f'counter in {counter_1.return_counter()[0]} + counter in {counter_2.return_counter()[0]}'
              f' = {counter_1.return_counter()[1] + counter_2.return_counter()[1]}')

    for i in range(3):
        counter = 0
        counter_1 = Counter(target=thread_task, name='Counter_1')
        counter_2 = Counter(target=thread_task, name='Counter_2')

        counter_1.start()
        counter_2.start()

        print(f"Iteration {i}: global counter = {counter}")
        print(f'counter in {counter_1.return_counter()[0]} + counter in {counter_2.return_counter()[0]}'
              f' = {counter_1.join() + counter_2.join()}')







