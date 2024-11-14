import explosive_consumer.app.repository.explosive_repository as explosive_repos
from db.repositories import device_repo, terrorist_repo, location_repo


def insert_explosive_service(kafka_explosive):
    explosive = kafka_explosive.value
    explosive_device = explosive["device_info"]
    explosive_location = explosive["location"]

    terrorist_id = terrorist_repo.insert_terrorist(
        email=explosive["email"],
        username=explosive["username"],
        created_at=explosive["created_at"],
        ip_address=explosive["ip_address"]
    )

    device_repo.insert_device(
        browser=explosive_device["browser"],
        device_id=explosive_device["device_id"],
        os=explosive_device["os"],
        terrorist_id=terrorist_id
    )

    location_repo.insert_location(
        latitude=explosive_location["latitude"],
        longitude=explosive_location["longitude"],
        country=explosive_location["country"],
        city=explosive_location["city"],
        terrorist_id=terrorist_id
    )
    explosive_repos.insert_explosive(
        sentence=explosive["sentence"],
        terrorist_id=terrorist_id
    )
    print("consumed explosive")

