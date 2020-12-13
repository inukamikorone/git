# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 14:55
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : test.py
# @Software: PyCharm

import requests

url = "https://movie.douban.com/top250"
html = requests.get(url)
response = html.text
s = response.encode
print(s)
print(response)