# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 14:15
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider02_cookie.py
# @Software: PyCharm

"""
    直接获取个人中心的页面

    1，代码登录 登录成功 cookie有效
    2，自动带着cookie去请求个人中心

    cookiejar 自动保存cookie
"""

from urllib import request,parse
from http import cookiejar
import string

# 1，代码登录
# 1.1，登录的网址
login_url = "https://www.yaozh.com/login"
# 1.2，登录的参数
login_from_data={
    "username":"sqdwsq",
    "pwd":"yangtj1013!",
    "fromhash":"956F50599F",
    "backurl":"https%3A%2F%2Fwww.yaozh.com%2F"
}
# 1.3，发送登录请求
cook_jar = cookiejar.CookieJar()
cook_hanlder = request.HTTPCookieProcessor(cook_jar)
opener = request.build_opener(cook_hanlder)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
login_str = parse.urlencode(login_from_data).encode("utf-8")
# 带着参数发送POST请求
login_request = request.Request(login_url,headers=headers,data=login_str)
# 如果登录成功，cookiejar自动保存cookie
opener.open(login_request)

# 2，代码带着cookie去访问 个人中心
center_url = "https://www.yaozh.com/member/"
center_request = request.Request(center_url,headers=headers)
response = opener.open(center_url)
data = response.read().decode("utf-8")

with open("02cookie.html","w",encoding="utf-8") as f:
    f.write(data)

# 一个用户，在不同的地点(IP)不同浏览器 上面不停的登录
# 封禁账号
# N个账号