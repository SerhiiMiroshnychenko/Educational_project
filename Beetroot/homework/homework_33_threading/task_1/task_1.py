#Task 1

#A shared counter

# Make a class called Counter, and make it a subclass of the Thread class
# in the Threading module. Make the class have two global variables, one
# called counter set to 0, and another called rounds set to 100.000.
# Now implement the run() method, let it include a simple for-loop that
# iterates through rounds (e.i. 100.000 times) and for each time increments
# the value of the counter by 1. Create 2 instances of the thread and start them,
# then join them and check the result of the counter, it should be 200.000, right?
# Run it a couple of times and consider some different reasons why you get
# the answer that you get.

import threading

counter = 0
rounds = 100_000

class Counter(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         args=args, kwargs=kwargs, daemon=daemon)

    def run(self):
        global counter
        global rounds
        for _ in range(rounds):
            counter += 1
        print(f'Counter = {counter} (in {threading.current_thread().name})')


def main():
    global counter, rounds
    counter_1 = Counter(name='Counter One')
    counter_2 = Counter(name='Counter Two')
    counter_1.start()
    counter_2.start()
    counter_1.join()
    counter_2.join()
    print(f'Counter = {counter} (in {threading.current_thread().name})')


if __name__ == "__main__":
    main()
