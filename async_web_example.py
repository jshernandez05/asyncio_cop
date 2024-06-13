from pathlib import Path
from time import perf_counter
from typing import List

import aiohttp
import aiofiles
import asyncio


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    print(f"starting fetch for {url}")
    async with session.get(url) as response:
        content = await response.text()
    print(f"Completed fetch for {url}")
    return content


async def write_to_file(filepath: Path, content: str) -> None:
    print(f"Strating write to {filepath.stem}")
    async with aiofiles.open(filepath, "w") as f:
        await f.write(content)
    print(f"Completed write to {filepath.stem}")

##### await fetch, then await write method #####
# async def main() -> None:
#     base_url: str = "http://example"
#     domain_ext: List[str] = [".com", ".org", ".net"]
#     urls: List[str] = [f"{base_url}{ext}" for ext in domain_ext]

#     dirname = Path("results")

#     start_time = perf_counter()

#     Path.mkdir(dirname, exist_ok=True)

#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch(session, url) for url in urls]
#         results: List[str] = await asyncio.gather(*tasks)

#     # Write results to files
#     file_tasks = [write_to_file(Path(f"{dirname}/async_result_{i+1}.txt"), result) for i, result in enumerate(results)]
#     await asyncio.gather(*file_tasks)

#     end_time = perf_counter()

#     print(f"Total execution time(asynchronous): {end_time - start_time:.2f} seconds")

##### Task Group Method w/ Separate fetch and write tasks #####
# async def main() -> None:
#     base_url: str = "http://example"
#     domain_ext: List[str] = [".com", ".org", ".net"]
#     urls: List[str] = [f"{base_url}{ext}" for ext in domain_ext]

#     dirname = Path("results")

#     start_time = perf_counter()

#     Path.mkdir(dirname, exist_ok=True)

#     async with aiohttp.ClientSession() as session:
#         async with asyncio.TaskGroup() as tg:
#             fetch_tasks = [tg.create_task(fetch(session, url)) for url in urls]
#             write_tasks = []

#             for i, fetch_task in enumerate(fetch_tasks):
#                 result = await fetch_task
#                 filepath = Path(f"{dirname}/async_result_{i+1}.txt")
#                 write_task = tg.create_task(write_to_file(filepath, result))
#                 write_tasks.append(write_task)

#     end_time = perf_counter()
#     print(f"Total execution time(asynchronous): {end_time - start_time:.2f} seconds")

##### Task Group w/ Combined Fetch and Write tasks for each URL #####
async def fetch_and_write(session: aiohttp.ClientSession, url: str, filepath: Path) -> None:
    content = await fetch(session, url)
    await write_to_file(filepath, content)


async def main() -> None:
    base_url: str = "http://example"
    domain_ext: List[str] = [".com", ".org", ".net"]
    urls: List[str] = [f"{base_url}{ext}" for ext in domain_ext]

    dirname = Path("results")

    start_time = perf_counter()

    Path.mkdir(dirname, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for i, url in enumerate(urls):
                filepath = Path(f"{dirname}/async_result_{i+1}.txt")
                tg.create_task(fetch_and_write(session, url, filepath))

    end_time = perf_counter()

    print(f"Total execution time(asynchronous): {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())