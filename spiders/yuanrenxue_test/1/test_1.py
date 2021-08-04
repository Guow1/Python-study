import execjs
import requests

"""
    题目时间: 2021年8月4日;
    题目类型: js加密;
    题目: js 混淆 - 源码乱码;
    题目要求: 爬取第4&5页数据
"""
with open("test_1.js", "r", encoding='utf_8')as f:
    js = f.read()
js_com = execjs.compile(js)
e = js_com.call("m")
url = "https://match.yuanrenxue.com/api/match/1?page=5&m={}".format(e)
headers = {
    "user-agent": "yuanrenxue.project"
}
res = requests.get(url, headers=headers)
print(res.text)
