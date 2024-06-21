import time
import asyncio

start = time.time()
async def fetch_file():
    print('Starting to fetch a file')
    await asyncio.sleep(1)
    print('Fetching file completed')

async def main():
    print('Starting main')
    await asyncio.gather(
    fetch_file(),
    fetch_file(),
    fetch_file(),
    )
    print('Main completed')

asyncio.run(main())

end = time.time()
print('Execution time is:',end-start)

#handling of file -aiofiles
#downloading image - aiohttp