from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, FLOAT, Date
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True)
    platform = Column(String)
    is_active = Column(Boolean, default=True)
    infos = relationship("Info", back_populates="user")


class Info(Base):
    __tablename__ = "infos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    end = Column(Date)
    cost = Column(FLOAT)
    platform = Column(String, unique=True)
    status = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="infos")


