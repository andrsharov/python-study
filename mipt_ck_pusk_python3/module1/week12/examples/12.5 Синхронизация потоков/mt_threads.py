from threading import Thread


def print_multiplication_table(n):
    for i in range(1, 10):
        print(n, '*', i, '=', i * n)


threads = [
    Thread(target=print_multiplication_table, args=(i,))
    for i in range(1, 10)
]
for t in threads:
    t.start()
