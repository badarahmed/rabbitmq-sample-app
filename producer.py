import pika
import json
import requests
from config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_QUEUE, RABBITMQ_USERNAME, RABBITMQ_PASSWORD
from config import KEYCLOAK_SERVER_URL, KEYCLOAK_REALM_NAME, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, KEYCLOAK_USERNAME, KEYCLOAK_PASSWORD, KEYCLOAK_GRANT_TYPE
from utils import get_access_token

def send_task(task):
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    message = json.dumps(task)
    channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=message, properties=pika.BasicProperties(delivery_mode=2))

    print(f" [x] Sent {task}")
    connection.close()

def main():
    access_token = get_access_token(KEYCLOAK_SERVER_URL, KEYCLOAK_REALM_NAME, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, KEYCLOAK_USERNAME, KEYCLOAK_PASSWORD, KEYCLOAK_GRANT_TYPE)
    headers = {'Authorization': f'Bearer {access_token}'}

    task = {'task_id': 1, 'task_data': 'Sample task data'}
    send_task(task)

if __name__ == "__main__":
    main()
