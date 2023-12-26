from queue import Queue
from threading import Thread
from time import sleep
import random

mock = [
    {'device': 'sensor1', 'temp': random.uniform(15, 25)},
    {'device': 'sensor2', 'humidity': random.uniform(70, 80)},
    {'device': 'estimated', 'value': random.choice([True, False])},
]

data = Queue()

def producer():
    for i in range(10):
        message = {"message": i, "data": random.choice(mock)}
        data.put(message)
        sleep(random.uniform(0.1, 0.5)) 
        print(f'Produced {message}')

def consumer():
    while True:
        sleep(random.uniform(0.4, 0.8)) 
        if data.empty():
            break
        message = data.get()
        print(f'Consumed {message}')
        data.task_done()

if __name__ == "__main__":
    producer_thread = Thread(target=producer)
    consumer_thread = Thread(target=consumer)
    
    producer_thread.start()
    consumer_thread.start() 
    
    producer_thread.join()
    consumer_thread.join()

# Produced {'message': 0, 'data': {'device': 'sensor1', 'temp': 16.4190}}
# Produced {'message': 1, 'data': {'device': 'sensor1', 'temp': 16.4190}}
# Consumed {'message': 0, 'data': {'device': 'sensor1', 'temp': 16.4190}}
# Produced {'message': 2, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Produced {'message': 3, 'data': {'device': 'estimated', 'value': True}}
# Consumed {'message': 1, 'data': {'device': 'sensor1', 'temp': 16.4190}}
# Produced {'message': 4, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Produced {'message': 5, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Produced {'message': 6, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Produced {'message': 7, 'data': {'device': 'sensor1', 'temp': 16.4190}}
# Consumed {'message': 2, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Produced {'message': 8, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Produced {'message': 9, 'data': {'device': 'sensor1', 'temp': 16.4190}}
# Consumed {'message': 3, 'data': {'device': 'estimated', 'value': True}}
# Consumed {'message': 4, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Consumed {'message': 5, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Consumed {'message': 6, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Consumed {'message': 7, 'data': {'device': 'sensor1', 'temp': 16.4190}}
# Consumed {'message': 8, 'data': {'device': 'sensor2', 'humidity': 72.6765}}
# Consumed {'message': 9, 'data': {'device': 'sensor1', 'temp': 16.4190}}