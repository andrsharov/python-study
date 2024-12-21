import asyncio
import time


async def check_free(domain):
    try:
        await asyncio.open_connection(
            'python' + domain, 80)
    except (OSError, asyncio.CancelledError):
        return domain, True
    else:
        return domain, False


async def main():
    domains = [line.strip() for line in open('domains.csv')]
    start = time.perf_counter()
    tasks = [check_free(d) for d in domains]
    for cor in asyncio.as_completed(tasks):
        domain, result = await cor
        free = 'free' if result else 'not free'
        print(f'python{domain} is {free}. '
              f'{time.perf_counter() - start:0.2f}')


if __name__ == '__main__':
    asyncio.run(main())
