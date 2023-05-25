import asyncio

async def cubic_number(n):
    for i in range(1,n+1):
        print("Cubic of ",i, "is ", i**3)


async def cubic_root(n):
    print("Cubic root of ",n," rounded to nearest integer is ",
          round(n**.5))


async def main():
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(cubic_number(5))
        task_group.create_task(cubic_root(25))
        task_group.create_task(cubic_root(18))

    print("All different tasks of task_group has executed successfully!!")


asyncio.run(main())
