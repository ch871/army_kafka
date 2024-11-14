from dotenv import load_dotenv
from kafka_settings.consumer import consume
import hostage_consumer.app.service.hostage_service as hostage_service
import os

load_dotenv(verbose=True)
hostage_topic = os.environ["HOSTAGE_TOPIC"]


def consume_hostage():
    consume(
        topic=hostage_topic,
        function=hostage_service.insert_hostage_service
    )
