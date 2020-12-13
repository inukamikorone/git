# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 15:22
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider04_request_header.py
# @Software: PyCharm

from urllib import request

def load_baudi():
    url = "http://www.baidu.com"
    # 添加请求头信息
    header = {
        # 浏览器的版本
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    }

    requests = request.Request(url,headers=header)

    # 请求网络数据
    response = request.urlopen(url)
    data = response.read().decode("utf-8")
    with open("04header.html","w") as f:
        f.write(data)

load_baudi()