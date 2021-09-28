from pydantic import BaseModel


class ParkingCreateReq(BaseModel):
    """Parking create req objects"""

    name: str
    address: str
    latitude: float
    longitude: float


class ParkingCreateRes(BaseModel):
    """Parking create req objects"""

    id: int
    name: str
    address: str
    latitude: float
    longitude: float


class LockerCreateReq(BaseModel):
    """Locker create req objects"""

    parking_id: int
    alloc: str
    pin: int
