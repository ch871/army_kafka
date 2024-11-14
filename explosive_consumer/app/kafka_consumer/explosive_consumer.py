from dotenv import load_dotenv
from kafka_settings.consumer import consume
import explosive_consumer.app.repository.explosive_repository as explosive_repo
import os

load_dotenv(verbose=True)
explosive_topic = os.environ["EXPLOSIVE_TOPIC"]


def consume_explosive():
    consume(
        topic=explosive_topic,
        function=explosive_repo.insert_explosive
    )
