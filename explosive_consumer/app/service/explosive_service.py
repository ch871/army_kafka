import explosive_consumer.app.repository.explosive_repository as explosive_repos


def insert_explosive_service(kafka_explosive):
    explosive = kafka_explosive.value
    explosive_repos.insert_explosive(explosive)
    print("consumed explosive")
