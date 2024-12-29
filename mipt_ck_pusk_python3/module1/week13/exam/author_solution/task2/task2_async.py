import asyncio
from itertools import cycle

done = asyncio.Event()
percent = asyncio.Semaphore(0)


async def indicate():
    for c in cycle('\|/-'):
        print(f'\033[9D[ {percent._value:3}% ]{c}', end='', flush=True)
        await asyncio.sleep(0.1)
        if done.is_set():
            print('\033[9DDone     ')
            break


async def work():
    a = 3
    b = 1000
    n = 3_111_111
    # разобъем заранее задачу на 100 кусочков, чтобы
    # не тратить время на дополнительные проверки на каждом шаге
    batch = n // 100
    for i in range(101):
        for j in range(batch * i, min(batch * (i + 1), n)):
            c = a ** b
        percent.release()
        await asyncio.sleep(0)
    done.set()


async def main():
    ind = asyncio.create_task(indicate())
    await work()
    await ind  # Чтобы увидеть последнюю надпись


if __name__ == '__main__':
    asyncio.run(main())
