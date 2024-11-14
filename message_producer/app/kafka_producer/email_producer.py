from dotenv import load_dotenv
from kafka_settings.producer import produce
import os

load_dotenv(verbose=True)
all_messages_topic = os.environ['ALL_MESSAGES_TOPIC']


def produce_all_messages(message_info):
    produce(
        topic=all_messages_topic,
        value=message_info)
