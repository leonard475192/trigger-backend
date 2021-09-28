from sqlalchemy import Column, Integer, DateTime

from db import Base


class Bill(Base):
    __tablename__ = "bill"

    id = Column(Integer, index=True, primary_key=True, comment="id")
    rental_id = Column(Integer, index=True, comment="レンタルID")
    use_start = Column(DateTime, index=True, comment="利用開始時間")
    use_end = Column(DateTime, index=True, comment="利用終了時間")
    fee = Column(Integer, index=True, comment="15分あたりの料金")
