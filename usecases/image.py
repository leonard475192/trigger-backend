from sqlalchemy.orm import Session

from models.image import Image


def create_image(db: Session, car_id: int, path: str):
    db_img = Image(
        car_id=car_id,
        path=path,
    )
    db.add(db_img)
    db.commit()
    db.refresh(db_img)
    return db_img


def get_images(db: Session, car_id: int):
    return db.query(Image).filter(Image.car_id == car_id).all()
