# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 14:59
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider02_requetss_ssl.py
# @Software: PyCharm

import requests

url = "http://www.12306.cn/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
response = requests.get(url,headers=headers)
data = response.content.decode("utf-8")

with open("02-ssl.html","w",encoding="utf-8") as f:
    f.write(data)
