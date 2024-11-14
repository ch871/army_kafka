import hostage_consumer.app.repository.hostage_repository as hostage_repos
from db.repositories import device_repo, terrorist_repo, location_repo


def insert_hostage_service(kafka_hostage):
    hostage = kafka_hostage.value
    hostage_device = hostage["device_info"]
    hostage_location = hostage["location"]

    terrorist_id = terrorist_repo.insert_terrorist(
        email=hostage["email"],
        username=hostage["username"],
        created_at=hostage["created_at"],
        ip_address=hostage["ip_address"]
    )

    device_repo.insert_device(
        browser=hostage_device["browser"],
        device_id=hostage_device["device_id"],
        os=hostage_device["os"],
        terrorist_id=terrorist_id
    )

    location_repo.insert_location(
        latitude=hostage_location["latitude"],
        longitude=hostage_location["longitude"],
        country=hostage_location["country"],
        city=hostage_location["city"],
        terrorist_id=terrorist_id
    )
    hostage_repos.insert_hostage(
        sentence=hostage["sentence"],
        terrorist_id=terrorist_id
    )
    print("consumed hostage")
