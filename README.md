# RabbitMQ Task Processing System with Keycloak Authentication

This project is a task processing system where tasks are sent to a RabbitMQ queue and workers consume these tasks to perform various operations. The communication between the task producer and the worker is secured using OAuth 2 authentication with Keycloak.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure RabbitMQ and Keycloak settings in `config.py`.

## Usage Instructions

1. Start the RabbitMQ server.

2. Run the producer to send tasks to the RabbitMQ queue:
   ```bash
   python producer.py
   ```

3. Run the worker to consume tasks from the RabbitMQ queue and process them:
   ```bash
   python worker.py
   ```

4. Monitor task status and retry failed tasks using:
   ```bash
   python monitor.py
   ```
