from sqlalchemy.orm import Session
from models.rental import Rental
from models.locker import Locker
from models.bill import Bill
from datetime import datetime


def get_car_by_id(db: Session, car_id: int):
    return db.query(Rental).filter(Rental.car_id == car_id).first()


def start_use(db: Session, rental: Rental, use_start: datetime) -> Bill:
    """
    Unlock car key.

    args:
        db(Session): Database connection object
        car_id(int): Car id
    returns:
        locker(Locker): Locker object
    """
    db_bill = Bill(rental_id=rental.id, use_start=use_start, fee=rental.fee_yen)
    db.add(db_bill)
    db.commit()
    return db_bill


def end_use(db: Session, rental_id: int, use_end: datetime) -> Bill:
    """
    Lock car key.
    args:
        db(Session): Database connection object
        car_id(int): Car id
    returns:
        fee_yen(int): Fee per 15 min.
    """

    bill = (
        db.query(Bill)
        .filter(Bill.rental_id == rental_id)
        .order_by(Bill.id.desc())
        .first()
    )
    bill.use_end = use_end
    db.commit()
    return bill
