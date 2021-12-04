from fastapi import FastAPI
from schemas import *
from util.wx import WX
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from crud import *
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import datetime

class Code(BaseModel):
    code: str
    class Config:
        schema_extra = {
            "example": {
                "code": "Foo"
            }
        }


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/wxlogin", status_code=200)
async def wx_login(code: Code, db: Session = Depends(get_db)):
    wx = WX(code.code)
    user_openid = wx.get_openid()
    if not user_openid:
        return {
            "status": 400,
            "err": "wx uuid error"
        }
    else:
        user = get_user(db, user_openid)
        if not user:
            return create_user(db, uuid=user_openid)
        else:
            return user


@app.post("/info/{uuid}", status_code=200, response_model=ItemBase)
async def add(item: ItemCreate, uuid: str,  db: Session = Depends(get_db)):
    user = get_user(db, uuid)
    ret = create_info(db, user.id, item)
    return ItemBase()


@app.get("/list/{uuid}", response_model=InfoOut)
async def get_list(uuid: str, db: session = Depends(get_db)):
    user = get_user(db, uuid)
    one_month = datetime.timedelta(days=31)
    this_month = datetime.datetime.now()
    this_cost = get_cost(db, user.id, this_month)
    next_cost = get_cost(db, user.id, this_month + one_month)
    last_cost = get_cost(db, user.id, this_month - one_month)
    infos = get_user_infos(db, user.id, this_month)
    ret = InfoOut()
    ret.next_month = next_cost
    ret.last_month = last_cost
    ret.this_month = this_cost
    ret.detail = infos
    return ret

