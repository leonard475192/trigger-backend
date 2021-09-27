from sqlalchemy.orm import Session

from models.car import Car
from schemas import lender


def create_car(db: Session, car: lender.CarCreateReq):
    # TODO **car.dict()による方法
    db_car = Car(
        type=car.type,
        number=car.number,
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car
