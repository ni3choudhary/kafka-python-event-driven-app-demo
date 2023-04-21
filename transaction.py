import json

from kafka import KafkaConsumer
from config import config

ORDER_TOPIC = config["ORDER_TOPIC"]

consumer = KafkaConsumer(
    ORDER_TOPIC, 
    bootstrap_servers="localhost:29092"
)

if __name__ == "__main__":
    print(' [*] Waiting for messages. To exit press CTRL+C')

    while True:
        for msg in consumer:
            consumed_message = json.loads(msg.value)
            print(consumed_message)
