import asyncio
from time import perf_counter

async def brew_coffee() -> str:
    print("Started brew_coffee")
    await asyncio.sleep(3)
    print("Completed brew_coffee")
    return "Coffee Ready"


async def toast_bagel() -> str:
    print("Started toast_bagel")
    await asyncio.sleep(3)
    print("Completed toast_bagel")
    return "Bagel Ready"


async def main () -> None:
    start_time = perf_counter()

    # # No performance gain tasks run synchronously
    # task_1 = brew_coffee()
    # task_2 = toast_bagel()
    # coffee_result = await task_1
    # bagel_result = await task_2

    # Tasks created using create_task()
    task_1 = asyncio.create_task(brew_coffee())
    task_2 = asyncio.create_task(toast_bagel())

    coffee_result = await task_1
    bagel_result = await task_2

    # # Tasks created using gather()
    # task_1 = brew_coffee()
    # task_2 = toast_bagel()

    # results = await asyncio.gather(task_1, task_2)
    # coffee_result, bagel_result = results

    # # Tasks created using TaskGroup()
    # async with asyncio.TaskGroup() as tg:
    #     task_1 = tg.create_task(brew_coffee())
    #     task_2 = tg.create_task(toast_bagel())

    # coffee_result = task_1.result()
    # bagel_result = task_2.result()

    elapsed_time = perf_counter() - start_time

    print(f"Coffee status: {coffee_result}")
    print(f"Bagel status: {bagel_result}")
    print(f"Total execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())


