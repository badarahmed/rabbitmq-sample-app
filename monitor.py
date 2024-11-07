import pika
import json
import time
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_QUEUE, RABBITMQ_USERNAME, RABBITMQ_PASSWORD

def monitor_tasks():
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    def callback(ch, method, properties, body):
        task = json.loads(body)
        print(f"Monitoring task: {task}")
        # Add logic to monitor task status and retry failed tasks
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)

    print(' [*] Monitoring tasks. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    monitor_tasks()
