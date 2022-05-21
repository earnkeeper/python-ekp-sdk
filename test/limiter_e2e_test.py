import asyncio
import time
from ekp_sdk.services import Limiter

async def limited_method(limiter, i, start_time):
    await limiter.acquire()
    print(f'{i} - {round(time.perf_counter() - start_time,1)} - {limiter.open} - start')
    await asyncio.sleep(5)
    limiter.release()

async def runner(start_time):
    limiter = Limiter(250, 4)
    i = 0
    futures = []
    while True:
        i += 1
        futures.append(limited_method(limiter, i, start_time))
        if i > 100:
            break
        
    await asyncio.gather(*futures)

start_time = time.perf_counter()
asyncio.run(runner(start_time))
