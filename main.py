from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from router import lender
from db import Base, engine

from models import car, image, locker, parking, rental

# テーブルクラスのテーブルを生成
Base.metadata.create_all(engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

# app.include_router(car.router)
app.include_router(lender.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
