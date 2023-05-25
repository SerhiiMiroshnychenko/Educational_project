"""
Task 1

Primes
NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]
We have the following input list of numbers, some of them are prime.
You need to create a utility function that takes as input a number
and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different
concurrent implementations for filtering NUMBERS.
Compare the results and performance of each of them.
"""


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import math


def is_prime(n: int) -> bool:
    """
    The function for checking if a number is prime
    with O(√n) runtime complexity

    :param n: a number to check (integer)
    :return: is prime number (bool)
    """

    return all(n%i != 0 for i in range(2, int(math.sqrt(n))+1))



numbers = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def run_1(executor_class, max_workers=len(numbers)):
    executor = executor_class(max_workers=max_workers)
    started = time.time()

    future_1 = executor.map(is_prime, numbers)
    results = list(future_1)

    print('Result:\n{result}.\nTime for {executor}: {spent_time}'.format(
        result=results,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


def run_2(executor_class, max_workers=len(numbers)):
    executor = executor_class(max_workers=max_workers)
    started = time.time()


    results = []
    for number in numbers:
        future_2 = executor.submit(is_prime, number)
        results.append(future_2.result())

    print('Result:\n{result}.\nTime for {executor}: {spent_time}'.format(
        result=results,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


def main():
    print('RUN 1 Execute using map...')
    run_1(ThreadPoolExecutor)
    run_1(ProcessPoolExecutor)

    print('RUN 2 Execute using submit...')
    run_2(ThreadPoolExecutor)
    run_2(ProcessPoolExecutor)


if __name__ == "__main__":
    main()
