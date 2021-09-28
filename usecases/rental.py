from datetime import datetime
from typing import List
from sqlalchemy.sql.expression import label
from schemas.borrower import CarUnlockReq
from sqlalchemy.orm import Session

from models.rental import Rental
from models.image import Image
from models.car import Car
from models.locker import Locker
from models.parking import Parking
from schemas import lender


def create_rental(db: Session, rental: lender.RentalCreateReq, locker_id: int):
    # TODO **rental.dict()による方法
    db_rental = Rental(
        car_id=rental.carId,
        locker_id=locker_id,
        fee_yen=rental.fee,
        available_begin=rental.availableDateTimes.begin,
        available_end=rental.availableDateTimes.end,
    )
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental


def select_all(db: Session) -> List[Rental]:
    now = datetime.now()
    return db.query(Rental).filter(Rental.available_end >= now).all()


def find_by_id(db: Session, id: int):
    # FIXME images が何故か取得できない
    db_rental = (
        db.query(
            Rental.id,
            Rental.car_id,
            Rental.fee_yen.label("fee"),
            Car.type,
            Car.number,
            Car.images.label("images"),
            Parking,
            Rental.available_begin,
            Rental.available_end,
        )
        .join(Car, Car.id == Rental.car_id)
        .join(Locker, Locker.id == Rental.locker_id)
        .join(Parking, Parking.id == Locker.parking_id)
        .filter(Rental.id == id)
        .first()
    )
    return db_rental


def find_rental_activate_by_car_id(db: Session, car_id: int):
    now = datetime.now()
    return (
        db.query(Rental)
        .filter(Rental.car_id == car_id and Rental.available_end >= now)
        .first()
    )


def delete_rental(db: Session, car_id: int):
    db_rental = find_rental_activate_by_car_id(db=db, car_id=car_id)
    db_rental.delete_flag = True
    db.commit()
    return db_rental


def enable_use_flag(db: Session, car_id: int) -> Rental:
    rnt = find_rental_activate_by_car_id(db, car_id)
    rnt.in_use_flag = True
    db.commit()
    return rnt


def disable_use_flag(db: Session, car_id: int) -> Rental:
    rnt = find_rental_activate_by_car_id(db, car_id)
    rnt.in_use_flag = False
    db.commit()
    return rnt
