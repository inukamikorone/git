# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 21:30
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider06_POST.py
# @Software: PyCharm

import requests
import json

url = "https://api.github.com/user"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
# 这个网址返回的内容不是HTML，而是标准的json
response  = requests.get(url,headers=headers)

# str
data = response.content.decode("utf-8")
print(data)

# json()自动将json字符串转换成python dict list
data_dict = json.loads(data)
print(data_dict["message"])