from dotenv import load_dotenv
from kafka_settings.consumer import consume
import hostage_consumer.app.repository.hostage_repository as hostage_repository
import os

load_dotenv(verbose=True)
hostage_topic = os.environ["HOSTAGE_TOPIC"]


def consume_hostage():
    consume(
        topic=hostage_topic,
        function=hostage_repository.insert_hostage
    )
