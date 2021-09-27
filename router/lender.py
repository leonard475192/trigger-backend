from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from schemas import lender

from utils.save_file import save_file
from usecases.car import create_car
from usecases.image import create_image
from db import get_db

router = APIRouter(prefix="/lender")


@router.post("/photo", response_model=lender.UploadImgRes)
def upload_car_img(img: UploadFile = File(...)):
    """
    Upload car img.
    args:
        img(UploadFile) :
    returns:
        schemas.UploadImgRes :
    """
    url = save_file(file=img.file, dir="static/car")
    return {"url": url}


@router.post("/car", response_model=lender.CarCreateRes)
def add_car(car: lender.CarCreateReq, db: Session = Depends(get_db)):
    """
    Create car.
    args:
        schemas.CarCreateReq :
    returns:
        schemas.CarCreateRes :
    """
    db_car = create_car(db=db, car=car)
    for img in car.images:
        db_img = create_image(db=db, path=img, car_id=db_car.id)
        db_car.images.append(db_img)
    return {"carId": db_car.id}
