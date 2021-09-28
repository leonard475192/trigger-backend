from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from db import Base


class Locker(Base):
    __tablename__ = "locker"

    id = Column(Integer, index=True, primary_key=True, comment="ID")
    parking_id = Column(Integer, ForeignKey("parking.id"))
    alloc = Column(String, index=True, comment="ロッカー番号")
    pin = Column(Integer, comment="ロッカーの鍵")

    parking = relationship("Parking", backref=backref("child"))
    rentals = relationship("Rental", back_populates="locker")
