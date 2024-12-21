import asyncio


async def main():
    process = await asyncio.create_subprocess_shell(
        "zip - gen_pipe.png",
        stdout=asyncio.subprocess.PIPE
    )
    size = 0
    while True:
        buf = await process.stdout.read(1024)
        if not buf:
            break
        size += len(buf)

    print(size)


if __name__ == '__main__':
    asyncio.run(main())
