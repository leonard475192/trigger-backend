from pydantic import BaseModel

from schemas.base import AvailableDateTimes, Locker


class UploadImgRes(BaseModel):
    """Image Upload res objects"""

    url: str


class CarCreateReq(BaseModel):
    """Car create req objects"""

    type: str
    number: str
    images: list


class CarCreateRes(BaseModel):
    """Car create res objects"""

    carId: int


class RentalCreateReq(BaseModel):
    """Rental create req objects"""

    carId: int
    parkingId: int
    fee: int
    availableDateTimes: AvailableDateTimes
    locker: Locker


class RentalCreateRes(BaseModel):
    """Rental create res objects"""


class RentalDeleteReq(BaseModel):
    """Rental delete req objects"""

    carId: int


class RentalDeleteRes(BaseModel):
    """Rental delete res objects"""
