# github.com/bryangoodrich/python-exercises
# code/0004/0004.py
import random
import asyncio

async def process_batches(batch):
    r = random.uniform(1, 5)
    print(f"Processing batch {batch}")
    await asyncio.sleep(r)
    return sum([item*2 for item in batch])

async def process_data(data):
    tasks = [process_batches(batch) for batch in data]
    return await asyncio.gather(*tasks)

data = [
    (1, 1, 1), (2, 2, 2), (3, 3, 3),
    (4, 4, 4), (5, 5, 5), (6, 6, 6),
    (7, 7, 7), (8, 8, 8), (9, 9, 9)
]

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    processed_data = loop.run_until_complete(process_data(data))
    loop.close()

    print(list(processed_data))
    # [6, 12, 18, 24, 30, 36, 42, 48, 54]
