import requests


class WX(object):
    def __init__(self, code):
        self.code = code
        self.session_key = None
        self.openid = None

    def get_openid(self):
        APPID = "wx3cde4545a748fa43"
        APPSECRET = "595f681996b606993fa8fd8eb7145101"
        url = f"https://api.weixin.qq.com/sns/jscode2session?appid={APPID}" \
              f"&secret={APPSECRET}&js_code={self.code}&grant_type=authorization_code"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            if "openid" in data.keys():
                return data['openid']
            else:
                return False