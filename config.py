# Configuration settings for RabbitMQ and Keycloak

# RabbitMQ settings
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = 'task_queue'
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'

# Keycloak settings
KEYCLOAK_SERVER_URL = 'http://localhost:8080/auth'
KEYCLOAK_REALM_NAME = 'myrealm'
KEYCLOAK_CLIENT_ID = 'myclient'
KEYCLOAK_CLIENT_SECRET = 'mysecret'
KEYCLOAK_USERNAME = 'myuser'
KEYCLOAK_PASSWORD = 'mypassword'
KEYCLOAK_GRANT_TYPE = 'password'
