import time
import hashlib
import requests
import hmac
import base64
import execjs
from loguru import logger


def get_sign_md5(data):
    ctx = execjs.compile(open('荔枝.js', encoding='utf-8').read(), cwd=r"C:\Users\sousuo\node_modules")
    funcName = """get_signature('{}')""".format(data)
    sign = ctx.eval(funcName)
    return sign


def get_sign_hmac(ts_ms, data_sign):
    ctx = execjs.compile(open('荔枝.js', encoding='utf-8').read(), cwd=r"C:\Users\sousuo\node_modules")
    funcName = """get_signature_2('{}', '{}')""".format(ts_ms, data_sign)
    sign = ctx.eval(funcName)
    return sign


def get_signature(data):
    """
    使用python模块加密参数
    :param data: 传入msg信息
    :return:
    """
    timestamp = int(time.time() * 1000)
    data_sign = base64.b64encode(hashlib.md5(data.encode()).digest()).decode()
    method = 'POST'
    target_url = 'https://gdtv-api.gdtv.cn/api/search/v1/news'
    message_text = '\n'.join([method, target_url, str(timestamp), data_sign])
    CONST_KEY = 'dfkcY1c3sfuw0Cii9DWjOUO3iQy2hqlDxyvDXd1oVMxwYAJSgeB6phO8eW1dfuwX'
    hmac_obj = hmac.new(key=CONST_KEY.encode(), msg=message_text.encode(), digestmod=hashlib.sha256)
    signature = base64.b64encode(hmac_obj.digest()).decode()
    return timestamp, signature


def get_signature_js(data):
    """
    使用js自带加密参数
    :param data: 传入msg信息
    :return:
    """
    timestamp = int(time.time() * 1000)
    data_sign = get_sign_md5(data)
    signature = get_sign_hmac(str(timestamp), data_sign)
    return timestamp, signature


def run(data):
    # timestamp, signature = get_signature(data)
    timestamp, signature = get_signature_js(data)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'x-itouchtv-ca-key': '89541443007807288657755311869534',
        'x-itouchtv-ca-signature': signature,
        'x-itouchtv-ca-timestamp': str(timestamp),
        'x-itouchtv-client': 'WEB_PC',
        'x-itouchtv-device-id': 'WEB_3ee50450-f38c-11ec-914c-f7b7f9f4989b',
        'content-type': 'application/json',
    }
    res = requests.post('https://gdtv-api.gdtv.cn/api/search/v1/news',
                        data=data.encode('utf-8'), headers=headers).json()
    return res


if __name__ == '__main__':
    msg = '{"keyword":"大数据","pageNum":1,"type":-1,"pageSize":40}'
    results = run(msg)
    total = results.get("newsItems").get("total")
    logger.info(f"新闻总数: {total}")
    news = results.get("newsItems").get("list")
    for i, j in enumerate(news):
        logger.info(f'新闻第{i+1}条:{j.get("title").strip()}')
