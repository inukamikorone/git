# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 21:01
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider04_requests.py
# @Software: PyCharm

import requests

# url = "http://www.baidu.com"
#
# response = requests.get(url)
#
# # content 返回的类型是字节 是bytes
# data = response.content.decode("utf-8")
#
# # text属性返回的是文本类型 str
# datas = response.text
# print(type(data))


class ResponseSpider(object):
    def __init__(self):
        get_url = "http://www.baidu.com"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        }
        self.response = requests.get(get_url,headers=headers)

    def run(self):

        data = self.response.content

        # 获取请求头
        request_headers = self.response.request.headers
        # print(request_headers)

        # 获取响应头
        response_headers = self.response.headers
        print(request_headers)

        # 响应状态码
        code = self.response.status_code
        print(code)

        # 请求的cookie
        request_cookie = self.response.request._cookies
        print(request_cookie)

        # 响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)

ResponseSpider().run()