import asyncio

async def func1():
    pass

async def func2():
    await func1()

async def func3():
    await asyncio.sleep(100)
    await func2()

async def main_func():
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    task3 = asyncio.create_task(func3())
    await asyncio.gather(task1, task2, task3)

if __name__ == "__main__":
    asyncio.run(main_func())

