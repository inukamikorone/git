# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 14:01
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider01_urlopen_code.py
# @Software: PyCharm
from urllib import request

def load_data():
    url = "http://www.baidu.com/"
    response = request.urlopen(url)
    data = response.read()
    str_data = data.decode("utf-8")
    with open("baidu.html","w",encoding="utf-8")as f:
        f.write(str_data)
    # 将字符串类型转换为bytes
    _str = "baidu"
    _bytes = str.encode("utf-8")
    print(_bytes)

    # python爬取的类型，str,bytes
    # 如果爬取回来的是bytes类型，但是你写入的时候需要字符串，：decode("utf-8")一下
    # 如果爬取的过来的是str类型：你要写入的是bytes类型，encode("utf-8")

load_data()