import datetime
from pydantic import BaseModel


class AvailableDateTimes(BaseModel):
    """Rental create req objects"""

    begin: datetime.datetime
    end: datetime.datetime


class Locker(BaseModel):
    """Locker objects"""

    alloc: str
    pin: int
