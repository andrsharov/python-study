import threading
import time


lock_1 = threading.Lock()
lock_2 = threading.Lock()


def f1():
    with lock_1:
        time.sleep(0.1)
        with lock_2:
            print('OK')


def f2():
    with lock_2:
        time.sleep(0.1)
        with lock_1:
            print('OK')


t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
