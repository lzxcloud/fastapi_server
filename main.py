from fastapi import FastAPI
import schemas
from util.wx import WX
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from crud import *
from database import SessionLocal, engine
from sqlalchemy.orm import Session


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
