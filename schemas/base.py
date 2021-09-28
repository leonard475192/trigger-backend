import datetime
from pydantic import BaseModel


class AvailableDateTimes(BaseModel):
    """AvailableDateTimes objects"""

    begin: datetime.datetime
    end: datetime.datetime


class Geometry(BaseModel):
    """Geometry objects"""

    latitude: float
    longitude: float
