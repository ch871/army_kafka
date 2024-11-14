from db.database import session_maker
from db.models import Hostage


def insert_hostage(sentence, terrorist_id):
    with session_maker() as session:
        hostage = Hostage(
            sentence=sentence,
            terrorist_id=terrorist_id
        )
        session.add(hostage)
        session.commit()
        session.refresh(hostage)
        return hostage

