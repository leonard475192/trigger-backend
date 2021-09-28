from fastapi import APIRouter, Depends, File, UploadFile, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from schemas import lender

from utils.save_file import save_file
from usecases.car import create_car
from usecases.image import create_image
from usecases.locker import find_locker_by_alloc
from usecases.rental import create_rental, delete_rental
from db import get_db

router = APIRouter(prefix="/v1/lender")


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


@router.post("/car:activate", response_model=lender.RentalCreateRes)
def add_rental(rental: lender.RentalCreateReq, db: Session = Depends(get_db)):
    """
    Activate car => Create rental
    args:
        schemas.RentalCreateReq :
    returns:
        schemas.RentalCreateRes :
    """
    locker = find_locker_by_alloc(
        db=db, parking_id=rental.parkingId, alloc=rental.locker.alloc
    )
    if not locker:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})
    create_rental(db=db, rental=rental, locker_id=locker.id)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})


@router.post("/car:deactivate", response_model=lender.RentalDeleteRes)
def del_rental(rental: lender.RentalDeleteReq, db: Session = Depends(get_db)):
    """
    Deactivate car => delete rental
    args:
        schemas.RentalDeleteReq :
    returns:
        schemas.RentalDeleteRes :
    """
    delete_rental(db=db, car_id=rental.carId)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})
