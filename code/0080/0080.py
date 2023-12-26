from pika import BlockingConnection, ConnectionParameters
from time import sleep
import random


mock = [
    {'device': 'sensor1', 'temp': random.uniform(15, 25)},
    {'device': 'sensor2', 'humidity': random.uniform(70, 80)}, 
    {'device': 'actuator1', 'value': random.choice([True, False])},
]

param = ConnectionParameters('localhost')
connection = BlockingConnection(param)
channel = connection.channel()
channel.queue_declare(queue='data')

def producer(queue):
    for i in range(10):
        sleep(random.uniform(0.1, 0.5)) 
        message = {'id': i, 'data': random.choice(mock)}
        queue.basic_publish(
            exchange='',
            routing_key='data',
            body=str(message))
        print(f'Published {message}')

def callback(ch, method, props, body):
    print(f"Received {body}")

def consumer(queue):
    sleep(random.uniform(0.3, 0.6)) 
    queue.basic_consume(
        queue='data', 
        on_message_callback=callback, 
        auto_ack=True)
    queue.start_consuming()

if __name__ == '__main__':
    producer(channel)
    consumer(channel)
