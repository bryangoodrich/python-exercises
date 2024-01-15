import random
import math

class Bag:
    def __init__(self):
        self._items = []
        self._size = 0
    
    def add(self, item):
        self._items.append(item)
        self._size += 1
    
    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def iterate(self):
        for item in self._items:
            yield item

class Stats:
    def __init__(self):
        self._bag = Bag()
    
    def add_data(self, data):
        self._bag.add(data)
    
    def calculate_mean(self):
        if self._bag.is_empty():
            return None
        return sum(self._bag.iterate()) / self._bag.size()
    
    def calculate_stddev(self):
        if self._bag.size() < 2:
            return None

        mean = self.calculate_mean()
        stddev_sum = sum((x - mean) ** 2 for x in self._bag.iterate())
        return math.sqrt(stddev_sum / (self._bag.size() - 1))

    def summary(self):
        mean = self.calculate_mean()
        stddev = self.calculate_stddev()

        if mean is not None:
            print(f"Mean:    {mean:.2f}")
        else:
            print("Mean:    N/A (Empty Bag)")

        if stddev is not None:
            print(f"Std dev: {stddev:.2f}")
        else:
            print("Std dev: N/A (Insufficient Data)")

        print(f"Size:    {self._bag.size()}")


# Example Usage:
calc = Stats()
for _ in range(100):
    random_number = random.uniform(1, 50)
    calc.add_data(random_number)

calc.summary()
# Mean:    23.96
# Std dev: 13.66
# Size:    100ß
