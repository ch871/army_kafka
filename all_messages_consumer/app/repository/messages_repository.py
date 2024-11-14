from db.database import get_messages_collection

messages_collection = get_messages_collection()


def insert_message(message_to_add):
    message = messages_collection.insert_one(message_to_add)
    return message.inserted_id
