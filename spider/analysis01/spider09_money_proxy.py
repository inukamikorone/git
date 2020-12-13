# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 11:03
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider09_money_proxy.py
# @Software: PyCharm

from urllib import request
import requests

# 付费的代理爬虫
# 1，用户名密码(带着)
# 通过验证的处理器来发送

def money_proxy_use():
    # 第一种方式付费代理发送请求
    # 代理IP
    money_proxy={
        "http":"username:password@192.168.12.11:8080"
    }
    # 2.代理的处理器
    proxy_handler = request.ProxyHandler(money_proxy)

    # 3.通过处理器创建opener
    opener = request.build_opener(proxy_handler)
    # 4.open发送请求
    opener.open("http://www.baidu.com")



    # 第二种方式发送付费的IP代理
    user_name = "abcname"
    pwd = "123456"
    proxy_money = "158.63.66.77:8080"
    # 创建密码管理器，添加用户名和密码
    password_manager = request.HTTPPasswordMgrWithPriorAuth()
    # uri定位 uri>url
    # url 资源地位符
    password_manager.add_password(None,proxy_money,user_name,pwd)
    # 创建可以验证代理IP的处理器
    handle_auth_proxy = request.ProxyBasicAuthHandler(password_manager)
    # 根据处理器创建opener
    opener_auth = request.build_opener(handle_auth_proxy)
    # 发送请求
    response = opener.open("http://www.baid.com")
    print(response.read())

    # 爬取自己公司的数据，做数据分析
    # admin

money_proxy_use()