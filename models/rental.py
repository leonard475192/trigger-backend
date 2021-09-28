from sqlalchemy import Boolean, Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from db import Base


class Rental(Base):
    __tablename__ = "rental"

    id = Column(Integer, index=True, primary_key=True, comment="ID")
    car_id = Column(Integer, ForeignKey("car.id"))
    locker_id = Column(Integer, ForeignKey("locker.id"))

    in_use_flag = Column(Boolean, default=False, comment="利用中判定")
    fee_yen = Column(Integer, index=True, comment="15分あたりの料金")
    available_begin = Column(DateTime, index=True, comment="貸し出し開始時間")
    available_end = Column(DateTime, index=True, comment="貸し出し終了時間")
    delete_flag = Column(Boolean, default=False, comment="論理削除")

    car = relationship("Car", back_populates="rentals")
    locker = relationship("Locker")
