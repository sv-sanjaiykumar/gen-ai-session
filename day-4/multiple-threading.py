import threading
import time
def cook_pasta():
    print("Cooking pasta...")
    time.sleep(10)
    print("Pasta is ready!")

def make_sauce():
    print("Making sauce...")
    time.sleep(8)
    print("Sauce is ready!")

def main():
    pasta_thread = threading.Thread(target=cook_pasta)
    sauce_thread = threading.Thread(target=make_sauce)

    pasta_thread.start()
    sauce_thread.start()  

    pasta_thread.join()
    sauce_thread.join()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    start_time = time.time()
    main()