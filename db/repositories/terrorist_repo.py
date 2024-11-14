from db.database import session_maker
from db.models import Terrorist


def insert_terrorist(email, username, ip_address, created_at):
    with session_maker() as session:
        terrorist = Terrorist(
            email=email,
            username=username,
            ip_address=ip_address,
            created_at=created_at
        )
        session.add(terrorist)
        session.commit()
        session.refresh(terrorist)
        return terrorist.id

