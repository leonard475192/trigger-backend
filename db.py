from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = "postgresql"
USER = "postgres"
PASSWORD = "postgres"
HOST = "localhost"
PORT = "5432"
DB_NAME = "trigger_db"

DATABASE_URL = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# databases
# database = databases.Database(DATABASE_URL, min_size=5, max_size=20)
# ECHO_LOG = False
# engine = create_engine(DATABASE_URL, echo=ECHO_LOG)
# metadata = sqlalchemy.MetaData()

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
