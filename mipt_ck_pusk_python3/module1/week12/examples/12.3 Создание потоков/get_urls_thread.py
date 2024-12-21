import threading
import time

import httpx


base_url = 'http://example'
domains = ['.com', '.net', '.org', '.edu', '.ru', '.su', '.au', '.fr', '.io']


def get_page(domain):
    print(f'connecting {domain}...')
    r = httpx.get(base_url + domain)
    print(f'response from {domain}: {r}')
    return r.text


start = time.perf_counter()
threads = []
for d in domains:
    t = threading.Thread(target=get_page, args=(d,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
end = time.perf_counter()
print(f'{len(domains)} pages loaded in {end-start:0.2f} sec.')
