from kafka import KafkaProducer
from config import config
import json
import time

from data import get_registered_user

sleep_time = config["SLEEP_TIME"]

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers = "localhost:29092",
                         value_serializer=json_serializer)


if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send(config["ORDER_TOPIC"], registered_user)
        time.sleep(sleep_time)
