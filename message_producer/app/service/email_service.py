import message_producer.app.kafka_producer.email_producer as email_producer


def produce_email(email_info):
    email_producer.produce_all_messages(email_info)