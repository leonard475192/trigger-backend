from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from db import Base


class Parking(Base):
    __tablename__ = "parking"

    id = Column(Integer, index=True, primary_key=True, comment="ID")
    name = Column(String, index=True, comment="パーキング名")
    address = Column(String, index=True, comment="住所")
    geometry = Column(Geometry(geometry_type="POINT", dimension=2, srid=4326))

    lockers = relationship("Locker", back_populates="parking")
