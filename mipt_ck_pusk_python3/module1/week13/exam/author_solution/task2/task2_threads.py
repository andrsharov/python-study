from itertools import cycle, islice
import threading
import time

percent = threading.Semaphore(0)
done = threading.Event()


def indicate():
    for c in cycle('\|/-'):
        print(f'\033[9D[ {percent._value:3}% ]{c}', end='', flush=True)
        time.sleep(0.1)
        if done.is_set():
            print('\033[9DDone     ')
            break


def work():
    a = 3
    b = 1000
    n = 3_111_111
    # разобъем заранее задачу на 100 кусочков, чтобы
    # не тратить время на дополнительные проверки на каждом шаге
    batch = n // 100
    for i in range(101):
        for j in range(batch * i, min(batch * (i + 1), n)):
            c = a ** b
        percent.release()
    done.set()


threading.Thread(target=indicate).start()
work()
