from db.database import session_maker
from db.models import Hostage


def insert_hostage(hostage_to_add):
    with session_maker() as session:
        hostage = Hostage(
            sentence=hostage_to_add["sentences"]
        )
        session.add(hostage)
        session.commit()
        session.refresh(hostage)
        return hostage

