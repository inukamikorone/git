# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 21:21
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider05_request_use.py
# @Software: PyCharm

import requests

# 参数自动转译
# url ="https://www.baidu.com/s?wd=美女"
url = "https://www.baidu.com/s?"
params = {
    "wd":"美女"
}

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
response = requests.get(url,headers=headers,params=params)

data = response.content.decode("utf-8")

with open("baidu.html","w",encoding="utf-8") as f:
    f.write(data)


# 发送POST请求和添加参数

requests.post(url,data=data)
