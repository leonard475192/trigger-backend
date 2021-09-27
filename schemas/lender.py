from pydantic import BaseModel


class UploadImgRes(BaseModel):
    """Image Upload res objects"""

    url: str


class CarCreateReq(BaseModel):
    """Car create req objects"""

    type: str
    number: str
    images: list


class CarCreateRes(BaseModel):
    """Car create re objects"""

    carId: int
