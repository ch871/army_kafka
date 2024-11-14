from db.database import session_maker
from db.models import Explosive


def insert_explosive(explosive_to_add):
    with session_maker() as session:
        explosive = Explosive(
            sentence=explosive_to_add["sentences"]
        )
        session.add(explosive)
        session.commit()
        session.refresh(explosive)
        return explosive

