import pika
import json
import requests
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_QUEUE, RABBITMQ_USERNAME, RABBITMQ_PASSWORD
from config import KEYCLOAK_SERVER_URL, KEYCLOAK_REALM_NAME, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, KEYCLOAK_USERNAME, KEYCLOAK_PASSWORD, KEYCLOAK_GRANT_TYPE
from utils import get_access_token

def process_task(task):
    print(f"Processing task: {task}")

def main():
    access_token = get_access_token(KEYCLOAK_SERVER_URL, KEYCLOAK_REALM_NAME, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, KEYCLOAK_USERNAME, KEYCLOAK_PASSWORD, KEYCLOAK_GRANT_TYPE)
    headers = {'Authorization': f'Bearer {access_token}'}

    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    def callback(ch, method, properties, body):
        task = json.loads(body)
        process_task(task)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
