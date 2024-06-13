from pathlib import Path
from time import perf_counter
from typing import List, Optional

import aiohttp
import aiofiles
import asyncio

PHOTO_IDS = [
    "4383298",
    "14640594",
    "6212801",
    "13799229",
    "6811992"
    ]

async def fetch_content(session: aiohttp.ClientSession, photo_id: str) -> Optional[bytes]:
    try:
        url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?w=640&h=480"
        print(f"Fetching: {photo_id}.jpg")

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        async with session.get(url, headers=headers, timeout=15) as response:
            if response.status == 200:
                print(f"Completed fetching {photo_id}.jpg")
                return await response.read()
    except Exception as e:
        print(e)

    return None

async def write_file(photo_id: str, content: bytes, dirname: str) -> None:
    try:
        filepath = Path(f"{dirname}/async_{photo_id}.jpg")
        async with aiofiles.open(filepath, "wb") as img_file:
            await img_file.write(content)
        print(f"Completed writing {photo_id}.jpg")

    except Exception as e:
        print(e)

async def download_and_write(session: aiohttp.ClientSession, photo_id: str, dirname: str) -> None:
    content = await fetch_content(session, photo_id)
    if content:
        await write_file(photo_id, content, dirname)

async def download_all(photo_id_lst: List[str], dirname: Optional[str] = "results") -> None:
    Path.mkdir(Path(dirname), exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for photo_id in photo_id_lst:
                tg.create_task(download_and_write(session, photo_id, dirname))

async def main() -> None:
    start_time = perf_counter()

    await download_all(photo_id_lst=PHOTO_IDS)

    end_time = perf_counter()

    print(f"Total execution time(asynchronous): {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
