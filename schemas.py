from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, time, timedelta, date


class ItemBase(BaseModel):
    message: str = "success"
    code: int = 200


class Item(ItemBase):
    id: int
    title: str
    cost: float
    platform: str

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    title: str
    cost: float
    platform: str
    end: date


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    uuid: str
    is_active: bool
    platform: str
    info: List[Item] = []

    class Config:
        orm_mode = True


class InfoOut(ItemBase):
    this_month: int = 0
    next_month: int = 0
    last_month: int = 0
    deitl: List[Item] = []



class UserInfo(BaseModel):
    data: List[User] = []
