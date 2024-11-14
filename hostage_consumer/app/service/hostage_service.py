import hostage_consumer.app.repository.hostage_repository as hostage_repos


def insert_hostage_service(kafka_hostage):
    hostage = kafka_hostage.value
    hostage_repos.insert_explosive(hostage)
    print("consumed hostage")
