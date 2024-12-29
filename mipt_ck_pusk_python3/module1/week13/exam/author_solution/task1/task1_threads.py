from itertools import cycle
import threading
import time

done = threading.Event()


def indicate():
    for c in cycle('\|/-'):
        print('\b' + c, end='', flush=True)
        time.sleep(0.1)
        if done.is_set():
            print()
            break


def work():
    a = 3
    b = 1000
    for i in range(10_000_000):
        c = a ** b
    done.set()


threading.Thread(target=indicate).start()
work()
