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
import os


def is_prime(n: int) -> bool:
    """
    The function for checking if a number is prime
    :param n: a number to check (integer)
    :return: is prime number (bool)
    """
    answer = all(n % i != 0 for i in range(2, n))
    print(answer)
    return answer



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


with ThreadPoolExecutor() as executor:
    executor.map(is_prime, numbers)


with ProcessPoolExecutor() as executor:
    executor.map(is_prime, numbers)

