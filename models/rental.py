from sqlalchemy import Boolean, Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

from .database import Base


class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, index=True, primary_key=True, comment="ID")
    car_id = Column(Integer, ForeignKey("cars.id"))
    locker_id = Column(Integer, ForeignKey("lockers.id"))

    in_use_flag = Column(Boolean, index=False, comment="利用中判定")
    fee_yen = Column(Integer, index=True, comment="15分あたりの料金")
    available_begin = Column(Date, index=True, comment="貸し出し開始時間")
    available_end = Column(Date, index=True, comment="貸し出し終了時間")

    car = relationship("Car", back_populates="rentals")
    locker = relationship("Locker")
