from kafka import KafkaConsumer
from config import config
import json
import sys
import os

ORDER_CONFIRMED_TOPIC = config["ORDER_CONFIRMED_TOPIC"]

consumer = KafkaConsumer(
    ORDER_CONFIRMED_TOPIC, 
    bootstrap_servers="localhost:29092"
)

total_orders_count = 0
total_revenue = 0

if __name__ == "__main__":
    print(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        while True:
            for msg in consumer:
                print("Updating analytics..")
                consumed_message = json.loads(msg.value)
                
                total_cost = float(consumed_message["total_cost"])
                total_orders_count += 1
                total_revenue += total_cost
                print(f"Orders so far today: {total_orders_count}")
                print(f"Revenue so far today: {total_revenue}")

    except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
