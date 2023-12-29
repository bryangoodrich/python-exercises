import json
import time
from datetime import datetime, timedelta
from random import normalvariate
from kafka import KafkaProducer 

def generate_data(device_id, num_records, interval, mean, std):
    dt = datetime.fromisoformat("2023-12-20 08:00:00")
    data = []
    for _ in range(num_records):
        data.append({
            "device": device_id,
            "interval": interval,
            "endtime": dt.strftime("%Y-%m-%d %H:%M:%S"),  
            "kwh": normalvariate(mean, std) 
        })
        if interval == 15:
            dt += timedelta(minutes=15)
        else:
            dt += timedelta(hours=1)
      
    return data

KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'meters'

if __name__ == '__main__':
    data = generate_data("001", 21, 15, 10, 2) \
        + generate_data("002", 21, 15, 15, 3) \
        + generate_data("003", 6, 60, 50, 10) \
        + generate_data("004", 6, 60, 80, 15) \
    
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
    for item in data:
        time.sleep(5)
        record = json.dumps(item).encode('utf-8')
        producer.send(KAFKA_TOPIC, record)
        print(f"Writing {record}")
