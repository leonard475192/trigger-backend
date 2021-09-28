from pydantic import BaseModel


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
