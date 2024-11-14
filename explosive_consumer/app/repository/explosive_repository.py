from db.database import session_maker
from db.models import Explosive


def insert_explosive(sentence, terrorist_id):
    with session_maker() as session:
        explosive = Explosive(
            sentence=sentence,
            terrorist_id=terrorist_id
        )
        session.add(explosive)
        session.commit()
        session.refresh(explosive)
        return explosive

