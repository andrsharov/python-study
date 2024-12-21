from threading import Thread, Lock

print_lock = Lock()


def print_multiplication_table(n):
    for i in range(1, 10):
        with print_lock:
            print(n, '*', i, '=', i * n)


threads = [
    Thread(target=print_multiplication_table, args=(i,))
    for i in range(1, 10)
]
for t in threads:
    t.start()
