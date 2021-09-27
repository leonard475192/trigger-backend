from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.admin import ParkingCreateReq, LockerCreateReq

from db import get_db
from usecases.parking import create_parking
from usecases.locker import create_locker


router = APIRouter(prefix="/admin")


@router.post("/parking")
def add_parking(parking: ParkingCreateReq, db: Session = Depends(get_db)):
    """
    Create parking.
    args:
        admin.ParkingCreateReq :
    returns:
        admin.ParkingCreateRes :
    """
    db_parking = create_parking(db=db, parking=parking)
    print(db_parking)
    return db_parking


@router.post("/locker")
def add_locker(locker: LockerCreateReq, db: Session = Depends(get_db)):
    """
    Create locker.
    args:
        admin.ParkingCreateReq :
    returns:
        admin.ParkingCreateRes :
    """
    db_locker = create_locker(db=db, locker=locker)
    print(db_locker)
    return db_locker
