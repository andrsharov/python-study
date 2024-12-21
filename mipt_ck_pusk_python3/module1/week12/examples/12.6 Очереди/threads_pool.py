from threading import Thread
import time
import socket
from queue import Queue


def main():
    domains = [line.strip() for line in open('domains.csv')]
    max_workers = 10

    start = time.perf_counter()
    jobs = Queue()
    results = Queue()
    create_threads(jobs, results, max_workers)
    process(jobs, domains)
    print_results(results)
    end = time.perf_counter()
    print(f'{len(domains)} domains in {end-start:0.2f} sec.')


def create_threads(jobs, results, max_workers):
    for _ in range(max_workers):
        thread = Thread(target=worker,
                        args=(jobs, results),
                        daemon=True)
        thread.start()


def process(jobs, domains):
    for d in domains:
        jobs.put(d)
    jobs.join()


def print_results(results):
    while not results.empty():
        domain, free = results.get()
        # print(f'python{domain} is ' + 'free' if free else 'occupied')


def worker(jobs, results):
    while True:
        domain = jobs.get()
        free = check_free(domain)
        results.put((domain, free))
        jobs.task_done()


def check_free(domain):
    addr = 'python' + domain
    try:
        socket.getaddrinfo(addr, 80)
    except OSError:
        return True
    return False


if __name__ == '__main__':
    main()

'''
1       5.30
2       4.07
4       1.19
5       1.56
10      2.01
20      1.12
50      2.46
100     4.14
'''
