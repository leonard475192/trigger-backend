from pydantic import BaseModel
from schemas.base import Geometry


class ParkingCreateReq(BaseModel):
    """Parking create req objects"""

    name: str
    address: str
    location: Geometry


class LockerCreateReq(BaseModel):
    """Locker create req objects"""

    parking_id: int
    alloc: str
    pin: int
