from sqlalchemy.orm import Session

from models.parking import Parking
from schemas import admin


def create_parking(db: Session, parking: admin.ParkingCreateReq):
    db_parking = Parking(**parking.dict())
    db.add(db_parking)
    db.commit()
    db.refresh(db_parking)
    return db_parking
