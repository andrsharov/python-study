import asyncio
import time

import httpx


async def check_speed(url):
    """
    Определяет скорость загрузки данных.
    Делает три запроса с небольшой задержкой
    и возвращает медианное значение.
    """
    print(f'Checking {url}...\n', end='', flush=True)
    results = []
    for i in range(3):
        t0 = time.time()
        # Создаем каждый раз нового клиента
        # чтобы избежать погрешностей
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
        r.raise_for_status()
        t1 = time.time()
        results.append(t1 - t0)
        await asyncio.sleep(0.5)
    results.sort()
    return url, results[1]


async def main():
    urls = [line.strip() + 'ls-lR.gz' for line in open('mirrors.txt')]
    tasks = [
        asyncio.create_task(check_speed(url))
        for url in urls
    ]
    for f in asyncio.as_completed(tasks):
        url, speed = await f
        print(url, speed)


if __name__ == '__main__':
    asyncio.run(main())
