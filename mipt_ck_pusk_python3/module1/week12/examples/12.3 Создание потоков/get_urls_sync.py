import time

import httpx


base_url = 'http://example'
domains = ['.com', '.net', '.org', '.edu']


def get_page(domain):
    print(f'connecting {domain}...')
    r = httpx.get(base_url + domain)
    r.raise_for_status()
    print(f'response from {domain}: {r}')
    return r.text


start = time.perf_counter()
for d in domains:
    get_page(d)
end = time.perf_counter()
print(f'{len(domains)} pages loaded in {end-start:0.2f} sec.')
