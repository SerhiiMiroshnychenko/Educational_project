"""
Fibonacci, factorial,
squares and cubic for an input number
"""
import asyncio as a


async def fib(num):
    cache = {0: 0, 1: 1}
    if num in cache:
        result = cache[num]
    else:
        result = await fib(num - 2) + await fib(num - 1)
    cache[num] = result
    return result


async def fibs(nums):
    fibs_ = []
    for num in nums:
        res = await fib(num)
        fibs_.append(res)
    print(f'Fibonacci numbers: {fibs_}')


async def factorial(num):
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    return fact


async def factorials(nums):
    facts_ = []
    for num in nums:
        res = await factorial(num)
        facts_.append(res)
    print(f'Factorials: {facts_}')


async def square_numbers(nums):
    print(f'Squares: {[n**2 for n in nums]}')


async def cubic_numbers(nums):
    print(f'Cubics: {[n**3 for n in nums]}')

async def main():
    numbers = list(range(1, 11))
    await a.gather(
        fibs(numbers),
        factorials(numbers),
        square_numbers(numbers),
        cubic_numbers(numbers)
    )


a.run(main())
