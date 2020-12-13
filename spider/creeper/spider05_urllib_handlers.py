# -*- coding:utf-8 -*-
# @Time : 2020/8/20 10:55
# @Author : 面包狗
# @File : spider05_urllib_handlers.py
# @Software: PyCharm


from urllib.request import Request,build_opener,HTTPHandler,HTTPCookieProcessor,ProxyHandler
from http.cookiejar import CookieJar
from urllib.parse import urlencode

opener = build_opener(HTTPHandler(),
                      HTTPCookieProcessor,
                      ProxyHandler(proxies={
                          "http":"http://125.108.79.254:9999"
                      }))




request = Request(post_url,
                  urlencode(data).encode("utf-8"),
                  headers)

resp = opener.open(request)
bytes_ = resp.read()
print(bytes_.decode())
