from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings


user = "root"
passwd = "123456"
host = "127.0.0.1"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{passwd}@{host}/db_wx?charset=utf8mb4"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
