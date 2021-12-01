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


@app.post("/info/{user_id}", status_code=200)
async def add(item: ItemCreate, user_id: int,  db: Session = Depends(get_db)):
    ret = create_info(db, user_id, item)
    return ret


@app.get("/list/{user_id}", status_code=200)
async def get_list(user_id: str, db: session = Depends(get_db)):
    one_month = datetime.timedelta(days=31)
    this_month = datetime.datetime.now()

    print(this_month)
    print(this_month + one_month)
    this_cost = get_cost(db, user_id, this_month)
    next_cost = get_cost(db, user_id, this_month + one_month)
    last_cost = get_cost(db, user_id, this_month - one_month)
    print(this_cost, next_cost, last_cost)
