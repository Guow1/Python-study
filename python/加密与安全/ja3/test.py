import requests

from python.加密与安全.ja3.requests_curl import CURLAdapter


class SessionRequests(requests.Session):

    def __init__(self, url_x, ua__, **kwargs):
        super().__init__()
        self.url_x = url_x
        self.timeout = 30
        self.verify = False
        if 'proxies' in kwargs:
            self.proxies = kwargs['proxies']
        self.headers = {}

    def get(self, url, **kwargs):
        kwargs.setdefault('timeout', self.timeout)
        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        kwargs.setdefault('timeout', self.timeout)
        return self.request('POST', url, data=data, json=json, **kwargs)


def create_req(url_x, ua__, **kwargs):
    session_v1 = SessionRequests(url_x, ua__, **kwargs)
    session_v1.mount("https://", CURLAdapter())
    return session_v1


req = create_req("", "")
