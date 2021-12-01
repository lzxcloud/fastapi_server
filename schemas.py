from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, time, timedelta, date


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


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


class Info(BaseModel):
    id: int
    title: str
    cost: float
    platform: str
    this_month: int
    next_month: int
    last_month: int


class UserInfo(BaseModel):
    message: str
    code: int
    data: List[Info] = []
