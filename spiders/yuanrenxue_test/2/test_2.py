import execjs
import requests

"""
    题目时间: 2021年8月4日;
    题目类型: js加密;
    题目: js 混淆 - 动态cookie 1;
    题目要求: 爬取数据
    流程: 
    1.访问页面,抓包看请求,知晓cookie中关键参数'm'决定访问是否成功;
    2.每次cookie重置，都会访问'https://match.yuanrenxue.com/match/2',并返回一段加密混淆后的js,m参数经由此js产生；
    3.用工具'http://tool.yuanrenxue.com/decode_obfuscator' 解这段混淆,分析m的大致流程；
    4.改写js,让execjs能正常运行js，并产生m值。
    坑: 无关对象不要运行，不要运行
"""
url_api = 'https://match.yuanrenxue.com/api/match/2?page=3'
with open('test_2.js', 'r', encoding='utf_8') as f:
    js = f.read()
js_com = execjs.compile(js)
e = js_com.call("_0x29a0ed")
headers = {
    "Host": 'match.yuanrenxue.com',
    "Connection": 'keep-alive',
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://match.yuanrenxue.com/match/2",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": e
}
res = requests.get(url=url_api, headers=headers)
print(res.text)
