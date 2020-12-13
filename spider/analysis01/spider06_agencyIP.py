# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 21:44
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider06_agencyIP.py
# @Software: PyCharm

from  urllib import request

def handler_opener():
    # 系统的urlopen并没有添加代理的功能，所以需要我们自定义这个功能
    #  安全 套阶层 ssl第三方的CA数字证书
    # http是80端口， https是5443端口
    # urlopen为什么可以添加数据 handler处理器
    # 自己的opener请求数据

    # urllib = request.urlopen()
    url = "https://blog.csdn.net/lbj1260200629/article/details/83010065"

    # 创建自己的处理器
    handler = request.HTTPHandler()
    # 创建自己的opener
    opener = request.build_opener(handler)
    # 用自己创建的opener调用open方法请求数据
    response = opener.open(url)
    data = response.read()

handler_opener()