from models import parking
from models.parking import Parking
from db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from schemas.borrower import CarUnlockReq, CarLockReq, CarDetail
from schemas.admin import ParkingCreateRes

from usecases.bill import start_use, end_use
from usecases.image import get_images
from usecases.rental import enable_use_flag, disable_use_flag, select_all, find_by_id
from usecases.locker import find_locker_by_id

import datetime
import math

# from db import get_db

router = APIRouter(prefix="/v1/borrower")


@router.get("/car/{id}")
def get_rental(id: int, db: Session = Depends(get_db)):
    """
    Get car by id.
    args:

    returns:
        cars(Car[]) : Listed Car info
    """
    db_rental = find_by_id(db=db, id=id)
    db_images = get_images(db=db, car_id=db_rental.car_id)
    img_paths = []
    for img in db_images:
        img_paths.append(img.path)
    parking = ParkingCreateRes(
        id=db_rental.Parking.id,
        name=db_rental.Parking.name,
        address=db_rental.Parking.address,
        latitude=db_rental.Parking.latitude,
        longitude=db_rental.Parking.longitude,
    )
    res = CarDetail(
        id=db_rental.id,
        car_id=db_rental.car_id,
        fee=db_rental.fee,
        type=db_rental.type,
        number=db_rental.number,
        images=img_paths,
        Parking=parking,
        available_begin=db_rental.available_begin,
        available_end=db_rental.available_end,
    )
    return res


@router.post("/car:search")
def search_cars(db: Session = Depends(get_db)):
    """
    Search car near the user.
    args:
        location(str[]) :
        db(Session): Database connection object
    returns:
        cars(Car[]) : Listed Car info
    """
    rentals = select_all(db)
    return {"car": rentals}


@router.post("/car:unlock")
def unlock_car(cu: CarUnlockReq, db: Session = Depends(get_db)):
    """
    Unlock car key.
    Substitute `True` for `in_use_flag` in the `Rental` table row
    specified by given `car_id`.
    Then get the `Locker` table row by `locker_id` that specified by `car_id`

    args:
        car_id(int) :
        db(Session): Database connection object
    returns:
        car_id(int) :
        date(date)  :
        locker(Locker):
    """

    dt_start = datetime.datetime.now()
    rnt = enable_use_flag(db, cu.car_id)

    start_use(db, rnt, dt_start)

    locker = find_locker_by_id(db, rnt.locker_id)

    return {"carId": cu.car_id, "date": dt_start, "locker": locker}


@router.post("/car:lock")
def lock_car(cu: CarLockReq, db: Session = Depends(get_db)):
    """
    Lock car key.
    Substitute `False` for `in_use_flag` in the `Rental` table row
    specified by given `car_id`.
    Then get the `fee_yen` specified by `car_id`

    args:
        car_id(int) :
        db(Session): Database connection object
    returns:
        car_id(int) :
        date(date)  :
        fee(int)    :
    """

    dt_end = datetime.datetime.now()

    rnt = disable_use_flag(db, cu.car_id)

    bill = end_use(db, rnt.id, dt_end)
    # cast deltatime to int before ceil
    unittime = math.ceil(
        (bill.use_end - bill.use_start) / datetime.timedelta(minutes=15)
    )
    print(unittime, bill.fee)

    return {"carId": cu.car_id, "date": dt_end, "fee": bill.fee * unittime}
