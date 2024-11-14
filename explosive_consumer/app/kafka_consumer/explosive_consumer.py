from dotenv import load_dotenv
from kafka_settings.consumer import consume
import explosive_consumer.app.service.explosive_service as explosive_service
import os

load_dotenv(verbose=True)
explosive_topic = os.environ["EXPLOSIVE_TOPIC"]


def consume_explosive():
    consume(
        topic=explosive_topic,
        function=explosive_service.insert_explosive_service
    )
