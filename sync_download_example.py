from pathlib import Path
from time import perf_counter
from typing import List, Optional

import requests

PHOTO_IDS = [
    "4383298",
    "14640594",
    "6212801",
    "13799229",
    "6811992"
    ]

def fetch_content(photo_id: str) -> Optional[bytes]:
    try:
        url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?w=640&h=480"
        print(f"Fetching: {photo_id}.jpg")

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 200:
            print(f"Completed fetching {photo_id}.jpg")
            return response.content

    except Exception as e:
        print(e)

    return None

def write_file(photo_id: str, content: bytes, dirname: str) -> None:
    try:
        filepath = Path(f"{dirname}/sync_{photo_id}.jpg")
        with open(filepath, "wb") as img_file:
            img_file.write(content)
        print(f"Completed writing {photo_id}.jpg")

    except Exception as e:
        print(e)

def download_all(photo_id_lst: List[str], dirname: Optional[str] = "results") -> None:
    Path.mkdir(Path(dirname), exist_ok=True)

    for photo_id in photo_id_lst:
        content = fetch_content(photo_id)
        if content:
            write_file(photo_id, content, dirname)

def main() -> None:
    start_time = perf_counter()

    download_all(photo_id_lst=PHOTO_IDS)

    end_time = perf_counter()

    print(f"Total execution time(synchronous): {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
