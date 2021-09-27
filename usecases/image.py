from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

import models


def create_image(db: Session, car_id: int, path: str):
    db_img = models.Image(
        car_id=car_id,
        path=path,
    )
    db.add(db_img)
    db.commit()
    db.refresh(db_img)
    return db_img
