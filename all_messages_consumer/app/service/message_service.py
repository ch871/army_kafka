import all_messages_consumer.app.repository.messages_repository as message_repos


def insert_message(kafka_message):
    message = kafka_message.value
    message_repos.insert_message(message)
    print("consumed message")
