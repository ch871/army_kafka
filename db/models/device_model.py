from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models import Base


class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)

    terrorist_id = Column(Integer, ForeignKey("terrorists.id"))
    terrorist = relationship("Terrorist", back_populates="device")

