from sqlalchemy.orm import Session

from models.locker import Locker
from schemas import admin


def create_locker(db: Session, locker: admin.LockerCreateReq):
    db_locker = Locker(**locker.dict())
    db.add(db_locker)
    db.commit()
    db.refresh(db_locker)
    return db_locker


def find_locker_by_alloc(db: Session, parking_id: int, alloc: str):
    return (
        db.query(Locker)
        .filter(Locker.parking_id == parking_id and Locker.alloc == alloc)
        .first()
    )


def find_locker_by_id(db: Session, locker_id: int) -> Locker:
    return db.query(Locker).filter(Locker.id == locker_id).first()
