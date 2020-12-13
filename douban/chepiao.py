# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 19:55
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : chepiao.py
# @Software: PyCharm
import requests
import urllib3
import re
url= 'https://699pic.com/static.699pic.com/best_album/59.jpg!/fw/316'

response = requests.get(url)
res = response.content
with open('123.png','wb') as f:
    f.write(res)
