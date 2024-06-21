import time 
import asyncio

start = time.time()

async def get_movie_tickets():
    await asyncio.sleep(7)
    print("Got the movie tickets")

async def like_ig():
    await asyncio.sleep(10)
    print('Finshed Instagram')


async def main():
    task1 = asyncio.create_task(get_movie_tickets())
    task2 = asyncio.create_task(get_movie_tickets())

    await task2
    await task1


asyncio.run(main())

end= time.time()
print("The time of execution",end-start)