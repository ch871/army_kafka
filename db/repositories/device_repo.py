from db.database import session_maker
from db.models import Device


def insert_device(browser, os, device_id, terrorist_id):
    with session_maker() as session:
        device = Device(
            browser=browser,
            os=os,
            device_id=device_id,
            terrorist_id=terrorist_id
        )
        session.add(device)
        session.commit()
        session.refresh(device)
        return device.id
