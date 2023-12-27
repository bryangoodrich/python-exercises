import time
from pika import ConnectionParameters, BlockingConnection

def on_message(ch, method_frame, header_frame, body):
    time.sleep(1)
    print(f"{method_frame.delivery_tag} - {body}")
    ch.basic_ack(delivery_tag=method_frame.delivery_tag)

parameters = ConnectionParameters('localhost')
connection = BlockingConnection(parameters)
channel = connection.channel()
channel.basic_consume('shared', on_message)

print(' [*] Waiting for messages. To exit press CTRL+C')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
