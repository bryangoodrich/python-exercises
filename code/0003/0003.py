# code/0003/0003.py
import concurrent.futures
import random
import time

def func(batch):
    r = random.uniform(1, 5)
    print(f"Processing batch {batch}")
    time.sleep(r)
    return sum([item*2 for item in batch])

data = [
    (1, 1, 1), (2, 2, 2), (3, 3, 3),
    (4, 4, 4), (5, 5, 5), (6, 6, 6),
    (7, 7, 7), (8, 8, 8), (9, 9, 9)
]

# If order is not necessary
# random.shuffle(data)

with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    processed_data = executor.map(func, data)

print(list(processed_data))
# [6, 12, 18, 24, 30, 36, 42, 48, 54]
