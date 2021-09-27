from fastapi import APIRouter, Depends, File, UploadFile, status
from sqlalchemy.orm import Session

from schemas import admin

from db import get_db
from usecases.parking import create_parking
from usecases.locker import create_locker


router = APIRouter(prefix="/admin")


@router.post("/parking")
def add_parking(parking: admin.ParkingCreateReq, db: Session = Depends(get_db)):
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
def add_locker(locker: admin.LockerCreateReq, db: Session = Depends(get_db)):
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
