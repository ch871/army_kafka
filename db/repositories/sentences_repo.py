from db.database import session_maker
from db.models import Terrorist


def get_all_sentences_by_email(email_to_serch):
    with session_maker() as session:
        terrorist = session.query(Terrorist).filter(Terrorist.email == email_to_serch).first()
        return {
            'hostages': [hostage.sentence for hostage in terrorist.hostages],
            "explosives": [explosive.sentence for explosive in terrorist.explosives]
        }
