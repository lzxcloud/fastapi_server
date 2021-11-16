from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, FLOAT
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, max_length=64)
    platform = Column(String, max_length=64)
    is_active = Column(Boolean, default=True)
    infos = relationship("Info", back_populates="owner")


class Info(Base):
    title = Column(String, nullable=False, max_length=64)
    end = Column(DateTime)
    cost = Column(FLOAT)
    platform = Column(String, unique=True, max_length=64)
    user_id = relationship("User", back_populates="infos")
