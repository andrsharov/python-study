import asyncio

async def say(text, times):
    for _ in range(times):
        print(text)
        await asyncio.sleep(0.1)


async def main():
    results = await asyncio.gather(
        say('Hello', 5),
        say('Good bye', 5)
    )
    print(results)


asyncio.run(main())
