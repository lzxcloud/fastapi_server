from fastapi import FastAPI
from util.wx import WX
from typing import Optional
from pydantic import BaseModel
from config import settings

class Code(BaseModel):
    code: str

    class Config:
        schema_extra = {
            "example": {
                "code": "Foo"
            }
        }


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/wxlogin", status_code=200)
async def wx_login(code: Code):
    wx = WX(code.code)
    user_openid = wx.get_openid()
    print(user_openid)

    if not user_openid:
        return {
            "status": 400,
            "err": "user exists"
        }
    else:
        pass
        # if not User.objects.filter(uuid=user_openid):
        #     print("no user")
        #     new_user = User.objects.create(uuid=user_openid, platform="web")
        #     new_user.save()
        #     return JsonResponse({
        #         "status": 200,
        #         "uuid": user_openid,
        #     }, safe=False)
        # else:
        #     return JsonResponse({
        #         "status": 200,
        #         "skey": user_openid
        #     }, safe=False)
