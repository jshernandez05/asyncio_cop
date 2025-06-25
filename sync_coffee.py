from time import perf_counter, sleep

def brew_coffee() -> str:
    print("Started brew_coffee")
    sleep(3)  # Regular blocking sleep
    print("Completed brew_coffee")
    return "Coffee Ready"

def toast_bagel() -> str:
    print("Started toast_bagel")
    sleep(3)  # Regular blocking sleep
    print("Completed toast_bagel")
    return "Bagel Ready"

def main() -> None:
    start_time = perf_counter()
    
    # Tasks run one after another (sequentially)
    coffee_result = brew_coffee()
    bagel_result = toast_bagel()

    elapsed_time = perf_counter() - start_time

    print(f"Coffee status: {coffee_result}")
    print(f"Bagel status: {bagel_result}")
    print(f"Total execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
