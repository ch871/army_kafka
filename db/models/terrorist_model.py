from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models import Base


class Terrorist(Base):
    __tablename__ = "terrorists"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(String)

    device = relationship("Device", back_populates="terrorist", uselist=False)
    location = relationship("Location", back_populates="terrorist", uselist=False)

    explosives = relationship("Explosive", back_populates="terrorist")
    hostages = relationship("Hostage", back_populates="terrorist")
