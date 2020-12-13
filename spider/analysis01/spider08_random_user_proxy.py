# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 10:20
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider08_random_user_proxy.py
# @Software: PyCharm

from urllib import request

def proxy_user():

    proxy_list = [
        {"http":"36.249.48.14:9999"},
        {"http":"58.253.152.214:9999"},
        {"http":"58.253.154.3:9999"},
        {"http":"58.253.159.33:9999"},
        {"http":"36.250.156.245:9999"},
    ]
    for proxy in proxy_list:
        print(proxy)
        # 利用遍历出来的IP创建处理器

        proxy_handler = request.ProxyHandler(proxy)
        # 创建opener
        opener = request.build_opener(proxy_handler)

        try:
            opener.open("https://www.baidu.com",timeout=1)
        except Exception as e:
            print(e)

proxy_user()