import requests
from config import settings


class WX(object):
    def __init__(self, code):
        self.code = code
        self.session_key = None
        self.openid = None

    def get_openid(self):
        APPID = settings.APPID
        APPSECRET = settings.APPSECRET
        url = f"https://api.weixin.qq.com/sns/jscode2session?appid={APPID}" \
              f"&secret={APPSECRET}&js_code={self.code}&grant_type=authorization_code"
        r = requests.get(url)
        print(r.status_code)
        if r.status_code == 200:
            data = r.json()
            if "openid" in data.keys():
                return data['openid']
            else:
                return False
