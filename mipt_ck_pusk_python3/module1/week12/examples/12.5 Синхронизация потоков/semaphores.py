import threading
import time
import socket


domains = [line.strip() for line in open('domains.csv')]
max_connections = 4

connection_sem = threading.BoundedSemaphore(value=max_connections)


def check_free(domain):
    ok = True
    addr = 'python' + domain
    with connection_sem:
        try:
            socket.getaddrinfo(addr, 80)
        except OSError:
            ok = False
    print(addr + ': ' + ('занято' if ok else 'свободно') + '\n', end='')


start = time.perf_counter()
threads = []
for d in domains:
    t = threading.Thread(target=check_free, args=(d,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
end = time.perf_counter()
print(f'{len(domains)} domains in {end-start:0.2f} sec.')

# 1   - 32.86
# 2   - 16.84
# 3   - 15.73
# 4   - 11.45
# 5   - 10.74
# 10  - 11.39
# 100 - 10.61
# 500 - 11.27
# no semaphore - 11.24

# python.mil 11.062690199999906
# python.ac 11.053585699999985
# python.sg 11.051137899999958

# 1   - 6.37
# 2   - 2.92
# 3   - 1.25
# 4   - 1.82
# 5   - 0.97
# 10  - 1.07
# 100 - 4.10
# 500 - 4.14
# no semaphore - 4.18
