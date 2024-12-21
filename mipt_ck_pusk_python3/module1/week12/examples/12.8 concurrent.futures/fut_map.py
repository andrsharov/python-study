from concurrent.futures import ThreadPoolExecutor
import socket

def check_free(domain):
    addr = 'python' + domain
    try:
        socket.getaddrinfo(addr, 80)
    except OSError:
        print(addr + ' is free')

domains = [line.strip() for line in open('domains.csv')]
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(check_free, domains)
