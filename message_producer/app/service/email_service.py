import message_producer.app.kafka_producer.email_producer as email_producer
from message_producer.app.service.uttils import check_terror_message


def sorting_emails(email):
    sentences = email["sentences"]
    for sentence in sentences:
        checked_message = check_terror_message(sentence)
        if checked_message is "explosive":
            email_producer.produce_explosive_messages(email)
            return
        if checked_message is "hostage":
            email_producer.produce_hostage_messages(email)
            return
        else:
            email_producer.produce_all_messages(email)
