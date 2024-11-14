from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models import Base


class Explosive(Base):
    __tablename__ = "explosives"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String)

    terrorist_id = Column(Integer, ForeignKey("terrorists.id"))

    terrorist = relationship("Terrorist", back_populates="explosives")

