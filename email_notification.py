import json

from kafka import KafkaConsumer
from config import config
import sys
import os

ORDER_CONFIRMED_TOPIC = config["ORDER_CONFIRMED_TOPIC"]

consumer = KafkaConsumer(
    ORDER_CONFIRMED_TOPIC, 
    bootstrap_servers="localhost:29092"
)

emails_sent_so_far = set()

if __name__ == "__main__":
    print(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        while True:
            for msg in consumer:
                consumed_message = json.loads(msg.value)
                customer_email = consumed_message["customer_email"]
                order_id = consumed_message["order_id"]

                print(f"Sending Email to {customer_email} for Order ID: {order_id} ")
                emails_sent_so_far.add(customer_email)
                print(f"So far Emails Sent to {len(emails_sent_so_far)} Unique Emails")
    except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)