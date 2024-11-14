from db.database import session_maker
from db.models import Location


def insert_location(latitude, longitude, city, country, terrorist_id):
    with session_maker() as session:
        location = Location(
            latitude=latitude,
            longitude=longitude,
            city=city,
            country=country,
            terrorist_id=terrorist_id
        )
        session.add(location)
        session.commit()
        session.refresh(location)
        return location.id
