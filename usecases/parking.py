from sqlalchemy.orm import Session
import geoalchemy2.functions as gf
from sqlalchemy.sql.functions import concat

from models.parking import Parking
from schemas import admin


def create_parking(db: Session, parking: admin.ParkingCreateReq):
    db_parking = Parking(
        name=parking.name,
        address=parking.address,
        geometry=f"SRID=4326;POINT({parking.location.longitude} {parking.location.latitude})",
    )
    db.add(db_parking)
    db.commit()
    db.refresh(db_parking)
    return db_parking
