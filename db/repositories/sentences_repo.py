from collections import Counter

from db.database import session_maker
from db.models import Terrorist, Explosive, Hostage


def get_all_sentences_by_email(email_to_serch):
    with session_maker() as session:
        terrorist = session.query(Terrorist).filter(Terrorist.email == email_to_serch).first()
        return {
            'hostages': [hostage.sentence for hostage in terrorist.hostages],
            "explosives": [explosive.sentence for explosive in terrorist.explosives]
        }


def find_most_common_word():
    with session_maker() as session:
        explosive_sentences = [explosive.sentence for explosive in session.query(Explosive).all()]
        hostage_sentences = [hostage.sentence for hostage in session.query(Hostage).all()]
        all_sentences = hostage_sentences + explosive_sentences
        all_joined = " ".join(all_sentences)
        all_words = all_joined.split()
        most_common_word = Counter(all_words).most_common(1)

        return most_common_word
