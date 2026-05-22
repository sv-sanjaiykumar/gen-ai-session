import threading
def task():
    for i in range(5):
        print(f"Running Thread: {i}")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()