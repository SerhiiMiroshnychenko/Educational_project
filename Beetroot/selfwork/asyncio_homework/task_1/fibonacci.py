import asyncio as a

cache = {0: 0, 1: 1}

async def fib(n):
    if n in cache:
        result = cache[n]
    else:
        result = await fib(n - 2) + await fib(n - 1)
    cache[n] = result
    return result

async def main():
    res = await fib(100)
    print(res)

a.run(main())
