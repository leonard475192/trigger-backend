from datetime import datetime
from sqlalchemy.orm import Session

from models.rental import Rental
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
