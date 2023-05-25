import asyncio


async def square_number(n):
    for i in range(1, n + 1):
        print("Square of ", i, "is ", i ** 2)
        await asyncio.sleep(0.001)


async def square_root(n):
    print("Square root of ", n, " rounded to nearest integer is ",
          round(n ** .5))


async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(square_number(5))
        task_group.create_task(square_root(25))
        task_group.create_task(square_root(18))

    print("All different tasks of task_group has executed successfully!!")


asyncio.run(main())
