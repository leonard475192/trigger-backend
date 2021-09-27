from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = "postgresql"
USER = "postgres"
PASSWORD = "postgres"
HOST = "0.0.0.0"
PORT = "5433"
DB_NAME = "trigger_db"

DATABASE_URL = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
