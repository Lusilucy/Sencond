from base import Base


class WeWork(Base):
    def __init__(self, corpid, corpsecret):
        self.token = self.get_access_token(corpid, corpsecret)

    def get_access_token(self, corpid, corpsecret):
        kwargs = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        }
        r = self.request(kwargs)
        return r.json()['access_token']
