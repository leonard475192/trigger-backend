from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from .database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, index=True, primary_key=True, comment="id")
    type = Column(String, index=True, comment="車種")
    number = Column(String, index=True, comment="ナンバープレート")

    images = relationship("Image", back_populates="car")
    rentals = relationship("Rental", back_populates="car")
