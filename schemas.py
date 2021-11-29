from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class Item(ItemBase):
    id: int
    title: str
    cost: float
    platform: str
    user_id: int

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    title: str
    cost: float
    platform: str


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


