# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 22:01
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider07_proxy_handler.py
# @Software: PyCharm

from urllib import request

def create_proxy_handler():
    url = "https://blog.csdn.net/lbj1260200629/article/details/83010065"

    # 添加代理
    proxy = {
        # 免费的IP代理写法
        # "http":"http://60.177.159.118:9000",
        "http":"60.177.159.118:9000",
    }
    # 代理处理器
    proxy_handler = request.ProxyHandler(proxy)

    # 创建自己的opener
    opener = request.build_opener(proxy_handler)
    # 拿着代理IP去发送请求
    data = opener.open(url).read()
    print(data)

create_proxy_handler()