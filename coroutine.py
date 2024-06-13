import asyncio

# coroutine function
async def main():
    print("Start of `main` coroutine")

if __name__ == "__main__":
    # run the `main` coroutine
    asyncio.run(main())

    # main() # -> <coroutine object...>
    # print(main())
