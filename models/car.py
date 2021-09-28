from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship

from db import Base


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, index=True, primary_key=True, comment="id")
    type = Column(String, index=True, comment="車種")
    number = Column(String, index=True, comment="ナンバープレート")

    images = relationship("Image", backref=backref("child"))
    rental = relationship("Rental", back_populates="car")
