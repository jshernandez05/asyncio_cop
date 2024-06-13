from pathlib import Path
from time import perf_counter
from typing import List
import requests


def fetch(url: str) -> str:
    print(f"Starting fetch for {url}")
    response = requests.get(url)
    print(f"Completed fetch for {url}")
    return response.text


def write_to_file(filename: Path, content: str) -> None:
    print(f"Starting write to {filename.stem}")
    with open(filename, "w") as f:
        f.write(content)
    print(f"Completed write to {filename.stem}")


def main() -> None:
    base_url: str = "http://example"
    domain_ext: List[str] = [".com", ".org", ".net"]
    urls: List[str] = [f"{base_url}{ext}" for ext in domain_ext]

    dirname = Path("results")

    start_time = perf_counter()

    Path.mkdir(dirname, exist_ok=True)

    results: List[str] = [fetch(url) for url in urls]

    # Write results to files
    for i, result in enumerate(results):
        filepath = Path(f"{dirname}/async_result_{i+1}.txt")
        write_to_file(filepath, result)

    end_time = perf_counter()

    print(f"Total execution time(synchronous): {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
