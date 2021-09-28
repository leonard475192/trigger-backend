from db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from schemas.borrower import CarUnlockReq, CarLockReq
from usecases.bill import start_use, end_use
from usecases.rental import enable_use_flag, disable_use_flag, select_all
from usecases.locker import find_locker_by_id
import datetime
import math

# from db import get_db

router = APIRouter(prefix="/v1/borrower")


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
    rnts = map(
        lambda r: {
            "id": r.id,
            "type": r.car.type,
            "number": r.car.number,
            "images": r.car.images,
            "parking": r.locker.parking,
            "fee": r.fee_yen,
            "availableDateTimes": {"begin": r.available_begin, "end": r.available_end},
        },
        rentals,
    )

    return list(rnts)


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
