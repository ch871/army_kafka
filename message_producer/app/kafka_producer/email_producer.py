from dotenv import load_dotenv
from kafka_settings.producer import produce
import os

load_dotenv(verbose=True)
all_messages_topic = os.environ["ALL_MESSAGES_TOPIC"]
explosive_topic = os.environ["EXPLOSIVE_TOPIC"]
hostage_topic = os.environ["HOSTAGE_TOPIC"]


def produce_all_messages(message_info):
    produce(
        topic=all_messages_topic,
        value=message_info)


def produce_explosive_messages(message_info):
    produce(
        topic=explosive_topic,
        value=message_info)


def produce_hostage_messages(message_info):
    produce(
        topic=hostage_topic,
        value=message_info)
