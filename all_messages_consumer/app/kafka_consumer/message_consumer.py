from dotenv import load_dotenv
from kafka_settings.consumer import consume
import all_messages_consumer.app.service.message_service as message_service
import os

load_dotenv(verbose=True)
new_message_topic = os.environ['ALL_MESSAGES_TOPIC']


def consume_members():
    consume(
        topic=new_message_topic,
        function=message_service.insert_message
    )
