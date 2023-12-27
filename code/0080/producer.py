import time
import random
import json

from pika import ConnectionParameters, BlockingConnection

parameters = ConnectionParameters('localhost')
connection = BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='shared')

mock = [
    {'device': 'sensor1', 'temp': random.uniform(15, 25)},
    {'device': 'sensor2', 'humidity': random.uniform(70, 80)},
    {'device': 'estimated', 'value': random.choice([True, False])},
]

for i in range(10):
    message = {"message": i, "data": random.choice(mock)}
    channel.basic_publish(
        exchange='',
        routing_key='shared',
        body=json.dumps(message))
    print("Sent:", message)
    time.sleep(0.5)

connection.close()
