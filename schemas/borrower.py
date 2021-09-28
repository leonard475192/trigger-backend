from datetime import datetime
from pydantic import BaseModel

from schemas.admin import ParkingCreateRes


class CarDetail(BaseModel):
    """
    Response body of Car Objects
    """

    id: int
    car_id: int
    fee: int
    type: str
    number: str
    images: list
    Parking: ParkingCreateRes
    available_begin: datetime
    available_end: datetime


class CarUnlockReq(BaseModel):
    """
    Request body of `car unlock` end point
    """

    car_id: int


class CarLockReq(BaseModel):
    """
    Request body of `car lock` end point
    """

    car_id: int
