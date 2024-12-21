from concurrent.futures import ThreadPoolExecutor, as_completed
import socket

def check_free(domain):
    addr = 'python' + domain
    try:
        socket.getaddrinfo(addr, 80)
    except OSError:
        return True
    return False

domains = [line.strip() for line in open('domains.csv')]
with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_addr = {executor.submit(check_free, d): d
               for d in domains}
    for f in as_completed(future_to_addr.keys()):
        result = f.result()
        addr = future_to_addr[f]
        print(addr, result)
