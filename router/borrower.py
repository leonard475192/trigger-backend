from fastapi import APIRouter

router = APIRouter(prefix="/borrower/v1")


@router.post("/car:search")
def search_cars():
    """
    Search car near the user.
    args:
        location(str[]) :
    returns:
        cars(Car[]) : Listed Car info
    """
    return {"car": []}


@router.post("/car:unlock")
def unlock_car():
    """
    Unlock user's car.
    args:
        car_id(int) :
    returns:
        car_id(int) :
        date(date)  :
        locker(Locker):
    """
    return {"carId": 0, "date": "", "locker": {}}


@router.post("/car:lock")
def lock_car():
    """
    Lock user's car.
    args:
        car_id(int) :
    returns:
        car_id(int) :
        date(date)  :
        fee(int)    :
    """
    return {"carId": 0, "date": "", "fee": 0}
