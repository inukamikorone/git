# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 8:15
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider01_requests_auth.py
# @Software: PyCharm

import requests

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
free_proxy = {"http":"118.190.199.163:8888"}

response = requests.get(url=url,headers=headers,proxies=free_proxy)

print(response.status_code)