import execjs
import requests

"""
网易音乐下载，纯扣js
"""
with open('wyy.js', 'r', encoding='utf_8') as f:
    js = f.read()
js_com = execjs.compile(js)
a = js_com.call("d", '30031035')
url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
data = {
    'params': a.get('encText'),
    'encSecKey': a.get('encSecKey')
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://music.163.com",
    "Host": "music.163.com"
}
c = requests.post(url=url, headers=headers, data=data)
music = c.json().get('data')[0].get('url')
with open("30031035.mp4", 'wb') as f:
    f.write(requests.get(url=music).content)
