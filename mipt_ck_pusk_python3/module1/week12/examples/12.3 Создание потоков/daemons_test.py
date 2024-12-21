import sys
import time
import threading

def f():
    for i in range(10):
        print(i)
        time.sleep(0.1)

daemon = None
if len(sys.argv) > 1 and sys.argv[1] == '-d':
    daemon = True
threading.Thread(target=f, daemon=daemon).start()
