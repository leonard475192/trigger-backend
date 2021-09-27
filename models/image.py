from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, index=True, primary_key=True, comment="ID")
    car_id = Column(Integer, ForeignKey("cars.id"))
    path = Column(String, comment="s3_path")

    car = relationship("Car", back_populates="images")