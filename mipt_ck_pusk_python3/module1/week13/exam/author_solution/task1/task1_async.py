import asyncio
from itertools import cycle

done = asyncio.Event()


async def indicate():
    for c in cycle('\|/-'):
        print('\b' + c, end='', flush=True)
        await asyncio.sleep(0.1)
        if done.is_set():
            print()
            break


async def work():
    a = 3
    b = 1000
    n = 3_111_111
    batch = n // 100
    for i in range(101):
        for j in range(batch * i, min(batch * (i + 1), n)):
            c = a ** b
        # Необходимо явно указать возможность переключения
        # на другие сопрограммы
        await asyncio.sleep(0)
    done.set()


async def main():
    ind = asyncio.create_task(indicate())
    await work()


if __name__ == '__main__':
    asyncio.run(main())
