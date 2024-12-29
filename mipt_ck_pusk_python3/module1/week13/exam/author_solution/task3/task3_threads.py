from concurrent.futures import ThreadPoolExecutor, as_completed
import time

import httpx


def check_speed(url):
    """
    Определяет скорость загрузки данных.
    Делает три запроса с небольшой задержкой
    и возвращает медианное значение.
    """
    print(f'Checking {url}...\n', end='', flush=True)
    results = []
    for i in range(3):
        t0 = time.time()
        r = httpx.get(url)
        r.raise_for_status()
        t1 = time.time()
        results.append(t1 - t0)
        time.sleep(0.5)
    results.sort()
    return results[1]


urls = [line.strip() + 'ls-lR.gz' for line in open('mirrors.txt')]
with ThreadPoolExecutor(max_workers=10) as executor:
    fut_to_url = {
        executor.submit(check_speed, url): url
        for url in urls
    }
    for f in as_completed(fut_to_url.keys()):
        print(fut_to_url[f], f.result())
