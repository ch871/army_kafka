from db.models import Terrorist, Device, Location, Explosive
from db.database import session_maker


def insert_explosive(kafka_hostage):
    hostage = kafka_hostage.value
    hostage_device = hostage["device_info"]
    hostage_location = hostage["location"]
    with session_maker() as session:
        sql_details = Terrorist(
            email=hostage["email"],
            username=hostage["username"],
            created_at=hostage["created_at"],
            ip_address=hostage["ip_address"],
            device=Device(
                browser=hostage_device["browser"],
                device_id=hostage_device["device_id"],
                os=hostage_device["os"],
            ),
            location=Location(
                latitude=hostage_location["latitude"],
                longitude=hostage_location["longitude"],
                country=hostage_location["country"],
                city=hostage_location["city"],
            ),
            explosives=[
                Explosive(sentence=sentence)
                for sentence in hostage["sentences"]
            ],
            hostages=[]
        )
        session.add(sql_details)
        session.commit()
        session.refresh(sql_details)
    print("consumed hostage")



