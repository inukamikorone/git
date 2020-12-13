# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 20:52
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider03_http_auth.py
# @Software: PyCharm


# urllib.request 提示错误 HTTPError UrlError

"""
raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 503: Forwarding failure


raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found
"""
from urllib import request

url = "https://www.yaozh.com/"
try:
    response = request.urlopen(url)
except request.HTTPError as error:
    print(error)