from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from .database import Base


class Parking(Base):
    __tablename__ = "parkings"

    id = Column(Integer, index=True, primary_key=True, comment="ID")
    name = Column(String, index=True, comment="パーキング名")
    address = Column(String, index=True, comment="住所")
    latitude = Column(Float, index=True, comment="緯度")
    longitude = Column(Float, index=True, comment="軽度")

    lockers = relationship("Lockers", back_populates="parking")
