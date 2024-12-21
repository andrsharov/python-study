import asyncio
import json

import httpx

link_source = {}
queue = asyncio.Queue()
done = asyncio.Event()

source = 'Python'
target = 'Карл Маркс'


async def worker(client: httpx.AsyncClient):
    while True:
        page_name = await queue.get()
        print('processing', page_name)
        for link in await get_links(client, page_name):
            if link == target:
                done.set()
            if link in link_source:
                continue
            if any(x.isdigit() for x in link):
                continue
            link_source[link] = page_name
            queue.put_nowait(link)


async def get_links(client: httpx.AsyncClient, page_name: str):
    url = 'https://ru.wikipedia.org/w/api.php'
    page_name = page_name.replace(' ', '_')
    params = {'action': 'parse', 'page': page_name, 'format': 'json'}
    response = await client.get(url, params=params)
    try:
        page = response.json()
    except json.JSONDecodeError:
        return ()

    try:
        return (link['*'] for link in page['parse']['links'])
    except KeyError:
        return ()


async def main():
    async with httpx.AsyncClient() as client:
        workers = [
            asyncio.create_task(worker(client))
            for _ in range(20)
        ]
        queue.put_nowait(source)
        await done.wait()

        for w in workers:
            w.cancel()
        await asyncio.gather(*workers, return_exceptions=True)

    print_path()


def print_path():
    node = target
    path = [node]
    while node != source:
        node = link_source[node]
        path.append(node)
    print(*reversed(path), sep=' -> ')


asyncio.run(main())

'Python -> Apple -> Антиутопия -> Карл Маркс'
