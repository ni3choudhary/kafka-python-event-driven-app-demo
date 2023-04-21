import json

from kafka import KafkaConsumer, KafkaProducer
from config import config
from order_backend import json_serializer
import sys
import os

ORDER_TOPIC = config["ORDER_TOPIC"]
ORDER_CONFIRMED_TOPIC = config["ORDER_CONFIRMED_TOPIC"]

consumer = KafkaConsumer(
    ORDER_TOPIC, 
    bootstrap_servers="localhost:29092"
)

producer = KafkaProducer(bootstrap_servers="localhost:29092",
                         value_serializer=json_serializer)

if __name__ == "__main__":
    print(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        while True:
            for msg in consumer:
                consumed_message = json.loads(msg.value)
                print(consumed_message)

                customer_id = consumed_message["user_id"]
                order_id = consumed_message["order_id"]
                customer_email = consumed_message["email"]
                total_cost = consumed_message["total_cost"]

                data = {
                "customer_id": customer_id,
                "order_id": order_id,
                "customer_email": customer_email,
                "total_cost": total_cost
                }

                print("Successful Transaction..")
                producer.send(ORDER_CONFIRMED_TOPIC, data)

    except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
