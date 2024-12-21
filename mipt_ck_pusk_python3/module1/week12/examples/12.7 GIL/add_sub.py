from threading import Thread
import time

x = 0

def add():
    global x
    for i in range(10_000_000):
        x += 1

def sub():
    global x
    for i in range(10_000_000):
        x -= 1

t1 = Thread(target=add)
t2 = Thread(target=sub)
t1.start()
t2.start()
while t1.is_alive() or t2.is_alive():
    print(x)
    time.sleep(0.05)

print(x)
