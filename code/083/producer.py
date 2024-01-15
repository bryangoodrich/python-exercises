import random
import time
import json
from datetime import datetime, timedelta
from kafka import KafkaProducer 

KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'data-viz'

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

if __name__ == "__main__":
    price = random.random()*100
    start = datetime(2023, 12, 1, 9, 0, 0)
    while start < datetime(2023, 12, 1, 16, 0, 0):
        data = {'timestamp': start.isoformat(), 'price': price}
        record = json.dumps(data).encode("utf-8")
        producer.send(KAFKA_TOPIC, record)
        print(f"Writing {record}")
        price += random.gauss(0, 5)
        start += timedelta(minutes=1)
        time.sleep(0.5)
