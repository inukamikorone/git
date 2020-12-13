# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 11:21
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider10_auth_user.py
# @Software: PyCharm

from urllib import request


def auth_nei_wang():
    # 1，用户名密码
    user = "admin"
    pwd = "admin123"
    nei_url = "http://192.168.66.68"


    # 2,创建密码管理器
    pwd_manager = request.HTTPPasswordMgrWithPriorAuth()
    pwd_manager.add_password(None,nei_url,user,pwd)

    # 3，创建认证处理器
    auth_handler = request.HTTPBasicAuthHandler(pwd_manager)
    opener = request.build_opener(auth_handler)

    response = opener.open(nei_url)
    print(response)

auth_nei_wang()