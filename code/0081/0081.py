import json
import sys

from threading import Thread
from kafka import KafkaConsumer, KafkaProducer 

KAFKA_BROKER = 'localhost:9092'
CHAT_TOPIC = 'chat'

class ChatClient:
    def __init__(self, username):
        self.username = username
        self.poll_thread = None
        self.consumer = KafkaConsumer(CHAT_TOPIC, bootstrap_servers=KAFKA_BROKER)
        self.producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

    def send_message(self, message):
        msg = {'sender': self.username, 'message': message}
        self.producer.send(CHAT_TOPIC, json.dumps(msg).encode('utf-8'))

    def poll_for_messages(self):
        for msg in self.consumer:
            data = json.loads(msg.value)
            sender = data['sender']
            if sender != self.username:
                print(f"[{sender}] --> {data['message']}")

    def run(self):
        self.poll_thread = Thread(target=self.poll_for_messages)
        self.poll_thread.daemon = True
        self.poll_thread.start()
        
        while True:
            message = input()
            self.send_message(message)

if __name__ == '__main__':
    user = input("Enter your username: ")
    client = ChatClient(user)
    try:
        client.run()
    except KeyboardInterrupt:
        print(f"{client.username} leaving ...")
        sys.exit(1)
